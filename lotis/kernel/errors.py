"""Wyjatki silnika.

Podzial jest celowy: `ContractViolation` oznacza blad programisty (zlamana
niezmiennik), `DataGap` oznacza brak danych, a `NoLawfulOption` i
`ExecutionFailure` to normalne stany operacyjne, ktore maja swoje sciezki
w przeplywie.
"""

from __future__ import annotations

from typing import Any


class LotisError(Exception):
    """Baza dla wszystkich bledow systemu."""


class ContractViolation(LotisError):
    """Zlamany niezmiennik silnika. Zawsze blad w kodzie, nigdy w danych."""


class CurrencyMismatch(LotisError):
    """Proba zsumowania kwot w roznych walutach."""


class DataGap(LotisError):
    """Brak danych uniemozliwiajacy policzenie opcji.

    Nie jest bledem krytycznym: node 02 klasyfikuje pole jako UNKNOWN,
    a opcje od niego zalezne dostaja status `blocked`.
    """

    def __init__(self, field: str, detail: str = "") -> None:
        self.field = field
        self.detail = detail
        super().__init__(f"brak danych: {field}" + (f" ({detail})" if detail else ""))


class InfeasibleOption(LotisError):
    """Opcja odpadla na bramce wykonalnosci (node 05)."""

    def __init__(self, option_id: str, gate: str, reason: str) -> None:
        self.option_id = option_id
        self.gate = gate
        self.reason = reason
        super().__init__(f"{option_id} odpada na bramce {gate}: {reason}")


class NoLawfulOption(LotisError):
    """Wszystkie opcje odpadly na filtrze prawnym (node 12).

    Niesie gotowy pakiet eskalacyjny -- to jest odpowiedz na luke 5 tablicy,
    ktora miala galaz `BRAK DOPUSZCZALNEJ OPCJI` bez adresata i bez tresci.
    """

    def __init__(self, packet: dict[str, Any]) -> None:
        self.packet = packet
        super().__init__(
            "brak dopuszczalnej opcji -- eskalacja do "
            f"{packet.get('addressee', {}).get('role', '?')}"
        )


class ExecutionFailure(LotisError):
    """Decyzja nie dala sie wykonac (node 15b).

    Rozni sie od bledu modelu i musi byc rozroznialna w node 17, inaczej
    kalibracja uczy sie na cudzych bledach.
    """

    def __init__(self, step: str, reason: str, recoverable: bool = True) -> None:
        self.step = step
        self.reason = reason
        self.recoverable = recoverable
        super().__init__(f"wykonanie nie powiodlo sie na kroku {step}: {reason}")


class BudgetExceeded(LotisError):
    """Przekroczony budzet czasu obliczen (luka 10 tablicy)."""

    def __init__(self, node_id: str, spent_ms: float, limit_ms: float) -> None:
        self.node_id = node_id
        self.spent_ms = spent_ms
        self.limit_ms = limit_ms
        super().__init__(
            f"node {node_id}: {spent_ms:.0f} ms przy limicie {limit_ms:.0f} ms"
        )
