"""Node 09 -- COST ENGINE.

Skladniki z tablicy: offload i odszkodowania, opieka (hotel, catering,
transport), rebooking na OAL, zaloga (nadgodziny, hotel, deadhead), koszt
opoznienia w siatce, roznica paliwa przy zmianie typu.

DWA TRYBY LICZENIA (box poboczny przy COST ENGINE)
  MODYFIKUJACE      (HOLD, CANCEL)  koszt = roznica wobec sytuacji bez zaklocenia
  RESTRUKTURYZUJACE (SWAP, SPLIT)   koszt = pelny nowy zestaw minus stary

Zmieszanie trybow sprawia, ze dwie opcje przestaja byc porownywalne: jedna
pokazuje delte, druga sume, a ranking porownuje jablka z gruszkami. Tryb
jest polem `CostBreakdown.mode` i wchodzi do raportu, zeby czlowiek widzial,
czym jest liczba, ktora czyta.

ODSZKODOWANIE JAKO KOSZT OCZEKIWANY
Art. 7 wchodzi jako `kwota x liczba pax x p(klasa kodu opoznienia)`, gdzie p
wynosi 1.0 dla odpowiedzialnosci przewoznika, 0.0 dla okolicznosci
nadzwyczajnej i 0.5 dla kodu reakcyjnego. To NIE jest to samo co wpisanie
odszkodowania w koszty i pozwolenie silnikowi je optymalizowac -- prawo nadal
odrzuca opcje w node 12. Tutaj jest tylko wycena ekspozycji.

OPIEKA JEST KOSZTEM PEWNYM
Art. 9 obowiazuje od progu NIEZALEZNIE od przyczyny. Nawet przy okolicznosci
nadzwyczajnej, gdy odszkodowanie nie przysluguje, opieka przysluguje.
"""

from __future__ import annotations

from ..adapters.lot_db import load_lot_db
from ..kernel.contracts import (
    CostBreakdown, Disruption, Option, PaxOutcomeKind, Snapshot,
)
from ..kernel.geo import haversine_km
from ..kernel.money import Money
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.pricing import pricing


