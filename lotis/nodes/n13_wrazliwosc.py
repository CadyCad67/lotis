"""Node 13 -- WRAZLIWOSC.

Test wrazliwosci +30 / +60 / +120 min, prog oplacalnosci, polityka firmy jako
waga, porownanie czolowki i ranking koncowy. Tutaj powstaje takze KARTA
WYKONANIA -- deterministycznie, z wyniku silnika.

PO CO TEST WRAZLIWOSCI
Ranking policzony na jednej wartosci opoznienia jest kruchy. Opoznienie jest
szacunkiem, a nie pomiarem, wiec pytanie brzmi nie "ktora opcja jest najlepsza",
tylko "do ilu minut ta opcja pozostaje najlepsza". Ta liczba -- prog
oplacalnosci -- jest jedynym wynikiem, ktory dyzurny moze uzyc, gdy sytuacja
zmieni sie w trakcie.

POLITYKA FIRMY JAKO WAGA, NIE JAKO KOSZT
`CF.weights` daje szesc wag: ochrona rotacji, pasazerow transferowych, osob
wymagajacych szczegolnej opieki, niepewnosci, kosztu kasacji i zalogi. Waga
przesuwa ranking, ale NIE zmienia kwoty w raporcie -- inaczej nikt nie
odroznilby zlotowki od preferencji.
"""

from __future__ import annotations

from ..kernel.contracts import (
    ExecutionCard, LegalVerdict, Option, OptionEvaluation, PaxOutcomeKind,
    RankedOption, Snapshot, SpecialNeed,
)
from ..kernel.money import Money
from ..kernel.node import Node, NodeOutput, RunContext

#: Kroki testu wrazliwosci z tablicy.
SENSITIVITY_STEPS = (30, 60, 120)

#: Ponizej tej roznicy dwie opcje sa "blisko" i node 14 ma o tym ostrzec.
CLOSE_CALL_PCT = 0.10


class WrazliwoscNode(Node):
    id = "13"
    name = "wrazliwosc"
    title = "WRAZLIWOSC"
    consumes = ("snapshot", "options", "evaluations", "lawful")
    produces = "ranking"

    def __init__(self, priority: int = 50, preset: str = "STANDARD") -> None:
        #: 0 to ranking wylacznie po pieniadzach, 100 wylacznie po tym, jak
        #: opcja odbija sie na pasazerach. Wartosc miesza obie osie liniowo.
        self.priority = max(0, min(100, int(priority)))
        #: Ktory zestaw wag z `CF.presets` obowiazuje w tym przebiegu.
        self.preset = preset or "STANDARD"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        options: tuple[Option, ...] = ctx.require("options")
        evaluations: dict[str, OptionEvaluation] = ctx.require("evaluations")
        lawful: tuple[str, ...] = ctx.require("lawful")
        verdicts: dict[str, LegalVerdict] = ctx.get("verdicts", {})
        disruption = ctx.require("disruption")
        report = self.new_report()

        by_id = {o.id: o for o in options}
        pool = [evaluations[oid] for oid in lawful if oid in evaluations]

        weights = _weights(ctx, self.preset)
        scored: list[tuple[OptionEvaluation, float, str]] = []
        for evaluation in pool:
            option = by_id[evaluation.option_id]
            score, note = _policy_score(snap, option, evaluation, weights,
                                        self.priority)
            scored.append((evaluation, score, note))
        scored.sort(key=lambda item: item[1])

        default_id = _default_option(by_id, lawful)
        default_loss = (evaluations[default_id].loss if default_id in evaluations
                        else Money.zero())

        ranking: list[RankedOption] = []
        for position, (evaluation, score, note) in enumerate(scored, 1):
            ranking.append(RankedOption(
                option_id=evaluation.option_id,
                rank=position,
                loss=evaluation.loss,
                band=evaluation.band,
                saving_vs_default=default_loss - evaluation.loss,
                score=score,
                policy_note=note,
            ))

        sensitivity = _sensitivity(by_id, evaluations, lawful, disruption)
        threshold = _threshold(sensitivity, ranking)
        close = _close_call(ranking)

        card = (_card(snap, ctx, by_id[ranking[0].option_id], ranking[0], disruption,
                      threshold) if ranking else None)

        report.summary = (
            f"Ranking koncowy {len(ranking)} dopuszczalnych opcji. "
            + (f"Rekomendacja: `{ranking[0].option_id}` "
               f"({ranking[0].loss}), oszczednosc wobec opcji domyslnej "
               f"`{default_id}`: {ranking[0].saving_vs_default}."
               if ranking else "")
        )
        if ranking:
            report.number("rekomendacja", ranking[0].option_id)
            report.number("strata_rekomendacji", ranking[0].loss, "PLN")
            report.number("widelki_min", ranking[0].band.low, "PLN")
            report.number("widelki_max", ranking[0].band.high, "PLN")
            report.number("opcja_domyslna", default_id)
            report.number("strata_opcji_domyslnej", default_loss, "PLN")
            report.number("oszczednosc", ranking[0].saving_vs_default, "PLN")
            report.number("prog_oplacalnosci", threshold["do_minut"], "min")
        report.number("opcji_w_rankingu", len(ranking), "szt")

        report.findings["ranking_koncowy"] = [
            {"id": r.option_id, "pozycja": r.rank, "label": by_id[r.option_id].label,
             "strata": r.loss, "min": r.band.low, "max": r.band.high,
             "oszczednosc": r.saving_vs_default, "wskaznik": round(r.score, 2),
             "uwaga_polityki": r.policy_note}
            for r in ranking
        ]
        report.findings["test_wrazliwosci"] = sensitivity
        report.findings["prog_oplacalnosci"] = threshold
        report.findings["wagi_polityki"] = weights
        report.findings["opcje_odrzucone_przez_prawo"] = [
            {"id": oid, "reguly": [p for p, _ in verdicts[oid].rules_failed]}
            for oid in by_id if oid not in lawful and oid in verdicts
        ]
        if card is not None:
            report.findings["karta_wykonania"] = card

        report.decide(
            f"opcja domyslna to `{default_id}` -- oszczednosc liczy sie wzgledem niej, "
            "a nie wzgledem nicnierobienia"
        )
        report.decide(threshold["opis"])
        report.decide(
            "waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty "
            "w raporcie"
        )
        if close:
            report.warn(
                f"opcje `{close[0]}` i `{close[1]}` roznia sie o mniej niz "
                f"{int(CLOSE_CALL_PCT * 100)}% -- roznica moze byc szumem"
            )
            report.decide("przy bliskiej czolowce decyzja nalezy do czlowieka, nie do rankingu")

        report.assume("prog oplacalnosci", "derived", 0.7,
                      "policzony na siatce +30/+60/+120 min, nie w sposob ciagly")

        return NodeOutput(report, {
            "ranking": ranking,
            "karta": card,
            "close_call": close,
            "sensitivity": sensitivity,
            "default_option": default_id,
        })


