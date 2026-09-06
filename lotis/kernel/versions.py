"""Wersje silnika i danych.

Kazdy raport i kazdy wpis w logu niesie te wersje. Bez nich nie da sie
odtworzyc, czym byl policzony run sprzed miesiaca.

Model kosztowy i prawo nie maja juz wlasnych numerow wersji -- oba pochodza
z bazy `loops.jsx`, wiec wersja bazy jest ich wersja. To jest zamierzone:
jeden numer zamiast trzech, ktore i tak zawsze zmienialy sie razem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ENGINE_VERSION = "1.0.0"
REPORT_SCHEMA = "lotis.report/v1"

POLICY_DIR = Path(__file__).resolve().parent.parent / "policy"


def _db_versions() -> tuple[str, str]:
    """(wersja bazy, data wygenerowania) -- albo znaczniki braku."""
    try:
        from ..adapters.lot_db import load_lot_db
        db = load_lot_db()
        return db.version, db.generated
    except Exception:
        return "unavailable", "unavailable"


def _local_version(filename: str, default: str = "brak") -> str:
    path = POLICY_DIR / filename
    if not path.exists():
        return default
    try:
        return str(json.loads(path.read_text(encoding="utf-8")).get("version", default))
    except (json.JSONDecodeError, OSError):
        return default


def overrides_fingerprint() -> str:
    """Odcisk pliku nadpisan. Pusty plik daje `brak`, kazdy wpis zmienia wartosc."""
    path = POLICY_DIR / "overrides.json"
    if not path.exists():
        return "brak"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return "nieczytelny"
    active = {k: v for k, v in data.items() if not k.startswith("_")}
    if not active:
        return "brak"
    import hashlib
    blob = json.dumps(active, sort_keys=True, ensure_ascii=False).encode()
    return f"{len(active)}@{hashlib.sha256(blob).hexdigest()[:8]}"


def version_block() -> dict[str, Any]:
    db_version, db_generated = _db_versions()
    return {
        "engine": ENGINE_VERSION,
        "data": db_version,
        "data_generated": db_generated,
        "authorization": _local_version("authorization.json"),
        "escalation": _local_version("escalation.json"),
        "sop": _local_version("sop_default.json"),
        "overrides": overrides_fingerprint(),
    }
