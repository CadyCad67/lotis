"""Skladanie promptu z raportow runu.

Wejsciem jest katalog `reports/run_<id>/` -- para plikow na node plus manifest.
Wyjsciem jest gotowa para (system, user) do wyslania do modelu.

Dwie decyzje warte uzasadnienia:

*Do promptu idzie `.md`, nie `.json`.* Oba renderuje ten sam obiekt, wiec nie
moga sie rozjechac, ale narracja czyta sie modelowi lepiej niz zagniezdzony
slownik i zostawia wiecej miejsca na tresc. JSON zostaje zrodlem prawdy dla
`guard.py` -- straznik porownuje odpowiedz z liczbami z JSON-a, nie z tekstu.

*Prompt niesie jawna liste dozwolonych liczb.* Bez niej model nie ma jak
odroznic liczby, ktora wolno mu zacytowac, od liczby, ktora sam wyliczyl.
Lista jest ta sama, na ktorej pracuje straznik, wiec regula i jej egzekwowanie
pochodza z jednego miejsca.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from collections.abc import Iterator

from .personas import Persona

#: Twardy limit znakow na czesc uzytkownika. Darmowe modele maja rozne okna
#: kontekstu; lepiej przyciac raporty jawnie niz dostac obciety wynik.
MAX_USER_CHARS = 60_000

MANIFEST = "_manifest.json"


@dataclass(frozen=True, slots=True)
class NodeReport:
    node_id: str
    node_name: str
    title: str
    status: str
    markdown: str
    payload: dict[str, Any]

    @property
    def stem(self) -> str:
        return f"{self.node_id}_{self.node_name}"


@dataclass(frozen=True, slots=True)
class RunBundle:
    """Komplet raportow jednego runu."""

    run_id: str
    directory: Path
    manifest: dict[str, Any]
    reports: tuple[NodeReport, ...]

    @property
    def snapshot(self) -> str:
        return str(self.manifest.get("snapshot", ""))

    @property
    def degradation(self) -> str:
        return str((self.manifest.get("budget") or {}).get("level", "FULL"))

    def for_persona(self, persona: Persona) -> tuple[NodeReport, ...]:
        return tuple(r for r in self.reports if persona.wants(r.node_id))


def load_run(directory: Path | str) -> RunBundle:
    """Wczytaj katalog runu. Manifest jest opcjonalny -- raporty sa obowiazkowe."""
    path = Path(directory)
    if not path.is_dir():
        raise FileNotFoundError(f"nie ma katalogu runu: {path}")

    manifest_path = path / MANIFEST
    manifest: dict[str, Any] = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    reports: list[NodeReport] = []
    for json_path in sorted(path.glob("*.json")):
        if json_path.name == MANIFEST:
            continue
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        node = payload.get("node", {})
        md_path = json_path.with_suffix(".md")
        reports.append(NodeReport(
            node_id=str(node.get("id", "??")),
            node_name=str(node.get("name", json_path.stem)),
            title=str(node.get("title", "")),
            status=str(payload.get("status", "?")),
            markdown=md_path.read_text(encoding="utf-8") if md_path.exists() else "",
            payload=payload,
        ))

    if not reports:
        raise FileNotFoundError(f"katalog {path} nie zawiera zadnego raportu node")

    run_id = str(manifest.get("run_id") or path.name.removeprefix("run_"))
    return RunBundle(run_id, path, manifest, tuple(sorted(reports, key=lambda r: r.node_id)))


def find_runs(root: Path | str = "reports") -> list[Path]:
    """Katalogi runow, najnowsze pierwsze."""
    base = Path(root)
    if not base.is_dir():
        return []
    runs = [p for p in base.iterdir() if p.is_dir() and p.name.startswith("run_")]
    return sorted(runs, key=lambda p: p.stat().st_mtime, reverse=True)


def latest_run(root: Path | str = "reports") -> Path | None:
    runs = find_runs(root)
    return runs[0] if runs else None


# ---------------------------------------------------------------- liczby


def iter_numbers(value: Any) -> Iterator[float]:
    """Wszystkie liczby w strukturze raportu, rekurencyjnie.

    `bool` jest podklasa `int` w Pythonie, wiec bez jawnego odsiania kazde
    `true` w raporcie stalo by sie dozwolona jedynka.
    """
    if isinstance(value, bool):
        return
    if isinstance(value, (int, float)):
        yield float(value)
    elif isinstance(value, dict):
        for item in value.values():
            yield from iter_numbers(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from iter_numbers(item)
    elif isinstance(value, str):
        # Kwoty sa serializowane jako napis ("major": "1234.56"), wiec napis
        # dajacy sie sparsowac w calosci tez jest liczba z raportu.
        try:
            yield float(value.replace(" ", "").replace(",", "."))
        except ValueError:
            return


def allowed_numbers(reports: tuple[NodeReport, ...]) -> set[float]:
    out: set[float] = set()
    for report in reports:
        out.update(iter_numbers(report.payload))
    return out


# ---------------------------------------------------------------- prompt


def build_prompt(bundle: RunBundle, persona: Persona,
                 question: str = "") -> tuple[str, str]:
    """Zwraca (system, user)."""
    selected = bundle.for_persona(persona)
    if not selected:
        raise ValueError(
            f"persona {persona.id!r} czyta nodes {persona.reads}, "
            f"a run {bundle.run_id} zawiera tylko "
            f"{sorted(r.node_id for r in bundle.reports)}"
        )

    head = [
        f"# RUN {bundle.run_id}",
        f"snapshot: {bundle.snapshot or 'brak'}",
        f"tryb obliczen: {bundle.degradation}",
        f"raporty w tym runie: {', '.join(r.stem for r in bundle.reports)}",
        f"raporty widoczne dla twojej roli: {', '.join(r.stem for r in selected)}",
    ]
    if bundle.manifest.get("halted"):
        head.append(f"UWAGA: przeplyw zatrzymany -- {bundle.manifest.get('halt_reason', '?')}")
    if bundle.degradation not in ("FULL", ""):
        head.append(
            "UWAGA: silnik nie zdazyl policzyc pelnej siatki. Napisz o tym w pierwszym akapicie."
        )

    teksty = [r.markdown or _fallback_markdown(r) for r in selected]
    ogon = _number_whitelist(selected)
    polecenie = (question.strip() if question.strip()
                 else "Przygotuj material zgodnie ze swoja rola i narzucona struktura.")
    naglowek = "\n".join(head)

    # Kazdy raport dokłada separator, dwie puste linie i ewentualna adnotacje
    # o skroceniu. Bez wliczenia tego prompt przekraczal limit o kilka procent
    # -- czyli dokladnie tam, gdzie model z ciasnym oknem kontekstu sie lamie.
    narzut = (len(SEPARATOR) + 2 + len(_TRIM_NOTE_MAX)) * len(teksty)
    budzet = MAX_USER_CHARS - len(naglowek) - len(ogon) - len(polecenie) - narzut - 64
    teksty = _fit(teksty, max(1000, budzet))

    body: list[str] = [naglowek, ""]
    for tekst in teksty:
        body.append(SEPARATOR)
        body.append(tekst)
        body.append("")
    body.append(SEPARATOR)
    body.append(ogon)
    body.append("")
    body.append(SEPARATOR)
    body.append(polecenie)
    return persona.system_prompt(), "\n".join(body)


def _fit(teksty: list[str], budzet: int) -> list[str]:
    """Dopasowuje raporty do budzetu znakow, skracajac je proporcjonalnie.

    Wczesniej prompt byl przycinany na koncu jednym cieciem. To znaczylo, ze
    dyspozytor, ktory czyta wszystkie osiemnascie raportow, tracil dokladnie
    te ostatnie -- LOG i WYNIK RZECZYWISTY. Model nie mial jak zauwazyc braku,
    bo tekst konczyl sie w polowie zdania.

    Teraz kazdy raport, ktory nie miesci sie w swoim przydziale, jest skracany
    osobno i JAWNIE oznaczony. Zachowujemy poczatek, bo tam sa status,
    podsumowanie i sekcja "Liczby" -- czyli wszystko, co model ma prawo
    zacytowac. Obcinane sa "Szczegoly", ktore bywaja dluga lista.
    """
    razem = sum(len(t) for t in teksty)
    if razem <= budzet or not teksty:
        return teksty

    przydzial = budzet // len(teksty)
    # Raporty krotsze od przydzialu oddaja nadwyzke pozostalym.
    nadwyzka = sum(przydzial - len(t) for t in teksty if len(t) < przydzial)
    dlugie = [t for t in teksty if len(t) > przydzial]
    bonus = nadwyzka // len(dlugie) if dlugie else 0

    out: list[str] = []
    for tekst in teksty:
        limit = przydzial + bonus
        if len(tekst) <= limit:
            out.append(tekst)
            continue
        # Miejsce na adnotacje odejmujemy OD limitu, a nie dokladamy po nim.
        tresc = max(200, limit - len(_TRIM_NOTE_MAX))
        out.append(tekst[:tresc].rstrip() + _trim_note(len(tekst) - tresc))
    return out


SEPARATOR = "=" * 70

#: Najdluzsza mozliwa adnotacja o skroceniu -- rezerwujemy tyle miejsca.
_TRIM_NOTE_MAX = ("\n\n_[raport skrocony o 999999 znakow -- pominieto dalsze "
                  "szczegoly; liczby powyzej sa kompletne]_")


def _trim_note(uciete: int) -> str:
    return (f"\n\n_[raport skrocony o {uciete} znakow -- pominieto dalsze "
            "szczegoly; liczby powyzej sa kompletne]_")


def _number_whitelist(reports: tuple[NodeReport, ...], limit: int = 400) -> str:
    values = sorted(allowed_numbers(reports))
    shown = values[:limit]
    text = ", ".join(_fmt(v) for v in shown)
    note = "" if len(values) <= limit else f" (i {len(values) - limit} dalszych)"
    return (
        "## LICZBY, KTORE WOLNO CI ZACYTOWAC\n\n"
        "Kazda liczba w twojej odpowiedzi musi byc jedna z ponizszych albo "
        "numerem rejsu, godzina lub data przepisana z raportu. Odpowiedz "
        "zawierajaca liczbe spoza tej listy jest odrzucana automatycznie.\n\n"
        f"{text}{note}"
    )


def _fmt(value: float) -> str:
    return str(int(value)) if float(value).is_integer() else f"{value:g}"


def _fallback_markdown(report: NodeReport) -> str:
    """Gdy brakuje `.md`, sklada minimalna narracje z JSON-a."""
    lines = [f"# [{report.node_id}] {report.title}", "",
             f"**Status:** {report.status}", ""]
    for key, item in (report.payload.get("numbers") or {}).items():
        unit = item.get("unit") or ""
        lines.append(f"- `{key}`: {item.get('value')} {unit}".rstrip())
    return "\n".join(lines)
