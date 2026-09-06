"""Node 14 -- AI REASONING.

Uwaga na nazwe: ten node NIE wola modelu. Robi to, co tablica przypisala AI
Reasoning, ale w sposob deterministyczny -- sprawdza spojnosc wyniku, wykrywa
anomalie, wyjasnia wybor i ostrzega, gdy opcje 1 i 2 sa blisko.

LUKA 7 TABLICY
Tablica nie zapisala wprost, ze karta wykonania musi powstawac deterministycznie
z wyniku silnika, a AI moze tylko dopisac komentarz obok. Tutaj to jest
rozstrzygniete konstrukcyjnie: karta powstaje w node 13, ten node ja sprawdza,
a warstwa `ai_layer` czyta juz tylko gotowe raporty i nie ma zadnej sciezki
zapisu do stanu runu.

Model jezykowy jest OSOBNYM wyjsciem systemu (OUTPUT 2), nie jego etapem.
Silnik dziala w calosci bez niego -- i to jest sprawdzane testem.

CO TU SIE SPRAWDZA
Kontrole ponizej sa arytmetyczne, nie stylistyczne. Kazda z nich lapie inna
klase bledu, ktora nie objawia sie wyjatkiem: liczby, ktore sie nie sumuja,
ranking niezgodny ze strata, widelki o zerowej rozpietosci, opcja darmowa.
"""

from __future__ import annotations

from ..kernel.contracts import (
    ExecutionCard, Option, OptionEvaluation, RankedOption, Snapshot,
)
from ..kernel.money import Money
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.report import Status

#: Strata ponizej tego progu przy niezerowym zakloceniu jest podejrzana.
SUSPICIOUS_LOSS_PLN = 100


class AiReasoningNode(Node):
    id = "14"
    name = "ai_reasoning"
    title = "AI REASONING"
    consumes = ("snapshot", "options", "evaluations", "ranking")
    produces = "checks"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        options: tuple[Option, ...] = ctx.require("options")
        evaluations: dict[str, OptionEvaluation] = ctx.require("evaluations")
        ranking: list[RankedOption] = ctx.require("ranking")
        card: ExecutionCard | None = ctx.get("karta")
        close = ctx.get("close_call")
        report = self.new_report()

        by_id = {o.id: o for o in options}
        checks: list[dict[str, object]] = []
        anomalies: list[dict[str, object]] = []

        checks.append(_check_ranking_order(ranking))
        checks.append(_check_bands(ranking))
        checks.append(_check_card(card, ranking))
        checks.append(_check_components(evaluations))
        checks.append(_check_pax_conservation(snap, by_id, evaluations))

        for evaluation in evaluations.values():
            anomalies.extend(_anomalies(by_id.get(evaluation.option_id), evaluation))
        anomalies.extend(_threshold_straddle(snap, by_id, evaluations, ranking))

        failed = [c for c in checks if not c["ok"]]

        report.summary = (
            f"Sprawdzono {len(checks)} niezmiennikow wyniku. "
            + ("Wszystkie przeszly." if not failed
               else f"Nie przeszlo: {', '.join(str(c['id']) for c in failed)}.")
            + (f" Wykryto {len(anomalies)} anomalii." if anomalies else "")
        )
        report.number("kontroli", len(checks), "szt")
        report.number("kontroli_nieudanych", len(failed), "szt")
        report.number("anomalii", len(anomalies), "szt")
        if ranking:
            report.number("rekomendacja", ranking[0].option_id)
            report.number("przewaga_nad_druga",
                          (ranking[1].loss - ranking[0].loss) if len(ranking) > 1
                          else Money.zero(), "PLN")

        report.findings["kontrole"] = checks
        report.findings["anomalie"] = anomalies
        report.findings["uzasadnienie"] = _explain(by_id, evaluations, ranking, close)

        for check in failed:
            report.warn(f"kontrola `{check['id']}`: {check['powod']}")
        for anomaly in anomalies:
            report.warn(f"anomalia w `{anomaly['id']}`: {anomaly['powod']}")

        if close:
            report.decide(
                f"opcje `{close[0]}` i `{close[1]}` sa blisko -- rekomendacja "
                "nie jest jednoznaczna i czlowiek powinien to zobaczyc"
            )
        report.decide(
            "karta wykonania powstala deterministycznie w node 13; model jezykowy "
            "dopisuje komentarz obok i nie ma sciezki zapisu do jej srodka"
        )
        report.decide(
            "warstwa AI jest osobnym wyjsciem systemu, nie etapem przeplywu "
            "-- silnik konczy run bez niej"
        )

        if failed:
            report.status = Status.DEGRADED

        return NodeOutput(report, {"checks": checks, "anomalies": anomalies})


