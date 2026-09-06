"""Typy statkow -- widok na baze `loops.jsx` (sekcja TY) plus czasy postoju (TU).

Zastapilem tu swoja tabele zuzycia paliwa czyms lepszym. Baza nie podaje paliwa,
tylko `cost_proxy` i `cost_scale`, a stawki minutowe siedza w `K.tac` -- tabela
kosztu opoznienia na minute wg typu (University of Westminster). To jest wlasciwa
wielkosc dla silnika IROPS: liczymy koszt minuty opoznienia, a nie spalanie.

Uwaga o mapowaniu: 787 jest liczony przez proxy B763 ze skala miejsc, nigdy przez
B744 -- adnotacja przy typie w bazie mowi to wprost i jest to celowe, bo B744
zawyzylby koszt kilkukrotnie.
"""

from __future__ import annotations

from ..kernel.contracts import AircraftType
from .lot_db import TypeSpec, load_lot_db

#: Kotwice tabeli kosztu minutowego: wartosci dla 5, 15 i 30 minut opoznienia.
TAC_ANCHORS_MIN = (5, 15, 30)


def spec(code: str) -> TypeSpec | None:
    return load_lot_db().types.get((code or "").strip().upper())


def get_type(code: str) -> AircraftType | None:
    s = spec(code)
    if s is None:
        return None
    j, pe, y = s.cabin
    return AircraftType(
        code=s.code, name=s.name, seats_declared=s.seats,
        seats_j=j, seats_pe=pe, seats_y=y,
        range_km=s.range_km, category=s.category, rating=s.rating,
        cabin_crew=s.cabin_crew, cost_proxy=s.cost_proxy, cost_scale=s.cost_scale,
    )


def build_types() -> dict[str, AircraftType]:
    return {code: t for code in load_lot_db().types if (t := get_type(code)) is not None}


def same_crew_rating(a: str, b: str) -> bool:
    """Czy SWAP miedzy typami nie wymaga zmiany zalogi.

    737 NG i MAX maja wspolne uprawnienie, wiec B738 <-> B38M jest darmowe
    zalogowo. E2 to osobne szkolenie roznicowe, wiec E195 <-> E295 juz nie.
    """
    sa, sb = spec(a), spec(b)
    return bool(sa and sb and sa.rating == sb.rating)


def delay_cost_eur_per_min(code: str, delay_min: int) -> float:
    """Koszt minuty opoznienia dla typu, interpolowany po kotwicach 5/15/30.

    Krzywa jest wypukla -- minuta przy 30 minutach opoznienia kosztuje
    wielokrotnie wiecej niz przy 5, bo dochodzi propagacja i obsluga pasazera.
    Liniowe stawki, ktorych uzywalem wczesniej, zanizaly dlugie opoznienia.
    """
    db = load_lot_db()
    s = spec(code)
    if s is None:
        return 0.0
    table = db.costs.get("tac", {})
    row = table.get(s.cost_proxy)
    if row is None:
        return 0.0
    scale = s.cost_scale * float(db.costs.get("tacK", 1.0))
    per_min = [row[i] / TAC_ANCHORS_MIN[i] for i in range(3)]
    if delay_min <= TAC_ANCHORS_MIN[0]:
        rate = per_min[0]
    elif delay_min >= TAC_ANCHORS_MIN[2]:
        rate = per_min[2]
    else:
        lo = 0 if delay_min <= TAC_ANCHORS_MIN[1] else 1
        a, b = TAC_ANCHORS_MIN[lo], TAC_ANCHORS_MIN[lo + 1]
        t = (delay_min - a) / (b - a)
        rate = per_min[lo] + t * (per_min[lo + 1] - per_min[lo])
    return rate * scale


def turnaround_min(code: str, sector: str) -> tuple[int, int]:
    """(czas rekomendowany, minimum zaobserwowane) dla typu i sektora.

    Wartosci policzone z rzeczywistych par ATA/ATD, nie z podrecznika --
    sekcja TUW podaje, na ilu postojach kazda z nich stoi.
    """
    table = load_lot_db().turnarounds.get((code or "").upper(), {})
    if sector in table:
        return table[sector]
    return table.get("europe", (45, 35))


def gauge_delta(from_code: str, to_code: str) -> int:
    """Roznica miejsc przy zmianie typu. Ujemna = downgauge."""
    a, b = spec(from_code), spec(to_code)
    if a is None or b is None:
        raise KeyError(f"nieznany typ: {from_code!r} albo {to_code!r}")
    return b.seats - a.seats
