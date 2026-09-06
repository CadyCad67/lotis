"""Node 11 -- OPTIMIZATION ENGINE.

Liczy strate kazdej opcji, porownuje do baseline'u, podaje widelki i uklada
ranking wstepny.

WZOR Z BLOKU 3B TABLICY
    STRATA = (BASELINE - revenue opcji) + koszty dodatkowe
    gdy opcja dotyka kilku rejsow: STRATA = suma strat wszystkich rejsow
    NAJLEPSZA = najmniejsza strata

WIDELKI (luka 11 tablicy)
Tablica nie mowila, co robic przy braku danych. Odpowiedz: nie zgadujemy
i nie odmawiamy -- podajemy szersze widelki i oznaczamy je zrodlem.

Rozpietosc nie jest wymyslona. Pochodzi z rzeczywistej statystyki opoznien
tej siatki: `p25 / mediana / p90` dla konkretnego numeru rejsu, a gdy jest
za malo obserwacji -- dla trasy, a na koncu dla calej siatki. Kaskada ma
znaczenie, bo rozklad dla jednego rejsu bywa zupelnie inny niz sredni,
a udawanie, ze nie jest, zawyza pewnosc wyniku.
"""

from __future__ import annotations

from ..adapters.siatka import load_siatka
from ..kernel.contracts import (
    Band, Baseline, CostBreakdown, NetworkImpact, Option, OptionEvaluation,
    RevenueBreakdown, Snapshot,
)
from ..kernel.money import Money
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.pricing import pricing

#: Minimalna rozpietosc widelek jako ulamek wartosci oczekiwanej. Widelki
#: wezsze niz to sa deklaracja pewnosci, ktorej nie mamy.
MIN_SPREAD_PCT = 0.08


#: Waga zdarzenia dla pasazera, w jednostkach umownych. Odmowa przyjecia jest
#: najciezsza, bo pasazer w ogole nie leci; przebukowanie na obcego przewoznika
#: gorsze niz na wlasny, bo lamie ciaglosc obslugi. Zwloka liczona osobno,
#: proporcjonalnie do godzin.
PAX_WAGA = {
    "OFFLOADED_INVOLUNTARY": 10.0,
    "CANCELLED_REFUND": 8.0,
    "OFFLOADED_VOLUNTARY": 4.0,
    "REBOOKED_OAL": 3.0,
    "REBOOKED_OWN": 2.0,
    "DELAYED": 0.0,
    "KEPT": 0.0,
}


def _indeks_pax(option) -> float:
    """Uciazliwosc opcji dla pasazerow, na jedna osobe.

    Ranking po samej stracie w zlotowkach nie widzi roznicy miedzy opcja, ktora
    kogos nie wpuszcza na poklad, a taka, ktora wszystkich opoznia. Suwak
    priorytetu potrzebuje drugiej osi, wiec ja tu liczymy.
    """
    outcomes = list(option.pax_outcomes.values())
    if not outcomes:
        return 0.0
    suma = 0.0
    for o in outcomes:
        suma += PAX_WAGA.get(str(o.kind), 1.0)
        suma += o.delay_min / 60.0
        suma += o.care_nights * 2.0
    return suma / len(outcomes)


def _znormalizuj(wartosci: list[float]) -> list[float]:
    """Skala 0-1 wzgledem najlepszej i najgorszej opcji w tym rankingu."""
    lo, hi = min(wartosci), max(wartosci)
    if hi - lo < 1e-9:
        return [0.0 for _ in wartosci]
    return [(v - lo) / (hi - lo) for v in wartosci]