# ---------------------------------------------------------------- kontrole


def _check_ranking_order(ranking: list[RankedOption]) -> dict[str, object]:
    """Pozycja w rankingu ma odpowiadac wskaznikowi, nie samej stracie.

    Wskaznik jest strata przesunieta wagami polityki, wiec ranking moze byc
    inny niz kolejnosc kwot -- ale musi byc monotoniczny wzgledem wskaznika.
    """
    scores = [r.score for r in ranking]
    ok = scores == sorted(scores)
    return {"id": "kolejnosc_rankingu", "ok": ok,
            "powod": "" if ok else "ranking nie jest monotoniczny wzgledem wskaznika"}


def _check_bands(ranking: list[RankedOption]) -> dict[str, object]:
    zle = [r.option_id for r in ranking
           if not (r.band.low <= r.band.expected <= r.band.high)]
    return {"id": "widelki", "ok": not zle,
            "powod": "" if not zle else f"widelki nie obejmuja wartosci oczekiwanej: {zle}"}


def _check_card(card: ExecutionCard | None, ranking: list[RankedOption]) -> dict[str, object]:
    if card is None:
        return {"id": "karta_wykonania", "ok": not ranking,
                "powod": "" if not ranking else "jest ranking, ale nie ma karty"}
    if not ranking:
        return {"id": "karta_wykonania", "ok": False, "powod": "karta bez rankingu"}
    ok = card.option_id == ranking[0].option_id
    return {"id": "karta_wykonania", "ok": ok,
            "powod": "" if ok else
            f"karta opisuje `{card.option_id}`, a rekomendacja to `{ranking[0].option_id}`"}


def _check_components(evaluations: dict[str, OptionEvaluation]) -> dict[str, object]:
    """Suma skladnikow kosztu ma sie rownac deklarowanej sumie."""
    zle: list[str] = []
    for evaluation in evaluations.values():
        suma = Money.zero()
        for value in evaluation.cost.components.values():
            suma = suma + value
        if suma != evaluation.cost.total:
            zle.append(evaluation.option_id)
    return {"id": "suma_skladnikow", "ok": not zle,
            "powod": "" if not zle else f"skladniki nie sumuja sie do calosci: {zle}"}


def _check_pax_conservation(snap: Snapshot, by_id: dict[str, Option],
                            evaluations: dict[str, OptionEvaluation]) -> dict[str, object]:
    """Kazdy pasazer rejsu ma dokladnie jeden los w kazdej opcji.

    Pasazer bez losu zniknalby z rachunku bezkosztowo, a to jest najgrozniejszy
    z cichych bledow: opcja wygladalaby na tania dokladnie dlatego, ze o kims
    zapomniala.
    """
    zle: list[str] = []
    for option in by_id.values():
        expected = {p.id for p in snap.passengers_on(option.affected_flights[0])}
        if expected and not expected <= set(option.pax_outcomes):
            zle.append(option.id)
    return {"id": "kompletnosc_pasazerow", "ok": not zle,
            "powod": "" if not zle else f"opcje gubia pasazerow: {zle}"}