# ---------------------------------------------------------------- polityka


def _weights(ctx, preset: str = "STANDARD") -> dict[str, float]:
    """Wagi z wybranego presetu bazy (`CF.presets`).

    Wczesniej preset byl wpisany na sztywno, wiec zmiana zestawu wag nie mogla
    wplynac na nic. Teraz nazwa przychodzi z zewnatrz i raport ja cytuje.
    """
    presets = ctx.policy.presets
    chosen = next((p for p in presets if p.get("k") == preset), None)
    if chosen is None:
        chosen = next((p for p in presets if p.get("k") == "STANDARD"), None)
    if chosen is None and presets:
        chosen = presets[0]
    return dict(chosen.get("w", {})) if chosen else {}


#: Waga zdarzenia dla pasazera. Odmowa przyjecia najciezsza, bo pasazer w ogole
#: nie leci; przebukowanie na obcego przewoznika gorsze niz na wlasny.
_PAX_WAGA = {
    PaxOutcomeKind.OFFLOADED_INVOLUNTARY: 10.0,
    PaxOutcomeKind.CANCELLED_REFUND: 8.0,
    PaxOutcomeKind.OFFLOADED_VOLUNTARY: 4.0,
    PaxOutcomeKind.REBOOKED_OAL: 3.0,
    PaxOutcomeKind.REBOOKED_OWN: 2.0,
}


def _indeks_pax(option: Option) -> float:
    """Uciazliwosc opcji dla pasazera, srednio na osobe."""
    outcomes = list(option.pax_outcomes.values())
    if not outcomes:
        return 0.0
    suma = 0.0
    for o in outcomes:
        suma += _PAX_WAGA.get(o.kind, 0.0)
        suma += o.delay_min / 60.0
        suma += o.care_nights * 2.0
    return suma / len(outcomes)


