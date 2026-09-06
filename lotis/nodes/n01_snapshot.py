"""Node 01 -- SNAPSHOT.

Zamraza stan swiata dla jednej rzeczywistej doby operacyjnej i liczy jego
odcisk. Kazdy nastepny raport ten odcisk cytuje, wiec run da sie odtworzyc
co do rejsu.

Node nie generuje rozkladu. Bierze siedem rzeczywistych dob z `lot-siatka.json`
i parametry z `loops.jsx`. Jedyna warstwa generowana to tozsamosci pasazerow,
i wlasnie dlatego jest tu wypisana jako jawne zalozenie -- model czytajacy ten
raport ma wiedziec, ze liczba pasazerow jest modelem, a liczba rejsow nie.
"""

from __future__ import annotations

from ..adapters.network import build_snapshot
from ..adapters.siatka import WEEKDAYS_PL
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.report import Status


class SnapshotNode(Node):
    id = "01"
    name = "snapshot"
    title = "DANE"
    produces = "snapshot"

    def __init__(self, weekday: int = 4, seed: int = 2026) -> None:
        if not 0 <= weekday <= 6:
            raise ValueError(f"dzien tygodnia poza zakresem 0-6: {weekday}")
        self.weekday = weekday
        self.seed = seed

    def run(self, ctx: RunContext) -> NodeOutput:
        snap, build = build_snapshot(weekday=self.weekday, seed=self.seed)

        # Odcisk musi trafic do kontekstu przed zapisem raportu -- klasa bazowa
        # czyta go w `_finish`, wiec tu jest ostatni moment.
        ctx.snapshot_digest = snap.digest

        report = self.new_report()
        report.summary = (
            f"Zamrozony stan {WEEKDAYS_PL[self.weekday]} {build.day}: "
            f"{build.flights} rejsow LOT-u na {build.rotations} lancuchach, "
            f"{build.passengers} pasazerow na {build.itineraries} podrozach."
        )

        report.number("doba", build.day)
        report.number("dzien_tygodnia", WEEKDAYS_PL[self.weekday])
        report.number("rejsy", build.flights, "szt")
        report.number("rotacje", build.rotations, "szt")
        report.number("rotacje_przerwane", build.broken_rotations, "szt")
        report.number("maszyny", build.aircraft, "szt")
        report.number("zaloga", build.crew, "osob")
        report.number("pasazerowie", build.passengers, "osob")
        report.number("podroze", build.itineraries, "szt")
        report.number("udzial_transferowych", round(build.connecting_share * 100, 1), "%")
        report.number("porty", len(snap.airports), "szt")
        report.number("typy_statkow", len(snap.aircraft_types), "szt")
        report.number("odcisk", snap.digest)

        report.findings["zasieg_doby"] = _day_span(snap)
        report.findings["najwieksze_porty"] = _busiest_ports(snap)
        report.findings["flota_wg_typu"] = _fleet_by_type(snap)
        report.findings["pewnosc_pol"] = {k: v.value for k, v in snap.confidence.items()}

        report.decide(f"snapshot {snap.digest} jest podstawa calego runu")
        report.decide(
            f"horyzont propagacji konczy sie na dobie operacyjnej {build.day} "
            f"albo na powrocie maszyny do {'WAW'}, co nastapi pierwsze"
        )

        for note in build.assumptions:
            report.assume("manifest", "synthetic", 0.6, note)
        report.assume("rozklad", "real", 1.0,
                      "siedem rzeczywistych dob operacyjnych, nie generator")
        report.assume("porty i prawo", "real", 1.0, "baza parametryczna loops.jsx")

        report.data_gaps.extend(build.gaps)
        if build.broken_rotations:
            report.warn(
                f"{build.broken_rotations} maszyn ma przerwany lancuch doby "
                "-- czesc odcinkow wypadla poza okno eksportu"
            )
        if not snap.flights:
            report.status = Status.BLOCKED
            report.summary = "Doba bez rejsow -- nie ma czego liczyc."
            ctx.halt("snapshot bez rejsow")

        return NodeOutput(report, {"snapshot": snap, "build_report": build})


def _day_span(snap) -> dict[str, str]:
    if not snap.flights:
        return {}
    first = min(f.std for f in snap.flights.values())
    last = max(f.sta for f in snap.flights.values())
    return {
        "pierwszy_odlot_utc": first.isoformat(),
        "ostatni_przylot_utc": last.isoformat(),
        "rozpietosc_h": round((last - first).total_seconds() / 3600, 1),
    }


def _busiest_ports(snap, top: int = 8) -> list[dict[str, object]]:
    counts: dict[str, int] = {}
    for f in snap.flights.values():
        counts[f.dep] = counts.get(f.dep, 0) + 1
        counts[f.arr] = counts.get(f.arr, 0) + 1
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:top]
    return [{"id": iata, "operacji": n} for iata, n in ordered]


def _fleet_by_type(snap) -> dict[str, int]:
    counts: dict[str, int] = {}
    for f in snap.flights.values():
        counts[f.type_code] = counts.get(f.type_code, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))
