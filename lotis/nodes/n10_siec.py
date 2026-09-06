"""Node 10 -- NETWORK IMPACT.

Kolejne odcinki tego samolotu, przesiadki, kolejne odcinki zalogi. Horyzont
z tablicy: do konca doby operacyjnej albo do powrotu samolotu do bazy, co
nastapi pierwsze. Definicja siedzi w `kernel.horizon`, wiec node 10 i node 13
licza ja tak samo.

DLACZEGO PROPAGACJA NIE JEST LINIOWA
Opoznienie nie przechodzi na kolejny odcinek w calosci. Zjada je bufor postoju:
jesli maszyna ma 60 minut przerwy, a minimalny postoj to 35, to 25 minut
opoznienia wchlania sie bez sladu. Liczenie propagacji jeden do jednego
zawyzaloby koszt kazdej opcji opoznieniowej.

Wczesniejsza analiza danych pokazala, ze mediana bufora w tej siatce wynosi
12 minut, a 10.5% postojow jest ponizej minimum typu -- czyli realnej zdolnosci
absorpcji jest malo i propagacja bywa niemal pelna.
"""

from __future__ import annotations

from ..adapters.aircraft_perf import turnaround_min
from ..adapters.lot_db import load_lot_db
from ..kernel.contracts import NetworkImpact, Option, Snapshot
from ..kernel.horizon import connecting_passengers, downstream_flights
from ..kernel.money import Money
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.pricing import pricing

HOME_BASE = "WAW"