class KosztNode(Node):
    id = "09"
    name = "koszt"
    title = "COST ENGINE"
    consumes = ("snapshot", "disruption", "options")
    produces = "costs"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        disruption: Disruption = ctx.require("disruption")
        options: tuple[Option, ...] = ctx.require("options")
        db = load_lot_db()
        price = pricing()
        report = self.new_report()

        flight = snap.flights[disruption.flight_id]
        tier = _tier(snap, db, flight)
        region = _region(snap, flight)
        sector = _sector(db, flight)
        probability = db.compensation_probability(_code(disruption))
        care_threshold = price.care_threshold_min(tier)

        costs: dict[str, CostBreakdown] = {}
        rows: list[dict[str, object]] = []

        for option in options:
            components: dict[str, Money] = {}

            # ---- opoznienie w siatce ----
            delay_cost = Money.zero()
            for fid, minutes in option.delay_min.items():
                target = snap.flights.get(fid)
                if target is not None and minutes > 0:
                    delay_cost = delay_cost + price.delay_total(target.type_code, minutes)
            if delay_cost.minor:
                components["opoznienie_w_siatce"] = delay_cost

            # ---- opieka (Art. 9) -- koszt pewny od progu ----
            care = Money.zero()
            compensable = 0
            nights = 0
            for outcome in option.pax_outcomes.values():
                if not outcome.kind.needs_care:
                    continue
                if outcome.delay_min >= care_threshold or outcome.care_nights:
                    care = care + price.care_per_pax(
                        outcome.delay_min, outcome.care_nights, region)
                    nights += outcome.care_nights
                if _is_compensable(outcome, price):
                    compensable += 1
            if care.minor:
                components["opieka_art9"] = care

            # ---- odszkodowanie (Art. 7) jako koszt oczekiwany ----
            if compensable and probability > 0:
                reduced = _reroute_within_window(option, price, tier)
                unit = (price.compensation_reduced(tier) if reduced
                        else price.compensation(tier))
                components["odszkodowanie_art7"] = unit * compensable * probability

            # ---- offload ----
            involuntary = sum(1 for o in option.pax_outcomes.values()
                              if o.kind is PaxOutcomeKind.OFFLOADED_INVOLUNTARY)
            voluntary = sum(1 for o in option.pax_outcomes.values()
                            if o.kind is PaxOutcomeKind.OFFLOADED_VOLUNTARY)
            if voluntary:
                components["rekompensata_ochotnikow"] = \
                    price.volunteer_voucher(tier) * voluntary
            if involuntary:
                # Odmowa wbrew woli: odszkodowanie natychmiast, bez mnoznika p.
                components["odmowa_przyjecia_art4"] = \
                    price.compensation(tier) * involuntary

            # ---- rebooking ----
            own = sum(1 for o in option.pax_outcomes.values()
                      if o.kind is PaxOutcomeKind.REBOOKED_OWN)
            oal = sum(1 for o in option.pax_outcomes.values()
                      if o.kind is PaxOutcomeKind.REBOOKED_OAL)
            if own:
                components["rebooking_wlasny_spill"] = price.rebook_own(sector) * own
            if oal:
                level = _best_partner_level(db, flight.arr)
                components["rozliczenie_interline"] = \
                    price.rebook_oal(sector, level, "Y") * oal

            # ---- zwroty przy kasacji ----
            refunds = sum(1 for o in option.pax_outcomes.values()
                          if o.kind is PaxOutcomeKind.CANCELLED_REFUND)
            if refunds and option.cancelled:
                slot = _slot_risk(snap, price, flight)
                if slot.minor:
                    components["ryzyko_serii_slotow"] = slot

            # ---- zaloga ----
            crew_cost = _crew_cost(snap, price, flight, option, nights)
            if crew_cost.minor:
                components["zaloga"] = crew_cost

            # ---- roznica paliwa przy zmianie typu ----
            if option.new_type:
                fuel = _fuel_delta(snap, price, option)
                if fuel.minor:
                    components["roznica_kosztu_typu"] = fuel

            # ---- ferry przy kasacji poza baza ----
            if option.cancelled and flight.arr != "WAW":
                spec = snap.aircraft_types.get(flight.type_code)
                category = spec.category if spec else ""
                components["pozycjonowanie"] = \
                    price.ferry_per_block_min(category) * flight.block_min

            # ---- roszczenia MC99 dla transferowych ----
            transfer = _transfer_pax(snap, option)
            if transfer and any(o.delay_min >= price.compensation_threshold_min
                                for o in option.pax_outcomes.values()):
                components["roszczenia_mc99"] = price.montreal_expected(transfer)

            breakdown = CostBreakdown(mode=option.kind, components=components)
            costs[option.id] = breakdown
            rows.append({
                "id": option.id,
                "tryb": option.kind.value,
                "koszt": breakdown.total,
                "najwieksze": [{"pozycja": k, "kwota": v} for k, v in breakdown.largest()],
                "pasazerow_z_odszkodowaniem": compensable,
                "noclegow": nights,
            })

        cheapest = min(rows, key=lambda r: r["koszt"].minor) if rows else None
        dearest = max(rows, key=lambda r: r["koszt"].minor) if rows else None

        report.summary = (
            f"Wyceniono {len(costs)} opcji. Kategoria EU261: {tier} "
            f"({price.compensation(tier)} na pasazera), prog opieki "
            f"{care_threshold} min, p(odszkodowanie) = {probability:.1f}. "
            + (f"Najtansza `{cheapest['id']}` ({cheapest['koszt']}), "
               f"najdrozsza `{dearest['id']}` ({dearest['koszt']})."
               if cheapest and dearest else "")
        )
        report.number("kategoria_eu261", tier)
        report.number("odszkodowanie_na_pasazera", price.compensation(tier), "PLN")
        report.number("prog_opieki", care_threshold, "min")
        report.number("prog_odszkodowania", price.compensation_threshold_min, "min")
        report.number("p_odszkodowania", probability)
        report.number("kurs_eur_pln", price.fx)
        if cheapest:
            report.number("koszt_najtanszej", cheapest["koszt"], "PLN")
            report.number("koszt_najdrozszej", dearest["koszt"], "PLN")

        report.findings["koszty_opcji"] = rows
        report.findings["tryby_liczenia"] = {
            "MODIFYING": "roznica wobec sytuacji bez zaklocenia",
            "RESTRUCTURING": "pelny nowy zestaw kosztow minus stary",
        }

        report.decide(
            f"opieka z Art. 9 wchodzi do kazdej opcji od {care_threshold} min "
            "NIEZALEZNIE od przyczyny -- to koszt pewny"
        )
        report.decide(
            f"odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: "
            f"kwota x liczba pax x {probability:.1f}"
        )
        if probability == 0.0:
            report.decide(
                "okolicznosc nadzwyczajna: ekspozycja z Art. 7 wynosi zero, "
                "ale opieka z Art. 9 nadal obowiazuje"
            )
        report.decide(
            "filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, "
            "node 12 usuwa opcje niedopuszczalne"
        )

        for field, source, confidence, note in price.assumptions():
            report.assume(field, source, confidence, note)
        report.data_gaps.append(
            "odsetek ochotnikow przy odmowie przyjecia (PoC) nie jest w bazie "
            "-- opcje z offloadem liczone sciezka 'wbrew woli', czyli najdrozsza"
        )

        return NodeOutput(report, {"costs": costs, "eu261_tier": tier})


# ---------------------------------------------------------------- pomocnicze


