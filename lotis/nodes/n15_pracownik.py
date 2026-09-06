"""Node 15 -- PRACOWNIK.

Accept / Modify / Reject. Tablica miala tu trzy slowa i nic wiecej -- luka 4
polegala na tym, ze decyzja za 20 tysiecy i za 300 tysiecy przechodzila
identycznie.

CO DOKLADA TEN NODE
Prog autoryzacji wg kwoty (`policy/authorization.json`): cztery pasma, kazde
z rola i wymogiem drugiego podpisu powyzej progu. Decyzja przekraczajaca
uprawnienia dyzurnego nie jest odrzucana -- jest **podnoszona** do wlasciwej
roli, bo odrzucenie zostawiloby rejs bez decyzji.

Odrzucenie wymaga kodu przyczyny. Bez niego node 17 nie odroznilby "model
policzyl zle" od "czlowiek mial informacje, ktorej model nie mial" -- a to
jest cala roznica miedzy kalibracja a szumem.

CZLOWIEK NIE MOZE WYBRAC OPCJI, KTORA PRAWO ODRZUCILO
Ten node czyta `lawful` z node 12, a nie pelna liste opcji. Bez tego caly filtr
prawny bylby dekoracja: audyt pokazal, ze `--option HOLD` na dobie, w ktorej
node 12 odrzucil HOLD za naruszenie Art. 9, przechodzil przez node 15 ze statusem
`ok`, bez ani jednego ostrzezenia, i byl WYKONYWANY przez node 15b. System
dokumentowalby wlasne naruszenie jako zwykla decyzje.

Zasada nadrzedna mowi "prawo blokuje" przed "czlowiek decyduje" wlasnie w tej
kolejnosci. Czlowiek wybiera z opcji dopuszczalnych; zeby wyjsc poza nie, musi
zmienic prawo albo dane, a nie kliknac inna pozycje na liscie.
"""

from __future__ import annotations

from enum import StrEnum

from ..kernel.contracts import ExecutionCard, RankedOption
from ..kernel.money import Money
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.report import Status


class Decision(StrEnum):
    ACCEPT = "ACCEPT"
    MODIFY = "MODIFY"
    REJECT = "REJECT"


