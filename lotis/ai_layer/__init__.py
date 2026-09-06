"""OUTPUT 2 -- warstwa AI.

Czyta raporty zapisane przez silnik i produkuje wlasny output. Nie ma zadnej
sciezki zapisu do stanu silnika: ranking powstaje deterministycznie w nodes,
a model moze tylko opisac go slowami obok.

Cala warstwa da sie usunac i silnik dalej dziala.

Cztery elementy:
  `personas`       kto czyta i co pisze -- oraz ktore nodes w ogole widzi,
  `prompt_builder` sklada prompt z katalogu runu,
  `guard`          sprawdza, czy kazda liczba w odpowiedzi jest z raportu,
  `run_ai`         spina to w calosc i zapisuje wynik do `out/`.
"""

from ..kernel.env import get, load_env, require
from .guard import GuardResult, Severity, Violation, annotate, check
from .openrouter_client import Completion, OpenRouterClient, OpenRouterError
from .personas import ALL as PERSONAS
from .personas import Persona
from .prompt_builder import NodeReport, RunBundle, build_prompt, find_runs, latest_run, load_run
from .run_ai import AiOutput, run_all, run_directory, run_persona

__all__ = [
    "PERSONAS",
    "AiOutput",
    "Completion",
    "GuardResult",
    "NodeReport",
    "OpenRouterClient",
    "OpenRouterError",
    "Persona",
    "RunBundle",
    "Severity",
    "Violation",
    "annotate",
    "build_prompt",
    "check",
    "find_runs",
    "get",
    "latest_run",
    "load_env",
    "load_run",
    "require",
    "run_all",
    "run_directory",
    "run_persona",
]
