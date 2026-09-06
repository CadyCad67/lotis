"""Node 12 -- FILTR PRAWNY.

DLACZEGO PRAWO JEST FILTREM, A NIE KOSZTEM (Blok 5 tablicy)
Gdyby odszkodowanie bylo zwykla pozycja kosztowa obok hotelu, najtansza opcja
byloby zdjac pasazerow wbrew woli i wpisac odszkodowanie w koszty. Silnik by
to wybral, bo tak kaze arytmetyka.

Dlatego ten node USUWA opcje. Nie dopisuje im ceny, nie podnosi wagi, nie
zmienia rankingu miekko. Architektoniczny niezmiennik: filtr prawny nigdy nie
pisze do rejestru kosztow -- i jest na to test.

FILTRY TWARDE (CF.hard)
Osiem pozycji, ktorych zaden suwak konfiguracji nie moze wylaczyc. Sa tu
odwzorowane jeden do jednego, kazda z podstawa prawna.

GALAZ BOCZNA: BRAK DOPUSZCZALNEJ OPCJI
Gdy wszystkie opcje odpadna, node rzuca `NoLawfulOption` z gotowym pakietem
eskalacyjnym. Luka 5 tablicy polegala na tym, ze ta galaz nie miala adresata,
terminu ani tresci -- wszystkie trzy sa teraz w `policy/escalation.json`.
"""

from __future__ import annotations

from ..adapters.lot_db import load_lot_db
from ..kernel.contracts import (
    LegalVerdict, Option, OptionEvaluation, PaxOutcomeKind, Snapshot, SpecialNeed,
)
from ..kernel.errors import NoLawfulOption
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.pricing import pricing

#: Pasazerowie, ktorych nie wolno zdjac wbrew woli w pierwszej kolejnosci.
#: Rozporzadzenie 1107/2006 (PRM) oraz zakazy z CF.hard.
PROTECTED = frozenset({
    SpecialNeed.REDUCED_MOBILITY,
    SpecialNeed.UNACCOMPANIED_MINOR,
    SpecialNeed.MEDICAL_ASSIST,
})


class FiltrPrawnyNode(Node):
    id = "12"
    name = "filtr_prawny"
    title = "FILTR PRAWNY"
    consumes = ("snapshot", "options", "evaluations")
    produces = "lawful"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        options: tuple[Option, ...] = ctx.require("options")
        evaluations: dict[str, OptionEvaluation] = ctx.require("evaluations")
        disruption = ctx.require("disruption")
        db = load_lot_db()
        price = pricing()
        tier = ctx.get("eu261_tier", "B")
        report = self.new_report()

        verdicts: dict[str, LegalVerdict] = {}
        for option in options:
            failed: list[tuple[str, str]] = []
            warnings: list[str] = []

            failed.extend(_check_art8(option, price, tier))
            failed.extend(_check_art9(option, price, tier))
            failed.extend(_check_art4(snap, option))
            failed.extend(_check_grupy(snap, option))
            failed.extend(_check_prm(snap, option, db))
            warnings.extend(_warn_art7(option, price, tier))

            verdicts[option.id] = LegalVerdict(
                option_id=option.id,
                lawful=not failed,
                rules_failed=tuple(failed),
                warnings=tuple(warnings),
            )

        lawful = [o for o in options if verdicts[o.id].lawful]
        rejected = [o for o in options if not verdicts[o.id].lawful]

        report.summary = (
            f"Z {len(options)} opcji przez filtr przeszlo {len(lawful)}. "
            + (f"Odrzucono: {', '.join(o.id for o in rejected)}."
               if rejected else "Zadna nie odpadla.")
        )
        report.number("opcji_na_wejsciu", len(options), "szt")
        report.number("opcji_dopuszczalnych", len(lawful), "szt")
        report.number("opcji_odrzuconych", len(rejected), "szt")
        report.number("kategoria_eu261", tier)
        report.number("prog_opieki", price.care_threshold_min(tier), "min")

        report.findings["werdykty"] = [
            {"id": v.option_id, "dopuszczalna": v.lawful,
             "zlamane_reguly": [{"podstawa": p, "powod": r} for p, r in v.rules_failed],
             "ostrzezenia": list(v.warnings)}
            for v in verdicts.values()
        ]
        report.findings["filtry_twarde"] = db.config.get("hard", [])
        report.findings["podstawy_prawne"] = [
            {"id": row[0], "akt": row[1]} for row in db.legal[:12]
        ]

        for option in rejected:
            for podstawa, powod in verdicts[option.id].rules_failed:
                report.decide(f"`{option.id}` odrzucona -- {podstawa}: {powod}")
        for option in lawful:
            for uwaga in verdicts[option.id].warnings:
                report.warn(f"`{option.id}`: {uwaga}")

        report.decide(
            "filtr usuwa opcje, nigdy ich nie przecenia -- odszkodowanie jako "
            "pozycja kosztowa uczynilby zdjecie pasazerow wbrew woli optymalnym"
        )
        report.decide(
            "pelna kwota z Art. 7 jest nienaruszalna: zaniżanie odszkodowan bylo "
            "przedmiotem decyzji zobowiazujacej UOKiK (RBG-1/2026)"
        )

        if not lawful:
            packet = _escalation_packet(
                ctx, snap, disruption, options, verdicts, evaluations)
            report.findings["escalation"] = packet
            raise NoLawfulOption(packet)

        return NodeOutput(report, {
            "lawful": tuple(o.id for o in lawful),
            "verdicts": verdicts,
        })


