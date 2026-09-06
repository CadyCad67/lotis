"""Horyzont propagacji dla NETWORK IMPACT.

Tablica stawia warunek wprost: liczymy do konca doby operacyjnej albo do
powrotu samolotu do bazy, co nastapi pierwsze. Oba warunki sa tutaj, w jednym
miejscu, zeby node 10 i node 13 uzywaly tej samej definicji.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .clock import operational_day_bounds
from .contracts import Flight, Snapshot


@dataclass(frozen=True, slots=True)
class HorizonResult:
    flights: tuple[Flight, ...]
    stop_reason: str          # 'BASE_RETURN' | 'END_OF_DAY' | 'ROTATION_END'
    cutoff: datetime


def downstream_flights(
    snapshot: Snapshot,
    from_flight_id: str,
    home_base: str,
    max_legs: int = 12,
) -> HorizonResult:
    """Kolejne odcinki tego samego samolotu po `from_flight_id`."""
    start = snapshot.flights.get(from_flight_id)
    if start is None:
        raise KeyError(f"nieznany rejs: {from_flight_id}")

    airport = snapshot.airports.get(start.dep)
    tz_offset = airport.tz_offset_min if airport else 0
    _, day_end = operational_day_bounds(start.std, tz_offset)

    rotation = snapshot.rotations.get(start.rotation_id)
    if rotation is None:
        return HorizonResult((), "ROTATION_END", day_end)

    ordered = [snapshot.flights[f] for f in rotation.flight_ids if f in snapshot.flights]
    ordered.sort(key=lambda f: (f.seq, f.std))

    try:
        index = next(i for i, f in enumerate(ordered) if f.id == from_flight_id)
    except StopIteration:
        return HorizonResult((), "ROTATION_END", day_end)

    collected: list[Flight] = []
    stop_reason = "ROTATION_END"
    for flight in ordered[index + 1:]:
        if len(collected) >= max_legs:
            stop_reason = "MAX_LEGS"
            break
        if flight.std >= day_end:
            stop_reason = "END_OF_DAY"
            break
        collected.append(flight)
        if flight.arr == home_base:
            stop_reason = "BASE_RETURN"
            break

    return HorizonResult(tuple(collected), stop_reason, day_end)


def connecting_passengers(snapshot: Snapshot, flight_id: str) -> list[str]:
    """Pasazerowie, dla ktorych `flight_id` nie jest ostatnim odcinkiem."""
    out: list[str] = []
    for pax in snapshot.passengers.values():
        itin = snapshot.itineraries.get(pax.itinerary_id)
        if not itin or flight_id not in itin.segments:
            continue
        if itin.segments.index(flight_id) < len(itin.segments) - 1:
            out.append(pax.id)
    return sorted(out)