class PracownikNode(Node):
    id = "15"
    name = "pracownik"
    title = "PRACOWNIK"
    consumes = ("ranking", "lawful")
    produces = "decision"

    def __init__(self, decision: Decision = Decision.ACCEPT,
                 chosen_option: str | None = None,
                 reason_code: str = "",
                 operator: str = "OCC-DUTY") -> None:
        self.decision = decision
        self.chosen_option = chosen_option
        self.reason_code = reason_code
        self.operator = operator

    def run(self, ctx: RunContext) -> NodeOutput:
        ranking: list[RankedOption] = ctx.require("ranking")
        card: ExecutionCard | None = ctx.get("karta")
        report = self.new_report()

        if not ranking:
            report.status = Status.BLOCKED
            report.summary = "Brak rankingu -- nie ma czego zatwierdzac."
            ctx.halt("brak rankingu do decyzji")
            return NodeOutput(report)

        recommended = ranking[0]
        chosen_id = self.chosen_option or recommended.option_id
        chosen = next((r for r in ranking if r.option_id == chosen_id), None)

        if chosen is None:
            blad = self._odrzuc_wybor(ctx, report, chosen_id, ranking)
            return NodeOutput(blad)

        bands = ctx.policy.authorization
        band = _band_for(bands, chosen.band.high)
        reason_codes = list(bands.get("reason_codes", []))

        problems: list[str] = []
        if self.decision is Decision.REJECT:
            if bands.get("reject_requires_reason_code") and not self.reason_code:
                problems.append("odrzucenie bez kodu przyczyny")
            elif self.reason_code and self.reason_code not in reason_codes:
                problems.append(f"nieznany kod przyczyny: {self.reason_code}")
        if self.decision is Decision.MODIFY and chosen_id == recommended.option_id:
            problems.append("modyfikacja bez wskazania innej opcji")

        odstepstwo = chosen_id != recommended.option_id

        report.summary = (
            f"{self.operator}: {self.decision.value} dla `{chosen_id}` "
            f"({chosen.loss}). Wymagana rola: {band['role']}"
            + (", drugi podpis" if band["second_signature"] else "")
            + (f". Odstepstwo od rekomendacji `{recommended.option_id}`."
               if odstepstwo else ".")
        )

        report.number("decyzja", self.decision.value)
        report.number("wybrana_opcja", chosen_id)
        report.number("rekomendacja_silnika", recommended.option_id)
        report.number("odstepstwo_od_rekomendacji", odstepstwo)
        report.number("kwota_do_autoryzacji", chosen.band.high, "PLN")
        report.number("rola_autoryzujaca", band["role"])
        report.number("drugi_podpis", band["second_signature"])
        report.number("kod_przyczyny", self.reason_code or "-")
        if odstepstwo:
            report.number("roznica_wobec_rekomendacji",
                          chosen.loss - recommended.loss, "PLN")

        report.findings["pasma_autoryzacji"] = bands.get("bands", [])
        report.findings["dopuszczalne_kody_odrzucenia"] = reason_codes
        report.findings["decyzja"] = {
            "operator": self.operator,
            "rodzaj": self.decision.value,
            "opcja": chosen_id,
            "kod_przyczyny": self.reason_code,
            "rola": band["role"],
            "drugi_podpis": band["second_signature"],
        }
        if card is not None:
            report.findings["karta_wykonania"] = card

        report.decide(
            f"kwota {chosen.band.high} miesci sie w pasmie roli `{band['role']}`"
            + (" i wymaga drugiego podpisu" if band["second_signature"] else "")
        )
        if odstepstwo:
            report.decide(
                f"czlowiek wybral `{chosen_id}` zamiast `{recommended.option_id}` "
                f"-- roznica {chosen.loss - recommended.loss}; node 17 policzy to "
                "jako odstepstwo, a nie jako blad modelu"
            )
        for problem in problems:
            report.warn(problem)

        if problems:
            report.status = Status.DEGRADED

        if self.decision is Decision.REJECT:
            report.decide("decyzja odrzucona -- wykonanie nie rusza")
            ctx.halt(f"decyzja odrzucona przez {self.operator}: {self.reason_code}")

        return NodeOutput(report, {
            "decision": {
                "rodzaj": self.decision.value,
                "opcja": chosen_id,
                "operator": self.operator,
                "kod_przyczyny": self.reason_code,
                "rola": band["role"],
                "drugi_podpis": band["second_signature"],
                "odstepstwo": odstepstwo,
            },
        })


    def _odrzuc_wybor(self, ctx: RunContext, report, chosen_id: str, ranking):
        """Wybor spoza listy dopuszczalnych opcji zatrzymuje przeplyw.

        Rozrozniamy dwa powody, bo znacza co innego: opcja odrzucona przez
        prawo to proba obejscia filtru, a opcja nieznana to blad wejscia.
        """
        verdicts = ctx.get("verdicts", {})
        lawful = set(ctx.require("lawful"))
        wszystkie = {o.id for o in ctx.get("options", ())}
        report.status = Status.BLOCKED

        if chosen_id in wszystkie and chosen_id not in lawful:
            verdict = verdicts.get(chosen_id)
            reguly = [{"podstawa": p, "powod": r}
                      for p, r in (verdict.rules_failed if verdict else ())]
            report.summary = (
                f"Odmowa: opcja `{chosen_id}` zostala odrzucona przez filtr prawny "
                f"i nie moze byc wykonana."
            )
            report.findings["odrzucona_opcja"] = {"id": chosen_id, "reguly": reguly}
            report.findings["dopuszczalne"] = sorted(lawful)
            for pozycja in reguly:
                report.decide(
                    f"`{chosen_id}` lamie {pozycja['podstawa']}: {pozycja['powod']}"
                )
            report.decide(
                "prawo blokuje przed tym, jak czlowiek decyduje -- wybor poza "
                "lista dopuszczalnych wymaga zmiany danych albo polityki, "
                "nie innego kliniecia"
            )
            report.findings["escalation"] = {
                "addressee": ctx.policy.escalation.get("addressee", {}),
                "sla_minutes": ctx.policy.escalation.get("sla_minutes"),
                "powod": f"proba wykonania opcji niedopuszczalnej `{chosen_id}`",
                "dopuszczalne_zamiast": sorted(lawful),
            }
            ctx.halt(f"opcja `{chosen_id}` odrzucona przez filtr prawny",
                     report.findings["escalation"])
        else:
            report.summary = (
                f"Odmowa: opcja `{chosen_id}` nie wystepuje w tym runie. "
                f"Dostepne: {', '.join(r.option_id for r in ranking)}."
            )
            report.data_gaps.append(f"nieznana opcja w decyzji: {chosen_id}")
            report.findings["dostepne"] = [r.option_id for r in ranking]
            ctx.halt(f"nieznana opcja w decyzji: {chosen_id}")

        report.number("decyzja", "ODRZUCONA_PRZEZ_SYSTEM")
        report.number("zadana_opcja", chosen_id)
        report.number("rekomendacja_silnika", ranking[0].option_id)
        return report


def _band_for(authorization: dict, value: Money) -> dict[str, object]:
    amount = float(value.major)
    for band in authorization.get("bands", []):
        limit = band.get("max_value")
        if limit is None or amount <= float(limit):
            return {"role": band.get("role", "?"),
                    "second_signature": bool(band.get("second_signature"))}
    return {"role": "?", "second_signature": True}
