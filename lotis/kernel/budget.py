"""Budzet czasu obliczen i drabina degradacji.

Odpowiedz na luke 10 tablicy: REZULTAT obiecuje "czas do decyzji", ale nikt
nie zapisal, ile system ma liczyc. Zamiast twardego timeoutu, ktory zwraca
nic, system schodzi po drabinie i zawsze oddaje wynik -- oznaczony jako
policzony pod presja czasu.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import IntEnum


class Degradation(IntEnum):
    """Im wyzej, tym mniej system zdazyl policzyc."""

    FULL = 0            # pelna siatka scenariuszy i pelny network impact
    REDUCED_SCENARIOS = 1  # zawezona siatka opoznien, mniej wariantow
    CACHED_NETWORK = 2     # network impact z cache zamiast przeliczenia
    HARD_STOP = 3          # czesciowy ranking, run oznaczony jako niepelny

    @property
    def label(self) -> str:
        return {
            Degradation.FULL: "pelny",
            Degradation.REDUCED_SCENARIOS: "zawezona siatka scenariuszy",
            Degradation.CACHED_NETWORK: "network impact z cache",
            Degradation.HARD_STOP: "twardy stop, ranking czesciowy",
        }[self]


@dataclass(slots=True)
class RunBudget:
    """Budzet calego runu, z progami degradacji jako ulamki budzetu."""

    total_ms: float = 20_000.0
    thresholds: tuple[float, float, float] = (0.55, 0.80, 0.95)
    _started: float = field(default_factory=time.perf_counter, init=False)
    _spent_by_node: dict[str, float] = field(default_factory=dict, init=False)

    def reset(self) -> None:
        self._started = time.perf_counter()
        self._spent_by_node.clear()

    @property
    def elapsed_ms(self) -> float:
        return (time.perf_counter() - self._started) * 1000.0

    @property
    def remaining_ms(self) -> float:
        return max(0.0, self.total_ms - self.elapsed_ms)

    def record(self, node_id: str, ms: float) -> None:
        self._spent_by_node[node_id] = self._spent_by_node.get(node_id, 0.0) + ms

    def spent(self) -> dict[str, float]:
        return dict(self._spent_by_node)

    def level(self) -> Degradation:
        used = self.elapsed_ms / self.total_ms if self.total_ms > 0 else 1.0
        low, mid, high = self.thresholds
        if used >= high:
            return Degradation.HARD_STOP
        if used >= mid:
            return Degradation.CACHED_NETWORK
        if used >= low:
            return Degradation.REDUCED_SCENARIOS
        return Degradation.FULL

    def snapshot(self) -> dict[str, object]:
        level = self.level()
        return {
            "total_ms": self.total_ms,
            "elapsed_ms": round(self.elapsed_ms, 1),
            "remaining_ms": round(self.remaining_ms, 1),
            "level": level.name,
            "level_label": level.label,
            "per_node_ms": {k: round(v, 1) for k, v in sorted(self._spent_by_node.items())},
        }
