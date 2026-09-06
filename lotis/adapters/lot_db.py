"""Loader bazy parametrycznej LOT-u osadzonej w `loops.jsx` (DB v5.0).

Plik `loops.jsx` niesie w stalej `DB` kompletna baze parametrow IROPS dla LOT-u:
porty, siatke, flote, prawo (EU261, Montreal, FTL), kody opoznien AHM 730,
klasy rezerwacyjne, statusy, partnerow i stawki kosztowe. Wszystko z podanymi
zrodlami w sekcji `SRC`.

Ta baza zastepuje moje wczesniejsze recznie pisane tabele i pliki `policy/*.json`.
Jest lepsza w kazdym wymiarze: 148 portow zamiast 44, realne strefy IANA zamiast
przesuniec letnich, realne curfew z rozroznieniem planowania od wykonania,
realne MCT, realne czasy postoju policzone z obserwacji, i prawo z cytowanym
orzecznictwem zamiast moich czterech regul.

DEKODOWANIE
-----------
Baza jest zakodowana tablicowo (oszczednosc miejsca). Znaczenia pol odczytane
z uzycia w komponencie Reacta w tym samym pliku, nie zgadniete -- kazda stala
`_IDX_*` ponizej ma w komentarzu linie, ktora ja potwierdza.

Uwaga o strefach: `L[2]` to nazwa strefy IANA, wiec przesuniecie zalezy od daty.
`zoneinfo` jest w stdlib od 3.9, wiec liczymy je poprawnie takze dla zimy --
w odroznieniu od mojej poprzedniej tabeli, ktora miala zaszyte lato.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import date, datetime, time
from functools import cached_property
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

# --------------------------------------------------------------- indeksy pol

# L[k] = [lat, lon, tz, EU, Schengen, EU261, poziom slotow, nazwa, curfew, MCT]
#   potw.: linia 3410 `[k, v[7], v[3]?"UE":"—", v[2].split("/")[1], v[4]?"tak":"nie"]`
#          linia 871  `const c = p && p[8]`  (curfew)
L_LAT, L_LON, L_TZ, L_EU, L_SCHENGEN, L_EU261, L_SLOT, L_NAME, L_CURFEW, L_MCT = range(10)

# T[k] = [o, d, km, tierEU261, blokMin, typDominujacy, sektor, kabiny, numery, 0, typy, operacji]
#   potw.: linia 3415 `[t[0], t[1], num(t[2]), t[3], hmn(t[4]), t[5], ...]`
(T_O, T_D, T_KM, T_TIER, T_BLOCK, T_TYPE,
 T_SECTOR, T_CABINS, T_NUMBERS, T_RES, T_TYPES, T_OPS) = range(12)

# R[k] = [nr, o, d, std, sta, przesuniecieDoby, maskaDni, 3, obserwacji, [rejestracje]]
#   potw.: linia 197 `obs:r[8]`, linia 104 `(r[8]||1)`, linia 120 komentarz "0=pon"
R_NR, R_O, R_D, R_STD, R_STA, R_DAYOFF, R_MASK, R_TIER, R_OBS, R_REGS = range(10)

# F[k] = [reg, typ, wetLease, operator, miejsca, malowanie, operacji]
#   potw.: linia 3432 `[f[0], f[1], f[4], f[3], f[2]?"wet-lease":"własna", f[6], f[5]]`
#          linia 222  `if(f[2]) return`  (pomijanie ACMI przy podmianach)
F_REG, F_TYPE, F_WETLEASE, F_OPERATOR, F_SEATS, F_LIVERY, F_OPS = range(7)

# TY[k] = [nazwa, miejsca, zasiegKm, kategoria, rodzinaUprawnien, [J,PE,Y],
#          typProxyKosztu, skalaKosztu, personelPokladowy, ?, uwaga]
#   potw.: linia 292 `rat[k]=v[4]` (uprawnienie), linia 353 `ileCC = td[8]`
TY_NAME, TY_SEATS, TY_RANGE, TY_CAT, TY_RATING, TY_CABIN, TY_PROXY, TY_SCALE, TY_CC = range(9)

# KO[kod] = [opis, klasa, ?, grupa, podkod, orzecznictwo]
#   potw.: linia 2329 -- `KO[kod][1]` mapuje sie na trzy etykiety:
#          "c" odpowiedzialność przewoźnika, "n" okoliczność nadzwyczajna,
#          "d" kod reakcyjny
#          linia 2331 `KO[kod][5] && <Znacz>orzecznictwo TSUE</Znacz>`
KO_DESC, KO_CLASS, KO_X, KO_GROUP, KO_SUB, KO_CJEU = range(6)

# SS[kod] = [wagaWizerunkowa, czasObslugiMin, wymagaDodatkowego, opis, kategoria, chroniony]
#   potw.: linia 898 `(DB.SS[k]||[,0])[1]` (czas), linia 1426 `(DB.SS[sp.ssr]||[,,0])[2]`,
#          linia 1548 `(DB.SS[sp.ssr]||[,,,,,0])[5]` (chroniony przy offloadzie)
SS_WEIGHT, SS_TIME, SS_EXTRA, SS_DESC, SS_CAT, SS_PROTECTED = range(6)

# KL[klasa] = [kabina, mnoznikWartosci, poziom, procentTaryfy, rodzinaTaryfowa]
KL_CABIN, KL_VALUE, KL_TIER, KL_PCT, KL_FAMILY = range(5)

# ST[status] = [wagaWizerunkowa, priorytet, nazwa, program, premium, kryterium]
ST_WEIGHT, ST_PRIORITY, ST_NAME, ST_PROGRAM, ST_PREMIUM, ST_CRITERIA = range(6)

# TF[poziom] = [nazwa, mnoznikKosztu, czasProceduryMin, opis]
TF_NAME, TF_COST, TF_TIME, TF_NOTE = range(4)

#: 0 = poniedzialek. Potwierdzone komentarzem w linii 120 `dzien tygodnia (0=pon)`.
WEEKDAYS_PL = ("poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela")

_SEARCH_ENV = "LOTIS_LOOPS_JSX"


def _find_jsx() -> Path:
    from ..kernel.env import load_env
    load_env()
    if (configured := os.environ.get(_SEARCH_ENV, "").strip()):
        path = Path(configured)
        if not path.exists():
            raise FileNotFoundError(
                f"{_SEARCH_ENV} wskazuje na nieistniejacy plik: {path}"
            )
        return path
    root = Path(__file__).resolve().parent.parent.parent
    candidates = (root / "data" / "loops.jsx", root / "loops.jsx",
                  Path.home() / "Downloads" / "dane" / "loops.jsx")
    for candidate in candidates:
        if candidate.exists():
            return candidate
    tried = "\n  ".join(str(c) for c in candidates)
    raise FileNotFoundError(
        f"nie znalazlem loops.jsx. Sprawdzone sciezki:\n  {tried}\n"
        f"Wskaz plik zmienna {_SEARCH_ENV} w .env"
    )


def _extract_db(source: str) -> dict[str, Any]:
    """Wycina literal obiektu `const DB = {...}` z pliku JSX.

    Skaner liczy nawiasy z pominieciem tego, co jest w stringach -- naiwne
    szukanie `};` lamie sie na nawiasach w opisach.
    """
    anchor = source.index("const DB =")
    start = source.index("{", anchor)
    depth = 0
    in_string = False
    escaped = False
    for i in range(start, len(source)):
        ch = source[i]
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(source[start:i + 1])
    raise ValueError("nie domknieto literalu DB w loops.jsx")


# --------------------------------------------------------------- widoki


@dataclass(frozen=True, slots=True)
class Curfew:
    """Cisza nocna portu.

    `hard_planning_ban` odwzorowuje `blok: c[2]===1 && plan` z linii 876:
    typ 1 zakazuje PLANOWANIA operacji w oknie, ale maszyna opozniona
    z przyczyn niezaleznych moze wykonac operacje. Typ 2 to kwoty nocne
    i ryzyko braku slotu, nie zakaz.
    """

    start_min: int
    end_min: int
    kind: int
    confirmed: bool

    @property
    def hard_planning_ban(self) -> bool:
        return self.kind == 1

    def covers(self, local_minute: int) -> bool:
        v = local_minute % 1440
        if self.start_min < self.end_min:
            return self.start_min <= v < self.end_min
        return v >= self.start_min or v < self.end_min   # okno przez polnoc

    def blocks(self, local_minute: int, planning: bool = True) -> bool:
        return self.covers(local_minute) and self.kind == 1 and planning


@dataclass(frozen=True, slots=True)
class Port:
    iata: str
    lat: float
    lon: float
    tz: str
    eu: bool
    schengen: bool
    eu261: bool
    slot_level: int
    name: str
    curfew: Curfew | None
    mct: dict[str, int]

    def utc_offset_min(self, when: datetime | date) -> int:
        """Przesuniecie strefy dla konkretnej daty -- poprawne takze zima."""
        moment = when if isinstance(when, datetime) else datetime.combine(when, time(12, 0))
        if moment.tzinfo is not None:
            moment = moment.replace(tzinfo=None)
        offset = ZoneInfo(self.tz).utcoffset(moment)
        return int(offset.total_seconds() // 60) if offset else 0


@dataclass(frozen=True, slots=True)
class Route:
    origin: str
    dest: str
    km: int
    eu261_tier: str          # 'A' | 'B' | 'C'
    block_min: int
    dominant_type: str
    sector: str              # domestic | schengen | europe | mid | longhaul
    cabins: str              # 'Y' | 'CY' | 'PY' | 'CPY'
    numbers: tuple[str, ...]
    type_counts: dict[str, int]
    operations: int


@dataclass(frozen=True, slots=True)
class ScheduledFlight:
    number: str
    origin: str
    dest: str
    std_local: str           # HH:MM w porcie wylotu
    sta_local: str           # HH:MM w porcie przylotu
    arrives_next_day: bool
    weekday_mask: str        # 7 znakow, indeks 0 = poniedzialek
    observations: int
    registrations: tuple[str, ...]

    def operates_on(self, weekday: int) -> bool:
        return self.weekday_mask[weekday] == "1"

    @property
    def days_per_week(self) -> int:
        return self.weekday_mask.count("1")


@dataclass(frozen=True, slots=True)
class FleetAircraft:
    reg: str
    type_code: str
    wet_lease: bool
    operator: str
    seats: int
    livery: str | None
    operations: int


@dataclass(frozen=True, slots=True)
class TypeSpec:
    code: str
    name: str
    seats: int
    range_km: int
    category: str
    rating: str              # rodzina uprawnien zalogi: EJET, EJET_E2, B737, B787...
    cabin: tuple[int, int, int]   # J, PremiumEconomy, Y
    cost_proxy: str
    cost_scale: float
    cabin_crew: int
    note: str


@dataclass(frozen=True, slots=True)
class RotationLeg:
    """Zaobserwowany odcinek w lancuchu doby.

    Uwaga z linii 163-165 pliku zrodlowego: znak rejestracyjny NIE nalezy do
    lancucha -- ten sam ciag odcinkow moze wykonac dowolna sprawna maszyna tego
    typu. To jest dokladnie semantyka SWAP-a i node 07 musi ja uszanowac.
    """

    number: str
    std_minute: int          # minuta doby lokalnej, z obserwacji
    block_min: int | None    # None gdy w obserwacji zabraklo czasu przylotu


class LotDB:
    """Zdekodowana baza z `loops.jsx`."""

    def __init__(self, raw: dict[str, Any], source: Path | None = None) -> None:
        self.raw = raw
        self.source = source

    # ---- ladowanie ----

    @classmethod
    def load(cls, path: Path | str | None = None) -> "LotDB":
        jsx = Path(path) if path else _find_jsx()
        return cls(_extract_db(jsx.read_text(encoding="utf-8")), jsx)

    @property
    def version(self) -> str:
        return str(self.raw.get("v", "?"))

    @property
    def generated(self) -> str:
        return str(self.raw.get("gen", "?"))

    # ---- porty ----

    @cached_property
    def ports(self) -> dict[str, Port]:
        out: dict[str, Port] = {}
        for iata, row in self.raw["L"].items():
            raw_curfew = row[L_CURFEW]
            curfew = None
            if isinstance(raw_curfew, list) and len(raw_curfew) >= 4:
                curfew = Curfew(
                    start_min=_hm(raw_curfew[0]),
                    end_min=_hm(raw_curfew[1]),
                    kind=int(raw_curfew[2]),
                    confirmed=bool(raw_curfew[3]),
                )
            out[iata] = Port(
                iata=iata,
                lat=float(row[L_LAT]), lon=float(row[L_LON]), tz=str(row[L_TZ]),
                eu=bool(row[L_EU]), schengen=bool(row[L_SCHENGEN]),
                eu261=bool(row[L_EU261]), slot_level=int(row[L_SLOT]),
                name=str(row[L_NAME]), curfew=curfew,
                mct=dict(row[L_MCT]),
            )
        return out

    # ---- siatka ----

    @cached_property
    def routes(self) -> dict[tuple[str, str], Route]:
        out: dict[tuple[str, str], Route] = {}
        for row in self.raw["T"]:
            route = Route(
                origin=row[T_O], dest=row[T_D], km=int(row[T_KM]),
                eu261_tier=str(row[T_TIER]), block_min=int(row[T_BLOCK]),
                dominant_type=str(row[T_TYPE]), sector=str(row[T_SECTOR]),
                cabins=str(row[T_CABINS]), numbers=tuple(row[T_NUMBERS]),
                type_counts=dict(row[T_TYPES]), operations=int(row[T_OPS]),
            )
            out[(route.origin, route.dest)] = route
        return out

    @cached_property
    def flights(self) -> dict[str, ScheduledFlight]:
        out: dict[str, ScheduledFlight] = {}
        for row in self.raw["R"]:
            out[row[R_NR]] = ScheduledFlight(
                number=row[R_NR], origin=row[R_O], dest=row[R_D],
                std_local=row[R_STD], sta_local=row[R_STA],
                arrives_next_day=bool(row[R_DAYOFF]),
                weekday_mask=str(row[R_MASK]), observations=int(row[R_OBS]),
                registrations=tuple(row[R_REGS]),
            )
        return out

    @cached_property
    def fleet(self) -> dict[str, FleetAircraft]:
        out: dict[str, FleetAircraft] = {}
        for row in self.raw["F"]:
            livery = row[F_LIVERY]
            out[row[F_REG]] = FleetAircraft(
                reg=row[F_REG], type_code=row[F_TYPE],
                wet_lease=bool(row[F_WETLEASE]), operator=str(row[F_OPERATOR]),
                seats=int(row[F_SEATS]),
                livery=livery if isinstance(livery, str) else None,
                operations=int(row[F_OPS]) if len(row) > F_OPS else 0,
            )
        return out

    @cached_property
    def types(self) -> dict[str, TypeSpec]:
        out: dict[str, TypeSpec] = {}
        for code, row in self.raw["TY"].items():
            cabin = tuple(row[TY_CABIN]) if isinstance(row[TY_CABIN], list) else (0, 0, 0)
            out[code] = TypeSpec(
                code=code, name=row[TY_NAME], seats=int(row[TY_SEATS]),
                range_km=int(row[TY_RANGE]), category=row[TY_CAT],
                # Dopelnienie zerami: baza podaje czasem sam podzial J/Y bez
                # premium economy, a kontrakt oczekuje zawsze trzech pozycji.
                rating=row[TY_RATING], cabin=(*cabin, 0, 0, 0)[:3],
                cost_proxy=row[TY_PROXY], cost_scale=float(row[TY_SCALE]),
                cabin_crew=int(row[TY_CC]),
                note=row[-1] if isinstance(row[-1], str) else "",
            )
        return out

    @cached_property
    def rotations(self) -> dict[str, dict[int, tuple[RotationLeg, ...]]]:
        """rejestracja -> dzien tygodnia (0=pon) -> lancuch odcinkow."""
        out: dict[str, dict[int, tuple[RotationLeg, ...]]] = {}
        for reg, by_day in self.raw["ROT"].items():
            days: dict[int, tuple[RotationLeg, ...]] = {}
            for day_key, legs in by_day.items():
                days[int(day_key)] = tuple(
                    RotationLeg(
                        number=leg[0],
                        std_minute=int(leg[1]),
                        block_min=int(leg[2]) if leg[2] is not None else None,
                    )
                    for leg in legs
                )
            out[reg] = days
        return out

    @cached_property
    def turnarounds(self) -> dict[str, dict[str, tuple[int, int]]]:
        """typ -> sektor -> (czas rekomendowany, minimum zaobserwowane).

    Wartosci policzone z rzeczywistych par ATA/ATD, nie z podrecznika.
    """
        return {
            code: {sector: (int(vals[0]), int(vals[1])) for sector, vals in sectors.items()}
            for code, sectors in self.raw["TU"].items()
        }

    # ---- prawo i parametry ----

    @property
    def eu261(self) -> dict[str, Any]:
        return self.raw["EU"]

    @property
    def ftl(self) -> dict[str, Any]:
        return self.raw["FT"]

    @property
    def costs(self) -> dict[str, Any]:
        """Sekcja K -- stawki w EUR, kazdy blok z polem `status`."""
        return self.raw["K"]

    @property
    def config(self) -> dict[str, Any]:
        return self.raw["CF"]

    @property
    def legal(self) -> list[list[Any]]:
        return self.raw["LG"]

    @property
    def delay_codes(self) -> dict[str, list[Any]]:
        return self.raw["KO"]

    @property
    def ssr(self) -> dict[str, list[Any]]:
        return self.raw["SS"]

    @property
    def booking_classes(self) -> dict[str, list[Any]]:
        return self.raw["KL"]

    @property
    def tiers(self) -> dict[str, list[Any]]:
        return self.raw["ST"]

    @property
    def transfer_levels(self) -> dict[str, list[Any]]:
        return self.raw["TF"]

    @property
    def partners(self) -> dict[str, list[Any]]:
        return self.raw["PT"]

    @property
    def onward(self) -> dict[str, list[list[Any]]]:
        return self.raw["ON"]

    @property
    def sources(self) -> dict[str, Any]:
        return self.raw["SRC"]

    @property
    def eur_pln(self) -> float:
        return float(self.costs["fx"]["EUR_PLN"])

    # ---- pochodne ----

    def delay_code_class(self, code: str) -> str:
        """'c' przewoznik | 'n' nadzwyczajne | 'd' reakcyjne | '?' nieznane.

        Ta litera decyduje o prawdopodobienstwie odszkodowania z Art. 7
        (EU.rules: carrier 1.0, case 0.5, extraordinary 0.0).
        """
        row = self.delay_codes.get(str(code))
        return str(row[KO_CLASS]) if row else "?"

    def compensation_probability(self, code: str) -> float:
        return {"c": 1.0, "n": 0.0, "d": 0.5}.get(self.delay_code_class(code), 0.5)

    def eu261_tier_for(self, km: float, intra_community: bool) -> str:
        """Regula z EU.tierRule -- przepisana wprost, nie z dystansu samego."""
        if km <= 1500:
            return "A"
        if intra_community or km <= 3500:
            return "B"
        return "C"

    def compensation_eur(self, tier: str) -> int:
        for row in self.eu261["tiers"]:
            if row["tier"] == tier:
                return int(row["compensation_eur"])
        raise KeyError(f"nieznany tier EU261: {tier}")

    def care_threshold_min(self, tier: str) -> int:
        for row in self.eu261["tiers"]:
            if row["tier"] == tier:
                return int(row["care_threshold_min"])
        raise KeyError(f"nieznany tier EU261: {tier}")

    def max_fdp_min(self, report_local_min: int, sectors: int) -> int:
        """Maksymalny FDP wg tabeli EASA: godzina zgloszenia x liczba odcinkow.

        Odwzorowanie `maxFDP` z linii 882-890: indeks kolumny to
        `min(max(sektory,2),10) - 2`, wiersz to pasmo godziny zgloszenia.
        """
        column = max(0, min(8, min(sectors, 10) - 2))
        minute = report_local_min % 1440
        for start, end, table in self.ftl["bands"]:
            a, b = _hm(start), _hm(end)
            inside = (a <= minute < b) if a < b else (minute >= a or minute < b)
            if inside:
                return int(table[column])
        return int(self.ftl["bands"][0][2][column])

    def flights_on(self, weekday: int) -> list[ScheduledFlight]:
        return [f for f in self.flights.values() if f.operates_on(weekday)]

    def summary(self) -> dict[str, Any]:
        return {
            "wersja": self.version,
            "wygenerowano": self.generated,
            "porty": len(self.ports),
            "trasy": len(self.routes),
            "numery_rejsow": len(self.flights),
            "flota": len(self.fleet),
            "typy": len(self.types),
            "rotacje_maszyn": len(self.rotations),
            "kody_opoznien": len(self.delay_codes),
            "kody_ssr": len(self.ssr),
            "klasy_rezerwacyjne": len(self.booking_classes),
            "partnerzy": len(self.partners),
            "podstawy_prawne": len(self.legal),
        }


def _hm(value: str) -> int:
    hours, _, minutes = value.partition(":")
    return int(hours) * 60 + int(minutes)


_CACHE: LotDB | None = None


def load_lot_db(path: Path | str | None = None, refresh: bool = False) -> LotDB:
    """Zaladuj baze raz na proces."""
    global _CACHE
    if _CACHE is None or refresh or path is not None:
        _CACHE = LotDB.load(path)
    return _CACHE
