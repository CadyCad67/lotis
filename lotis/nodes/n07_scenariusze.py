"""Node 07 -- SCENARIO ENGINE.

Generuje mozliwe rozwiazania. Katalog nie jest wymyslony: baza ma sekcje `SZ`
z osmioma opcjami decyzyjnymi, kazda z warunkami wykonalnosci i skladnikami
kosztu. Ten node bierze te osiem, konfrontuje je z bramkami z node 05
i produkuje konkretne warianty osadzone w rzeczywistej dobie.

SWAP ZAWSZE JAKO PARA REJSOW (Blok 5 tablicy)
Rejs A oddaje samolot, rejs B go dostaje. Liczac sam rejs A, downgauge zawsze
wychodzi na minus -- tracisz miejsca i nic nie zyskujesz, wiec silnik nigdy by
tego nie wybral. Kontrakt `Option` wymusza obecnosc obu rejsow i wybucha, jesli
ktorys zabraknie.

Rejs B nie zarabia na SWAPie. On UNIKA STRATY: bez podmiany by nie polecial.

CZEGO TU NIE MA
Opcje `SPLIT` generujemy tylko wtedy, gdy baza dopuszcza ja przelacznikiem
(`CF.switches.allowSplit`), bo rozdzielanie pasazerow ma twarde zakazy --
rodzin, grup i maloletnich bez opieki rozdzielac nie wolno i zaden suwak
tego nie zmienia.
"""

from __future__ import annotations

from datetime import timedelta

from ..adapters.aircraft_perf import same_crew_rating, turnaround_min
from ..adapters.lot_db import load_lot_db
from ..kernel.contracts import (
    Disruption, Flight, Option, OptionKind, PaxOutcome, PaxOutcomeKind, Snapshot,
)
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.report import Status

#: Ile pozniejszych wlasnych rejsow rozwazamy przy rebookingu.
MAX_ALTERNATIVES = 4

#: Okno, w ktorym rebooking liczy sie jako "najblizsza okazja" (Art. 8).
SAME_DAY_WINDOW_H = 12


