"""Granica systemu -- jedyne miejsce, ktore zna zrodla danych.

Wszystko powyzej (`kernel`, `nodes`) dziala na znormalizowanym snapshocie
i nie wie, skad przyszly dane.

Dwa zrodla, rozdzielone rolami:

* `lot_db` -- baza parametryczna z `loops.jsx` (v5.0): porty, siatka, flota,
  prawo (EU261, Montreal, FTL EASA), 76 kodow opoznien AHM 730, klasy
  rezerwacyjne, statusy, partnerzy, stawki kosztowe. To jest prawda
  o *regulach i parametrach*.
* `siatka` -- baza operacyjna z `lot-siatka.json`: siedem rzeczywistych dob
  (2602 rejsy) i statystyka 6236 wykonanych operacji. To jest prawda
  o *tym, co sie dzieje*.

Nic tu nie jest generowane poza tozsamoscia pojedynczego pasazera -- tej nie
ma w zadnym publicznym zrodle, a jej rozklady i tak pochodza z `CF.pax`.
"""

from .aircraft_perf import build_types, get_type, same_crew_rating, turnaround_min
from .airports import build_airports, minimum_connection_min, port
from .lot_db import LotDB, load_lot_db
from .siatka import Siatka, load_siatka

__all__ = [
    "LotDB", "Siatka", "build_airports", "build_types", "get_type",
    "load_lot_db", "load_siatka", "minimum_connection_min", "port",
    "same_crew_rating", "turnaround_min",
]
