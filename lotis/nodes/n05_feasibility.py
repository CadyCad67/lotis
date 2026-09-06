"""Node 05 -- FEASIBILITY.

Cztery bramki tablicy: samolot, zaloga, port, miejsca. Bramka nie wycenia --
mowi tylko, czy dana klasa opcji jest w ogole wykonalna. Opcja niewykonalna
nie ma prawa wejsc do rankingu, bo ranking z opcja, ktorej nie da sie zrobic,
jest gorszy niz krotszy ranking.

DWIE REGULY Z BAZY, KTORE ZMIENIAJA WYNIK
`CF.base.swap = ["WAW"]` -- SWAP jest mozliwy WYLACZNIE w bazie glownej. Poza
nia nie ma zapasowej maszyny, obslugi technicznej ani zapasowej zalogi.
Wczesniejsza analiza danych pokazala, ze 53% odlotow zaczyna sie poza WAW, wiec
ta jedna linijka bazy wyklucza SWAP dla polowy siatki.

`FT.rules` -- dyskrecja dowodcy (+2 h) NIE jest opcja planistyczna. Silnik
pokazuje ja jako informacje, ale nie wlicza do wykonalnosci. Wliczenie
znaczyloby planowanie cudzej decyzji.
"""

from __future__ import annotations

from datetime import timedelta

from ..adapters.aircraft_perf import same_crew_rating, turnaround_min
from ..adapters.lot_db import load_lot_db
from ..kernel.contracts import Disruption, GateResult, Snapshot
from ..kernel.node import Node, NodeOutput, RunContext

#: Zapas FDP, ponizej ktorego zaloga nie utrzyma zadnego opoznienia.
FDP_SAFETY_MIN = 15


class FeasibilityNode(Node):
    id = "05"
    name = "feasibility"
    title = "FEASIBILITY"
    consumes = ("snapshot", "disruption")
    produces = "feasibility"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        disruption: Disruption = ctx.require("disruption")
        db = load_lot_db()
        report = self.new_report()

        flight = snap.flights[disruption.flight_id]
        delay = disruption.estimated_delay_min
        new_std = flight.std + timedelta(minutes=delay)
        new_sta = flight.sta + timedelta(minutes=delay)

        gates: list[GateResult] = [
            _gate_aircraft(snap, db, flight, delay),
            _gate_crew(snap, flight, delay),
            _gate_airport(snap, flight, new_std, new_sta),
            _gate_seats(snap, flight),
        ]

        allowed = {
            "HOLD": all(g.passed for g in gates if g.gate in ("zaloga", "port")),
            "DEPART": True,
            "SWAP": next(g.passed for g in gates if g.gate == "samolot"),
            "REBOOK-OWN": next(g.passed for g in gates if g.gate == "miejsca"),
            "REBOOK-OAL": True,
            "OVERNIGHT": True,
            "SPLIT": next(g.passed for g in gates if g.gate == "miejsca"),
            "CANCEL": True,
        }

        feasibility = {
            "gates": {g.gate: {"passed": g.passed, "reason": g.reason, **g.detail}
                      for g in gates},
            "allowed_kinds": allowed,
            "new_std": new_std,
            "new_sta": new_sta,
        }

        odrzucone = [g for g in gates if not g.passed]
        report.summary = (
            f"Cztery bramki na rejsie {flight.number} przy opoznieniu {delay} min. "
            + ("Wszystkie przeszly." if not odrzucone
               else f"Odpadly: {', '.join(g.gate for g in odrzucone)}.")
        )

        for g in gates:
            report.number(f"bramka_{g.gate}", "przeszla" if g.passed else "odpadla")
        report.number("dopuszczonych_rodzajow", sum(1 for v in allowed.values() if v), "szt")
        report.number("nowy_std", new_std)
        report.number("nowy_sta", new_sta)

        report.findings["bramki"] = [
            {"id": g.gate, "przeszla": g.passed, "powod": g.reason, **g.detail}
            for g in gates
        ]
        report.findings["dopuszczone_rodzaje_opcji"] = allowed

        for g in gates:
            if not g.passed:
                report.decide(f"bramka {g.gate}: {g.reason} -- opcje od niej zalezne odpadaja")

        report.decide(
            "dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana "
            "w wykonalnosc -- to decyzja dowodcy, nie planisty"
        )
        report.assume("MEL i ETOPS", "policy", 0.4,
                      "brak biezacego statusu technicznego floty w zrodlach")

        return NodeOutput(report, {"feasibility": feasibility})