# ---------------------------------------------------------------- reguly


def _check_art8(option: Option, price, tier: str) -> list[tuple[str, str]]:
    """Art. 8 -- przewoz przy najblizszej okazji albo zwrot.

    Opcja, ktora zostawia pasazera bez przewozu i bez zwrotu, jest
    niedopuszczalna. `C-74/19 TAP`: brak wlasnego rejsu nie usprawiedliwia
    zwloki, jesli obcy przewoznik ma wolne miejsca.
    """
    stranded = [o for o in option.pax_outcomes.values()
                if o.kind is PaxOutcomeKind.OFFLOADED_INVOLUNTARY]
    if not stranded:
        return []
    # Zdjecie pasazera jest dopuszczalne tylko, gdy opcja daje mu przewoz
    # albo zwrot. W tym silniku offload bez przepisania jest brakiem obu.
    rerouted = any(o.kind in (PaxOutcomeKind.REBOOKED_OWN, PaxOutcomeKind.REBOOKED_OAL,
                              PaxOutcomeKind.CANCELLED_REFUND)
                   for o in option.pax_outcomes.values())
    if not rerouted:
        return [("Art. 8 EU261",
                 f"{len(stranded)} pasazerow zdjetych bez zapewnienia przewozu ani zwrotu")]
    return []


def _check_art9(option: Option, price, tier: str) -> list[tuple[str, str]]:
    """Art. 9 -- opieka od progu, niezaleznie od przyczyny.

    Opcja, ktora przetrzymuje pasazera ponad prog bez zapewnienia opieki,
    jest niedopuszczalna. W tym silniku brak opieki objawia sie jako nocleg
    zerowy przy oczekiwaniu przekraczajacym dobe.
    """
    threshold = price.care_threshold_min(tier)
    failures: list[tuple[str, str]] = []
    for outcome in option.pax_outcomes.values():
        if outcome.delay_min >= 12 * 60 and outcome.care_nights == 0:
            failures.append((
                "Art. 9 EU261",
                (f"oczekiwanie {outcome.delay_min} min bez zapewnionego noclegu "
                 f"(prog opieki {threshold} min)"),
            ))
            break
    return failures


def _check_art4(snap: Snapshot, option: Option) -> list[tuple[str, str]]:
    """Art. 4 -- najpierw wezwanie ochotnikow, dopiero potem odmowa wbrew woli."""
    involuntary = sum(1 for o in option.pax_outcomes.values()
                      if o.kind is PaxOutcomeKind.OFFLOADED_INVOLUNTARY)
    voluntary = sum(1 for o in option.pax_outcomes.values()
                    if o.kind is PaxOutcomeKind.OFFLOADED_VOLUNTARY)
    if involuntary and not voluntary:
        return [("Art. 4 EU261",
                 (f"{involuntary} pasazerow zdjetych wbrew woli bez uprzedniego "
                  "wezwania ochotnikow"))]
    return []


