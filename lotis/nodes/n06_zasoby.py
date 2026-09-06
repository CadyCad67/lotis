"""Node 06 -- REZERWACJA ZASOBU.

Zapasowy samolot, zaloga rezerwowa, miejsca u partnera, slot. Ten node nie
rezerwuje niczego naprawde -- opisuje, co jest do wziecia i **co jest sporne**.

DLACZEGO SPORNOSC MA WLASNE POLE
Dwie opcje moga wygladac na wykonalne osobno i byc niewykonalne razem, bo
obie siegaja po ten sam zapasowy samolot. Ranking, ktory tego nie widzi,
proponuje wariant, ktory rozpadnie sie przy wykonaniu -- a wtedy node 15b
zglasza `ExecutionFailure` i cala petla rusza od nowa. Taniej oznaczyc zasob
jako sporny tutaj.
"""

from __future__ import annotations

from ..adapters.lot_db import load_lot_db
from ..kernel.contracts import Disruption, Resource, ResourceKind, Snapshot
from ..kernel.node import Node, NodeOutput, RunContext


class ZasobyNode(Node):
    id = "06"
    name = "zasoby"
    title = "REZERWACJA ZASOBU"
    consumes = ("snapshot", "disruption", "feasibility")
    produces = "resources"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        disruption: Disruption = ctx.require("disruption")
        feasibility = ctx.require("feasibility")
        db = load_lot_db()
        report = self.new_report()

        flight = snap.flights[disruption.flight_id]
        resources: list[Resource] = []

        # ---- zapasowy samolot ----
        spare_bases = list(db.config.get("base", {}).get("spare", ["WAW"]))
        aircraft_gate = feasibility["gates"].get("samolot", {})
        spare_count = int(aircraft_gate.get("kandydaci", 0))
        if spare_count:
            resources.append(Resource(
                ResourceKind.SPARE_AIRCRAFT, flight.dep, spare_count,
                contested=spare_count == 1,
            ))

        # ---- zaloga rezerwowa ----
        standby = _standby_estimate(snap, flight.dep)
        if standby:
            resources.append(Resource(
                ResourceKind.RESERVE_CREW, flight.dep, standby, contested=standby <= 2))

        # ---- miejsca u partnera ----
        partners = _partners_at(db, flight.arr)
        if partners:
            resources.append(Resource(
                ResourceKind.PARTNER_SEATS, flight.arr, len(partners), contested=False))

        # ---- slot ----
        dep_port = snap.airports.get(flight.dep)
        if dep_port is not None and dep_port.slot_controlled:
            resources.append(Resource(ResourceKind.SLOT, flight.dep, 1, contested=True))

        contested = [r for r in resources if r.contested]

        report.summary = (
            f"W {flight.dep} do dyspozycji {len(resources)} rodzajow zasobu. "
            + (f"Sporne: {', '.join(r.kind.value for r in contested)}."
               if contested else "Zaden nie jest sporny.")
        )
        report.number("rodzajow_zasobu", len(resources), "szt")
        report.number("zasobow_spornych", len(contested), "szt")
        report.number("zapasowych_maszyn", spare_count, "szt")
        report.number("zalogi_rezerwowej", standby, "osob")
        report.number("partnerow_w_porcie_docelowym", len(partners), "szt")

        report.findings["zasoby"] = [
            {"id": f"{r.kind.value}@{r.key}", "ilosc": r.quantity, "sporny": r.contested}
            for r in resources
        ]
        report.findings["partnerzy"] = partners[:10]
        report.findings["bazy_maszyn_zapasowych"] = spare_bases

        for r in contested:
            report.decide(
                f"{r.kind.value} w {r.key} jest sporny ({r.quantity} szt) -- "
                "dwie opcje nie moga po niego siegnac naraz"
            )
        if not spare_count:
            report.decide(f"brak zapasowej maszyny w {flight.dep} -- SWAP odpada")
        if dep_port is not None and dep_port.slot_controlled:
            report.decide(
                f"{flight.dep} jest portem koordynowanym (poziom {dep_port.slot_level}) "
                "-- kazda zmiana godziny wymaga nowego slotu"
            )

        report.assume("zaloga rezerwowa", "derived", 0.4,
                      "oszacowana z obsady bazy; zrodla nie podaja grafiku standby")
        report.assume("miejsca u partnera", "derived", 0.4,
                      "obecnosc partnera w porcie, nie potwierdzona dostepnosc miejsc")

        return NodeOutput(report, {"resources": tuple(resources)})


def _standby_estimate(snap: Snapshot, station: str) -> int:
    """Zaloga rezerwowa: przyblizenie z obsady bazy.

    Grafiku standby nie ma w zadnym ze zrodel, wiec liczymy odsetek zalogi
    przypisanej do bazy. To jest jawnie oznaczone jako zalozenie -- silnik
    nie ma prawa traktowac tego jak potwierdzonej dostepnosci.
    """
    at_base = sum(1 for c in snap.crew.values() if c.base == station)
    return max(0, round(at_base * 0.04))


def _partners_at(db, station: str) -> list[dict[str, object]]:
    """Partnerzy operujacy w danym porcie, z poziomem umowy.

    `PT[kod] = [nazwa, poziom, [porty], star_alliance, uwaga]`. Poziom wchodzi
    wprost do mnoznika kosztu rebookingu w node 09.
    """
    out: list[dict[str, object]] = []
    for code, row in db.partners.items():
        ports = row[2] if len(row) > 2 and isinstance(row[2], list) else []
        if station in ports:
            level = int(row[1]) if len(row) > 1 else 3
            level_row = db.transfer_levels.get(str(level))
            out.append({
                "id": code,
                "nazwa": row[0],
                "poziom": level,
                "rodzaj": level_row[0] if level_row else "?",
                "mnoznik_kosztu": float(level_row[1]) if level_row else 1.4,
            })
    return sorted(out, key=lambda p: p["mnoznik_kosztu"])
