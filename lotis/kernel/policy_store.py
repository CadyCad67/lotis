"""Polityka i stawki -- jedno zrodlo prawdy, z warstwa nadpisan.

Wczesniej trzymalem stawki i reguly w recznie pisanych plikach `policy/*.json`.
Baza `loops.jsx` pokrywa je w calosci i lepiej: kwoty EU261 z cytowanym
orzecznictwem, tabele FDP EASA, koszty minuty opoznienia z University of
Westminster, czasy postoju policzone z obserwacji. Trzymanie obok tego wlasnej
kopii oznaczaloby dwa zrodla prawdy, ktore rozjada sie przy pierwszej zmianie.

Dlatego teraz:
  warstwa 1  baza z `loops.jsx` -- wszystko, czego nie nadpisano,
  warstwa 2  `policy/overrides.json` -- swiadome odstepstwa operatora.

Kazda wartosc z warstwy 2 jest raportowana jako odstepstwo, zeby nie dalo sie
po cichu podmienic kwoty odszkodowania i zapomniec o tym.

Waluta: baza jest w EUR, silnik liczy w PLN. Przelicznik siedzi w `K.fx` i sam
jest oznaczony w bazie jako placeholder -- node 09 raportuje go jako zalozenie.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_POLICY_DIR = Path(__file__).resolve().parent.parent / "policy"
OVERRIDES_FILE = "overrides.json"


class PolicyStore:
    """Dostep do parametrow po sciezce kropkowej, z nadpisaniami."""

    def __init__(self, directory: Path | str | None = None, db: Any = None) -> None:
        self.dir = Path(directory) if directory else DEFAULT_POLICY_DIR
        if db is None:
            from ..adapters.lot_db import load_lot_db
            db = load_lot_db()
        self.db = db
        self._overrides: dict[str, Any] = {}
        path = self.dir / OVERRIDES_FILE
        if path.exists():
            with path.open(encoding="utf-8") as fh:
                loaded = json.load(fh)
            self._overrides = {k: v for k, v in loaded.items() if not k.startswith("_")}
        self._used_overrides: set[str] = set()

        # Trzy pliki, ktorych baza NIE pokrywa -- to sa moje uzupelnienia luk
        # tablicy: progi autoryzacji (luka 4), adresat eskalacji (luka 5)
        # i definicja opcji domyslnej (luka 6).
        self._local: dict[str, dict[str, Any]] = {}
        for key, filename in (("authorization", "authorization.json"),
                              ("escalation", "escalation.json"),
                              ("sop", "sop_default.json")):
            local_path = self.dir / filename
            self._local[key] = (
                json.loads(local_path.read_text(encoding="utf-8"))
                if local_path.exists() else {}
            )

    # ---- uzupelnienia spoza bazy ----

    @property
    def authorization(self) -> dict[str, Any]:
        return self._local["authorization"]

    @property
    def escalation(self) -> dict[str, Any]:
        return self._local["escalation"]

    @property
    def sop(self) -> dict[str, Any]:
        return self._local["sop"]

    # ---- sekcje bazy ----

    @property
    def cost(self) -> dict[str, Any]:
        return self.db.costs

    @property
    def legal(self) -> dict[str, Any]:
        return self.db.eu261

    @property
    def ftl(self) -> dict[str, Any]:
        return self.db.ftl

    @property
    def config(self) -> dict[str, Any]:
        return self.db.config

    @property
    def hard_filters(self) -> list[str]:
        """Filtry, ktorych zaden suwak nie moze wylaczyc (CF.hard)."""
        return list(self.db.config.get("hard", []))

    @property
    def presets(self) -> list[dict[str, Any]]:
        return list(self.db.config.get("presets", []))

    @property
    def eur_pln(self) -> float:
        return float(self.get("fx.EUR_PLN", self.db.eur_pln))

    # ---- dostep ----

    def get(self, path: str, default: Any = None) -> Any:
        """`store.get("care.hotel_night_eur.WAW")`.

        Najpierw nadpisania, potem baza. Sciezka wchodzi w `K`, a jesli tam
        nie ma -- w caly obiekt DB.
        """
        if path in self._overrides:
            self._used_overrides.add(path)
            return self._overrides[path]
        for root in (self.db.costs, self.db.raw):
            node: Any = root
            for part in path.split("."):
                if not isinstance(node, dict) or part not in node:
                    node = None
                    break
                node = node[part]
            if node is not None:
                return node
        return default

    def require(self, path: str) -> Any:
        sentinel = object()
        value = self.get(path, sentinel)
        if value is sentinel:
            raise KeyError(f"brak wpisu polityki: {path}")
        return value

    def pln(self, path: str, default: float = 0.0) -> float:
        """Wartosc z bazy (EUR) przeliczona na PLN."""
        return float(self.get(path, default)) * self.eur_pln

    # ---- przejrzystosc ----

    def provenance(self, path: str) -> str:
        """'override' | 'baza' -- node raportuje, skad wzieta jest liczba."""
        return "override" if path in self._overrides else "baza"

    def applied_overrides(self) -> dict[str, Any]:
        return {k: self._overrides[k] for k in sorted(self._used_overrides)}

    def declared_overrides(self) -> dict[str, Any]:
        return dict(self._overrides)
