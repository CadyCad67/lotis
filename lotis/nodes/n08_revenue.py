"""Node 08 -- REVENUE ENGINE.

Przychod kazdej opcji: ile z baseline'u przetrwalo. Kluczowa jest lista
`PaxOutcomeKind.keeps_revenue` -- i to, ze jest na niej REBOOKED_OAL.

Przerzucenie pasazera na inna linie ZACHOWUJE przychod z biletu (LOT wystawil
kupon i pieniadze zostaly), ale rodzi zobowiazanie rozliczenia interline, ktore
liczy node 09. Rozdzielenie tych dwoch rzeczy jest istotne: gdyby rebooking na
OAL kasowal przychod, opcja wygladalaby na katastrofe, a gdyby nie generowal
kosztu rozliczenia -- wygladalaby na darmowa. Ani jedno, ani drugie nie jest
prawda.

REVENUE AT RISK = BASELINE - revenue opcji. Wynik odejmowania, nie osobna
liczba do policzenia (Blok 3 tablicy).
"""

from __future__ import annotations

from ..kernel.contracts import (
    Baseline, Option, PaxOutcomeKind, RevenueBreakdown, Snapshot,
)
from ..kernel.money import Money
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.pricing import pricing
from ..kernel.prorate import value_on


class RevenueNode(Node):
    id = "08"
    name = "revenue"
    title = "REVENUE ENGINE"
    consumes = ("snapshot", "baseline", "options")
    produces = "revenue"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        baseline: Baseline = ctx.require("baseline")
        options: tuple[Option, ...] = ctx.require("options")
        price = pricing()
        report = self.new_report()

        result: dict[str, RevenueBreakdown] = {}
        rows: list[dict[str, object]] = []

        for option in options:
            touched = _touched_baseline(baseline, option)
            lost = Money.zero()
            refunded = Money.zero()
            ancillary_lost = Money.zero()

            # Liczymy STRATE, a przychod wyprowadzamy odejmowaniem.
            #
            # Poprzednio bylo odwrotnie: sumowalismy przychod zachowany i dodawali
            # "przychod rejsow niedotknietych" jako roznice miedzy baseline'em
            # a suma po pasazerach. Ta roznica mieszala dwie miary -- baseline
            # prorowany dystansem i wartosc pasazera prorowana liczba odcinkow --
            # przez co na siedmiu dobach wychodzila UJEMNA w 30 przypadkach.
            # Przychod z rejsu nie moze byc ujemny; liczba byla bez sensu, a mimo
            # to wygladala jak kwota i wchodzila do rankingu.
            for pax_id, outcome in option.pax_outcomes.items():
                pax = snap.passengers.get(pax_id)
                if pax is None:
                    continue
                if outcome.kind.keeps_revenue:
                    continue
                value = _prorated_value(snap, pax, option)
                lost = lost + value
                ancillary_lost = ancillary_lost + pax.ancillary
                if outcome.kind is PaxOutcomeKind.CANCELLED_REFUND:
                    refunded = refunded + value

            kept = touched - lost

            breakdown = RevenueBreakdown(
                kept=kept, lost=lost, refunded=refunded,
                components={
                    "baseline_dotknietych": touched,
                    "utracona_wartosc_pasazerow": lost,
                    "utracone_ancillary": ancillary_lost,
                    "zwroty": refunded,
                },
            )
            result[option.id] = breakdown
            rows.append({
                "id": option.id,
                "baseline_dotknietych": touched,
                "revenue_opcji": kept,
                "revenue_at_risk": touched - kept,
                "zwroty": refunded,
                "pasazerow": len(option.pax_outcomes),
            })

        best = min(rows, key=lambda r: r["revenue_at_risk"].minor) if rows else None
        worst = max(rows, key=lambda r: r["revenue_at_risk"].minor) if rows else None

        report.summary = (
            f"Policzono przychod {len(result)} opcji. "
            + (f"Najmniej traci `{best['id']}` ({best['revenue_at_risk']}), "
               f"najwiecej `{worst['id']}` ({worst['revenue_at_risk']})."
               if best and worst else "")
        )
        report.number("opcji_wycenionych", len(result), "szt")
        if best:
            report.number("najmniejszy_revenue_at_risk", best["revenue_at_risk"], "PLN")
            report.number("najwiekszy_revenue_at_risk", worst["revenue_at_risk"], "PLN")
        report.number("baseline_doby", baseline.total, "PLN")

        report.findings["revenue_opcji"] = rows
        report.findings["zasada"] = {
            "revenue_at_risk": "baseline dotknietych rejsow minus revenue opcji",
            "rebooking_na_OAL": "zachowuje przychod, generuje koszt rozliczenia w node 09",
            "zwrot": "kasuje przychod w calosci",
        }

        report.decide(
            "rebooking na obcego przewoznika zachowuje przychod z biletu; "
            "rozliczenie interline jest kosztem, nie utrata przychodu"
        )
        report.decide("revenue at risk to wynik odejmowania, nie osobna wielkosc")
        for field, source, confidence, note in price.assumptions()[:1]:
            report.assume(field, source, confidence, note)

        return NodeOutput(report, {"revenue": result})


def _touched_baseline(baseline: Baseline, option: Option) -> Money:
    total = Money.zero()
    for flight_id in option.affected_flights:
        total = total + baseline.of(flight_id)
    return total


def _prorated_value(snap: Snapshot, pax, option: Option) -> Money:
    """Ulamek wartosci podrozy przypadajacy na odcinki dotkniete opcja.

    Pasazer transferowy traci wiecej niz bezposredni, bo opcja psuje mu dwa
    odcinki -- ale liczymy tylko te, ktorych opcja faktycznie dotyka. Bez tego
    bilet przez punkt policzylby sie dwa razy (luka 8).

    Podzial idzie przez `kernel.prorate`, czyli DOKLADNIE ta sama regula, ktora
    node 03 rozklada baseline. Wczesniej stal tu wlasny wzor na udzial wedlug
    liczby odcinkow -- inna miara niz dystansowa -- i odejmowanie jednej od
    drugiej dawalo wyniki bez sensu.
    """
    itin = snap.itineraries.get(pax.itinerary_id)
    if itin is None:
        return Money.zero()
    return value_on(snap, itin, pax.value, option.affected_flights)
