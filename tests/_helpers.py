"""Wspolne narzedzia testow.

Budowa snapshotu trwa okolo dwoch sekund, wiec caly zestaw dzieli jeden
egzemplarz na dobe. Testy i tak go nie modyfikuja -- `Snapshot` jest mrozony.
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from functools import lru_cache
from typing import Any

from lotis.kernel.contracts import (
    Aircraft, AircraftType, Airport, Basket, Cabin, CrewMember, CrewRole, Flight,
    Itinerary, Passenger, PaxStatus, Purchase, Rotation, Snapshot, TripType,
)
from lotis.kernel.money import Money

BASE = datetime(2026, 8, 21, 6, 0, tzinfo=UTC)


@lru_cache(maxsize=8)
def snapshot(weekday: int = 4):
    from lotis.adapters.network import build_snapshot
    return build_snapshot(weekday=weekday, seed=2026)


@lru_cache(maxsize=1)
def db():
    from lotis.adapters.lot_db import load_lot_db
    return load_lot_db()


@lru_cache(maxsize=1)
def siatka():
    from lotis.adapters.siatka import load_siatka
    return load_siatka()


# ---------------------------------------------------------------- atrapy


def flight(fid: str = "LO1", dep: str = "WAW", arr: str = "KRK",
           offset_min: int = 0, block_min: int = 60, seq: int = 0,
           rotation_id: str = "ROT1", type_code: str = "E75S",
           reg: str = "SP-LIA", crew: tuple[str, ...] = ()) -> Flight:
    std = BASE + timedelta(minutes=offset_min)
    return Flight(
        id=fid, number=fid, dep=dep, arr=arr,
        std=std, sta=std + timedelta(minutes=block_min),
        aircraft_reg=reg, type_code=type_code,
        rotation_id=rotation_id, seq=seq, crew_ids=crew,
    )


def airport(iata: str = "WAW", offset: int = 120, **kw: Any) -> Airport:
    defaults: dict[str, Any] = dict(
        icao="EPWA", tz_offset_min=offset, lat=52.17, lon=20.97,
        tz="Europe/Warsaw", name=iata, schengen=True, eu261=True,
    )
    defaults.update(kw)
    return Airport(iata=iata, **defaults)


def aircraft_type(code: str = "E75S", **kw: Any) -> AircraftType:
    defaults: dict[str, Any] = dict(
        name=code, seats_declared=82, seats_j=0, seats_pe=0, seats_y=0,
        range_km=3700, category="waskokadlubowy", rating="EJET", cabin_crew=2,
    )
    defaults.update(kw)
    return AircraftType(code=code, **defaults)


def crew_member(cid: str = "C1", role: CrewRole = CrewRole.CAPTAIN,
                rating: str = "EJET", limit: int = 780, used: int = 0) -> CrewMember:
    return CrewMember(
        id=cid, role=role, base="WAW", qualifications=frozenset({rating}),
        duty_start=BASE - timedelta(minutes=60), fdp_limit_min=limit, duty_used_min=used,
    )


def passenger(pid: str = "P1", itin: str = "OD1", fare: int = 100_00,
              anc: int = 20_00) -> Passenger:
    return Passenger(
        id=pid, itinerary_id=itin,
        basket=Basket(Cabin.ECONOMY, TripType.DIRECT, Purchase.EARLY, PaxStatus.BASE),
        fare=Money(fare), ancillary=Money(anc),
    )


def tiny_snapshot(flights: list[Flight] | None = None, **kw: Any) -> Snapshot:
    """Maly, w pelni kontrolowany snapshot do testow niezmiennikow."""
    legs = flights if flights is not None else [
        flight("F1", "WAW", "KRK", 0, 60, seq=0),
        flight("F2", "KRK", "WAW", 120, 60, seq=1),
    ]
    by_rotation: dict[str, list[str]] = {}
    for f in legs:
        by_rotation.setdefault(f.rotation_id, []).append(f.id)

    payload: dict[str, Any] = dict(
        taken_at=BASE,
        flights={f.id: f for f in legs},
        rotations={rid: Rotation(rid, "SP-LIA", tuple(ids))
                   for rid, ids in by_rotation.items()},
        airports={"WAW": airport("WAW"), "KRK": airport("KRK", icao="EPKK")},
        aircraft={"SP-LIA": Aircraft("SP-LIA", "", "E75S", "WAW")},
        aircraft_types={"E75S": aircraft_type("E75S")},
        crew={},
        passengers={},
        itineraries={},
    )
    payload.update(kw)
    return Snapshot(**payload)


def itinerary(iid: str = "OD1", segments: tuple[str, ...] = ("F1",)) -> Itinerary:
    return Itinerary(id=iid, origin="WAW", destination="KRK", segments=segments)