class SiecNode(Node):
    id = "10"
    name = "siec"
    title = "NETWORK IMPACT"
    consumes = ("snapshot", "disruption", "options")
    produces = "network"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        disruption = ctx.require("disruption")
        options: tuple[Option, ...] = ctx.require("options")
        db = load_lot_db()
        price = pricing()
        report = self.new_report()

        source = snap.flights[disruption.flight_id]
        horizon = downstream_flights(snap, source.id, HOME_BASE)
        transfer_pax = connecting_passengers(snap, source.id)

        impacts: dict[str, NetworkImpact] = {}
        extra_cost: dict[str, Money] = {}
        rows: list[dict[str, object]] = []

        for option in options:
            initial = option.delay_min.get(source.id, 0)
            propagated: dict[str, int] = {}
            dotkniete: list[str] = []
            powody: set[str] = set()
            stranded = 0

            # Propagacja idzie od KAZDEGO opoznionego rejsu, nie tylko od
            # zrodlowego. SWAP opoznia rejs B o cale opoznienie, a jego dalsze
            # odcinki dziedziczyly zero, bo horyzont liczyl sie wylacznie od
            # rejsu A. Na SWAP-SP-LID rejs B mial szesc odcinkow ponizej i zaden
            # nie wchodzil do kosztu -- czyli opcja, ktora silnik najchetniej
            # rekomenduje, byla systematycznie zanizana.
            zrodla = dict(option.delay_min)
            zrodla.setdefault(source.id, initial)

            for flight_id, minutes in sorted(zrodla.items()):
                start = snap.flights.get(flight_id)
                if start is None:
                    continue
                zasieg = downstream_flights(snap, flight_id, HOME_BASE)
                powody.add(zasieg.stop_reason)
                dotkniete.extend(f.id for f in zasieg.flights)

                if flight_id in option.cancelled:
                    # Kasacja nie propaguje opoznienia, ale zostawia maszyne
                    # w zlym porcie: kolejne odcinki rotacji traca podstawienie.
                    # Tablica nazywa to "przestawieniem rotacji" i wymienia jako
                    # skladnik kosztu CANCEL.
                    for f in zasieg.flights:
                        propagated.setdefault(f.id, 0)
                    stranded += len(zasieg.flights)
                    continue

                for f, minut in _propagate(snap, db, start, zasieg.flights, minutes).items():
                    # Rejs moze lezec ponizej dwoch opoznionych rejsow naraz
                    # (para SWAPu). Liczy sie wieksze opoznienie, nie suma.
                    propagated[f] = max(propagated.get(f, 0), minut)

            for flight_id in option.cancelled:
                if flight_id in zrodla:
                    continue
                zasieg = downstream_flights(snap, flight_id, HOME_BASE)
                powody.add(zasieg.stop_reason)
                dotkniete.extend(f.id for f in zasieg.flights)
                for f in zasieg.flights:
                    propagated.setdefault(f.id, 0)
                stranded += len(zasieg.flights)

            missed = _missed_connections(snap, option, transfer_pax, initial)
            unikalne = sorted(set(dotkniete))
            affected = sum(len(snap.passengers_on(f)) for f in unikalne)

            cost = Money.zero()
            for flight_id, minutes in propagated.items():
                target = snap.flights.get(flight_id)
                if target is not None and minutes > 0:
                    cost = cost + price.delay_total(target.type_code, minutes)

            if stranded:
                cost = cost + _reposition_cost(snap, price, source, horizon.flights)

            impact = NetworkImpact(
                downstream_flights=tuple(unikalne),
                stop_reason=(horizon.stop_reason if len(powody) <= 1
                             else "+".join(sorted(powody))),
                delay_propagated_min=propagated,
                connections_missed=missed,
                pax_affected=affected,
                crew_over_fdp=_crew_over_fdp(snap, source, initial),
            )
            impacts[option.id] = impact
            extra_cost[option.id] = cost
            rows.append({
                "id": option.id,
                "odcinkow_ponizej": len(unikalne),
                "suma_propagacji_min": sum(propagated.values()),
                "przesiadek_utraconych": missed,
                "koszt_propagacji": cost,
                "rejsow_bez_podstawienia": stranded,
            })

        report.summary = (
            f"Horyzont propagacji: {len(horizon.flights)} odcinkow, "
            f"zatrzymany na `{horizon.stop_reason}`. "
            f"{len(transfer_pax)} pasazerow transferowych na rejsie zrodlowym."
        )
        report.number("odcinkow_w_horyzoncie", len(horizon.flights), "szt")
        report.number("powod_zatrzymania", horizon.stop_reason)
        report.number("koniec_doby_operacyjnej", horizon.cutoff)
        report.number("pasazerow_transferowych", len(transfer_pax), "osob")
        report.number("zalogi_poza_fdp",
                      len(_crew_over_fdp(snap, source, disruption.estimated_delay_min)),
                      "osob")

        report.findings["horyzont"] = [
            {"id": f.id, "numer": f.number, "z": f.dep, "do": f.arr,
             "std": f.std, "bufor_min": _buffer(snap, db, f)}
            for f in horizon.flights
        ]
        report.findings["propagacja_wg_opcji"] = rows

        report.decide(
            f"horyzont konczy sie na `{horizon.stop_reason}` -- dalej opcje "
            "przestaja sie roznic i liczenie nie zmienia rankingu"
        )
        report.decide(
            "opoznienie propaguje sie pomniejszone o bufor postoju; "
            "bufor wieszy od opoznienia wchlania je w calosci"
        )
        if not horizon.flights:
            report.warn(
                "rejs zrodlowy nie ma odcinkow ponizej -- network impact wynosi zero "
                "i nie rozroznia opcji"
            )

        return NodeOutput(report, {"network": impacts, "network_cost": extra_cost})


def _reposition_cost(snap: Snapshot, price, source, downstream) -> Money:
    """Koszt przestawienia rotacji po odwolaniu rejsu.

    Maszyna zostaje tam, gdzie stoi. Zeby kolejne odcinki doszly do skutku,
    ktoras maszyna musi doleciec pusta -- a lot pozycjonujacy ma stawke za
    minute bloku w `K.cxl.ferry_flight_cost_per_block_min_eur`.

    Bez tej pozycji odwolanie wygladalo na operacje bez konsekwencji dla reszty
    doby, co jest nieprawda: to wlasnie zerwana rotacja jest najdrozszym
    skutkiem kasacji.
    """
    if not downstream:
        return Money.zero()
    spec = snap.aircraft_types.get(source.type_code)
    category = spec.category if spec else ""
    first = downstream[0]
    return price.ferry_per_block_min(category) * first.block_min


