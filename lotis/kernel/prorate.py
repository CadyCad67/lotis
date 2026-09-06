"""Prorata wartosci podrozy na odcinki -- jedna regula dla calego silnika.

LUKA 8 TABLICY
Box WYNIK mowil "wartosc przypisana do O&D, nie do odcinka", a box WARTOSC
PASAZERA "pasazer przesiadkowy: wartosc obu odcinkow". Przy sumowaniu po siatce
ten sam bilet liczylby sie dwa razy.

Rozstrzygniecie: wartosc wisi na podrozy, a odcinek konsumuje jej ULAMEK
proporcjonalny do dystansu. Prorata po dystansie, a nie po liczbie odcinkow,
bo WAW-FRA-JFK to nie sa dwa rowne kawalki -- dowoz do huba jest tania czescia
biletu i tak tez ma sie liczyc.

DLACZEGO TO JEST OSOBNY MODUL
Bo regula musi byc jedna. Node 03 liczyl prorate po dystansie, a node 08 po
LICZBIE odcinkow -- i odejmowal jedna miare od drugiej. Na siedmiu dobach dawalo
to 30 przypadkow UJEMNEGO przychodu z rejsow niedotknietych, a na pojedynczym
pasazerze rozjazd siegal trzykrotnosci (109,97 zl wobec 36,32 zl). Blad nie
rzucal wyjatkiem: obie liczby wygladaly na kwoty.
"""

from __future__ import annotations

from .contracts import Itinerary, Snapshot
from .geo import haversine_km
from .money import Money


def distance_shares(snapshot: Snapshot, segments: tuple[str, ...]) -> list[float]:
    """Udzial kazdego odcinka w calkowitym dystansie podrozy.

    Suma zawsze wynosi 1.0. Gdy dystansu nie da sie policzyc -- brak portu
    w snapshocie albo podroz o zerowej dlugosci -- dzielimy po rowno, bo
    zwrocenie zer kasowaloby wartosc pasazera.
    """
    lengths: list[float] = []
    for segment in segments:
        flight = snapshot.flights.get(segment)
        if flight is None:
            lengths.append(0.0)
            continue
        a = snapshot.airports.get(flight.dep)
        b = snapshot.airports.get(flight.arr)
        lengths.append(haversine_km(a.lat, a.lon, b.lat, b.lon) if a and b else 0.0)

    total = sum(lengths)
    if total <= 0:
        equal = 1.0 / max(1, len(segments))
        return [equal] * len(segments)
    return [length / total for length in lengths]


def split_value(snapshot: Snapshot, itinerary: Itinerary, value: Money) -> dict[str, Money]:
    """Rozklada wartosc podrozy na odcinki. Suma czesci rowna sie calosci.

    Ostatni odcinek dostaje reszte z dzielenia, wiec suma zgadza sie CO DO
    GROSZA. Bez tego prorata gubilaby grosze na kazdej podrozy transferowej,
    a przy trzydziestu tysiacach pasazerow te grosze robia kwote.
    """
    shares = distance_shares(snapshot, itinerary.segments)
    out: dict[str, Money] = {}
    assigned = 0
    for index, segment in enumerate(itinerary.segments):
        if index == len(itinerary.segments) - 1:
            part = Money(value.minor - assigned, value.currency)
        else:
            part = Money(int(value.minor * shares[index]), value.currency)
            assigned += part.minor
        # Ten sam odcinek moze wystapic w podrozy dwa razy tylko przy bledzie
        # danych; sumujemy, zeby taka podroz nie gubila wartosci po cichu.
        out[segment] = out.get(segment, Money.zero(value.currency)) + part
    return out


def value_on(snapshot: Snapshot, itinerary: Itinerary, value: Money,
             flights: frozenset[str] | set[str] | tuple[str, ...]) -> Money:
    """Ta czesc wartosci podrozy, ktora przypada na WSKAZANE odcinki.

    To jest funkcja, ktorej potrzebuje node 08: ile pasazer wnosi do rejsow,
    ktorych dotyka opcja. Dla podrozy dotknietej w calosci zwraca pelna wartosc,
    dla dotknietej w polowie -- polowe liczona dystansem, nie liczba odcinkow.
    """
    wanted = set(flights)
    parts = split_value(snapshot, itinerary, value)
    total = Money.zero(value.currency)
    for segment, part in parts.items():
        if segment in wanted:
            total = total + part
    return total
