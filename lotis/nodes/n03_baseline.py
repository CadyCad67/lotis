"""Node 03 -- BASELINE REVENUE.

Wartosc pasazerow wg koszykow plus ancillary, policzona PRZED zakloceniem.
To jest punkt odniesienia: strata kazdej opcji to `baseline - revenue opcji`,
a nie osobna liczba do policzenia.

LUKA 8 TABLICY -- PRORATA O&D
Tablica byla wewnetrznie sprzeczna. Box WYNIK mowil "wartosc przypisana do
O&D, nie do odcinka", a box WARTOSC PASAZERA "pasazer przesiadkowy: wartosc
obu odcinkow". Przy sumowaniu po calej siatce ten sam bilet liczylby sie dwa
razy i baseline sieci bylby zawyzony o wartosc calego ruchu transferowego.

Rozstrzygniecie: wartosc wisi na podrozy, a odcinek konsumuje jej ULAMEK
proporcjonalny do dystansu. Suma po odcinkach rowna sie wtedy dokladnie sumie
po podrozach -- i ten niezmiennik jest sprawdzany w tescie.

Prorata po dystansie, a nie po liczbie odcinków, bo WAW-FRA-JFK to nie sa dwa
rowne kawalki: dowoz do huba jest tania czescia biletu i tak tez ma sie liczyc.
"""

from __future__ import annotations

from ..kernel.contracts import Baseline, Snapshot
from ..kernel.money import Money, money_sum
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.prorate import split_value


class BaselineNode(Node):
    id = "03"
    name = "baseline"
    title = "BASELINE REVENUE"
    consumes = ("snapshot",)
    produces = "baseline"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        report = self.new_report()

        per_itinerary: dict[str, Money] = {}
        per_flight: dict[str, Money] = {}
        pax_per_flight: dict[str, int] = {}
        ancillary_total = Money.zero()
        fare_total = Money.zero()

        for pax in snap.passengers.values():
            itin = snap.itineraries.get(pax.itinerary_id)
            if itin is None:
                continue
            value = pax.value
            per_itinerary[itin.id] = per_itinerary.get(itin.id, Money.zero()) + value
            fare_total = fare_total + pax.fare
            ancillary_total = ancillary_total + pax.ancillary

            # Ta sama regula, ktorej uzywa node 08. Wspolny modul, bo dwie
            # implementacje tego samego podzialu rozjechaly sie juz raz.
            for segment, part in split_value(snap, itin, value).items():
                pax_per_flight[segment] = pax_per_flight.get(segment, 0) + 1
                per_flight[segment] = per_flight.get(segment, Money.zero()) + part

        total = money_sum(per_itinerary.values())

        baseline = Baseline(
            per_flight=per_flight,
            per_itinerary=per_itinerary,
            pax_per_flight=pax_per_flight,
            total=total,
            computed_at=snap.taken_at,
        )

        report.summary = (
            f"Baseline calej doby: {total}. "
            f"{len(per_itinerary)} podrozy rozlozonych na {len(per_flight)} rejsow "
            "wedlug udzialu dystansu."
        )
        report.number("baseline_doby", total, "PLN")
        report.number("taryfy", fare_total, "PLN")
        report.number("ancillary", ancillary_total, "PLN")
        report.number("udzial_ancillary", _pct(ancillary_total, total), "%")
        report.number("podroze", len(per_itinerary), "szt")
        report.number("rejsy_z_przychodem", len(per_flight), "szt")
        report.number("srednia_wartosc_podrozy",
                      total / max(1, len(per_itinerary)), "PLN")

        report.findings["najcenniejsze_rejsy"] = [
            {"id": fid, "revenue": per_flight[fid], "pasazerow": pax_per_flight.get(fid, 0)}
            for fid in sorted(per_flight, key=lambda k: -per_flight[k].minor)[:10]
        ]
        report.findings["wartosc_wg_koszyka"] = _by_basket(snap)

        # Niezmiennik proraty. Jesli sie nie zgadza, luka 8 wrocila.
        suma_odcinkow = money_sum(per_flight.values())
        report.number("kontrola_proraty", suma_odcinkow, "PLN")
        if suma_odcinkow != total:
            report.warn(
                f"suma po odcinkach ({suma_odcinkow}) rozni sie od sumy po podrozach "
                f"({total}) -- prorata O&D gubi grosze"
            )
        else:
            report.decide(
                "prorata O&D domyka sie co do grosza: suma po odcinkach = suma po podrozach"
            )

        report.decide(
            "wartosc pasazera wisi na podrozy; odcinek konsumuje ulamek wedlug dystansu"
        )
        report.decide(
            "strata opcji liczy sie jako baseline minus revenue opcji, "
            "a nie jako osobna wielkosc"
        )
        report.assume("wartosc biletu", "synthetic", 0.6,
                      "manifest modelowany z rozkladow bazy")
        report.assume("prorata", "derived", 0.8,
                      "udzial dystansu wielkiego kola, nie udzial taryfowy IATA")

        return NodeOutput(report, {"baseline": baseline})


def _by_basket(snap: Snapshot) -> dict[str, dict[str, object]]:
    """Rozklad wartosci na 16 koszykow -- material dla node 08 i dla modelu."""
    buckets: dict[str, tuple[int, Money]] = {}
    for pax in snap.passengers.values():
        key = pax.basket.key
        count, value = buckets.get(key, (0, Money.zero()))
        buckets[key] = (count + 1, value + pax.value)
    return {
        key: {"pasazerow": count, "wartosc": value,
              "srednia": value / max(1, count)}
        for key, (count, value) in sorted(buckets.items(), key=lambda kv: -kv[1][1].minor)
    }


def _pct(part: Money, whole: Money) -> float:
    return round(100.0 * part.minor / whole.minor, 2) if whole.minor else 0.0
