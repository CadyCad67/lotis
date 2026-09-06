"""Node 17 -- WYNIK RZECZYWISTY.

Co sie faktycznie stalo, porownanie z prognoza, blad. Strzalka zwrotna wraca
stad do node 01.

LUKA 3 TABLICY
Tablica miala tu jedna pozycje: "blad modelu". To za malo. Blad modelu (silnik
zle policzyl) i blad wykonania (nie dalo sie zrobic) to dwie rozne rzeczy
i mieszanie ich psuje kalibracje w konkretny sposob: model uczy sie obnizac
swoje szacunki dlatego, ze partner nie potwierdzil miejsc. Po kilku takich
cyklach zaczyna zanizac koszty tam, gdzie liczyl dobrze.

Trzeci przypadek to ODSTEPSTWO CZLOWIEKA -- dyzurny wybral inna opcje niz
rekomendowana. To tez nie jest blad modelu; to sygnal, ze czlowiek mial
informacje, ktorej model nie mial, i tego nalezy sie nauczyc osobno.

BEZ KALIBRACJI PETLA ZWROTNA JEST DEKORACYJNA
Sama strzalka wracajaca do node 01 nic nie zmienia. Ten node produkuje
konkretne poprawki wspolczynnikow -- z jawnym tlumieniem, zeby pojedyncza
doba nie przestawiala modelu.

SKAD BIERZE SIE "RZECZYWISTOSC"
Ze statystyki 6236 wykonanych operacji w `lot-siatka.json`: rozklad opoznien
dla tego numeru rejsu, a gdy obserwacji jest za malo -- dla trasy. To nie jest
prognoza podstawiona pod wynik, tylko niezalezny pomiar tej samej siatki.
"""

from __future__ import annotations

from ..adapters.siatka import load_siatka
from ..kernel.contracts import Option, OptionEvaluation, RankedOption, Snapshot
from ..kernel.money import Money
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.pricing import pricing

#: Tlumienie kalibracji. Jedna doba nie ma prawa przestawic modelu -- poprawka
#: wchodzi z waga 20%, wiec potrzeba kilkunastu zgodnych obserwacji.
CALIBRATION_DAMPING = 0.20

#: Blad ponizej tego progu to szum pomiarowy, nie sygnal do kalibracji.
NOISE_FLOOR_PCT = 0.05


class WynikNode(Node):
    id = "17"
    name = "wynik"
    title = "WYNIK RZECZYWISTY"
    consumes = ("snapshot", "evaluations", "ranking")
    produces = "calibration"

    def __init__(self, actual_delay_min: int | None = None) -> None:
        #: Gdy nie podano, rzeczywistosc bierze sie z rozkladu opoznien tej
        #: siatki. Podanie wartosci sluzy do odtworzenia konkretnej doby.
        self.actual_delay_min = actual_delay_min

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        evaluations: dict[str, OptionEvaluation] = ctx.require("evaluations")
        ranking: list[RankedOption] = ctx.require("ranking")
        options: tuple[Option, ...] = ctx.get("options", ())
        disruption = ctx.require("disruption")
        decision = ctx.get("decision")
        execution = ctx.get("execution")
        failure = ctx.get("execution_failure")
        price = pricing()
        sn = load_siatka()
        report = self.new_report()

        flight = snap.flights[disruption.flight_id]
        route = f"{flight.dep}-{flight.arr}"
        low, median, high = sn.departure_band(flight.number, route)
        actual_delay = (self.actual_delay_min if self.actual_delay_min is not None
                        else round(median))

        wykonana_id = (decision or {}).get("opcja") or (
            ranking[0].option_id if ranking else "")
        prognoza = evaluations.get(wykonana_id)
        by_id = {o.id: o for o in options}

        rzeczywisty = _actual_loss(snap, price, by_id.get(wykonana_id),
                                   prognoza, actual_delay, disruption)

        blad_modelu = Money.zero()
        blad_pct = 0.0
        if prognoza is not None:
            blad_modelu = rzeczywisty - prognoza.loss
            anchor = max(1, abs(prognoza.loss.minor))
            blad_pct = round(100.0 * blad_modelu.minor / anchor, 2)

        rodzaj, opis = _classify(failure, decision, ranking, blad_pct, prognoza)

        w_widelkach = bool(
            prognoza is not None
            and prognoza.band.low <= rzeczywisty <= prognoza.band.high
        )

        kalibracja = _calibration(rodzaj, blad_pct, actual_delay,
                                  disruption.estimated_delay_min)

        report.summary = (
            f"Rejs {flight.number}: prognoza {prognoza.loss if prognoza else '-'}, "
            f"rzeczywistosc {rzeczywisty}, blad {blad_pct:+.1f}%. "
            f"Klasyfikacja: {rodzaj}. "
            + ("Wynik miesci sie w widelkach." if w_widelkach
               else "Wynik POZA widelkami prognozy.")
        )

        report.number("opcja_wykonana", wykonana_id)
        report.number("opoznienie_prognozowane", disruption.estimated_delay_min, "min")
        report.number("opoznienie_rzeczywiste", actual_delay, "min")
        report.number("strata_prognozowana",
                      prognoza.loss if prognoza else Money.zero(), "PLN")
        report.number("strata_rzeczywista", rzeczywisty, "PLN")
        report.number("blad", blad_modelu, "PLN")
        report.number("blad_procentowo", blad_pct, "%")
        report.number("w_widelkach", w_widelkach)
        report.number("rodzaj_bledu", rodzaj)

        report.findings["klasyfikacja"] = {
            "rodzaj": rodzaj,
            "opis": opis,
            "blad_modelu": rodzaj == "BLAD_MODELU",
            "blad_wykonania": rodzaj == "BLAD_WYKONANIA",
            "odstepstwo_czlowieka": rodzaj == "ODSTEPSTWO_CZLOWIEKA",
        }
        report.findings["zrodlo_rzeczywistosci"] = {
            "poziom": "rejs" if sn.by_flight.get(flight.number) else "trasa",
            "p25": low, "mediana": median, "p90": high,
        }
        report.findings["kalibracja"] = kalibracja
        report.findings["wykonanie"] = execution or {"udane": False, "powod": failure}

        report.decide(opis)
        report.decide(
            "blad modelu, blad wykonania i odstepstwo czlowieka sa liczone osobno "
            "-- mieszanie ich uczy model na cudzych pomylkach"
        )
        if kalibracja["poprawki"]:
            report.decide(
                f"kalibracja z tlumieniem {CALIBRATION_DAMPING:.0%}: "
                "jedna doba nie przestawia modelu"
            )
        else:
            report.decide(
                f"blad {blad_pct:+.1f}% miesci sie w szumie "
                f"({NOISE_FLOOR_PCT:.0%}) -- bez poprawek"
            )

        if not w_widelkach and prognoza is not None:
            report.warn(
                "rzeczywistosc wypadla poza widelkami prognozy -- widelki byly "
                "za waskie albo model pominal skladnik"
            )

        report.assume("rzeczywiste opoznienie", "real", 0.9,
                      f"mediana rozkladu z {sn.provenance.get('operacji', '?')} operacji")
        report.data_gaps.append(
            "rzeczywisty koszt operacji nie jest w zadnym ze zrodel "
            "-- porownanie opiera sie na opoznieniu, nie na fakturach"
        )

        return NodeOutput(report, {"calibration": kalibracja,
                                   "actual": {"opoznienie_min": actual_delay,
                                              "strata": rzeczywisty,
                                              "rodzaj_bledu": rodzaj}})


