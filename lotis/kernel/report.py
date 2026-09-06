"""Raport node -- jedyny styk silnika ze swiatem.

Kazdy z osiemnastu nodes zapisuje dokladnie te sama koperte w dwoch formach:
`.json` jest kanoniczny i z niego cytuje sie liczby, `.md` jest narracja dla
modelu. Oba renderuje ten sam obiekt, wiec nie moga sie rozjechac.
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
from datetime import date, datetime
from decimal import Decimal
from enum import Enum, StrEnum
from pathlib import Path
from typing import Any
from collections.abc import Iterable

from .money import Money
from .versions import REPORT_SCHEMA, version_block


class Status(StrEnum):
    OK = "ok"
    DEGRADED = "degraded"     # policzone, ale z zalozeniami albo pod presja czasu
    BLOCKED = "blocked"       # nie da sie policzyc, wymaga czlowieka


@dataclasses.dataclass(frozen=True, slots=True)
class Assumption:
    """Jawne zalozenie. To ta lista mowi modelowi, czego nie wolno podac jako fakt."""

    field: str
    source: str               # 'real' | 'synthetic' | 'policy' | 'derived'
    confidence: float = 1.0
    note: str = ""


@dataclasses.dataclass(slots=True)
class Report:
    node_id: str
    node_name: str
    node_title: str
    status: Status = Status.OK
    summary: str = ""
    numbers: dict[str, Any] = dataclasses.field(default_factory=dict)
    findings: dict[str, Any] = dataclasses.field(default_factory=dict)
    decisions: list[str] = dataclasses.field(default_factory=list)
    assumptions: list[Assumption] = dataclasses.field(default_factory=list)
    data_gaps: list[str] = dataclasses.field(default_factory=list)
    warnings: list[str] = dataclasses.field(default_factory=list)
    duration_ms: float = 0.0

    # wypelniane przez ReportWriter
    run_id: str = ""
    snapshot: str = ""
    degradation: str = "FULL"

    # ---- budowanie ----

    def number(self, key: str, value: Any, unit: str = "") -> None:
        """Skalar do zacytowania przez model. Zawsze z jednostka."""
        self.numbers[key] = {"value": to_jsonable(value), "unit": unit}

    def decide(self, text: str) -> None:
        self.decisions.append(text)

    def warn(self, text: str) -> None:
        self.warnings.append(text)
        if self.status is Status.OK:
            self.status = Status.DEGRADED

    def assume(self, field: str, source: str, confidence: float = 1.0, note: str = "") -> None:
        self.assumptions.append(Assumption(field, source, confidence, note))

    # ---- serializacja ----

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": REPORT_SCHEMA,
            "run_id": self.run_id,
            "node": {"id": self.node_id, "name": self.node_name, "title": self.node_title},
            "versions": version_block(),
            "snapshot": self.snapshot,
            "status": self.status.value,
            "degradation": self.degradation,
            "summary": self.summary,
            "numbers": self.numbers,
            "findings": to_jsonable(self.findings),
            "decisions": list(self.decisions),
            "assumptions": [dataclasses.asdict(a) for a in self.assumptions],
            "data_gaps": list(self.data_gaps),
            "warnings": list(self.warnings),
            "duration_ms": round(self.duration_ms, 2),
        }

    def to_markdown(self) -> str:
        d = self.to_dict()
        out: list[str] = []
        out.append(f"# [{self.node_id}] {self.node_title}")
        out.append("")
        out.append(f"**Status:** {d['status']} · **run:** `{d['run_id'] or '-'}` "
                   f"· **snapshot:** `{(d['snapshot'] or '-')[:23]}` · **{d['duration_ms']} ms**")
        if d["degradation"] != "FULL":
            out.append("")
            out.append(f"> Policzone w trybie degradacji: **{d['degradation']}**.")
        if self.summary:
            out.append("")
            out.append(self.summary)

        if self.numbers:
            out.append("")
            out.append("## Liczby")
            out.append("")
            out.append("| pole | wartosc | jednostka |")
            out.append("| --- | --- | --- |")
            for key, item in self.numbers.items():
                out.append(f"| `{key}` | {_fmt(item['value'])} | {item['unit'] or '-'} |")

        if self.decisions:
            out.append("")
            out.append("## Co ten node ustalil")
            out.append("")
            out.extend(f"- {line}" for line in self.decisions)

        if self.findings:
            out.append("")
            out.append("## Szczegoly")
            out.append("")
            out.extend(_render_findings(to_jsonable(self.findings)))

        if self.assumptions:
            out.append("")
            out.append("## Zalozenia")
            out.append("")
            out.append("| pole | zrodlo | pewnosc | uwaga |")
            out.append("| --- | --- | --- | --- |")
            for a in self.assumptions:
                out.append(f"| `{a.field}` | {a.source} | {a.confidence:.2f} | {a.note or '-'} |")

        if self.data_gaps:
            out.append("")
            out.append("## Braki danych")
            out.append("")
            out.extend(f"- {g}" for g in self.data_gaps)

        if self.warnings:
            out.append("")
            out.append("## Ostrzezenia")
            out.append("")
            out.extend(f"- {w}" for w in self.warnings)

        out.append("")
        v = d["versions"]
        footer = (f"_silnik {v['engine']} · baza danych {v.get('data', '?')} "
                  f"({v.get('data_generated', '?')})")
        if v.get("overrides", "brak") != "brak":
            footer += f" · **nadpisania: {v['overrides']}**"
        out.append(footer + "_")
        out.append("")
        return "\n".join(out)


# ---------------------------------------------------------------- pomocnicze


def to_jsonable(value: Any, _widziane: frozenset[int] = frozenset()) -> Any:
    """Rekurencyjnie sprowadza obiekty dziedzinowe do typow JSON-owych.

    `_widziane` niesie identyfikatory kontenerow na biezacej sciezce, zeby cykl
    w danych nie konczyl sie `RecursionError`. Zaden node cyklu nie tworzy, ale
    ta funkcja jest jedynym wyjsciem raportu na dysk: awaria tutaj wywraca caly
    run zamiast zdegradowac jeden node, a przyczyna bylaby widoczna dopiero
    w sladzie stosu na tysiac ramek.
    """
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Money):
        return value.to_json()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)

    marker = id(value)
    if marker in _widziane:
        return "<cykl w danych raportu>"
    glebiej = _widziane | {marker}

    if isinstance(value, dict):
        return {str(k): to_jsonable(v, glebiej) for k, v in value.items()}
    if isinstance(value, (set, frozenset)):
        return sorted(to_jsonable(v, glebiej) for v in value)
    if isinstance(value, (list, tuple)):
        return [to_jsonable(v, glebiej) for v in value]
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return {f.name: to_jsonable(getattr(value, f.name), glebiej)
                for f in dataclasses.fields(value)}
    return str(value)


def _fmt(value: Any) -> str:
    if isinstance(value, dict) and "major" in value and "currency" in value:
        return f"{value['major']} {value['currency']}"
    if isinstance(value, float):
        return f"{value:,.2f}".replace(",", " ")
    if isinstance(value, int):
        return f"{value:,}".replace(",", " ")
    if isinstance(value, list):
        return ", ".join(_fmt(v) for v in value) or "-"
    return str(value)


def _render_findings(node: Any, depth: int = 0) -> list[str]:
    """Plaskie, deterministyczne renderowanie zagniezdzonego slownika."""
    lines: list[str] = []
    pad = "  " * depth
    if isinstance(node, dict):
        for key, val in node.items():
            if isinstance(val, (dict, list)) and val:
                lines.append(f"{pad}- **{key}**")
                lines.extend(_render_findings(val, depth + 1))
            else:
                lines.append(f"{pad}- **{key}:** {_fmt(val)}")
    elif isinstance(node, list):
        for item in node:
            if isinstance(item, dict):
                head = item.get("id") or item.get("label") or item.get("name")
                if head:
                    rest = {k: v for k, v in item.items()
                            if k not in {"id", "label", "name"}}
                    lines.append(f"{pad}- **{head}**")
                    lines.extend(_render_findings(rest, depth + 1))
                    continue
                lines.extend(_render_findings(item, depth))
            else:
                lines.append(f"{pad}- {_fmt(item)}")
    else:
        lines.append(f"{pad}- {_fmt(node)}")
    return lines


# ---------------------------------------------------------------- writer


class ReportWriter:
    """Zapisuje pare plikow na node i utrzymuje manifest runu."""

    def __init__(self, run_id: str, root: Path) -> None:
        self.run_id = run_id
        self.dir = Path(root) / f"run_{run_id}"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.entries: list[dict[str, Any]] = []

    def write(self, report: Report, snapshot: str = "", degradation: str = "FULL") -> Path:
        report.run_id = self.run_id
        report.snapshot = snapshot
        report.degradation = degradation

        stem = f"{report.node_id}_{report.node_name}"
        payload = report.to_dict()
        blob = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False)

        json_path = self.dir / f"{stem}.json"
        md_path = self.dir / f"{stem}.md"
        json_path.write_text(blob, encoding="utf-8")
        md_path.write_text(report.to_markdown(), encoding="utf-8")

        self.entries.append({
            "node_id": report.node_id,
            "node_name": report.node_name,
            "title": report.node_title,
            "status": report.status.value,
            "json": json_path.name,
            "md": md_path.name,
            "duration_ms": round(report.duration_ms, 2),
            "digest": hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16],
            "warnings": len(report.warnings),
            "data_gaps": len(report.data_gaps),
        })
        return json_path

    def write_manifest(self, extra: dict[str, Any] | None = None) -> Path:
        manifest = {
            "schema": "lotis.manifest/v1",
            "run_id": self.run_id,
            "versions": version_block(),
            "nodes": self.entries,
            **(extra or {}),
        }
        path = self.dir / "_manifest.json"
        path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return path

    def paths(self) -> Iterable[Path]:
        return sorted(self.dir.glob("*.json"))