class ScenariuszeNode(Node):
    id = "07"
    name = "scenariusze"
    title = "SCENARIO ENGINE"
    consumes = ("snapshot", "disruption", "feasibility")
    produces = "options"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        disruption: Disruption = ctx.require("disruption")
        feasibility = ctx.require("feasibility")
        db = load_lot_db()
        report = self.new_report()

        flight = snap.flights[disruption.flight_id]
        delay = disruption.estimated_delay_min
        allowed = feasibility["allowed_kinds"]
        switches = {row[0]: bool(row[2]) for row in db.config.get("switches", [])}
        pax_ids = tuple(p.id for p in snap.passengers_on(flight.id))

        options: list[Option] = []
        skipped: list[dict[str, str]] = []

        # ---- 1. HOLD: opcja zero, czyli poczekaj i lec ----
        options.append(_hold(flight, delay, pax_ids))

        # ---- 2. SWAP: para rejsow ----
        if allowed.get("SWAP"):
            swaps = _swaps(snap, db, flight, delay, pax_ids)
            options.extend(swaps)
            if not swaps:
                skipped.append({"id": "SWAP", "powod": "brak pary rejsow do podmiany"})
        else:
            skipped.append({"id": "SWAP",
                            "powod": feasibility["gates"]["samolot"]["reason"]})

        # ---- 3. REBOOK-OWN: przenies na wlasny rejs ----
        if allowed.get("REBOOK-OWN"):
            alternatives = _own_alternatives(snap, flight)
            if alternatives:
                options.append(_rebook_own(flight, alternatives, pax_ids))
            else:
                skipped.append({"id": "REBOOK-OWN", "powod": "brak pozniejszego wlasnego rejsu"})
        else:
            skipped.append({"id": "REBOOK-OWN",
                            "powod": feasibility["gates"]["miejsca"]["reason"]})

        # ---- 4. REBOOK-OAL: przenies na przewoznika obcego ----
        if switches.get("allowOAL", True):
            options.append(_rebook_oal(snap, db, flight, pax_ids))
        else:
            skipped.append({"id": "REBOOK-OAL", "powod": "wylaczone przelacznikiem allowOAL"})

        # ---- 5. OVERNIGHT: nocleg i rejs nastepnego dnia ----
        options.append(_overnight(flight, pax_ids))

        # ---- 6. CANCEL: odwolaj rejs ----
        options.append(_cancel(snap, flight, _own_alternatives(snap, flight), pax_ids))

        # ---- 7. SPLIT: rozdziel pasazerow ----
        if switches.get("allowSplit", True) and allowed.get("SPLIT"):
            alternatives = _own_alternatives(snap, flight)
            if alternatives:
                        options.append(_split(snap, db, flight, alternatives, pax_ids))
        else:
            skipped.append({"id": "SPLIT", "powod": "wylaczone przelacznikiem albo brak miejsc"})

        report.summary = (
            f"Wygenerowano {len(options)} opcji dla rejsu {flight.number} "
            f"({len(pax_ids)} pasazerow, opoznienie {delay} min). "
            f"Odrzucono {len(skipped)} rodzajow przed wycena."
        )
        report.number("opcji", len(options), "szt")
        report.number("rodzajow_odrzuconych", len(skipped), "szt")
        report.number("pasazerow_dotknietych", len(pax_ids), "osob")
        report.number("modyfikujacych",
                      sum(1 for o in options if o.kind is OptionKind.MODIFYING), "szt")
        report.number("restrukturyzujacych",
                      sum(1 for o in options if o.kind is OptionKind.RESTRUCTURING), "szt")

        report.findings["opcje"] = [
            {"id": o.id, "label": o.label, "tryb": o.kind.value,
             "generator": o.generator, "rejsy": list(o.affected_flights),
             "opoznienia": o.delay_min, "kasowane": sorted(o.cancelled),
             "uwagi": list(o.notes)}
            for o in options
        ]
        report.findings["odrzucone_rodzaje"] = skipped

        report.decide(
            "SWAP wchodzi zawsze jako para rejsow -- rejs oddajacy i rejs "
            "otrzymujacy maszyne liczy sie razem"
        )
        report.decide(
            "opcje modyfikujace wycenia sie jako roznice wobec sytuacji bez "
            "zaklocenia, restrukturyzujace jako pelny nowy zestaw minus stary"
        )
        if len(options) < 2:
            report.status = Status.DEGRADED
            report.warn("mniej niz dwie opcje -- nie ma czego porownywac")

        return NodeOutput(report, {"options": tuple(options)})


# ---------------------------------------------------------------- generatory


def _hold(flight: Flight, delay: int, pax_ids: tuple[str, ...]) -> Option:
    return Option(
        id="HOLD",
        kind=OptionKind.MODIFYING,
        generator="SZ.HOLD",
        label=f"Wstrzymaj odlot o {delay} min",
        affected_flights=(flight.id,),
        delay_min={flight.id: delay},
        pax_outcomes={p: PaxOutcome(PaxOutcomeKind.DELAYED, delay_min=delay)
                      for p in pax_ids},
        notes=("koszt = minuty x stawka krancowa typu + propagacja",
               "ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie"),
    )


