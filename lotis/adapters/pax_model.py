"""Manifest pasazerski -- jedyna warstwa, ktora nadal jest generowana.

Tozsamosci pasazerow nie ma w zadnym publicznym zrodle i miec nie moze. Ale
wszystkie *rozklady*, wedlug ktorych ten generator pracuje, pochodza teraz
z bazy, a nie z mojej glowy:

* `CF.pax.lf`        -- wypelnienie wg sektora, przedzialy min-max
* `CF.pax.trf`       -- udzial pasazerow transferowych wg sektora
* `CF.pax.status`    -- udzial pasazerow ze statusem
* `CF.pax.ssrRate`   -- udzial zgloszen specjalnych
* `KL` (22 klasy)    -- mnozniki wartosci biletu wzgledem Y pelnej
* `ST` (7 statusow)  -- wagi i priorytety programu lojalnosciowego
* `SS` (47 kodow)    -- zgloszenia specjalne, z flaga ochrony przy offloadzie
* `K.reb.one_way_fare_estimate_eur` -- poziom taryfy wg sektora

Zostaja dwa zalozenia wlasne i sa oznaczone w raporcie node 01: rozklad klas
rezerwacyjnych w obrebie kabiny oraz wysokosc ancillary. Bazy ich nie podaja.

Determinizm: ziarno to numer rejsu, wiec ten sam rejs zawsze dostaje ten sam
manifest. Bez tego testy golden-file nie mialyby sensu, a porownania miedzy
wersjami silnika bylyby zaszumione losowoscia.
"""

from __future__ import annotations

from dataclasses import dataclass
from random import Random

from ..kernel.contracts import (
    Basket, Cabin, Itinerary, Passenger, PaxStatus, Purchase, SpecialNeed, TripType,
)
from ..kernel.money import Money
from .lot_db import KL_CABIN, KL_FAMILY, KL_VALUE, LotDB

#: Udzial klas w obrebie rodziny taryfowej. To jedno z dwoch zalozen wlasnych --
#: baza podaje mnozniki wartosci, ale nie mowi, ilu pasazerow leci w ktorej klasie.
FARE_FAMILY_SHARE = {
    "business_flex": 0.010,
    "business_saver": 0.030,
    "premium": 0.040,
    "economy_full": 0.080,
    "economy_pex": 0.220,
    "economy_discount": 0.380,
    "economy_lowest": 0.240,
}

#: Ancillary jako ulamek taryfy. Drugie zalozenie wlasne.
ANCILLARY_SHARE = {"C": (0.00, 0.05), "P": (0.03, 0.10), "Y": (0.10, 0.24)}

#: Rozklad statusow wsrod pasazerow, ktorzy w ogole maja status.
STATUS_MIX = (("FTL", 0.55), ("SEN", 0.22), ("SA_GOLD", 0.10),
              ("SA_SILVER", 0.09), ("HON", 0.04))

_SSR_TO_SPECIAL = {
    "mobility": SpecialNeed.REDUCED_MOBILITY,
    "medical": SpecialNeed.MEDICAL_ASSIST,
    "minor": SpecialNeed.UNACCOMPANIED_MINOR,
    "pet": SpecialNeed.PET_IN_HOLD,
}


def _special_for(code: str, category: str) -> SpecialNeed | None:
    if category in _SSR_TO_SPECIAL:
        return _SSR_TO_SPECIAL[category]
    upper = code.upper()
    if upper.startswith("WCH") or upper in {"WCMP", "WCBD", "BLND", "DEAF"}:
        return SpecialNeed.REDUCED_MOBILITY
    if upper in {"UMNR", "UM"}:
        return SpecialNeed.UNACCOMPANIED_MINOR
    if upper in {"MEDA", "STCR", "OXYG", "PORT"}:
        return SpecialNeed.MEDICAL_ASSIST
    if upper in {"PETC", "AVIH", "SVAN", "ESAN"}:
        return SpecialNeed.PET_IN_HOLD
    return None