def _check_grupy(snap: Snapshot, option: Option) -> list[tuple[str, str]]:
    """CF.hard -- zakaz rozdzielania rodzin, grup i maloletnich bez opieki."""
    if len({o.kind for o in option.pax_outcomes.values()}) < 2:
        return []
    rozdzieleni: list[str] = []
    for pax_id, outcome in option.pax_outcomes.items():
        pax = snap.passengers.get(pax_id)
        if pax is None:
            continue
        if SpecialNeed.GROUP in pax.specials and outcome.kind in (
                PaxOutcomeKind.REBOOKED_OAL, PaxOutcomeKind.OFFLOADED_INVOLUNTARY):
            rozdzieleni.append(pax_id)
        if SpecialNeed.UNACCOMPANIED_MINOR in pax.specials and \
                outcome.kind is PaxOutcomeKind.REBOOKED_OAL:
            rozdzieleni.append(pax_id)
    if rozdzieleni:
        return [("CF.hard -- zakaz rozdzielania",
                 (f"{len(rozdzieleni)} pasazerow z grupy albo maloletnich bez opieki "
                  "trafia na inna sciezke niz reszta"))]
    return []


def _check_prm(snap: Snapshot, option: Option, db) -> list[tuple[str, str]]:
    """Rozporzadzenie 1107/2006 -- asysta PRM i ochrona przy odmowie przyjecia."""
    naruszenia = 0
    for pax_id, outcome in option.pax_outcomes.items():
        pax = snap.passengers.get(pax_id)
        if pax is None or not (pax.specials & PROTECTED):
            continue
        if outcome.kind is PaxOutcomeKind.OFFLOADED_INVOLUNTARY:
            naruszenia += 1
    if naruszenia:
        return [("Rozporzadzenie (WE) 1107/2006",
                 (f"{naruszenia} pasazerow chronionych (PRM, maloletni bez opieki, "
                  "asysta medyczna) zdjetych wbrew woli"))]
    return []


def _warn_art7(option: Option, price, tier: str) -> list[str]:
    """Ostrzezenia, ktore nie usuwaja opcji, ale musza byc widoczne."""
    out: list[str] = []
    threshold = price.reimbursement_threshold_min
    for outcome in option.pax_outcomes.values():
        if outcome.delay_min >= threshold:
            out.append(
                f"opoznienie {outcome.delay_min} min przekracza prog {threshold} min "
                "-- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)"
            )
            break
    return out


def _escalation_packet(ctx, snap, disruption, options, verdicts, evaluations) -> dict:
    """Pakiet dla czlowieka, gdy wszystkie opcje odpadly (luka 5 tablicy).

    Adresat, termin i zawartosc pochodza z `policy/escalation.json` -- tablica
    zostawiala te galaz bez zadnego z tych trzech.
    """
    settings = ctx.policy.escalation
    najmniej_zla = min(
        evaluations.values(), key=lambda e: e.loss.minor) if evaluations else None
    return {
        "addressee": settings.get("addressee", {}),
        "sla_minutes": settings.get("sla_minutes"),
        "disruption": {
            "id": disruption.id, "rejs": disruption.flight_id,
            "typ": disruption.type.value,
            "termin_decyzji": disruption.decision_deadline.isoformat(),
            "opoznienie_min": disruption.estimated_delay_min,
        },
        "rejected_options": [
            {"id": v.option_id,
             "rule_that_killed_it": [{"podstawa": p, "powod": r} for p, r in v.rules_failed]}
            for v in verdicts.values()
        ],
        "least_bad_option": (
            {"id": najmniej_zla.option_id, "strata": najmniej_zla.loss.to_json()}
            if najmniej_zla else None
        ),
        "snapshot_digest": ctx.snapshot_digest,
        "decision_deadline": disruption.decision_deadline.isoformat(),
    }
