"""Node 04 -- ZAKLOCENIE.

Co sie stalo, kiedy, czego dotyczy i do kiedy trzeba zdecydowac. Cztery pola
tablicy, ale ostatnie jest najwazniejsze: bez terminu decyzji budzet czasu
z node 11 nie ma do czego sie odniesc.

PUNKT PONOWNEGO WEJSCIA
Do tego node wraca strzalka z bocznego boxu PRZELICZENIE. Cztery powody
ponownego uruchomienia: zmiana ETA, wygasniecie opcji, nowe zaklocenie w tej
samej rotacji i nieudane wykonanie. `Trigger` je rozroznia, a `iteration`
liczy nawroty -- bez tego licznika petla przeliczen nie mialaby konca.

KOD OPOZNIENIA DECYDUJE O PIENIADZACH
`delay_code` to kod AHM 730. Jego klasa (`c` przewoznik / `n` nadzwyczajne /
`d` reakcyjne) przeklada sie wprost na prawdopodobienstwo odszkodowania
z Art. 7: 1.0 / 0.0 / 0.5. Zaklocenie bez kodu jest wiec zakloceniem bez ceny.
"""

from __future__ import annotations

from datetime import timedelta

from ..adapters.lot_db import KO_CJEU, KO_DESC, KO_GROUP, load_lot_db
from ..kernel.contracts import (
    Disruption, DisruptionType, Scope, Snapshot, Trigger,
)
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.report import Status

#: Domyslny czas na decyzje, gdy nie podano wprost. Krotki celowo: dyzurny OCC
#: nie ma godziny, a budzet obliczen ma sie do czego odniesc.
DEFAULT_DECISION_WINDOW_MIN = 45

#: Kod AHM 730 uzywany, gdy zaklocenie zglaszane jest bez kodu.
#: 41 = usterka techniczna statku powietrznego, klasa `c` (odpowiedzialnosc
#: przewoznika) -- to najostrozniejsze zalozenie kosztowe, bo daje p=1.0.
DEFAULT_DELAY_CODE = "41"

#: Kod dla zaklocenia bez opoznienia, ktore jest sama nadsprzedaza.
#: 14 PO "OVERSALES, booking errors" to dokladnie ten przypadek w AHM 730,
#: klasa `c`, bo nadsprzedaz jest zawsze po stronie przewoznika.
OVERSALES_DELAY_CODE = "14"


