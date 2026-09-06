"""Tozsamosc przewoznika: LOT Polish Airlines.

Caly system jest zawezony do jednej linii. Ten plik jest jedynym miejscem,
w ktorym zapisane jest, ktora. Zmiana przewoznika = zmiana tego pliku,
a nie przegladanie adapterow.

Filtrowanie dziala na dwoch poziomach:
  * OpenSky zwraca ruch calego portu -- odsiewamy po prefiksie callsignu `LOT`,
  * rozklad zapasowy generuje wylacznie floty i siatke LOT-u.
"""

from __future__ import annotations

import re

ICAO = "LOT"          # kod ICAO przewoznika, uzywany w callsignach
IATA = "LO"           # kod IATA, uzywany w numerach rejsow
NAME = "LOT Polish Airlines"
HOME_BASE = "WAW"     # Warszawa Chopina, EPWA
CREW_BASES = ("WAW", "KRK", "GDN")

#: Porty, z ktorych ma sens pobierac ruch LOT-u przy zasilaniu z OpenSky.
SOURCE_AIRPORTS = ("EPWA", "EPKK", "EPGD", "EPWR")

#: Prefiksy rejestracji wg rodziny. Rejestracje LOT-u sa w bloku SP-L**.
REGISTRATION_PREFIX = "SP-L"

_CALLSIGN = re.compile(r"^LOT[0-9A-Z]{1,5}$")
_REGISTRATION = re.compile(r"^SP-L[A-Z]{2}$")


def is_lot_callsign(callsign: str | None) -> bool:
    """Czy callsign z OpenSky nalezy do LOT-u.

    OpenSky zwraca callsigny dopelnione spacjami, np. `'LOT282  '`.
    """
    if not callsign:
        return False
    return bool(_CALLSIGN.match(callsign.strip().upper()))


def is_lot_registration(reg: str | None) -> bool:
    if not reg:
        return False
    return bool(_REGISTRATION.match(reg.strip().upper()))


def flight_number_from_callsign(callsign: str) -> str:
    """`'LOT282  '` -> `'LO282'`. Callsigny alfanumeryczne zostaja jak sa."""
    tail = callsign.strip().upper().removeprefix(ICAO)
    return f"{IATA}{tail}"


def family_of(type_code: str) -> str | None:
    """Rodzina uprawnien zalogi dla typu -- wprost z bazy (`TY[4]`).

    Zaloga jest kwalifikowana na rodzine, nie na pojedynczy typ: E175 i E195
    dziela uprawnienie EJET, 737 NG i MAX dziela B737, ale E195-E2 ma osobne
    EJET_E2, bo wymaga szkolenia roznicowego.

    Wczesniej byla tu moja recznie pisana tabela. Miala kody, ktorych w bazie
    nie ma (`E75` zamiast `E75S`), wiec cicho zwracala `None` dla kazdego
    realnego typu -- a `None` znaczy tu "brak uprawnienia".
    """
    from .aircraft_perf import spec
    s = spec(type_code)
    return s.rating if s and s.rating else None


def qualified(qualifications: frozenset[str] | set[str], type_code: str) -> bool:
    """Czy zaloga z takimi kwalifikacjami moze leciec tym typem."""
    fam = family_of(type_code)
    return fam is not None and fam in qualifications
