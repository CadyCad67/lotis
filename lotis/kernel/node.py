"""Kontrakt node i uruchamianie przeplywu.

Kazdy z osiemnastu plikow w `lotis/nodes/` eksportuje jedna klase o tym samym
ksztalcie. Klasa bazowa mierzy czas, sprawdza obecnosc wejsc i zapisuje raport
-- plik node zawiera wylacznie logike dziedzinowa.
"""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from collections.abc import Sequence

from .budget import Degradation, RunBudget
from .clock import RunClock
from .errors import ExecutionFailure, LotisError, NoLawfulOption
from .policy_store import PolicyStore
from .report import Report, ReportWriter, Status


@dataclass(slots=True)
class NodeOutput:
    """To, co node oddaje: zmiana stanu plus raport."""

    report: Report
    state: dict[str, Any] = field(default_factory=dict)


class RunContext:
    """Stan jednego uruchomienia. Nodes czytaja i pisza wylacznie tutaj."""

    def __init__(
        self,
        run_id: str,
        *,
        clock: RunClock | None = None,
        budget: RunBudget | None = None,
        policy: PolicyStore | None = None,
        reports_root: Path | str = "reports",
        seed: int = 0,
    ) -> None:
        self.run_id = run_id
        self.clock = clock or RunClock()
        self.budget = budget or RunBudget()
        self.policy = policy or PolicyStore()
        self.writer = ReportWriter(run_id, Path(reports_root))
        self.seed = seed
        self.state: dict[str, Any] = {}
        self.snapshot_digest: str = ""
        self.halted: bool = False
        self.halt_reason: str = ""
        self.escalation: dict[str, Any] | None = None
        self.recalc_trigger: str | None = None

    # ---- stan ----

    def put(self, key: str, value: Any) -> None:
        self.state[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)

    def require(self, key: str) -> Any:
        if key not in self.state:
            raise KeyError(f"brak w stanie runu: {key}")
        return self.state[key]

    def has(self, *keys: str) -> bool:
        return all(k in self.state for k in keys)

    # ---- sterowanie ----

    def halt(self, reason: str, escalation: dict[str, Any] | None = None) -> None:
        self.halted = True
        self.halt_reason = reason
        if escalation is not None:
            self.escalation = escalation

    def request_recalc(self, trigger: str) -> None:
        self.recalc_trigger = trigger

    @property
    def degradation(self) -> Degradation:
        return self.budget.level()


class Node(ABC):
    """Baza wszystkich osiemnastu nodes."""

    id: str = "??"
    name: str = "unnamed"
    title: str = "UNNAMED"
    consumes: tuple[str, ...] = ()
    produces: str = ""

    # ---- do nadpisania ----

    @abstractmethod
    def run(self, ctx: RunContext) -> NodeOutput:
        """Logika dziedzinowa. Nie zapisuje plikow, nie mierzy czasu."""

    # ---- szkielet ----

    def new_report(self) -> Report:
        return Report(node_id=self.id, node_name=self.name, node_title=self.title)

    def execute(self, ctx: RunContext) -> Report:
        """Uruchamia node i zapisuje jego raport.

        Wyjatki z rodziny `LotisError` sa zamieniane na raport ze statusem
        `blocked` albo `degraded` -- to sa stany operacyjne, ktore maja swoje
        sciezki w przeplywie, a nie awarie.

        Kazdy inny wyjatek propaguje. `ZeroDivisionError` w node nie jest
        stanem operacyjnym, tylko bledem w kodzie, i zamiecenie go pod raport
        ze statusem `degraded` znaczyloby, ze run konczy sie liczba, ktorej
        nikt nie policzyl.
        """
        started = time.perf_counter()

        if ctx.halted:
            report = self.new_report()
            report.status = Status.BLOCKED
            report.summary = (
                f"Nie uruchomiony: przeplyw zatrzymany wczesniej ({ctx.halt_reason})."
            )
            report.data_gaps.append(f"przeplyw wstrzymany: {ctx.halt_reason}")
            return self._finish(ctx, report, started)

        missing = [k for k in self.consumes if k not in ctx.state]
        if missing:
            report = self.new_report()
            report.status = Status.BLOCKED
            report.summary = f"Brak wejsc: {', '.join(missing)}."
            report.data_gaps.extend(f"brak wejscia `{m}`" for m in missing)
            return self._finish(ctx, report, started)

        try:
            output = self.run(ctx)
        except NoLawfulOption as exc:
            report = self.new_report()
            report.status = Status.BLOCKED
            report.summary = str(exc)
            report.findings["escalation"] = exc.packet
            ctx.halt("brak dopuszczalnej opcji", exc.packet)
            return self._finish(ctx, report, started)
        except ExecutionFailure as exc:
            report = self.new_report()
            report.status = Status.DEGRADED
            report.summary = str(exc)
            report.findings["execution_failure"] = {
                "step": exc.step,
                "reason": exc.reason,
                "recoverable": exc.recoverable,
            }
            ctx.request_recalc("EXECUTION_FAILED")
            ctx.put("execution_failure", report.findings["execution_failure"])
            return self._finish(ctx, report, started)
        except LotisError as exc:
            report = self.new_report()
            report.status = Status.BLOCKED
            report.summary = f"{type(exc).__name__}: {exc}"
            report.data_gaps.append(str(exc))
            return self._finish(ctx, report, started)

        for key, value in output.state.items():
            ctx.put(key, value)
        return self._finish(ctx, output.report, started)

    def _finish(self, ctx: RunContext, report: Report, started: float) -> Report:
        elapsed = (time.perf_counter() - started) * 1000.0
        report.duration_ms = elapsed
        ctx.budget.record(self.id, elapsed)
        level = ctx.degradation
        if level is not Degradation.FULL and report.status is Status.OK:
            report.status = Status.DEGRADED
            report.warn(f"budzet czasu: tryb {level.label}")
        ctx.writer.write(report, snapshot=ctx.snapshot_digest, degradation=level.name)
        return report


class Pipeline:
    """Uruchamia nodes po kolei i domyka manifest."""

    def __init__(self, nodes: Sequence[Node]) -> None:
        self.nodes = list(nodes)

    def run(self, ctx: RunContext) -> list[Report]:
        reports = [node.execute(ctx) for node in self.nodes]
        ctx.writer.write_manifest({
            "halted": ctx.halted,
            "halt_reason": ctx.halt_reason,
            "escalation": ctx.escalation,
            "recalc_trigger": ctx.recalc_trigger,
            "snapshot": ctx.snapshot_digest,
            "budget": ctx.budget.snapshot(),
            "statuses": {r.node_id: r.status.value for r in reports},
        })
        return reports