def _policy_score(snap: Snapshot, option: Option, evaluation: OptionEvaluation,
                  weights: dict[str, float], priority: int = 50) -> tuple[float, str]:
    """Wskaznik rankingowy: strata przesunieta wagami polityki i priorytetem.

    Punktem wyjscia jest strata w zlotowkach. Wagi ja MODULUJA -- opcja, ktora
    psuje rotacje albo dotyka pasazerow transferowych, dostaje gorszy wskaznik
    przy tej samej kwocie. Priorytet dokłada druga os: im bardziej w strone
    pasazera, tym mocniej wskaznik rosnie opcjom, ktore kogos wysadzaja albo
    kaza dlugo czekac. Zadna kwota w raporcie sie przez to nie zmienia.
    """
    base = float(evaluation.loss.minor)
    notes: list[str] = []

    if evaluation.network and evaluation.network.delay_propagated_min:
        propagated = sum(evaluation.network.delay_propagated_min.values())
        if propagated:
            factor = weights.get("rot", 1.0)
            base *= 1.0 + 0.05 * factor * min(4.0, propagated / 60.0)
            notes.append(f"propagacja {propagated} min (waga rotacji {factor})")

    if evaluation.network and evaluation.network.connections_missed:
        factor = weights.get("trf", 1.0)
        base *= 1.0 + 0.03 * factor * min(4.0, evaluation.network.connections_missed / 10.0)
        notes.append(f"{evaluation.network.connections_missed} utraconych przesiadek")

    vulnerable = sum(
        1 for pax_id, outcome in option.pax_outcomes.items()
        if outcome.kind in (PaxOutcomeKind.OFFLOADED_INVOLUNTARY,
                            PaxOutcomeKind.OFFLOADED_VOLUNTARY)
        and (pax := snap.passengers.get(pax_id)) is not None
        and (pax.specials & {SpecialNeed.REDUCED_MOBILITY,
                             SpecialNeed.UNACCOMPANIED_MINOR,
                             SpecialNeed.MEDICAL_ASSIST})
    )
    if vulnerable:
        factor = weights.get("vuln", 1.0)
        base *= 1.0 + 0.10 * factor * vulnerable
        notes.append(f"{vulnerable} pasazerow wymagajacych szczegolnej opieki")

    spread = evaluation.band.spread.minor
    if spread and evaluation.loss.minor:
        factor = weights.get("unc", 1.0)
        base *= 1.0 + 0.02 * factor * min(3.0, spread / max(1, abs(evaluation.loss.minor)))
        notes.append("szerokie widelki")

    # Priorytet dokłada KARE za uciazliwosc dla pasazera i nigdy nie daje
    # premii. Wczesniej mnoznik schodzil ponizej 1.0 przy priorytecie blizej
    # finansow, wiec opcja najbardziej dotkliwa dla pasazerow dostawala
    # najwiekszy rabat na wskazniku i potrafila wyprzedzic tansza. Przy 0
    # mnoznik wynosi dokladnie 1.0, czyli ranking idzie wylacznie po pieniadzach,
    # a to znaczy najmniejsza strate, czyli najlepszy wynik finansowy.
    if priority:
        indeks = _indeks_pax(option)
        base *= 1.0 + 0.35 * (priority / 100.0) * min(6.0, indeks)
        notes.append(f"priorytet {priority}, indeks pasazerski {indeks:.2f}")

    return base, "; ".join(notes)


def _default_option(by_id: dict[str, Option], lawful: tuple[str, ...]) -> str:
    """Opcja domyslna -- luka 6 tablicy.

    Tablica nie rozstrzygala, czy to nicnierobienie, czy to, co zrobilby dzis
    dyzurny wedlug SOP. To sa dwie rozne liczby, a oszczednosc wzgledem nich
    jest glownym wskaznikiem wartosci calego projektu.

    Rozstrzygniecie: opcja domyslna to `HOLD` -- czekanie na usuniecie
    przyczyny. Tak wyglada zachowanie bez systemu i to jest uczciwy punkt
    odniesienia. Wybor jest zapisany w `policy/sop_default.json`.
    """
    for candidate in ("HOLD", "DEPART"):
        if candidate in lawful:
            return candidate
    return lawful[0] if lawful else ""


# ---------------------------------------------------------------- wrazliwosc