@dataclass(frozen=True, slots=True)
class Manifest:
    passengers: dict[str, Passenger]
    itineraries: dict[str, Itinerary]
    seated: dict[str, int]
    assumptions: tuple[str, ...]


class PaxModel:
    def __init__(self, db: LotDB, seed: int = 2026) -> None:
        self.db = db
        self.seed = seed
        self.cf = db.config["pax"]
        self.fares = db.costs["reb"]["one_way_fare_estimate_eur"]
        self.eur_pln = db.eur_pln
        self._classes = self._class_table()

    # ---- tabele pochodne ----

    def _class_table(self) -> dict[str, list[tuple[str, float, float]]]:
        """kabina -> [(klasa, mnoznik wartosci, waga udzialu)]."""
        by_family: dict[str, list[tuple[str, float]]] = {}
        for code, row in self.db.booking_classes.items():
            by_family.setdefault(str(row[KL_FAMILY]), []).append((code, float(row[KL_VALUE])))
        out: dict[str, list[tuple[str, float, float]]] = {}
        for family, members in by_family.items():
            share = FARE_FAMILY_SHARE.get(family, 0.0) / max(1, len(members))
            cabin = str(self.db.booking_classes[members[0][0]][KL_CABIN])
            for code, value in members:
                out.setdefault(cabin, []).append((code, value, share))
        return out

    def _available_cabins(self, cabins: str) -> list[str]:
        """Kabiny faktycznie sprzedawane na trasie: 'CY', 'Y', 'CPY', 'PY'."""
        return [c for c in ("C", "P", "Y") if c in (cabins or "Y")]

    def _pick_class(self, rng: Random, cabins: str) -> tuple[str, float, str]:
        pool: list[tuple[str, float, float, str]] = []
        for cabin in self._available_cabins(cabins):
            for code, value, share in self._classes.get(cabin, []):
                pool.append((code, value, share, cabin))
        if not pool:
            return "Y", 1.0, "Y"
        total = sum(p[2] for p in pool)
        pick = rng.random() * total
        acc = 0.0
        for code, value, share, cabin in pool:
            acc += share
            if pick <= acc:
                return code, value, cabin
        code, value, _, cabin = pool[-1]
        return code, value, cabin

    def _load_factor(self, rng: Random, sector: str) -> float:
        low, high = self.cf["lf"].get(sector, self.cf["lf"]["europe"])
        lf = (low + rng.random() * (high - low)) / 100.0
        if sector != "longhaul" and rng.random() * 100 < self.cf["halfFullShare"]:
            lf *= 0.70 + rng.random() * 0.14
        return min(1.0, lf)

    # ---- generowanie ----

    def build(self, flights: dict, routes: dict, types: dict) -> Manifest:
        """Zbuduj manifest dla calej doby.

        `flights` to slownik kernel.Flight, posortowany chronologicznie przy
        wyszukiwaniu polaczen. Pasazer transferowy powstaje raz, na pierwszym
        odcinku, i zajmuje miejsce na obu -- inaczej policzylby sie dwa razy.
        """
        ordered = sorted(flights.values(), key=lambda f: f.std)
        by_origin: dict[str, list] = {}
        for f in ordered:
            by_origin.setdefault(f.dep, []).append(f)

        seated: dict[str, int] = {f.id: 0 for f in ordered}
        capacity: dict[str, int] = {}
        for f in ordered:
            spec = types.get(f.type_code)
            capacity[f.id] = spec.seats_total if spec else 150

        passengers: dict[str, Passenger] = {}
        itineraries: dict[str, Itinerary] = {}
        counter = 0

        for flight in ordered:
            rng = Random(f"{self.seed}|{flight.number}|{flight.std.date()}")
            route = routes.get((flight.dep, flight.arr))
            sector = route.sector if route else "europe"
            cabins = route.cabins if route else "Y"
            target = round(capacity[flight.id] * self._load_factor(rng, sector))
            need = max(0, target - seated[flight.id])
            transfer_pct = self.cf["trf"].get(sector, 35) / 100.0
            status_pct = self.cf["status"].get(sector, 5) / 100.0
            base_eur = float(self.fares.get(sector, self.fares["europe"]))

            for _ in range(need):
                counter += 1
                onward = None
                if rng.random() < transfer_pct:
                    onward = self._find_onward(rng, flight, by_origin, seated, capacity)

                segments = (flight.id,) if onward is None else (flight.id, onward.id)
                itin_id = f"OD{counter:06d}"
                itineraries[itin_id] = Itinerary(
                    id=itin_id,
                    origin=flight.dep,
                    destination=onward.arr if onward else flight.arr,
                    segments=segments,
                )
                seated[flight.id] += 1
                if onward is not None:
                    seated[onward.id] += 1

                _cls, value, cabin = self._pick_class(rng, cabins)
                fare_eur = base_eur * value
                if onward is not None:
                    fare_eur *= 1.55        # bilet przez punkt, nie suma dwoch odcinkow
                lo, hi = ANCILLARY_SHARE.get(cabin, ANCILLARY_SHARE["Y"])
                anc_eur = fare_eur * (lo + rng.random() * (hi - lo))

                has_status = rng.random() < status_pct
                specials = self._specials(rng)

                pax_id = f"PAX{counter:06d}"
                passengers[pax_id] = Passenger(
                    id=pax_id,
                    itinerary_id=itin_id,
                    basket=Basket(
                        cabin=Cabin.BUSINESS if cabin in ("C", "P") else Cabin.ECONOMY,
                        trip=TripType.CONNECTING if onward is not None else TripType.DIRECT,
                        purchase=self._purchase(rng, value),
                        status=PaxStatus.LOYALTY if has_status else PaxStatus.BASE,
                    ),
                    fare=Money.from_major(round(fare_eur * self.eur_pln, 2)),
                    ancillary=Money.from_major(round(anc_eur * self.eur_pln, 2)),
                    specials=specials,
                )

        return Manifest(
            passengers=passengers,
            itineraries=itineraries,
            seated=seated,
            assumptions=(
                "rozklad klas rezerwacyjnych w obrebie kabiny (baza podaje mnozniki, nie udzialy)",
                "ancillary jako ulamek taryfy",
                "moment zakupu skorelowany z elastycznoscia klasy",
            ),
        )

    def _purchase(self, rng: Random, value: float) -> Purchase:
        """Taryfy elastyczne kupuje sie pozno, promocyjne wczesnie.

        Momentu zakupu nie ma w danych -- korelacja z mnoznikiem klasy jest
        przyblizeniem, nie pomiarem.
        """
        p_late = min(0.9, 0.15 + 0.16 * value)
        return Purchase.LATE if rng.random() < p_late else Purchase.EARLY

    def _specials(self, rng: Random) -> frozenset[SpecialNeed]:
        if rng.random() * 100 >= self.cf["ssrRate"]:
            return frozenset()
        codes = list(self.db.ssr.items())
        code, row = codes[rng.randrange(len(codes))]
        category = str(row[4]) if len(row) > 4 else ""
        need = _special_for(code, category)
        return frozenset({need}) if need else frozenset()

    def _find_onward(self, rng: Random, flight, by_origin, seated, capacity):
        """Rejs kontynuujacy z portu przylotu, z zachowanym MCT i wolnym miejscem."""
        from .airports import minimum_connection_min, port

        candidates = by_origin.get(flight.arr, [])
        if not candidates:
            return None
        inbound_schengen = bool(port(flight.dep) and port(flight.dep).schengen)
        window: list = []
        for nxt in candidates:
            gap = (nxt.std - flight.sta).total_seconds() / 60.0
            if gap <= 0:
                continue
            if gap > 8 * 60:
                break
            out_schengen = bool(port(nxt.arr) and port(nxt.arr).schengen)
            mct = minimum_connection_min(flight.arr, inbound_schengen, out_schengen)
            if gap < mct:
                continue
            if seated.get(nxt.id, 0) >= capacity.get(nxt.id, 0):
                continue
            window.append(nxt)
        if not window:
            return None
        return window[rng.randrange(min(len(window), 5))]