def _anomalies(option: Option | None, evaluation: OptionEvaluation) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    if option is None:
        return out

    if evaluation.loss.minor < 0:
        out.append({"id": option.id, "powod":
                    f"strata ujemna ({evaluation.loss}) -- opcja rzekomo zarabia na zakloceniu"})

    if 0 <= evaluation.loss.minor < SUSPICIOUS_LOSS_PLN * 100 and option.pax_outcomes:
        out.append({"id": option.id, "powod":
                    f"strata bliska zeru ({evaluation.loss}) mimo "
                    f"{len(option.pax_outcomes)} dotknietych pasazerow"})

    if evaluation.band.spread.minor == 0 and evaluation.loss.minor:
        out.append({"id": option.id, "powod":
                    "zerowa rozpietosc widelek to deklaracja pewnosci, ktorej nie ma"})

    if not evaluation.cost.components and option.pax_outcomes:
        out.append({"id": option.id, "powod":
                    "opcja dotyka pasazerow, a nie ma zadnego skladnika kosztu"})

    return out


def _threshold_straddle(snap, by_id, evaluations, ranking) -> list[dict[str, object]]:
    """Opcje balansujace na progu 3 h z Art. 7.

    To jest najgrozniejsza wrazliwosc w calym silniku. Prog odszkodowania jest
    skokowy: 179 minut kosztuje zero, 181 minut kosztuje pelna kwote razy
    liczba pasazerow. Przy szescdziesieciu osobach to roznica kilkudziesieciu
    tysiecy zlotych zawieszona na dwoch minutach szacunku.

    Opcja, ktora wygrywa dlatego, ze jej zakladane oczekiwanie wypadlo tuz pod
    progiem, nie wygrywa naprawde -- wygrywa zaokraglenie. Czlowiek ma to
    zobaczyc, zanim podpisze.
    """
    from ..kernel.pricing import pricing
    price = pricing()
    threshold = price.compensation_threshold_min
    margin = 45

    out: list[dict[str, object]] = []
    for evaluation in evaluations.values():
        option = by_id.get(evaluation.option_id)
        if option is None or not option.pax_outcomes:
            continue
        waits = {o.delay_min for o in option.pax_outcomes.values() if o.delay_min}
        blisko = [w for w in waits if abs(w - threshold) <= margin]
        if not blisko:
            continue
        ponizej = all(w < threshold for w in blisko)
        pax = len(option.pax_outcomes)
        stawka = price.compensation("A") * pax
        out.append({
            "id": option.id,
            "powod": (
                f"zakladane oczekiwanie {sorted(blisko)} min lezy w promieniu "
                f"{margin} min od progu {threshold} min z Art. 7. "
                + (f"Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; "
                   f"przesuniecie o {min(abs(w - threshold) for w in blisko)} min "
                   f"dodaje okolo {stawka} kosztu."
                   if ponizej else
                   "Opcja jest powyzej progu i nalicza pelne odszkodowanie.")
            ),
        })
    return out


def _explain(by_id, evaluations, ranking, close) -> dict[str, object]:
    """Uzasadnienie wyboru -- w liczbach, nie w przymiotnikach."""
    if not ranking:
        return {"wniosek": "brak dopuszczalnych opcji do porownania"}
    best = ranking[0]
    option = by_id.get(best.option_id)
    evaluation = evaluations.get(best.option_id)
    powody: list[str] = []

    if evaluation is not None:
        for pozycja, kwota in evaluation.cost.largest(3):
            powody.append(f"{pozycja}: {kwota}")

    alternatywa = ranking[1] if len(ranking) > 1 else None
    return {
        "wybrana": best.option_id,
        "label": option.label if option else "",
        "strata": best.loss,
        "widelki": {"min": best.band.low, "max": best.band.high},
        "najwieksze_skladniki_kosztu": powody,
        "oszczednosc_wobec_domyslnej": best.saving_vs_default,
        "alternatywa": (
            {"id": alternatywa.option_id, "strata": alternatywa.loss,
             "roznica": alternatywa.loss - best.loss}
            if alternatywa else None
        ),
        "czolowka_blisko": bool(close),
        "uwaga_polityki": best.policy_note,
    }