def _actual_loss(snap, price, option, prognoza, actual_delay: int,
                 disruption) -> Money:
    """Strata przeliczona na rzeczywistym opoznieniu.

    Skaluje sie tylko czesc zalezna od czasu. Koszty stale -- rozliczenie
    interline, zwroty, rekompensaty -- nie zmieniaja sie od tego, ze rejs
    byl opozniony inaczej niz zakladano.
    """
    if prognoza is None:
        return Money.zero()
    prognozowane = max(1, disruption.estimated_delay_min)
    czasowe = prognoza.cost.components.get("opoznienie_w_siatce", Money.zero())
    reszta = prognoza.loss - czasowe
    return reszta + czasowe * (actual_delay / prognozowane)


def _classify(failure, decision, ranking, blad_pct: float,
              prognoza) -> tuple[str, str]:
    """Trzy rozlaczne rodzaje rozjazdu prognozy z rzeczywistoscia (luka 3)."""
    if failure:
        return ("BLAD_WYKONANIA",
                (f"wykonanie nie powiodlo sie na kroku `{failure.get('step', '?')}` "
                 f"({failure.get('reason', '')}) -- model nie ponosi za to "
                 "odpowiedzialnosci"))
    if decision and decision.get("odstepstwo"):
        return ("ODSTEPSTWO_CZLOWIEKA",
                (f"czlowiek wybral `{decision['opcja']}` zamiast rekomendacji "
                 "-- to sygnal o informacji spoza modelu, nie blad wyceny"))
    if prognoza is None:
        return ("BRAK_PROGNOZY", "nie ma wyceny opcji wykonanej -- nie ma czego porownac")
    if abs(blad_pct) <= NOISE_FLOOR_PCT * 100:
        return ("ZGODNY", f"prognoza zgodna z rzeczywistoscia w granicach {blad_pct:+.1f}%")
    return ("BLAD_MODELU",
            (f"wycena rozminela sie o {blad_pct:+.1f}% przy poprawnym wykonaniu "
             "i przyjetej rekomendacji"))


def _calibration(rodzaj: str, blad_pct: float, actual: int, forecast: int) -> dict:
    """Poprawki wspolczynnikow -- tylko przy prawdziwym bledzie modelu.

    Blad wykonania i odstepstwo czlowieka NIE kalibruja niczego. To jest cala
    poprawka luki 3: bez tego rozroznienia model uczylby sie na pomylkach,
    ktore nie sa jego.
    """
    if rodzaj != "BLAD_MODELU":
        return {
            "poprawki": [],
            "powod_pominiecia": f"rodzaj `{rodzaj}` nie kalibruje modelu",
            "tlumienie": CALIBRATION_DAMPING,
        }

    poprawki: list[dict[str, object]] = []
    if abs(blad_pct) > NOISE_FLOOR_PCT * 100:
        poprawki.append({
            "parametr": "koszt_minuty_opoznienia",
            "kierunek": "w gore" if blad_pct > 0 else "w dol",
            "sugerowana_zmiana_pct": round(blad_pct * CALIBRATION_DAMPING, 2),
            "podstawa": "roznica miedzy strata prognozowana a rzeczywista",
        })
    if forecast and abs(actual - forecast) / max(1, forecast) > 0.15:
        poprawki.append({
            "parametr": "szacunek_opoznienia",
            "kierunek": "w gore" if actual > forecast else "w dol",
            "sugerowana_zmiana_pct": round(
                100.0 * (actual - forecast) / max(1, forecast) * CALIBRATION_DAMPING, 2),
            "podstawa": f"prognoza {forecast} min wobec rzeczywistych {actual} min",
        })
    return {
        "poprawki": poprawki,
        "tlumienie": CALIBRATION_DAMPING,
        "zasada": "poprawka wchodzi z waga 20% -- potrzeba kilkunastu zgodnych obserwacji",
    }