class OptymalizacjaNode(Node):
    id = "11"
    name = "optymalizacja"
    title = "OPTIMIZATION ENGINE"
    consumes = ("snapshot", "baseline", "options", "revenue", "costs")
    produces = "evaluations"

    def __init__(self, priority: int = 50) -> None:
        #: 0 oznacza ranking wylacznie po pieniadzach, 100 wylacznie po
        #: uciazliwosci dla pasazera. Wartosci posrednie miesza sie liniowo.
        self.priority = max(0, min(100, int(priority)))

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        baseline: Baseline = ctx.require("baseline")
        options: tuple[Option, ...] = ctx.require("options")
        revenue: dict[str, RevenueBreakdown] = ctx.require("revenue")
        costs: dict[str, CostBreakdown] = ctx.require("costs")
        network: dict[str, NetworkImpact] = ctx.get("network", {})
        network_cost: dict[str, Money] = ctx.get("network_cost", {})
        disruption = ctx.require("disruption")

        price = pricing()
        sn = load_siatka()
        report = self.new_report()

        source = snap.flights[disruption.flight_id]
        # Srodkowy wspolczynnik jest z definicji 1.0 -- wartosc oczekiwana jest
        # kotwica, wzgledem ktorej liczone sa oba ramiona widelek.
        low_f, _, high_f = _uncertainty_factors(sn, source)

        evaluations: dict[str, OptionEvaluation] = {}
        rows: list[dict[str, object]] = []

        for option in options:
            rev = revenue[option.id]
            cost = costs[option.id]
            propagation = network_cost.get(option.id, Money.zero())

            baseline_touched = Money.zero()
            for flight_id in option.affected_flights:
                baseline_touched = baseline_touched + baseline.of(flight_id)

            revenue_at_risk = baseline_touched - rev.kept
            loss = revenue_at_risk + cost.total + propagation

            band = _band(loss, low_f, high_f)

            evaluation = OptionEvaluation(
                option_id=option.id,
                revenue=rev,
                cost=cost,
                network=network.get(option.id),
                loss=loss,
                band=band,
                notes=option.notes,
            )
            evaluations[option.id] = evaluation
            rows.append({
                "id": option.id,
                "indeks_pax": round(_indeks_pax(option), 3),
                "label": option.label,
                "tryb": option.kind.value,
                "revenue_at_risk": revenue_at_risk,
                "koszty": cost.total,
                "propagacja": propagation,
                "strata": loss,
                "widelki_min": band.low,
                "widelki_max": band.high,
                "rozpietosc": band.spread,
            })

        # Ranking miesza dwie znormalizowane osie: strate w zlotowkach
        # i uciazliwosc dla pasazera. Kwoty w raporcie zostaja bez zmian --
        # suwak zmienia kolejnosc, nie liczby.
        waga = self.priority / 100.0
        if rows:
            straty = _znormalizuj([float(r["strata"].minor) for r in rows])
            paxy = _znormalizuj([float(r["indeks_pax"]) for r in rows])
            for row, sn_, pn in zip(rows, straty, paxy, strict=True):
                row["wynik_wazony"] = round((1 - waga) * sn_ + waga * pn, 4)
        ranked = sorted(rows, key=lambda r: (r["wynik_wazony"], r["strata"].minor))
        for position, row in enumerate(ranked, 1):
            row["pozycja_wstepna"] = position

        report.number("priorytet", self.priority,
                      "0 finanse, 100 pasazer")
        najtansza = min(rows, key=lambda r: r["strata"].minor) if rows else None
        if najtansza and ranked and najtansza["id"] != ranked[0]["id"]:
            report.warn(
                f"przy priorytecie {self.priority} ranking wskazuje "
                f"`{ranked[0]['id']}`, a najtansza jest `{najtansza['id']}` "
                f"({najtansza['strata']})"
            )

        report.summary = (
            f"Ranking wstepny {len(ranked)} opcji, priorytet {self.priority}. "
            + (f"Najmniejsza strata: `{ranked[0]['id']}` ({ranked[0]['strata']}), "
               f"najwieksza: `{ranked[-1]['id']}` ({ranked[-1]['strata']})."
               if ranked else "Brak opcji do porownania.")
        )
        if ranked:
            report.number("najlepsza_opcja", ranked[0]["id"])
            report.number("strata_najlepszej", ranked[0]["strata"], "PLN")
            report.number("strata_najgorszej", ranked[-1]["strata"], "PLN")
            report.number("rozpietosc_rankingu",
                          ranked[-1]["strata"] - ranked[0]["strata"], "PLN")
        report.number("wspolczynnik_dolny", round(low_f, 3))
        report.number("wspolczynnik_gorny", round(high_f, 3))
        report.number("opcji", len(rows), "szt")

        report.findings["ranking_wstepny"] = ranked
        report.findings["zrodlo_widelek"] = _band_source(sn, source)

        report.decide("strata = (baseline - revenue opcji) + koszty + propagacja")
        report.decide("najlepsza opcja to najmniejsza strata, nie najmniejszy koszt")

        if len(ranked) >= 2:
            first = evaluations[ranked[0]["id"]].band
            second = evaluations[ranked[1]["id"]].band
            if first.overlaps(second):
                report.warn(
                    f"widelki opcji `{ranked[0]['id']}` i `{ranked[1]['id']}` zachodza "
                    "na siebie -- roznica miedzy nimi nie jest istotna statystycznie"
                )
                report.decide(
                    "przy zachodzacych widelkach o wyborze decyduja kryteria "
                    "poza kosztem: node 13 dokłada wage polityki firmy"
                )

        report.assume("widelki", "real", 0.8,
                      "kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki")
        for field, source_name, confidence, note in price.assumptions()[:1]:
            report.assume(field, source_name, confidence, note)

        return NodeOutput(report, {"evaluations": evaluations,
                                   "ranking_wstepny": [r["id"] for r in ranked]})


