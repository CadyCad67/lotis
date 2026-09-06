"""Node 15b -- WYKONANIE.

Tego boxa na tablicy NIE MA. To jest luka 1 i najpowazniejsza z jedenastu.

Tablica prowadzila strzalke wprost z PRACOWNIK do LOG, wiec nie bylo miejsca,
w ktorym zapisuje sie, kto realizuje decyzje i co sie dzieje, gdy realizacja
sie nie powiedzie. Skutek byl konkretny: WYNIK RZECZYWISTY nie odrozniał bledu
modelu od nieudanego wykonania. Model, ktory policzyl dobrze, ale nie dostal
miejsc u partnera, uczyl sie na cudzym bledzie i psul sobie kalibracje.

CO ROBI TEN NODE
Rozklada decyzje na kroki wykonawcze, kazdy z wykonawca i kazdy zdolny do
porazki. Krok, ktory sie nie uda, rzuca `ExecutionFailure` -- a ten wyjatek
ustawia wyzwalacz `EXECUTION_FAILED` i caly przeplyw wraca do node 04. To jest
czwarty z powodow przeliczenia wypisanych w bocznym boxie PRZELICZENIE.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..kernel.contracts import ExecutionCard, Option
from ..kernel.errors import ExecutionFailure
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.report import Status


@dataclass(frozen=True, slots=True)
class Step:
    """Jeden krok wykonania: kto, co i czy da sie cofnac."""

    key: str
    executor: str
    description: str
    reversible: bool = True
    critical: bool = False


class WykonanieNode(Node):
    id = "15b"
    name = "wykonanie"
    title = "WYKONANIE"
    consumes = ("decision", "options")
    produces = "execution"

    def __init__(self, fail_step: str | None = None, recoverable: bool = True) -> None:
        #: `fail_step` sluzy do proby na sucho: pozwala zasymulowac porazke
        #: konkretnego kroku i sprawdzic, czy petla przeliczenia dziala.
        self.fail_step = fail_step
        self.recoverable = recoverable

    def run(self, ctx: RunContext) -> NodeOutput:
        decision = ctx.require("decision")
        options: tuple[Option, ...] = ctx.require("options")
        card: ExecutionCard | None = ctx.get("karta")
        report = self.new_report()

        option = next((o for o in options if o.id == decision["opcja"]), None)
        if option is None:
            report.status = Status.BLOCKED
            report.summary = f"Nieznana opcja do wykonania: {decision['opcja']}."
            ctx.halt("decyzja wskazuje opcje spoza zestawu")
            return NodeOutput(report)

        # Druga linia obrony. Node 15 juz to sprawdza, ale gwarancja filtru
        # prawnego nie moze wisiec na jednym wywolujacym: to jest ostatnie
        # miejsce przed zmiana stanu w swiecie zewnetrznym.
        lawful = ctx.get("lawful")
        if lawful is not None and option.id not in lawful:
            report.status = Status.BLOCKED
            report.summary = (
                f"Odmowa wykonania: `{option.id}` nie przeszla filtru prawnego."
            )
            report.findings["dopuszczalne"] = sorted(lawful)
            report.decide(
                "wykonanie nie rusza dla opcji niedopuszczalnej, niezaleznie od "
                "tego, co zapisano w decyzji"
            )
            ctx.halt(f"proba wykonania niedopuszczalnej opcji `{option.id}`")
            return NodeOutput(report)

        steps = _steps(option, card)

        if self.fail_step:
            target = next((s for s in steps if s.key == self.fail_step), None)
            if target is None:
                report.warn(f"nieznany krok do zasymulowania porazki: {self.fail_step}")
            else:
                raise ExecutionFailure(
                    step=target.key,
                    reason=f"{target.executor} nie potwierdzil kroku "
                           f"`{target.description}`",
                    recoverable=self.recoverable,
                )

        wykonane = [{"id": s.key, "wykonawca": s.executor, "opis": s.description,
                     "odwracalny": s.reversible, "krytyczny": s.critical,
                     "status": "wykonany"} for s in steps]

        nieodwracalne = [s for s in steps if not s.reversible]

        report.summary = (
            f"Wykonano {len(steps)} krokow opcji `{option.id}`. "
            + (f"{len(nieodwracalne)} krokow nieodwracalnych."
               if nieodwracalne else "Wszystkie kroki odwracalne.")
        )
        report.number("krokow", len(steps), "szt")
        report.number("krokow_nieodwracalnych", len(nieodwracalne), "szt")
        report.number("wykonawcow", len({s.executor for s in steps}), "szt")
        report.number("opcja", option.id)

        report.findings["kroki"] = wykonane
        report.findings["punkt_bez_powrotu"] = (
            {"krok": nieodwracalne[0].key, "opis": nieodwracalne[0].description}
            if nieodwracalne else None
        )
        report.findings["sciezka_porazki"] = {
            "wyzwalacz": "EXECUTION_FAILED",
            "wraca_do": "node 04 ZAKLOCENIE",
            "po_co": "blad wykonania nie moze byc liczony jako blad modelu (luka 3)",
        }

        report.decide(
            "wykonanie jest osobnym etapem miedzy decyzja a logiem -- bez niego "
            "node 17 nie odroznilby bledu modelu od nieudanej realizacji"
        )
        if nieodwracalne:
            report.decide(
                f"krok `{nieodwracalne[0].key}` jest nieodwracalny -- po nim "
                "przeliczenie nie przywroci stanu wyjsciowego"
            )

        return NodeOutput(report, {
            "execution": {"opcja": option.id, "kroki": wykonane, "udane": True},
        })


def _steps(option: Option, card: ExecutionCard | None) -> list[Step]:
    """Kroki wynikaja z ksztaltu opcji, nie z listy zyczen."""
    steps: list[Step] = []

    if option.aircraft_swap:
        steps.append(Step("przydzial_maszyny", "OCC / Maintenance Control",
                          "przepiecie rejsow miedzy maszynami", reversible=True))
        steps.append(Step("obsluga_naziemna", "Handling",
                          "przestawienie sprzetu i bagazu", reversible=True))

    if option.delay_min:
        steps.append(Step("nowy_slot", "Slot Coordination / EUROCONTROL",
                          "wystapienie o nowe okno startowe", reversible=False,
                          critical=True))

    if option.cancelled:
        steps.append(Step("kasacja_w_systemie", "System rezerwacyjny",
                          "odwolanie rejsu i zwolnienie miejsc", reversible=False,
                          critical=True))

    kinds = {o.kind.value for o in option.pax_outcomes.values()}
    if "REBOOKED_OWN" in kinds:
        steps.append(Step("przepisanie_wlasne", "System rezerwacyjny",
                          "przepisanie pasazerow na wlasny rejs"))
    if "REBOOKED_OAL" in kinds:
        steps.append(Step("potwierdzenie_partnera", "Interline Desk",
                          "potwierdzenie miejsc u przewoznika obcego",
                          reversible=False, critical=True))
    if any(o.care_nights for o in option.pax_outcomes.values()):
        steps.append(Step("rezerwacja_hotelu", "Pax Care",
                          "rezerwacja hoteli i transportu"))
    if "OFFLOADED_INVOLUNTARY" in kinds or "OFFLOADED_VOLUNTARY" in kinds:
        steps.append(Step("wezwanie_ochotnikow", "Obsluga bramki",
                          "wezwanie ochotnikow przed odmowa przyjecia"))

    steps.append(Step("powiadomienie_pax", "Komunikacja",
                      "wyslanie SMS i e-mail do pasazerow"))
    steps.append(Step("brief_zalogi", "Crew Control",
                      "poinformowanie zalogi o zmianie"))
    return steps
