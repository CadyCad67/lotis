"""Porty -- widok na baze `loops.jsx` (sekcja L, 148 portow).

Zastapil moja recznie pisana tabele 44 portow. Roznice, ktore maja znaczenie
operacyjne:

* strefa jest nazwa IANA, wiec przesuniecie liczy sie poprawnie dla kazdej daty,
  a nie tylko dla lata,
* curfew ma typ: 1 = zakaz PLANOWANIA (opozniona maszyna moze operowac),
  2 = ograniczenia i kwoty nocne. To rozroznienie decyduje, czy bramka portowa
  w node 05 odrzuca opcje, czy tylko podnosi ryzyko slotu,
* MCT jest realne i rozbite na DD/SS/SN/NN/XL, wiec przesiadka Schengen ->
  non-Schengen nie liczy sie tak samo jak krajowa,
* poziom slotow to WSG (0 / 2 / 3), a nie moje zgadywane "koordynowany".
"""

from __future__ import annotations

from datetime import date
from functools import lru_cache

from ..kernel.contracts import Airport
from .lot_db import Port, load_lot_db

#: Kody ICAO tam, gdzie sa potrzebne (zasilanie z OpenSky). Baza L ich nie ma.
_ICAO = {
    "WAW": "EPWA", "KRK": "EPKK", "GDN": "EPGD", "WRO": "EPWR",
    "POZ": "EPPO", "KTW": "EPKT", "RZE": "EPRZ", "SZZ": "EPSC",
    "BZG": "EPBY", "LUZ": "EPLB", "SZY": "EPSY", "IEG": "EPZG", "RDO": "EPRA",
}


def port(iata: str) -> Port | None:
    """Surowy rekord portu z bazy, bez rozwiazywania strefy."""
    return load_lot_db().ports.get((iata or "").strip().upper())


def all_ports() -> dict[str, Port]:
    return load_lot_db().ports


@lru_cache(maxsize=8)
def build_airports(day: date) -> dict[str, Airport]:
    """Porty jako kontrakt silnika, z przesunieciem strefy rozwiazanym na `day`."""
    out: dict[str, Airport] = {}
    for iata, p in load_lot_db().ports.items():
        curfew = p.curfew
        out[iata] = Airport(
            iata=iata,
            icao=_ICAO.get(iata, ""),
            tz_offset_min=p.utc_offset_min(day),
            lat=p.lat, lon=p.lon,
            tz=p.tz, name=p.name,
            schengen=p.schengen, eu261=p.eu261,
            curfew_start_min=curfew.start_min if curfew else None,
            curfew_end_min=curfew.end_min if curfew else None,
            curfew_kind=curfew.kind if curfew else 0,
            slot_level=p.slot_level,
            mct=dict(p.mct),
        )
    return out


def minimum_connection_min(via: str, inbound_schengen: bool, outbound_schengen: bool,
                           long_haul: bool = False) -> int:
    """MCT w porcie przesiadkowym wg rodzaju polaczenia.

    Klucze bazy: DD krajowy-krajowy, SS Schengen-Schengen, SN Schengen-non,
    NN non-non, XL dalekiego zasiegu. Zle dobrany klucz zaniza czas przesiadki
    i silnik zaczyna proponowac rebooking, ktory fizycznie nie zdazy.
    """
    p = port(via)
    if p is None:
        return 45
    if long_haul:
        key = "XL"
    elif inbound_schengen and outbound_schengen:
        key = "SS"
    elif inbound_schengen != outbound_schengen:
        key = "SN"
    else:
        key = "NN"
    return int(p.mct.get(key, p.mct.get("SS", 45)))