def _uncertainty_factors(sn, flight) -> tuple[float, float, float]:
    """Mnozniki widelek z rozkladu opoznien tego rejsu.

    Bierzemy p25 / mediane / p90 i zamieniamy na wspolczynniki wzgledem
    mediany. Rejs o szerokim rozkladzie dostaje szersze widelki -- i to jest
    cala roznica wobec zgadywanej stalej.
    """
    route = f"{flight.dep}-{flight.arr}"
    low, mid, high = sn.departure_band(flight.number, route)
    anchor = max(1.0, abs(mid))
    return (
        max(0.55, 1.0 - abs(mid - low) / (anchor * 4)),
        1.0,
        min(2.2, 1.0 + abs(high - mid) / (anchor * 3)),
    )


def _band_source(sn, flight) -> dict[str, object]:
    route = f"{flight.dep}-{flight.arr}"
    per_flight = sn.by_flight.get(flight.number, {}).get("odlot")
    per_route = sn.by_route.get(route, {}).get("odlot")
    if per_flight and per_flight.n >= 5:
        level, stats = "rejs", per_flight
    elif per_route and per_route.n >= 5:
        level, stats = "trasa", per_route
    else:
        level, stats = "siatka", sn.global_stats["odlot"]
    return {
        "poziom": level, "obserwacji": stats.n, "p25": stats.p25,
        "mediana": stats.median, "p90": stats.p90,
        "punktualnosc15": stats.on_time_15_pct,
    }


def _band(loss: Money, low_f: float, high_f: float) -> Band:
    """Widelki wokol wartosci oczekiwanej, z zachowanym porzadkiem.

    Mnozenie kwoty przez wspolczynnik odwraca porzadek, gdy kwota jest ujemna:
    dla straty -500 zl `low = max(0, -450) = 0`, a `high = -600`, wiec wychodzilo
    `0 <= -500 <= -600` -- niezmiennik zlamany w obu miejscach naraz. Na dzisiejszych
    danych strata nigdy nie schodzi ponizej zera, wiec blad nie objawial sie w wyniku,
    ale opcja przynoszaca oszczednosc netto jest w tym systemie zupelnie normalna
    (SWAP ratujacy rejs B) i wywrocilaby ranking.

    Dlatego widelki liczymy na WARTOSCI BEZWZGLEDNEJ i porzadkujemy jawnie.
    """
    rozpietosc_dol = abs(loss.minor) * abs(1.0 - low_f)
    rozpietosc_gora = abs(loss.minor) * abs(high_f - 1.0)
    minimum = abs(loss.minor) * MIN_SPREAD_PCT / 2
    dol = max(rozpietosc_dol, minimum)
    gora = max(rozpietosc_gora, minimum)

    low = Money(loss.minor - int(dol), loss.currency)
    high = Money(loss.minor + int(gora), loss.currency)
    # Widelki nie schodza ponizej zera tylko wtedy, gdy sama strata jest dodatnia
    # -- inaczej przyciecie do zera zjadaloby wartosc oczekiwana.
    if loss.minor >= 0 and low.minor < 0:
        low = Money(0, loss.currency)
    return Band(low=low, expected=loss, high=high)