def _code(disruption: Disruption) -> str:
    detail = disruption.detail or ""
    return detail.rsplit(":", 1)[-1].strip() if ":" in detail else "41"


def _tier(snap: Snapshot, db, flight) -> str:
    a, b = snap.airports.get(flight.dep), snap.airports.get(flight.arr)
    if a is None or b is None:
        return "B"
    km = haversine_km(a.lat, a.lon, b.lat, b.lon)
    port_a, port_b = db.ports.get(flight.dep), db.ports.get(flight.arr)
    intra = bool(port_a and port_b and port_a.eu and port_b.eu)
    return db.eu261_tier_for(km, intra)


def _region(snap: Snapshot, flight) -> str:
    if flight.dep == "WAW":
        return "WAW"
    a, b = snap.airports.get(flight.dep), snap.airports.get(flight.arr)
    if a and b and haversine_km(a.lat, a.lon, b.lat, b.lon) > 3500:
        return "longhaul"
    return "europe"


def _sector(db, flight) -> str:
    route = db.routes.get((flight.dep, flight.arr))
    return route.sector if route else "europe"


def _best_partner_level(db, station: str) -> int:
    """Najkorzystniejszy poziom umowy wsrod partnerow w porcie."""
    levels = [int(row[1]) for row in db.partners.values()
              if len(row) > 2 and isinstance(row[2], list) and station in row[2]]
    return min(levels) if levels else 3


def _slot_risk(snap: Snapshot, price, flight) -> Money:
    port = snap.airports.get(flight.dep)
    return price.slot_series_risk(port.slot_level if port else 0)


def _crew_cost(snap: Snapshot, price, flight, option: Option, nights: int) -> Money:
    """Nadgodziny wg opoznienia rejsu plus nocleg zalogi, gdy pasazerowie nocuja."""
    minutes = option.delay_min.get(flight.id, 0)
    spec = snap.aircraft_types.get(flight.type_code)
    cabin = spec.cabin_crew if spec else 4
    cockpit = max(2, len(flight.crew_ids) - cabin)
    total = Money.zero()
    if minutes > 0:
        total = total + price.crew_overtime(minutes, cockpit, cabin)
    if nights > 0:
        total = total + price.crew_hotel_night * (cockpit + cabin)
    if option.aircraft_swap:
        total = total + price.standby_callout
    return total


def _fuel_delta(snap: Snapshot, price, option: Option) -> Money:
    """Roznica kosztu minuty miedzy starym a nowym typem, na czas bloku."""
    total = Money.zero()
    for flight_id, new_code in option.new_type.items():
        flight = snap.flights.get(flight_id)
        if flight is None or new_code == flight.type_code:
            continue
        old = price.delay_minute(flight.type_code, 30) * flight.block_min
        new = price.delay_minute(new_code, 30) * flight.block_min
        total = total + (new - old)
    return total


def _transfer_pax(snap: Snapshot, option: Option) -> int:
    count = 0
    for pax_id in option.pax_outcomes:
        pax = snap.passengers.get(pax_id)
        itin = snap.itineraries.get(pax.itinerary_id) if pax else None
        if itin and len(itin.segments) > 1:
            count += 1
    return count


def _is_compensable(outcome, price) -> bool:
    """Czy temu pasazerowi nalezy sie odszkodowanie z Art. 7.

    Dwie rozne podstawy i dwa rozne progi -- mylenie ich zanizalo koszt
    kasacji tak bardzo, ze silnik zaczynal ja rekomendowac:

    * OPOZNIENIE (Art. 6 + C-402/07 Sturgeon): dopiero od 3 h na PRZYLOCIE.
    * ODWOLANIE (Art. 5 ust. 1 lit. c): za sam fakt odwolania, BEZ progu
      czasowego. Zwolnienie przysluguje tylko przy powiadomieniu z 14-dniowym
      wyprzedzeniem albo przy zmianie planu w waskich oknach z Art. 5 --
      w IROPS, z definicji nagłym, zaden z tych warunkow nie zachodzi.
    * ODMOWA PRZYJECIA (Art. 4): natychmiast, liczona osobna pozycja.
    """
    if outcome.kind is PaxOutcomeKind.CANCELLED_REFUND:
        return True
    return outcome.delay_min >= price.compensation_threshold_min


def _reroute_within_window(option: Option, price, tier: str) -> bool:
    """Art. 7 ust. 2: obnizka o 50% przy zmianie planu w oknie kategorii."""
    if not option.pax_outcomes:
        return False
    window = price.reroute_window_min(tier)
    rerouted = [o for o in option.pax_outcomes.values()
                if o.kind in (PaxOutcomeKind.REBOOKED_OWN, PaxOutcomeKind.REBOOKED_OAL)]
    if not rerouted:
        return False
    return all(o.delay_min <= window for o in rerouted)