def _gate_aircraft(snap: Snapshot, db, flight, delay_min: int) -> GateResult:
    """Samolot: gdzie stoi, czy jest zamiennik, ACMI wykluczone."""
    swap_bases = list(db.config.get("base", {}).get("swap", ["WAW"]))
    if flight.dep not in swap_bases:
        return GateResult(
            "samolot", False,
            f"port {flight.dep} nie jest baza SWAP (baza dopuszcza {', '.join(swap_bases)})",
            {"kandydaci": 0, "bazy_swap": swap_bases},
        )

    candidates = []
    for reg, aircraft in snap.aircraft.items():
        if reg == flight.aircraft_reg or aircraft.position != flight.dep:
            continue
        fleet_row = db.fleet.get(reg)
        if fleet_row is None or fleet_row.wet_lease:
            continue                      # ZAKAZ dla ACMI (SZ: warunek SWAP)
        if not same_crew_rating(aircraft.type_code, flight.type_code):
            continue
        candidates.append({"reg": reg, "typ": aircraft.type_code})

    if not candidates:
        return GateResult(
            "samolot", False,
            f"brak sprawnej maszyny zgodnego typu w {flight.dep}",
            {"kandydaci": 0, "bazy_swap": swap_bases},
        )
    turn = turnaround_min(flight.type_code, "europe")[1]
    return GateResult(
        "samolot", True, f"{len(candidates)} maszyn do podmiany w {flight.dep}",
        {"kandydaci": len(candidates), "lista": candidates[:6],
         "minimalny_postoj_min": turn},
    )


def _gate_crew(snap: Snapshot, flight, delay_min: int) -> GateResult:
    """Zaloga: czy FDP wytrzyma opoznienie do konca lancucha."""
    rotation = snap.rotations.get(flight.rotation_id)
    legs = [snap.flights[f] for f in (rotation.flight_ids if rotation else ())]
    if not legs:
        legs = [flight]
    last_on_block = max(f.sta for f in legs) + timedelta(minutes=delay_min)

    tight: list[dict[str, object]] = []
    for crew_id in flight.crew_ids:
        member = snap.crew.get(crew_id)
        if member is None:
            continue
        needed = int((last_on_block - member.duty_start).total_seconds() // 60)
        margin = member.fdp_limit_min - needed
        if margin < FDP_SAFETY_MIN:
            tight.append({"id": crew_id, "rola": member.role.value,
                          "potrzeba_min": needed, "limit_min": member.fdp_limit_min,
                          "zapas_min": margin})

    if tight:
        worst = min(t["zapas_min"] for t in tight)
        return GateResult(
            "zaloga", False,
            f"{len(tight)} osob przekracza FDP przy opoznieniu {delay_min} min "
            f"(najgorszy zapas {worst} min)",
            {"przekroczen": len(tight), "lista": tight[:6]},
        )
    return GateResult(
        "zaloga", True, f"FDP wytrzymuje opoznienie {delay_min} min",
        {"przekroczen": 0, "osob": len(flight.crew_ids)},
    )


def _gate_airport(snap: Snapshot, flight, new_std, new_sta) -> GateResult:
    """Port: cisza nocna typu 1 na nowej godzinie, poziom slotow."""
    problems: list[dict[str, object]] = []
    for role, iata, moment in (("wylot", flight.dep, new_std),
                               ("przylot", flight.arr, new_sta)):
        port = snap.airports.get(iata)
        if port is None:
            problems.append({"pole": role, "port": iata, "powod": "nieznany port"})
            continue
        local = (moment.hour * 60 + moment.minute + port.tz_offset_min) % 1440
        if port.blocks_planning(local):
            problems.append({
                "pole": role, "port": iata,
                "lokalnie": f"{local // 60:02d}:{local % 60:02d}",
                "powod": "cisza nocna typu 1 -- zakaz planowania operacji",
            })

    dep_port = snap.airports.get(flight.dep)
    slot = dep_port.slot_level if dep_port else 0
    detail = {"poziom_slotow_wylotu": slot,
              "port_koordynowany": bool(dep_port and dep_port.slot_controlled)}

    if problems:
        return GateResult("port", False, problems[0]["powod"],
                          {**detail, "konflikty": problems})
    return GateResult("port", True, "nowe godziny poza oknem zakazu planowania", detail)


def _gate_seats(snap: Snapshot, flight) -> GateResult:
    """Miejsca: wolne fotele na wlasnych rejsach w tej samej relacji tego dnia."""
    seated: dict[str, int] = {}
    for pax in snap.passengers.values():
        itin = snap.itineraries.get(pax.itinerary_id)
        for segment in (itin.segments if itin else ()):
            seated[segment] = seated.get(segment, 0) + 1

    free = 0
    alternatives: list[dict[str, object]] = []
    for other in snap.flights.values():
        if other.id == flight.id or other.dep != flight.dep or other.arr != flight.arr:
            continue
        if other.std <= flight.std:
            continue
        spec = snap.aircraft_types.get(other.type_code)
        capacity = spec.seats_total if spec else 0
        available = max(0, capacity - seated.get(other.id, 0))
        if available > 0:
            free += available
            alternatives.append({"id": other.id, "numer": other.number,
                                 "std": other.std, "wolnych": available})

    if not alternatives:
        return GateResult(
            "miejsca", False,
            f"brak pozniejszego wlasnego rejsu {flight.dep}-{flight.arr} z wolnymi miejscami",
            {"wolnych_miejsc": 0, "rejsow": 0},
        )
    return GateResult(
        "miejsca", True, f"{free} wolnych miejsc na {len(alternatives)} wlasnych rejsach",
        {"wolnych_miejsc": free, "rejsow": len(alternatives),
         "lista": sorted(alternatives, key=lambda a: a["std"])[:5]},
    )
