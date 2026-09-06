"""Budowa snapshotu silnika z obu rzeczywistych zrodel.

To jest miejsce, w ktorym `loops.jsx` i `lot-siatka.json` spotykaja sie
i zamieniaja w jeden `kernel.Snapshot`. Powyzej tej warstwy nic juz nie wie,
skad przyszly dane.

Podzial rol jest scisly:
  rozklad i rotacje  -> lot-siatka (siedem rzeczywistych dob)
  porty, typy, prawo -> loops.jsx (baza parametryczna)
  zaloga             -> wyliczona z tabel FDP EASA na podstawie realnych rotacji
  manifest           -> wygenerowany z rozkladow z CF.pax
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, replace
from datetime import UTC, datetime, timedelta

from ..kernel.contracts import (
    Aircraft, Confidence, CrewMember, CrewRole, Flight, Rotation, Snapshot,
)
from . import airline
from .aircraft_perf import build_types
from .airports import build_airports
from .lot_db import load_lot_db
from .pax_model import PaxModel
from .siatka import load_siatka

#: Zgloszenie zalogi przed odlotem, z FT.def.report_time_before_departure_min
REPORT_BEFORE_MIN = 60


@dataclass(frozen=True, slots=True)
class BuildReport:
    """Co powstalo i czego zabraklo -- material do raportu node 01."""

    weekday: int
    day: str
    flights: int
    rotations: int
    broken_rotations: int
    aircraft: int
    crew: int
    passengers: int
    itineraries: int
    connecting_share: float
    assumptions: tuple[str, ...]
    gaps: tuple[str, ...]


def build_snapshot(weekday: int = 0, seed: int = 2026) -> tuple[Snapshot, BuildReport]:
    """Snapshot jednej rzeczywistej doby operacyjnej (0 = poniedzialek)."""
    db = load_lot_db()
    sn = load_siatka()
    day = sn.day_for(weekday)

    airports = build_airports(day.day)
    types = build_types()
    routes = db.routes

    # ---- rejsy i rotacje, wprost z zaobserwowanej doby ----
    flights: dict[str, Flight] = {}
    rotations: dict[str, Rotation] = {}
    gaps: list[str] = []

    for reg, legs in sorted(day.by_registration().items()):
        rotation_id = f"ROT-{reg}-{day.day.isoformat()}"
        leg_ids: list[str] = []
        for seq, leg in enumerate(legs):
            std = leg.std_utc(day.day)
            block = leg.block_min
            if block <= 0:
                gaps.append(f"{leg.number}: blok {block} min, rejs pominiety")
                continue
            flight_id = f"{leg.number}-{day.day.isoformat()}"
            if flight_id in flights:
                flight_id = f"{flight_id}-{seq}"
            flights[flight_id] = Flight(
                id=flight_id, number=leg.number,
                dep=leg.origin, arr=leg.dest,
                std=std, sta=std + timedelta(minutes=block),
                aircraft_reg=reg, type_code=leg.type_code,
                rotation_id=rotation_id, seq=seq,
            )
            leg_ids.append(flight_id)
        if leg_ids:
            rotations[rotation_id] = Rotation(
                id=rotation_id, aircraft_reg=reg, flight_ids=tuple(leg_ids)
            )

    # ---- flota, z pozycja wyjsciowa z pierwszego odcinka doby ----
    first_origin: dict[str, str] = {}
    for rotation in rotations.values():
        first_origin[rotation.aircraft_reg] = flights[rotation.flight_ids[0]].dep

    aircraft: dict[str, Aircraft] = {}
    for reg, row in db.fleet.items():
        aircraft[reg] = Aircraft(
            reg=reg,
            icao24="",
            type_code=row.type_code,
            position=first_origin.get(reg, airline.HOME_BASE),
            etops_certified=(db.types[row.type_code].category == "szerokokadlubowy"
                             if row.type_code in db.types else False),
        )

    # ---- zaloga, z realnych tabel FDP ----
    crew: dict[str, CrewMember] = {}
    crewed_flights: dict[str, tuple[str, ...]] = {}
    for rotation in rotations.values():
        legs = [flights[f] for f in rotation.flight_ids]
        first = legs[0]
        port = airports.get(first.dep)
        offset = port.tz_offset_min if port else 0
        report_utc = first.std - timedelta(minutes=REPORT_BEFORE_MIN)
        report_local_min = int(
            ((report_utc.hour * 60 + report_utc.minute) + offset) % 1440
        )
        fdp_limit = db.max_fdp_min(report_local_min, sectors=len(legs))
        spec = db.types.get(first.type_code)
        longest = max(f.block_min for f in legs)
        cockpit = 3 if longest > 480 else 2
        cabin = spec.cabin_crew if spec else 4
        rating = spec.rating if spec else "EJET"
        base = first.dep if first.dep in airline.CREW_BASES else airline.HOME_BASE

        ids: list[str] = []
        for index in range(cockpit + cabin):
            role = (CrewRole.CAPTAIN if index == 0
                    else CrewRole.FIRST_OFFICER if index < cockpit
                    else CrewRole.CABIN)
            # personel pokladowy ma FDP o 60 min dluzszy (ORO.FTL.205 lit. e)
            limit = fdp_limit + (60 if role is CrewRole.CABIN else 0)
            crew_id = f"{rotation.aircraft_reg}-{role.value[:3]}{index}"
            crew[crew_id] = CrewMember(
                id=crew_id, role=role, base=base,
                qualifications=frozenset({rating}),
                duty_start=report_utc, fdp_limit_min=limit,
            )
            ids.append(crew_id)
        crewed_flights[rotation.id] = tuple(ids)

    # Flight jest mrozony, wiec dopiecie zalogi znaczy odtworzenie rekordu.
    for flight_id, flight in list(flights.items()):
        flights[flight_id] = replace(
            flight, crew_ids=crewed_flights.get(flight.rotation_id, ())
        )

    # ---- manifest ----
    manifest = PaxModel(db, seed=seed).build(flights, routes, types)

    connecting = sum(
        1 for i in manifest.itineraries.values() if len(i.segments) > 1
    )
    share = connecting / len(manifest.itineraries) if manifest.itineraries else 0.0

    # ---- pewnosc danych (node 02 czyta to wprost) ----
    confidence: dict[str, Confidence] = {
        "flights": Confidence.KNOWN,
        "rotations": Confidence.KNOWN,
        "airports": Confidence.KNOWN,
        "aircraft_types": Confidence.KNOWN,
        "crew": Confidence.ESTIMATED,       # z tabel FDP, nie z grafiku operatora
        "passengers": Confidence.ESTIMATED,  # rozklady realne, tozsamosci nie
        "fares": Confidence.ESTIMATED,
    }

    breaks = day.continuity_breaks()
    if breaks:
        gaps.append(
            f"{len(breaks)} przerw w lancuchach rotacji "
            f"({len({b[0] for b in breaks})} maszyn) -- okno eksportu, nie blad"
        )

    snapshot = Snapshot(
        taken_at=datetime.combine(day.day, datetime.min.time(), UTC),
        flights=flights,
        rotations=rotations,
        airports=airports,
        aircraft=aircraft,
        aircraft_types=types,
        crew=crew,
        passengers=manifest.passengers,
        itineraries=manifest.itineraries,
        confidence=confidence,
    )
    snapshot = replace(snapshot, digest=_digest(snapshot))

    report = BuildReport(
        weekday=weekday, day=day.day.isoformat(),
        flights=len(flights), rotations=len(rotations),
        broken_rotations=len({b[0] for b in breaks}),
        aircraft=len(aircraft), crew=len(crew),
        passengers=len(manifest.passengers), itineraries=len(manifest.itineraries),
        connecting_share=share,
        assumptions=(
            *manifest.assumptions,
            "zaloga wyliczona z tabel FDP EASA, nie z grafiku operatora",
        ),
        gaps=tuple(gaps),
    )
    return snapshot, report


def _digest(s: Snapshot) -> str:
    """Odcisk snapshotu. Kazdy nastepny raport go cytuje, wiec run jest odtwarzalny."""
    h = hashlib.sha256()
    h.update(s.taken_at.isoformat().encode())
    for flight_id in sorted(s.flights):
        f = s.flights[flight_id]
        h.update(f"{f.id}|{f.dep}{f.arr}|{f.std.isoformat()}|{f.aircraft_reg}".encode())
    for key in ("passengers", "itineraries", "crew", "aircraft"):
        h.update(f"{key}={len(getattr(s, key))}".encode())
    return f"sha256:{h.hexdigest()[:32]}"