def _swaps(snap: Snapshot, db, flight: Flight, delay: int,
           pax_ids: tuple[str, ...]) -> list[Option]:
    """Podmiana z maszyna stojaca w tym samym porcie.

    Rejs B to najblizszy odlot maszyny-dawcy z tego portu. Bez niego SWAP nie
    ma pary i kontrakt `Option` odrzucilby taka opcje.
    """
    out: list[Option] = []
    turn = turnaround_min(flight.type_code, "europe")[1]

    for reg, aircraft in sorted(snap.aircraft.items()):
        if reg == flight.aircraft_reg or aircraft.position != flight.dep:
            continue
        fleet_row = db.fleet.get(reg)
        if fleet_row is None or fleet_row.wet_lease:
            continue
        if not same_crew_rating(aircraft.type_code, flight.type_code):
            continue

        donor = _next_departure(snap, reg, flight.dep, flight.std)
        if donor is None:
            continue

        spec_new = snap.aircraft_types.get(aircraft.type_code)
        spec_old = snap.aircraft_types.get(flight.type_code)
        gauge = (spec_new.seats_total if spec_new else 0) - \
                (spec_old.seats_total if spec_old else 0)

        # Rejs A odlatuje po minimalnym postoju, rejs B przejmuje opoznienie.
        offloaded = max(0, len(pax_ids) - (spec_new.seats_total if spec_new else len(pax_ids)))
        outcomes: dict[str, PaxOutcome] = {}
        for index, pax in enumerate(pax_ids):
            if index < len(pax_ids) - offloaded:
                outcomes[pax] = PaxOutcome(PaxOutcomeKind.DELAYED, delay_min=turn)
            else:
                outcomes[pax] = PaxOutcome(PaxOutcomeKind.OFFLOADED_INVOLUNTARY,
                                           delay_min=delay)

        out.append(Option(
            id=f"SWAP-{reg}",
            kind=OptionKind.RESTRUCTURING,
            generator="SZ.SWAP",
            label=f"Podmien maszyne na {reg} ({aircraft.type_code})",
            affected_flights=(flight.id, donor.id),
            delay_min={flight.id: turn, donor.id: delay},
            pax_outcomes=outcomes,
            aircraft_swap=(flight.id, donor.id),
            new_type={flight.id: aircraft.type_code, donor.id: flight.type_code},
            resources=(f"SPARE_AIRCRAFT@{flight.dep}",),
            notes=(
                f"zmiana pojemnosci {gauge:+d} miejsc",
                f"rejs {donor.number} przejmuje opoznienie {delay} min",
                "rejs otrzymujacy maszyne nie zarabia -- unika straty",
            ) + ((f"downgauge: {offloaded} pasazerow schodzi",) if offloaded else ()),
        ))
        if len(out) >= 3:
            break
    return out