def _sensitivity(by_id, evaluations, lawful, disruption) -> list[dict[str, object]]:
    """Jak zmienia sie czolowka przy +30 / +60 / +120 min.

    Opcje opoznieniowe rosna liniowo z czasem, opcje restrukturyzujace prawie
    nie. Dlatego przy dostatecznie dlugim opoznieniu SWAP albo rebooking
    zawsze w koncu wygrywa -- pytanie tylko, od ktorej minuty.
    """
    out: list[dict[str, object]] = []
    for step in SENSITIVITY_STEPS:
        przesuniete: list[tuple[str, int]] = []
        for option_id in lawful:
            evaluation = evaluations.get(option_id)
            option = by_id.get(option_id)
            if evaluation is None or option is None:
                continue
            wrazliwosc = _sensitivity_factor(option)
            przesuniete.append(
                (option_id, evaluation.loss.minor + int(wrazliwosc * step * 100))
            )
        przesuniete.sort(key=lambda item: item[1])
        out.append({
            "krok_min": step,
            "lider": przesuniete[0][0] if przesuniete else "",
            "ranking": [{"id": oid, "strata": Money(value)} for oid, value in przesuniete],
        })
    return out


def _sensitivity_factor(option: Option) -> float:
    """Ile zlotych na minute dokłada dodatkowe opoznienie tej opcji.

    Opcja czekajaca rosnie z kazda minuta. Opcja, ktora juz przestawila
    pasazerow, jest na dalsze opoznienie odporna.
    """
    if option.cancelled:
        return 0.0
    if option.aircraft_swap:
        return 12.0
    return 55.0 if option.delay_min else 0.0


def _threshold(sensitivity, ranking) -> dict[str, object]:
    """Do ilu minut rekomendacja pozostaje rekomendacja."""
    if not ranking:
        return {"do_minut": 0, "opis": "brak rankingu -- prog nieokreslony"}
    leader = ranking[0].option_id
    for step in sensitivity:
        if step["lider"] != leader:
            return {
                "do_minut": step["krok_min"],
                "przejmuje": step["lider"],
                "opis": (f"`{leader}` jest najlepsza do okolo +{step['krok_min']} min "
                         f"dodatkowego opoznienia; powyzej przejmuje `{step['lider']}`"),
            }
    ostatni = SENSITIVITY_STEPS[-1]
    return {
        "do_minut": ostatni,
        "przejmuje": "",
        "opis": (f"`{leader}` pozostaje najlepsza w calym badanym zakresie "
                 f"do +{ostatni} min"),
    }


def _close_call(ranking) -> tuple[str, str] | None:
    if len(ranking) < 2:
        return None
    first, second = ranking[0], ranking[1]
    anchor = max(1, abs(first.loss.minor))
    if abs(second.loss.minor - first.loss.minor) / anchor < CLOSE_CALL_PCT:
        return (first.option_id, second.option_id)
    return None


# ---------------------------------------------------------------- karta


