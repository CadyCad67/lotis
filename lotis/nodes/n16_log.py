"""Node 16 -- LOG.

Co system policzyl, ktora opcje wybral, dlaczego odrzucil pozostale, co wybral
pracownik i o ktorej, oraz wersje: silnika, modelu kosztowego i polityki firmy.

DLACZEGO ODRZUCONE OPCJE SA WAZNIEJSZE OD WYBRANEJ
W sporze -- z pasazerem, z UOKiK, z ubezpieczycielem -- nie liczy sie to, co
wybrano, tylko to, czego swiadomie nie wybrano i na jakiej podstawie. Log,
ktory zapisuje sama rekomendacje, nie broni niczego.

WERSJE
Model kosztowy i prawo nie maja juz wlasnych numerow -- oba pochodza z bazy
`loops.jsx`, wiec wersja bazy jest ich wersja. Osobno idzie odcisk pliku
nadpisan: jesli ktos podmienil stawke, log to pokaze, nawet gdy kwota wyglada
zwyczajnie.
"""

from __future__ import annotations

import hashlib
import json

from ..kernel.contracts import (
    ExecutionCard, LegalVerdict, Option, OptionEvaluation, RankedOption,
)
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.report import to_jsonable
from ..kernel.versions import version_block


class LogNode(Node):
    id = "16"
    name = "log"
    title = "LOG"
    consumes = ("options", "evaluations", "ranking")
    produces = "audit"

    def run(self, ctx: RunContext) -> NodeOutput:
        options: tuple[Option, ...] = ctx.require("options")
        evaluations: dict[str, OptionEvaluation] = ctx.require("evaluations")
        ranking: list[RankedOption] = ctx.require("ranking")
        verdicts: dict[str, LegalVerdict] = ctx.get("verdicts", {})
        decision = ctx.get("decision")
        execution = ctx.get("execution")
        card: ExecutionCard | None = ctx.get("karta")
        disruption = ctx.require("disruption")
        report = self.new_report()

        rozwazone = []
        for option in options:
            evaluation = evaluations.get(option.id)
            verdict = verdicts.get(option.id)
            rozwazone.append({
                "id": option.id,
                "label": option.label,
                "tryb": option.kind.value,
                "generator": option.generator,
                "strata": evaluation.loss if evaluation else None,
                "widelki": ({"min": evaluation.band.low, "max": evaluation.band.high}
                            if evaluation else None),
                "dopuszczalna": verdict.lawful if verdict else None,
                "powod_odrzucenia": (
                    [{"podstawa": p, "powod": r} for p, r in verdict.rules_failed]
                    if verdict and not verdict.lawful else []
                ),
                "pozycja_koncowa": next(
                    (r.rank for r in ranking if r.option_id == option.id), None),
            })

        audit = {
            "schema": "lotis.audit/v1",
            "run_id": ctx.run_id,
            "snapshot": ctx.snapshot_digest,
            "czas_runu": ctx.clock.now(),
            "zaklocenie": {
                "id": disruption.id,
                "rejs": disruption.flight_id,
                "typ": disruption.type.value,
                "opoznienie_min": disruption.estimated_delay_min,
                "termin_decyzji": disruption.decision_deadline,
                "iteracja": disruption.iteration,
                "wyzwalacz": disruption.trigger.value,
            },
            "opcje_rozwazone": rozwazone,
            "rekomendacja": (
                {"id": ranking[0].option_id, "strata": ranking[0].loss,
                 "oszczednosc": ranking[0].saving_vs_default}
                if ranking else None
            ),
            "decyzja_czlowieka": decision,
            "wykonanie": execution,
            "karta_wykonania": card,
            "wersje": version_block(),
            "nadpisania_uzyte": ctx.policy.applied_overrides(),
            "budzet": ctx.budget.snapshot(),
            "degradacja": ctx.degradation.name,
        }
        audit["odcisk"] = _digest(audit)

        odrzucone = [r for r in rozwazone if r["dopuszczalna"] is False]

        report.summary = (
            f"Zapisano {len(rozwazone)} rozwazonych opcji, w tym {len(odrzucone)} "
            "odrzuconych przez filtr prawny wraz z podstawa kazdego odrzucenia."
        )
        report.number("opcji_w_logu", len(rozwazone), "szt")
        report.number("opcji_odrzuconych", len(odrzucone), "szt")
        report.number("odcisk_wpisu", audit["odcisk"])
        report.number("wersja_silnika", version_block()["engine"])
        report.number("wersja_bazy", version_block()["data"])
        report.number("nadpisania", version_block()["overrides"])
        if decision:
            report.number("decyzja", decision["rodzaj"])
            report.number("wybrana_opcja", decision["opcja"])

        report.findings["wpis"] = audit

        report.decide(
            "log zapisuje podstawe odrzucenia kazdej opcji -- w sporze liczy sie "
            "to, czego nie wybrano i dlaczego"
        )
        report.decide(
            f"wersja bazy `{version_block()['data']}` jest jednoczesnie wersja "
            "modelu kosztowego i prawa -- oba pochodza z tego samego pliku"
        )
        if version_block()["overrides"] != "brak":
            report.warn(
                f"run policzony z nadpisaniami polityki ({version_block()['overrides']}) "
                "-- kwoty moga odbiegac od bazy"
            )

        return NodeOutput(report, {"audit": audit})


def _digest(audit: dict) -> str:
    """Odcisk wpisu. Zmiana czegokolwiek w logu zmienia te wartosc."""
    blob = json.dumps(to_jsonable(
        {k: v for k, v in audit.items() if k != "odcisk"}),
        sort_keys=True, ensure_ascii=False)
    return f"sha256:{hashlib.sha256(blob.encode('utf-8')).hexdigest()[:24]}"