def _propagate(snap: Snapshot, db, source, downstream, initial: int) -> dict[str, int]:
    """Opoznienie przechodzace na kolejne odcinki, pomniejszone o bufory."""
    out: dict[str, int] = {}
    carried = initial
    previous = source
    for flight in downstream:
        buffer_min = _buffer(snap, db, flight, previous)
        carried = max(0, carried - buffer_min)
        out[flight.id] = carried
        previous = flight
        if carried == 0:
            break
    return out


def _buffer(snap: Snapshot, db, flight, previous=None) -> int:
    """Zapas postoju miedzy poprzednim przylotem a tym odlotem, ponad minimum typu."""
    if previous is None:
        rotation = snap.rotations.get(flight.rotation_id)
        legs = sorted((snap.flights[f] for f in (rotation.flight_ids if rotation else ())),
                      key=lambda f: f.seq)
        earlier = [f for f in legs if f.seq < flight.seq]
        if not earlier:
            return 0
        previous = earlier[-1]
    gap = int((flight.std - previous.sta).total_seconds() // 60)
    route = db.routes.get((flight.dep, flight.arr))
    minimum = turnaround_min(flight.type_code, route.sector if route else "europe")[1]
    return max(0, gap - minimum)


def _missed_connections(snap: Snapshot, option: Option, transfer_pax, delay: int) -> int:
    """Pasazerowie transferowi, ktorym opcja psuje przesiadke.

    Luz liczymy miedzy odcinkiem FAKTYCZNIE OPOZNIONYM a nastepnym w podrozy,
    a nie miedzy pierwszym a drugim. Dzis `connecting_passengers` oddaje wylacznie
    osoby, dla ktorych rejs zrodlowy jest pierwszym odcinkiem, wiec obie wersje
    daja to samo -- ale zalozenie bylo nigdzie nie zapisane, a podroz trojodcinkowa
    albo zaklocenie drugiego odcinka mierzylyby nie te przerwe.
    """
    if not transfer_pax:
        return 0
    if option.cancelled:
        return len(transfer_pax)

    opoznione = {fid for fid, minut in option.delay_min.items() if minut > 0}
    missed = 0
    for pax_id in transfer_pax:
        pax = snap.passengers.get(pax_id)
        itin = snap.itineraries.get(pax.itinerary_id) if pax else None
        if itin is None or len(itin.segments) < 2:
            continue
        for index, segment in enumerate(itin.segments[:-1]):
            if opoznione and segment not in opoznione:
                continue
            wczesniejszy = snap.flights.get(segment)
            nastepny = snap.flights.get(itin.segments[index + 1])
            if wczesniejszy is None or nastepny is None:
                continue
            slack = int((nastepny.std - wczesniejszy.sta).total_seconds() // 60)
            if delay > slack:
                missed += 1
                break
    return missed


def _crew_over_fdp(snap: Snapshot, flight, delay: int) -> tuple[str, ...]:
    from datetime import timedelta
    rotation = snap.rotations.get(flight.rotation_id)
    legs = [snap.flights[f] for f in (rotation.flight_ids if rotation else ())] or [flight]
    last = max(f.sta for f in legs) + timedelta(minutes=delay)
    out: list[str] = []
    for crew_id in flight.crew_ids:
        member = snap.crew.get(crew_id)
        if member is None:
            continue
        needed = int((last - member.duty_start).total_seconds() // 60)
        if needed > member.fdp_limit_min:
            out.append(crew_id)
    return tuple(out)