class ZaklocenieNode(Node):
    id = "04"
    name = "zaklocenie"
    title = "ZAKLOCENIE"
    consumes = ("snapshot",)
    produces = "disruption"

    def __init__(
        self,
        flight_id: str | None = None,
        kind: DisruptionType = DisruptionType.TECHNICAL,
        delay_min: int = 180,
        delay_code: str | None = DEFAULT_DELAY_CODE,
        decision_window_min: int = DEFAULT_DECISION_WINDOW_MIN,
        trigger: Trigger = Trigger.INITIAL,
        iteration: int = 0,
        overbooking: int = 0,
    ) -> None:
        self.flight_id = flight_id
        self.overbooking = max(0, int(overbooking))
        self.delay_min = max(0, int(delay_min))
        # Zaklocenie bez minuty opoznienia, za to z nadsprzedaza, nie jest
        # usterka techniczna. Ma wlasny typ i wlasny kod AHM 730, inaczej caly
        # przeplyw liczylby cene opoznienia, ktorego nie ma.
        czysta_nadsprzedaz = self.overbooking > 0 and self.delay_min == 0
        self.kind = DisruptionType.PAX if czysta_nadsprzedaz else kind
        self.delay_code = (
            OVERSALES_DELAY_CODE if czysta_nadsprzedaz and not delay_code
            else (delay_code or DEFAULT_DELAY_CODE)
        )
        self.decision_window_min = decision_window_min
        self.trigger = trigger
        self.iteration = iteration

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        report = self.new_report()
        db = load_lot_db()

        flight_id = self.flight_id or _pick_flight(snap)
        flight = snap.flights.get(flight_id)
        if flight is None:
            report.status = Status.BLOCKED
            report.summary = f"Nieznany rejs: {flight_id}."
            report.data_gaps.append(f"rejs {flight_id} nie wystepuje w snapshocie")
            ctx.halt(f"nieznany rejs {flight_id}")
            return NodeOutput(report)

        at = flight.std - timedelta(minutes=max(30, self.decision_window_min))
        disruption = Disruption(
            id=f"DSR-{flight.id}-{self.iteration}",
            type=self.kind,
            scope=Scope.ROTATION,
            flight_id=flight.id,
            rotation_id=flight.rotation_id,
            at=at,
            decision_deadline=at + timedelta(minutes=self.decision_window_min),
            detail=f"kod AHM 730: {self.delay_code}",
            iteration=self.iteration,
            trigger=self.trigger,
            estimated_delay_min=self.delay_min,
            overbooking=self.overbooking,
        )

        code_row = db.delay_codes.get(self.delay_code, [])
        code_class = db.delay_code_class(self.delay_code)
        probability = db.compensation_probability(self.delay_code)
        rotation = snap.rotations.get(flight.rotation_id)
        downstream = [f for f in (rotation.flight_ids if rotation else ())
                      if snap.flights[f].seq > flight.seq]

        seats = 0
        spec = snap.aircraft_types.get(flight.type_code)
        if spec is not None:
            seats = spec.seats_total
        na_pokladzie = len(snap.passengers_on(flight.id)) + self.overbooking
        spill = max(0, na_pokladzie - seats) if seats else 0

        opis_skali = (
            f"nadsprzedaz {self.overbooking} rezerwacji" if self.delay_min == 0
            else f"szacowane opoznienie {self.delay_min} min"
            + (f" i nadsprzedaz {self.overbooking}" if self.overbooking else "")
        )
        report.summary = (
            f"{_kind_pl(self.kind)} na rejsie {flight.number} {flight.dep}-{flight.arr}, "
            f"{opis_skali}. "
            f"Decyzja do {disruption.decision_deadline.strftime('%H:%M')} UTC "
            f"({self.decision_window_min} min)."
        )
        if spill:
            report.warnings.append(
                f"nadsprzedaz: {spill} pasazerow nie miesci sie w kabinie "
                f"({na_pokladzie} na {seats} miejsc)"
            )

        report.number("rejs", flight.number)
        report.number("relacja", f"{flight.dep}-{flight.arr}")
        report.number("typ_zaklocenia", self.kind.value)
        report.number("opoznienie_szacowane", self.delay_min, "min")
        report.number("nadsprzedaz", self.overbooking, "rezerwacji")
        report.number("ponad_pojemnosc", spill, "osob")
        report.number("kod_opoznienia", self.delay_code)
        report.number("klasa_kodu", code_class)
        report.number("p_odszkodowania", probability)
        report.number("okno_decyzji", self.decision_window_min, "min")
        report.number("iteracja", self.iteration, "szt")
        report.number("powod_wejscia", self.trigger.value)
        report.number("odcinkow_ponizej", len(downstream), "szt")
        report.number("pasazerow_na_rejsie", len(snap.passengers_on(flight.id)), "osob")

        report.findings["rejs"] = {
            "id": flight.id, "numer": flight.number,
            "z": flight.dep, "do": flight.arr,
            "std": flight.std, "sta": flight.sta,
            "typ": flight.type_code, "maszyna": flight.aircraft_reg,
            "rotacja": flight.rotation_id,
        }
        if code_row:
            report.findings["kod_opoznienia"] = {
                "kod": self.delay_code,
                "opis": code_row[KO_DESC] if len(code_row) > KO_DESC else "",
                "grupa": code_row[KO_GROUP] if len(code_row) > KO_GROUP else "",
                "orzecznictwo_tsue": bool(code_row[KO_CJEU]) if len(code_row) > KO_CJEU else False,
            }
        report.findings["odcinki_ponizej"] = [
            {"id": f, "numer": snap.flights[f].number,
             "z": snap.flights[f].dep, "do": snap.flights[f].arr}
            for f in downstream
        ]

        report.decide(
            f"klasa kodu `{code_class}` daje prawdopodobienstwo odszkodowania "
            f"{probability:.1f} -- node 09 mnozy przez nie kwote z Art. 7"
        )
        if code_class == "n":
            report.decide(
                "okolicznosc nadzwyczajna: odszkodowanie z Art. 7 nie przysluguje, "
                "ale opieka z Art. 9 przysluguje niezaleznie od przyczyny"
            )
        if code_class == "?":
            report.warn(
                f"kod {self.delay_code} nie ma klasy w bazie -- przyjeto p=0.5, "
                "czyli srodek miedzy odpowiedzialnoscia a okolicznoscia nadzwyczajna"
            )
        if self.trigger is not Trigger.INITIAL:
            report.decide(
                f"ponowne wejscie z powodu `{self.trigger.value}`, iteracja {self.iteration}"
            )

        report.assume("opoznienie szacowane", "policy", 0.5,
                      "wartosc podana przy zgloszeniu, nie zmierzona")

        return NodeOutput(report, {"disruption": disruption})


def _pick_flight(snap: Snapshot) -> str:
    """Rejs o najwiekszym potencjale propagacji.

    Wybieramy ten, ktory ma najwiecej odcinkow ponizej siebie w rotacji, a przy
    remisie najwiecej pasazerow. Zaklocenie ostatniego odcinka doby nie ma czego
    propagowac i pokazywaloby silnik od najlatwiejszej strony.
    """
    best, best_key = "", (-1, -1)
    seated = _seated(snap)
    for rotation in snap.rotations.values():
        legs = sorted((snap.flights[f] for f in rotation.flight_ids),
                      key=lambda f: f.seq)
        for index, flight in enumerate(legs):
            key = (len(legs) - index - 1, seated.get(flight.id, 0))
            if key > best_key:
                best, best_key = flight.id, key
    return best or next(iter(snap.flights))


def _seated(snap: Snapshot) -> dict[str, int]:
    out: dict[str, int] = {}
    for pax in snap.passengers.values():
        itin = snap.itineraries.get(pax.itinerary_id)
        for segment in (itin.segments if itin else ()):
            out[segment] = out.get(segment, 0) + 1
    return out


def _kind_pl(kind: DisruptionType) -> str:
    return {
        DisruptionType.TECHNICAL: "Usterka techniczna",
        DisruptionType.CREW: "Brak zalogi",
        DisruptionType.WEATHER: "Pogoda",
        DisruptionType.ATC_SLOT: "Ograniczenie ATC",
        DisruptionType.AIRPORT: "Ograniczenie portu",
        DisruptionType.PAX: "Zdarzenie pasazerskie",
        DisruptionType.SECURITY: "Zdarzenie ochrony",
    }[kind]