def _card(snap: Snapshot, ctx, option: Option, ranked: RankedOption,
          disruption, threshold) -> ExecutionCard:
    """KARTA WYKONANIA -- deterministycznie z wyniku silnika (luka 7 tablicy).

    Model z warstwy AI moze dopisac komentarz OBOK karty, ale nie ma sciezki
    zapisu do jej srodka. Gdyby miał, karta przestalaby byc odtwarzalna.
    """
    flight = snap.flights[disruption.flight_id]
    what: list[str] = []
    if option.aircraft_swap:
        a, b = option.aircraft_swap
        what.append(f"podmiana maszyny miedzy {snap.flights[a].number} "
                    f"i {snap.flights[b].number}")
    for flight_id, minutes in sorted(option.delay_min.items()):
        if minutes:
            target = snap.flights.get(flight_id)
            if target is not None:
                nowy = target.std.replace(microsecond=0)
                what.append(f"{target.number}: odlot pozniej o {minutes} min "
                            f"(z {nowy.strftime('%H:%M')} UTC)")
    for flight_id in sorted(option.cancelled):
        target = snap.flights.get(flight_id)
        if target is not None:
            what.append(f"{target.number}: rejs odwolany")

    # Dokad ida pasazerowie -- bez tego karta mowi tylko, co znika.
    przeniesieni: dict[str, int] = {}
    for outcome in option.pax_outcomes.values():
        if outcome.kind is PaxOutcomeKind.REBOOKED_OWN:
            przeniesieni["wlasny rejs"] = przeniesieni.get("wlasny rejs", 0) + 1
        elif outcome.kind is PaxOutcomeKind.REBOOKED_OAL:
            przeniesieni["przewoznik obcy"] = przeniesieni.get("przewoznik obcy", 0) + 1
    docelowy = next((snap.flights[f] for f in option.affected_flights
                     if f != flight.id and f in snap.flights), None)
    for gdzie, ile in sorted(przeniesieni.items()):
        czekanie = max((o.delay_min for o in option.pax_outcomes.values()
                        if (o.kind is PaxOutcomeKind.REBOOKED_OWN) == (gdzie == "wlasny rejs")),
                       default=0)
        cel = (f" ({docelowy.number}, odlot {docelowy.std.strftime('%H:%M')} UTC)"
               if gdzie == "wlasny rejs" and docelowy is not None else "")
        what.append(f"{ile} pasazerow na {gdzie}{cel} -- oczekiwanie {czekanie} min")
    nocujacy = sum(1 for o in option.pax_outcomes.values() if o.care_nights)
    if nocujacy:
        what.append(f"{nocujacy} pasazerow z noclegiem na koszt przewoznika (Art. 9)")
    for flight_id, type_code in sorted(option.new_type.items()):
        target = snap.flights.get(flight_id)
        if target is not None and type_code != target.type_code:
            what.append(f"{target.number}: typ {target.type_code} -> {type_code}")

    offloaded = [pid for pid, o in option.pax_outcomes.items()
                 if o.kind in (PaxOutcomeKind.OFFLOADED_INVOLUNTARY,
                               PaxOutcomeKind.OFFLOADED_VOLUNTARY)]
    order = _offload_order(snap, offloaded)

    rebooked: dict[str, str] = {}
    for pid, outcome in option.pax_outcomes.items():
        if outcome.kind is PaxOutcomeKind.REBOOKED_OWN:
            rebooked[pid] = "wlasny rejs"
        elif outcome.kind is PaxOutcomeKind.REBOOKED_OAL:
            rebooked[pid] = "przewoznik obcy"

    crew: list[str] = []
    if option.delay_min.get(flight.id):
        crew.append(f"zaloga rejsu {flight.number} pozostaje na sluzbie "
                    f"+{option.delay_min[flight.id]} min -- sprawdzic FDP przed odlotem")
    if option.aircraft_swap:
        crew.append("wezwanie zalogi z rezerwy dla rejsu przejmujacego maszyne")
    if any(o.care_nights for o in option.pax_outcomes.values()):
        crew.append("nocleg zalogi poza baza")
    if not crew:
        crew.append("bez zmian dla zalogi")

    band = ranked.band
    authorization = _authorization(ctx, band.high)

    return ExecutionCard(
        option_id=option.id,
        label=option.label,
        what_changes=tuple(what) or ("bez zmian operacyjnych",),
        pax_offloaded=len(offloaded),
        pax_order=tuple(order[:20]),
        rebooked_to=dict(list(rebooked.items())[:20]),
        crew_actions=tuple(crew),
        valid_until=disruption.decision_deadline,
        cost_low=band.low,
        cost_expected=band.expected,
        cost_high=band.high,
        threshold_note=str(threshold["opis"]),
        authorization_role=authorization["role"],
        second_signature=authorization["second_signature"],
    )


def _offload_order(snap: Snapshot, pax_ids: list[str]) -> list[str]:
    """Kolejnosc przy odmowie przyjecia.

    Najpierw schodza pasazerowie o najnizszym priorytecie. Chronieni --
    PRM, maloletni bez opieki, asysta medyczna -- ida na sam koniec i w praktyce
    nie schodza wcale, bo filtr prawny usuwa opcje, ktora ich zdejmuje.
    """
    def klucz(pax_id: str):
        pax = snap.passengers.get(pax_id)
        if pax is None:
            return (0, 0)
        chroniony = bool(pax.specials & {SpecialNeed.REDUCED_MOBILITY,
                                         SpecialNeed.UNACCOMPANIED_MINOR,
                                         SpecialNeed.MEDICAL_ASSIST})
        lojalny = pax.basket.status.value == "LOYALTY"
        return (int(chroniony) + int(lojalny), pax.value.minor)

    return sorted(pax_ids, key=klucz)


def _authorization(ctx, value: Money) -> dict[str, object]:
    """Prog autoryzacji wg kwoty (luka 4 tablicy)."""
    bands = ctx.policy.authorization.get("bands", [])
    amount = float(value.major)
    for band in bands:
        limit = band.get("max_value")
        if limit is None or amount <= float(limit):
            return {"role": band.get("role", "?"),
                    "second_signature": bool(band.get("second_signature"))}
    return {"role": "?", "second_signature": True}
