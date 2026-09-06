"""OUTPUT 2 -- uruchomienie warstwy AI na raportach runu.

Przeplyw jest jednokierunkowy i to jest cala jego istota:

    reports/run_<id>/*.json  ->  prompt  ->  model  ->  straznik  ->  out/run_<id>/*.md

Nic z prawej strony nie wraca na lewa. Model nie zapisuje do stanu silnika,
nie zmienia rankingu i nie ma dostepu do snapshotu -- widzi wylacznie to, co
silnik juz policzyl i zapisal. Cala warstwa da sie usunac i silnik dalej dziala.

Tryb `--dry-run` sklada kompletny prompt i zapisuje go do pliku, nie dzwoniac
nigdzie. Dziala bez klucza API i jest wlasciwym sposobem sprawdzenia, co model
w ogole dostanie do reki.
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from collections.abc import Sequence

from ..kernel import env
from . import personas as personas_mod
from .guard import GuardResult, annotate, check
from .openrouter_client import Completion, OpenRouterClient, OpenRouterError
from .personas import Persona
from .prompt_builder import RunBundle, build_prompt, load_run

DEFAULT_OUT = "out"


@dataclass(slots=True)
class AiOutput:
    """Wynik jednej persony na jednym runie."""

    run_id: str
    persona: str
    model: str
    dry_run: bool
    system: str
    user: str
    text: str = ""
    guard: GuardResult | None = None
    prompt_tokens: int = 0
    completion_tokens: int = 0
    duration_ms: float = 0.0
    error: str = ""
    files: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.error and (self.dry_run or bool(self.text))

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": "lotis.ai/v1",
            "run_id": self.run_id,
            "persona": self.persona,
            "model": self.model,
            "dry_run": self.dry_run,
            "ok": self.ok,
            "error": self.error,
            "prompt_chars": len(self.user),
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "duration_ms": round(self.duration_ms, 1),
            "guard": self.guard.as_dict() if self.guard else None,
            "text": self.text,
            "files": list(self.files),
        }


def run_persona(
    bundle: RunBundle,
    persona: Persona | str,
    *,
    question: str = "",
    dry_run: bool = False,
    client: OpenRouterClient | None = None,
    out_root: Path | str = DEFAULT_OUT,
) -> AiOutput:
    """Zbuduj prompt, ewentualnie zawolaj model, sprawdz liczby, zapisz."""
    p = personas_mod.get(persona) if isinstance(persona, str) else persona
    system, user = build_prompt(bundle, p, question)

    active = client or OpenRouterClient()
    out = AiOutput(
        run_id=bundle.run_id, persona=p.id, model=active.model,
        dry_run=dry_run, system=system, user=user,
    )

    started = time.perf_counter()
    if not dry_run:
        try:
            completion: Completion = active.complete(
                system, user,
                temperature=p.temperature, max_tokens=p.max_tokens,
            )
        except (OpenRouterError, RuntimeError) as exc:
            out.error = str(exc)
        else:
            out.text = completion.text
            out.model = completion.model
            out.prompt_tokens = completion.prompt_tokens
            out.completion_tokens = completion.completion_tokens
            out.guard = check(completion.text, bundle.for_persona(p))
    out.duration_ms = (time.perf_counter() - started) * 1000.0

    out.files = _write(out, bundle, out_root)
    return out


def run_all(
    bundle: RunBundle,
    which: Sequence[str] | None = None,
    *,
    question: str = "",
    dry_run: bool = False,
    client: OpenRouterClient | None = None,
    out_root: Path | str = DEFAULT_OUT,
) -> list[AiOutput]:
    """Wszystkie persony po kolei. Blad jednej nie zatrzymuje pozostalych."""
    names = list(which) if which else personas_mod.names()
    shared = client or OpenRouterClient()
    results: list[AiOutput] = []
    for name in names:
        try:
            results.append(run_persona(
                bundle, name, question=question, dry_run=dry_run,
                client=shared, out_root=out_root,
            ))
        except (KeyError, ValueError) as exc:
            results.append(AiOutput(
                run_id=bundle.run_id, persona=name, model=shared.model,
                dry_run=dry_run, system="", user="", error=str(exc),
            ))
    _write_index(results, bundle, out_root)
    return results


def run_directory(
    directory: Path | str,
    which: Sequence[str] | None = None,
    **kwargs: Any,
) -> list[AiOutput]:
    return run_all(load_run(directory), which, **kwargs)


def api_key_present() -> bool:
    return bool(env.get("OPENROUTER_API_KEY", "").strip())


# ---------------------------------------------------------------- zapis


def _dir_for(bundle: RunBundle, out_root: Path | str) -> Path:
    target = Path(out_root) / f"run_{bundle.run_id}"
    target.mkdir(parents=True, exist_ok=True)
    return target


def _write(out: AiOutput, bundle: RunBundle, out_root: Path | str) -> list[str]:
    target = _dir_for(bundle, out_root)
    written: list[str] = []

    prompt_path = target / f"{out.persona}.prompt.txt"
    prompt_path.write_text(
        f"===== SYSTEM =====\n{out.system}\n\n===== USER =====\n{out.user}\n",
        encoding="utf-8",
    )
    written.append(prompt_path.name)

    if out.text:
        body = annotate(out.text, out.guard) if out.guard else out.text
        md_path = target / f"{out.persona}.md"
        md_path.write_text(body, encoding="utf-8")
        written.append(md_path.name)

    json_path = target / f"{out.persona}.json"
    json_path.write_text(
        json.dumps(out.as_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    written.append(json_path.name)
    return written


def _write_index(results: Sequence[AiOutput], bundle: RunBundle,
                 out_root: Path | str) -> Path:
    target = _dir_for(bundle, out_root)
    index = {
        "schema": "lotis.ai.index/v1",
        "run_id": bundle.run_id,
        "snapshot": bundle.snapshot,
        "personas": [
            {
                "persona": r.persona,
                "ok": r.ok,
                "dry_run": r.dry_run,
                "model": r.model,
                "error": r.error,
                "guard_clean": r.guard.clean if r.guard else None,
                "guard_summary": r.guard.summary() if r.guard else None,
                "files": r.files,
            }
            for r in results
        ],
    }
    path = target / "_index.json"
    path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    return path
