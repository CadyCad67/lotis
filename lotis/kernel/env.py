"""Wczytywanie `.env` bez zaleznosci.

`python-dotenv` zrobilby to samo, ale silnik ma nie miec zaleznosci, a plik
`.env` to kilkanascie linii `KLUCZ=wartosc`. Parser jest celowo scisly:
cicho przepuszczone smieci w konfiguracji sa gorsze niz blad.

Zasada pierwszenstwa: zmienna juz ustawiona w srodowisku wygrywa z plikiem.
Dzieki temu `set LOTIS_AI_MODEL=...` w terminalu nadpisuje `.env` bez edycji
pliku, a CI moze wstrzyknac sekrety bez podkladania pliku.

Modul siedzi w `kernel`, a nie w `ai_layer`, bo adaptery tez z niego korzystaja
-- sciezki do zrodel danych sa konfigurowalne tak samo jak klucz API.
"""

from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_ENV = PROJECT_ROOT / ".env"

_LOADED = False


def parse_env(text: str) -> dict[str, str]:
    """Sparsuj tresc pliku `.env`. Zwraca pary klucz-wartosc."""
    out: dict[str, str] = {}
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        line = line.removeprefix("export ").strip()
        if "=" not in line:
            raise ValueError(f".env linia {lineno}: brak znaku '=' -> {raw!r}")
        key, _, value = line.partition("=")
        key = key.strip()
        if not key:
            raise ValueError(f".env linia {lineno}: pusty klucz")
        value = value.strip()
        # Zdejmij cudzyslowy tylko gdy otaczaja calosc.
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        else:
            # Komentarz na koncu linii jest dozwolony tylko poza cudzyslowami.
            hash_at = value.find(" #")
            if hash_at >= 0:
                value = value[:hash_at].rstrip()
        out[key] = value
    return out


def load_env(path: Path | str | None = None, override: bool = False,
             force: bool = False) -> dict[str, str]:
    """Wczytaj `.env` do `os.environ`. Zwraca to, co faktycznie ustawiono.

    Domyslnie robi to raz na proces -- kolejne wywolania sa darmowe, wiec
    loadery moga wolac to bez obaw na kazdej sciezce.
    """
    global _LOADED
    if _LOADED and not force and path is None:
        return {}
    target = Path(path) if path else DEFAULT_ENV
    if path is None:
        _LOADED = True
    if not target.exists():
        return {}
    values = parse_env(target.read_text(encoding="utf-8"))
    applied: dict[str, str] = {}
    for key, value in values.items():
        if not value:
            continue          # pusty wpis znaczy "nie ustawiaj", nie "ustaw na pusto"
        if override or key not in os.environ:
            os.environ[key] = value
            applied[key] = value
    return applied


def get(key: str, default: str = "") -> str:
    load_env()
    return os.environ.get(key, default) or default


def get_int(key: str, default: int) -> int:
    raw = get(key, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"{key} musi byc liczba calkowita, jest {raw!r}") from exc


def require(key: str, hint: str = "") -> str:
    """Pobierz zmienna albo powiedz wprost, czego brakuje i gdzie to ustawic."""
    load_env()
    value = os.environ.get(key, "").strip()
    if not value:
        raise RuntimeError(
            f"brak zmiennej {key}." + (f" {hint}" if hint else "")
            + f" Ustaw ja w {DEFAULT_ENV} albo w srodowisku."
        )
    return value
