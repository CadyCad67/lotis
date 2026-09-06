"""Zegar runu i granice doby operacyjnej.

Run ma jeden zamrozony `now()`. Gdyby kazdy node pytal system o czas,
dwa uruchomienia tego samego snapshotu daloby dwa rozne wyniki i log
przestalby cokolwiek dowodzic.
"""

from __future__ import annotations

from datetime import UTC, datetime, time, timedelta

OPERATIONAL_DAY_START_LOCAL = time(4, 0)  # doba operacyjna: 04:00 -> 03:59 nastepnego dnia


class RunClock:
    """Zamrozony czas runu."""

    def __init__(self, now: datetime | None = None) -> None:
        moment = now or datetime.now(UTC)
        if moment.tzinfo is None:
            raise ValueError("RunClock wymaga czasu ze strefa (uzyj UTC)")
        self._now = moment.astimezone(UTC)

    def now(self) -> datetime:
        return self._now

    def minutes_until(self, moment: datetime) -> float:
        if moment.tzinfo is None:
            raise ValueError("porownanie z czasem bez strefy")
        return (moment.astimezone(UTC) - self._now).total_seconds() / 60.0

    def __repr__(self) -> str:
        return f"RunClock({self._now.isoformat()})"


def operational_day_bounds(moment: datetime, tz_offset_min: int = 0) -> tuple[datetime, datetime]:
    """Poczatek i koniec doby operacyjnej zawierajacej `moment`.

    Doba operacyjna nie pokrywa sie z kalendarzowa: zaczyna sie o 04:00 czasu
    lokalnego portu, bo rejsy po polnocy naleza do poprzedniego dnia pracy.
    """
    if moment.tzinfo is None:
        raise ValueError("operational_day_bounds wymaga czasu ze strefa")
    utc = moment.astimezone(UTC)
    local = utc + timedelta(minutes=tz_offset_min)
    start_local = local.replace(
        hour=OPERATIONAL_DAY_START_LOCAL.hour,
        minute=OPERATIONAL_DAY_START_LOCAL.minute,
        second=0,
        microsecond=0,
    )
    if local < start_local:
        start_local -= timedelta(days=1)
    end_local = start_local + timedelta(days=1)
    return (
        start_local - timedelta(minutes=tz_offset_min),
        end_local - timedelta(minutes=tz_offset_min),
    )