def _rebook_own(flight: Flight, alternatives: list[Flight],
                pax_ids: tuple[str, ...]) -> Option:
    target = alternatives[0]
    wait = int((target.std - flight.std).total_seconds() // 60)
    return Option(
        id="REBOOK-OWN",
        kind=OptionKind.RESTRUCTURING,
        generator="SZ.REBOOK-OWN",
        label=f"Przenies na wlasny rejs {target.number} (+{wait} min)",
        affected_flights=(flight.id, target.id),
        delay_min={},
        cancelled=frozenset({flight.id}),
        pax_outcomes={p: PaxOutcome(PaxOutcomeKind.REBOOKED_OWN, delay_min=wait)
                      for p in pax_ids},
        notes=("koszt = utracona sprzedaz miejsca (spill), nie pelna taryfa",
               f"czekanie {wait} min liczy sie do progu opieki z Art. 9"),
    )


def _rebook_oal(snap: Snapshot, db, flight: Flight, pax_ids: tuple[str, ...]) -> Option:
    """Rebooking na przewoznika obcego.

    CZAS OCZEKIWANIA JEST TU NAJWAZNIEJSZA LICZBA
    Nie dlatego, ze pasazer czeka, tylko dlatego, ze prog 3 h z Art. 7 lezy
    dokladnie w srodku prawdopodobnego zakresu. Oczekiwanie 179 minut kosztuje
    zero odszkodowania, oczekiwanie 181 minut kosztuje pelna kwote razy liczba
    pasazerow -- przy 61 osobach to skok o 65 tysiecy zlotych na jednej minucie.

    Dlatego ta liczba NIE moze byc zgadnieta. Bierzemy ja z `CF.onward.next_bank_min`
    bazy: czas do nastepnej fali odlotow zalezny od czestotliwosci relacji
    (3 rejsy dziennie -> 420 min, 2 -> 600, 1 -> 900), powiekszony o
    `partner_mct_extra` -- przesiadka miedzy przewoznikami wymaga wiecej czasu,
    bo bywa inny terminal i ponowna odprawa bagazu.

    Wczesniej stalo tu 150 -- liczba, ktora sama wymyslilem, lezaca tuz pod
    progiem. To ona, a nie zadne dane, czynila te opcje najlepsza.
    """
    partners = [c for c, row in db.partners.items()
                if len(row) > 2 and isinstance(row[2], list) and flight.arr in row[2]]
    wait, frequency = _oal_wait(snap, db, flight)

    return Option(
        id="REBOOK-OAL",
        kind=OptionKind.RESTRUCTURING,
        generator="SZ.REBOOK-OAL",
        label=f"Przenies na przewoznika obcego do {flight.arr}",
        affected_flights=(flight.id,),
        cancelled=frozenset({flight.id}),
        pax_outcomes={p: PaxOutcome(PaxOutcomeKind.REBOOKED_OAL, delay_min=wait)
                      for p in pax_ids},
        resources=tuple(f"PARTNER_SEATS@{flight.arr}" for _ in partners[:1]),
        notes=("doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio",
               "mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)",
               (f"oczekiwanie {wait} min z CF.onward.next_bank_min "
                f"({frequency} rejsow dziennie na tej relacji) + MCT partnera"),
               f"partnerzy w porcie docelowym: {', '.join(partners[:5]) or 'brak'}"),
    )


def _overnight(flight: Flight, pax_ids: tuple[str, ...]) -> Option:
    return Option(
        id="OVERNIGHT",
        kind=OptionKind.RESTRUCTURING,
        generator="SZ.OVERNIGHT",
        label="Nocleg i rejs nastepnego dnia",
        affected_flights=(flight.id,),
        cancelled=frozenset({flight.id}),
        pax_outcomes={p: PaxOutcome(PaxOutcomeKind.REBOOKED_OWN,
                                    delay_min=14 * 60, care_nights=1)
                      for p in pax_ids},
        notes=("pelna opieka: hotel, posilki, transport",
               "pelna ekspozycja EU261 przy klasie kodu przewoznika",
               "nocleg zalogi dochodzi osobno"),
    )


def _cancel(snap: Snapshot, flight: Flight, alternatives: list[Flight],
            pax_ids: tuple[str, ...]) -> Option:
    """Odwolanie rejsu.

    `delay_min` NIE jest zerem. Pasazer odwolanego rejsu czeka do najblizszej
    realnej mozliwosci wylotu, a linia placi opieke przez caly ten czas.
    Ustawienie zera sprawialo, ze kasacja wygladala na najtansza opcje --
    bo nie generowala ani opieki, ani ekspozycji odszkodowawczej. To jest
    dokladnie ta patologia, przed ktora ostrzega Blok 5 tablicy, tylko wzieta
    od drugiej strony.
    """
    if alternatives:
        wait = int((alternatives[0].std - flight.std).total_seconds() // 60)
        nights = 0
    else:
        wait = 14 * 60          # najblizszy rejs nastepnego dnia
        nights = 1
    return Option(
        id="CANCEL",
        kind=OptionKind.MODIFYING,
        generator="SZ.CANCEL",
        label="Odwolaj rejs",
        affected_flights=(flight.id,),
        cancelled=frozenset({flight.id}),
        pax_outcomes={p: PaxOutcome(PaxOutcomeKind.CANCELLED_REFUND,
                                    delay_min=wait, care_nights=nights)
                      for p in pax_ids},
        notes=("Art. 5: prawo wyboru zwrotu albo zmiany planu",
               ("Art. 5 ust. 1 lit. c: odszkodowanie nalezy sie za SAM fakt "
                "odwolania, bez progu opoznienia"),
               "pelna opieka przez czas oczekiwania (Art. 9)",
               "pelna utrata przychodu z pasazerow nieprzebukowanych",
               "przestawienie rotacji na kolejne odcinki"),
    )


def _split(snap: Snapshot, db, flight: Flight, alternatives: list[Flight],
           pax_ids: tuple[str, ...]) -> Option:
    """Polowa na wlasny rejs, polowa na obcego.

    Czas oczekiwania czesci przekazanej obcemu przewoznikowi liczy sie TAK SAMO
    jak w `REBOOK-OAL`. Gdy stala tu inna liczba, ta sama operacja byla
    wyceniana dwoma sposobami w dwoch opcjach, a SPLIT wygrywal ranking
    wylacznie dlatego, ze jego polowa OAL korzystala z korzystniejszego
    zalozenia.

    Zakazy rozdzielania -- rodzin, grup i maloletnich bez opieki -- sprawdza
    filtr prawny w node 12. Tutaj wariant powstaje, tam moze odpasc.
    """
    target = alternatives[0]
    wait_own = int((target.std - flight.std).total_seconds() // 60)
    wait_oal, _ = _oal_wait(snap, db, flight)
    half = len(pax_ids) // 2
    outcomes: dict[str, PaxOutcome] = {}
    for index, pax in enumerate(pax_ids):
        if index < half:
            outcomes[pax] = PaxOutcome(PaxOutcomeKind.REBOOKED_OWN, delay_min=wait_own)
        else:
            outcomes[pax] = PaxOutcome(PaxOutcomeKind.REBOOKED_OAL, delay_min=wait_oal)
    return Option(
        id="SPLIT",
        kind=OptionKind.RESTRUCTURING,
        generator="SZ.SPLIT",
        label=f"Rozdziel: {half} na {target.number}, reszta na obcego",
        affected_flights=(flight.id, target.id),
        cancelled=frozenset({flight.id}),
        pax_outcomes=outcomes,
        notes=("koszt = suma kosztow skladowych",
               ("ZAKAZ rozdzielania rodzin, grup i maloletnich bez opieki "
                "-- sprawdza filtr prawny")),
    )


# ---------------------------------------------------------------- pomocnicze


def _oal_wait(snap: Snapshot, db, flight: Flight) -> tuple[int, int]:
    """Czas do wylotu u obcego przewoznika, wraz z czestotliwoscia relacji.

    NAJWAZNIEJSZA LICZBA W CALYM GENERATORZE
    Nie dlatego, ze pasazer czeka, tylko dlatego, ze prog 3 h z Art. 7 jest
    skokowy. Oczekiwanie 179 minut kosztuje zero odszkodowania, oczekiwanie
    181 minut kosztuje pelna kwote razy liczba pasazerow -- przy szescdziesieciu
    osobach to kilkadziesiat tysiecy zlotych zawieszone na dwoch minutach.

    Dlatego nie moze byc zgadnieta. Pochodzi z `CF.onward.next_bank_min`:
    czas do nastepnej fali odlotow wedlug czestotliwosci relacji (3 rejsy
    dziennie -> 420 min, 2 -> 600, 1 -> 900), powiekszony o `partner_mct_extra`,
    bo przesiadka miedzy przewoznikami wymaga wiecej czasu.

    Zwraca (minuty, czestotliwosc) -- oba trafiaja do raportu, zeby czlowiek
    widzial, skad wzieta jest liczba, ktora decyduje o rankingu.
    """
    frequency = sum(1 for f in snap.flights.values()
                    if f.dep == flight.dep and f.arr == flight.arr)
    onward = db.config.get("onward", {})
    banks = onward.get("next_bank_min", {"1": 900})
    key = str(min(3, max(1, frequency)))
    wait = int(banks.get(key, banks["1"])) + int(onward.get("partner_mct_extra", 25))
    return wait, frequency


def _own_alternatives(snap: Snapshot, flight: Flight) -> list[Flight]:
    """Pozniejsze wlasne rejsy w tej samej relacji, z wolnymi miejscami."""
    seated: dict[str, int] = {}
    for pax in snap.passengers.values():
        itin = snap.itineraries.get(pax.itinerary_id)
        for segment in (itin.segments if itin else ()):
            seated[segment] = seated.get(segment, 0) + 1

    horizon = flight.std + timedelta(hours=SAME_DAY_WINDOW_H)
    out: list[Flight] = []
    for other in snap.flights.values():
        if other.id == flight.id or other.dep != flight.dep or other.arr != flight.arr:
            continue
        if not (flight.std < other.std <= horizon):
            continue
        spec = snap.aircraft_types.get(other.type_code)
        if spec and seated.get(other.id, 0) < spec.seats_total:
            out.append(other)
    return sorted(out, key=lambda f: f.std)[:MAX_ALTERNATIVES]


def _next_departure(snap: Snapshot, reg: str, station: str, after) -> Flight | None:
    """Najblizszy odlot danej maszyny z danego portu -- to jest rejs B SWAPu."""
    candidates = [f for f in snap.flights.values()
                  if f.aircraft_reg == reg and f.dep == station and f.std > after]
    return min(candidates, key=lambda f: f.std) if candidates else None
