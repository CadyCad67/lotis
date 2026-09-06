"""Loader bazy operacyjnej `lot-siatka.json`.

Uzupelnia `lot_db` o dwie rzeczy, ktorych tam nie ma:

* **tydzien operacyjny** -- siedem rzeczywistych dob (21-27 sierpnia 2026),
  po jednej na kazdy dzien tygodnia, z gotowymi rotacjami maszyn. To jest
  material wejsciowy dla node 01, a nie zaden generator.
* **statystyka** -- 6236 rzeczywistych operacji z rozkladem opoznien odlotu
  i przylotu, rozpisanym na 452 numery rejsu, 212 tras i 68 portow wylotu.

Ta druga sekcja jest w tym projekcie najcenniejsza. Daje node 11 realne
widelki niepewnosci zamiast zgadywanych, a node 17 punkt odniesienia do
kalibracji, ktory nie jest wymyslony.

Zasada rozdzialu przyjeta w zrodle i respektowana tutaj: rozklad (STD, STA,
blok) to dane twarde, wartosci rzeczywiste (ATD, ATA) siedza wylacznie
w `statystyka` i nigdy nie wchodza do rozkladu.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, UTC
from functools import cached_property
from itertools import pairwise
from pathlib import Path
from typing import Any

_SEARCH_ENV = "LOTIS_SIATKA_JSON"

WEEKDAYS_PL = ("poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela")


def _find_json() -> Path:
    from ..kernel.env import load_env
    load_env()
    if (configured := os.environ.get(_SEARCH_ENV, "").strip()):
        path = Path(configured)
        if not path.exists():
            raise FileNotFoundError(
                f"{_SEARCH_ENV} wskazuje na nieistniejacy plik: {path}"
            )
        return path
    root = Path(__file__).resolve().parent.parent.parent
    candidates = (root / "data" / "lot-siatka.json",
                  root / "lot-siatka.json",
                  Path.home() / "Downloads" / "dane" / "lot-siatka.json")
    for candidate in candidates:
        if candidate.exists():
            return candidate
    tried = "\n  ".join(str(c) for c in candidates)
    raise FileNotFoundError(
        f"nie znalazlem lot-siatka.json. Sprawdzone sciezki:\n  {tried}\n"
        f"Wskaz plik zmienna {_SEARCH_ENV} w .env"
    )


@dataclass(frozen=True, slots=True)
class DelayStats:
    """Rozklad opoznien w minutach. Ujemne = przed czasem."""

    n: int
    median: float
    mean: float
    p25: float
    p75: float
    p90: float
    max: float
    on_time_15_pct: float

    @classmethod
    def parse(cls, row: dict[str, Any]) -> "DelayStats":
        return cls(
            n=int(row["n"]), median=float(row["mediana"]), mean=float(row["srednia"]),
            p25=float(row["p25"]), p75=float(row["p75"]), p90=float(row["p90"]),
            max=float(row["max"]), on_time_15_pct=float(row["punktualnosc15"]),
        )

    @property
    def iqr(self) -> float:
        return self.p75 - self.p25

    def band(self) -> tuple[float, float, float]:
        """Widelki min / oczekiwane / max dla node 11, oparte na kwantylach."""
        return (self.p25, self.median, self.p90)


@dataclass(frozen=True, slots=True)
class OperationalFlight:
    """Jeden rejs z rzeczywistej doby operacyjnej."""

    number: str
    origin: str
    dest: str
    std_local: str
    sta_local: str
    std_utc_min: int          # minuta doby UTC
    block_min: int
    type_code: str
    reg: str

    def std_utc(self, day: date) -> datetime:
        return datetime.combine(day, time(0, 0), UTC) + timedelta(minutes=self.std_utc_min)

    def sta_utc(self, day: date) -> datetime:
        return self.std_utc(day) + timedelta(minutes=self.block_min)


@dataclass(frozen=True, slots=True)
class OperationalDay:
    weekday: int                       # 0 = poniedzialek
    name: str
    day: date
    flights: tuple[OperationalFlight, ...]
    rotations: Any                     # surowa sekcja, ksztalt zalezny od zrodla

    def by_registration(self) -> dict[str, list[OperationalFlight]]:
        out: dict[str, list[OperationalFlight]] = {}
        for flight in self.flights:
            out.setdefault(flight.reg, []).append(flight)
        for legs in out.values():
            legs.sort(key=lambda f: f.std_utc_min)
        return out

    def continuity_breaks(self) -> list[tuple[str, str, str]]:
        """Miejsca, w ktorych kolejny odcinek nie startuje tam, gdzie skonczyl poprzedni.

        Zrodlo podaje 92-98% ciaglosci; reszta to maszyny, ktorych czesc doby
        wypadla poza okno eksportu. Node 01 musi o tym wiedziec, bo przerwany
        lancuch to nie to samo co lancuch domkniety.
        """
        breaks: list[tuple[str, str, str]] = []
        for reg, legs in self.by_registration().items():
            for prev, nxt in pairwise(legs):
                if prev.dest != nxt.origin:
                    breaks.append((reg, prev.number, nxt.number))
        return breaks


class Siatka:
    def __init__(self, raw: dict[str, Any], source: Path | None = None) -> None:
        self.raw = raw
        self.source = source

    @classmethod
    def load(cls, path: Path | str | None = None) -> "Siatka":
        target = Path(path) if path else _find_json()
        return cls(json.loads(target.read_text(encoding="utf-8")), target)

    # ---- metadane ----

    @property
    def provenance(self) -> dict[str, Any]:
        return self.raw["zrodlo"]

    @property
    def tz_vs_waw(self) -> dict[str, int]:
        return self.raw["strefyCzasoweWzglWAW"]

    # ---- tydzien operacyjny ----

    @cached_property
    def week(self) -> dict[int, OperationalDay]:
        section = self.raw["tydzienOperacyjny"]
        out: dict[int, OperationalDay] = {}
        for index, name in enumerate(WEEKDAYS_PL):
            entry = section["dni"].get(name)
            if not entry:
                continue
            flights = tuple(
                OperationalFlight(
                    number=f["nr"], origin=f["o"], dest=f["d"],
                    std_local=f["std"], sta_local=f["sta"],
                    std_utc_min=_hm(f["stdUTC"]), block_min=int(f["blokMin"]),
                    type_code=f["typ"], reg=f["reg"],
                )
                for f in entry["loty"]
            )
            out[index] = OperationalDay(
                weekday=index, name=name,
                day=date.fromisoformat(entry["doba"]),
                flights=flights, rotations=entry.get("rotacje"),
            )
        return out

    def day_for(self, weekday: int) -> OperationalDay:
        return self.week[weekday]

    def busiest_day(self) -> OperationalDay:
        return max(self.week.values(), key=lambda d: len(d.flights))

    # ---- statystyka ----

    @cached_property
    def global_stats(self) -> dict[str, DelayStats]:
        g = self.raw["statystyka"]["globalna"]
        return {"odlot": DelayStats.parse(g["odlot"]), "przylot": DelayStats.parse(g["przylot"])}

    @cached_property
    def by_flight(self) -> dict[str, dict[str, DelayStats]]:
        return {
            nr: {k: DelayStats.parse(v) for k, v in row.items()}
            for nr, row in self.raw["statystyka"]["wgRejsu"].items()
        }

    @cached_property
    def by_route(self) -> dict[str, dict[str, DelayStats]]:
        return {
            key: {k: DelayStats.parse(v) for k, v in row.items()}
            for key, row in self.raw["statystyka"]["wgTrasy"].items()
        }

    @cached_property
    def by_departure_port(self) -> dict[str, DelayStats]:
        return {
            key: DelayStats.parse(row)
            for key, row in self.raw["statystyka"]["wgPortuWylotu"].items()
        }

    @property
    def flight_states(self) -> dict[str, int]:
        return self.raw["statystyka"]["stanyRejsow"]

    def departure_band(self, number: str, route: str | None = None) -> tuple[float, float, float]:
        """Widelki opoznienia odlotu: najpierw per numer, potem per trasa, potem globalnie.

        To jest wejscie dla node 11. Kaskada ma znaczenie: rozklad dla LO521
        jest inny niz sredni dla siatki, a udawanie ze nie jest, zawyza pewnosc.
        """
        stats = self.by_flight.get(number, {}).get("odlot")
        if stats and stats.n >= 5:
            return stats.band()
        route_stats = self.by_route.get(route, {}).get("odlot") if route else None
        if route_stats and route_stats.n >= 5:
            return route_stats.band()
        return self.global_stats["odlot"].band()

    def summary(self) -> dict[str, Any]:
        return {
            "zakres": self.provenance.get("zakresDanych"),
            "operacji": self.provenance.get("operacji"),
            "maszyn": self.provenance.get("maszyn"),
            "porty": len(self.raw["porty"]),
            "trasy": len(self.raw["trasy"]),
            "numery_rejsow": len(self.raw["rejsy"]),
            "doby_tygodnia": len(self.week),
            "rejsow_w_tygodniu": sum(len(d.flights) for d in self.week.values()),
            "statystyka_rejsow": len(self.by_flight),
            "statystyka_tras": len(self.by_route),
            "statystyka_portow": len(self.by_departure_port),
        }


def _hm(value: str) -> int:
    hours, _, minutes = value.partition(":")
    return int(hours) * 60 + int(minutes)


_CACHE: Siatka | None = None


def load_siatka(path: Path | str | None = None, refresh: bool = False) -> Siatka:
    global _CACHE
    if _CACHE is None or refresh or path is not None:
        _CACHE = Siatka.load(path)
    return _CACHE
