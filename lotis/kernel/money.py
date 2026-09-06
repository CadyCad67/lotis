"""Pieniadze jako liczby calkowite w jednostkach mniejszych (grosze).

Float nie ma prawa dotknac kwoty w tym systemie. Cala arytmetyka idzie na
`int` w groszach, a jedyne miejsce, gdzie wchodzi zaokraglanie, to mnozenie
przez wspolczynnik -- i tam jest jawnie ROUND_HALF_UP.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from collections.abc import Iterable

from .errors import CurrencyMismatch

DEFAULT_CURRENCY = "PLN"


@dataclass(frozen=True, slots=True, order=False)
class Money:
    """Kwota w jednostkach mniejszych. `Money(12345)` to 123,45 PLN."""

    minor: int
    currency: str = DEFAULT_CURRENCY

    def __post_init__(self) -> None:
        if not isinstance(self.minor, int) or isinstance(self.minor, bool):
            raise TypeError(f"Money.minor musi byc int, dostalem {type(self.minor).__name__}")
        if not self.currency or len(self.currency) != 3:
            raise ValueError(f"nieprawidlowy kod waluty: {self.currency!r}")

    # ---- konstruktory ----

    @classmethod
    def zero(cls, currency: str = DEFAULT_CURRENCY) -> "Money":
        return cls(0, currency)

    @classmethod
    def from_major(cls, amount: int | float | str | Decimal,
                   currency: str = DEFAULT_CURRENCY) -> "Money":
        """Z jednostek glownych. `from_major("123.45")` -> 12345 groszy."""
        dec = Decimal(str(amount))
        minor = int((dec * 100).quantize(Decimal(1), rounding=ROUND_HALF_UP))
        return cls(minor, currency)

    # ---- wlasciwosci ----

    @property
    def major(self) -> Decimal:
        return (Decimal(self.minor) / 100).quantize(Decimal("0.01"))

    # ---- arytmetyka ----

    def _check(self, other: "Money") -> None:
        if self.currency != other.currency:
            raise CurrencyMismatch(
                f"nie sumuje {self.currency} z {other.currency}"
            )

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        self._check(other)
        return Money(self.minor + other.minor, self.currency)

    def __sub__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        self._check(other)
        return Money(self.minor - other.minor, self.currency)

    def __neg__(self) -> "Money":
        return Money(-self.minor, self.currency)

    def __abs__(self) -> "Money":
        return Money(abs(self.minor), self.currency)

    def __mul__(self, factor: int | float | Decimal) -> "Money":
        if isinstance(factor, bool) or not isinstance(factor, (int, float, Decimal)):
            return NotImplemented
        product = Decimal(self.minor) * Decimal(str(factor))
        return Money(
            int(product.quantize(Decimal(1), rounding=ROUND_HALF_UP)),
            self.currency,
        )

    __rmul__ = __mul__

    def __truediv__(self, divisor: int | float | Decimal) -> "Money":
        if isinstance(divisor, bool) or not isinstance(divisor, (int, float, Decimal)):
            return NotImplemented
        d = Decimal(str(divisor))
        if d == 0:
            raise ZeroDivisionError("dzielenie kwoty przez zero")
        quotient = Decimal(self.minor) / d
        return Money(
            int(quotient.quantize(Decimal(1), rounding=ROUND_HALF_UP)),
            self.currency,
        )

    # ---- porownania ----

    def _cmp_check(self, other: object) -> "Money":
        if not isinstance(other, Money):
            raise TypeError(f"nie porownuje Money z {type(other).__name__}")
        self._check(other)
        return other

    def __lt__(self, other: object) -> bool:
        return self.minor < self._cmp_check(other).minor

    def __le__(self, other: object) -> bool:
        return self.minor <= self._cmp_check(other).minor

    def __gt__(self, other: object) -> bool:
        return self.minor > self._cmp_check(other).minor

    def __ge__(self, other: object) -> bool:
        return self.minor >= self._cmp_check(other).minor

    # ---- prezentacja ----

    def __str__(self) -> str:
        return f"{self.major} {self.currency}"

    def __repr__(self) -> str:
        return f"Money({self.minor}, {self.currency!r})"

    def to_json(self) -> dict[str, object]:
        return {"minor": self.minor, "currency": self.currency, "major": str(self.major)}


def money_sum(values: Iterable[Money], currency: str = DEFAULT_CURRENCY) -> Money:
    """Suma kwot. Pusta sekwencja daje zero we wskazanej walucie."""
    total = Money.zero(currency)
    for value in values:
        total = total + value
    return total
