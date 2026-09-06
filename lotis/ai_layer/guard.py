"""Straznik liczb -- kontrola odpowiedzi modelu.

Model dostaje raporty i ma je wyjasnic, a nie przeliczyc. Roznica jest istotna,
bo tekst z halucynowana kwota wyglada dokladnie tak samo jak tekst z kwota
policzona przez silnik, a trafia do czlowieka, ktory podpisuje decyzje.

Straznik robi jedna rzecz: wyciaga z odpowiedzi wszystkie liczby i sprawdza,
czy kazda z nich wystepuje w raportach tego runu.

DLACZEGO TO DZIALA NA JSON, A NIE NA TEKSCIE PROMPTU
Zbior dozwolonych liczb pochodzi z kanonicznych plikow `.json`, tych samych,
z ktorych renderowany jest markdown. Gdyby straznik czytal tekst promptu,
sprawdzalby model wzgledem tego, co model sam widzial -- czyli nic.

O DOPUSZCZENIACH
Data, godzina, numer rejsu, znak rejestracyjny, sygnatura sprawy i numer
artykulu to nie sa wyniki obliczen, wiec sa zdejmowane z tekstu przed skanem.
Kazdy taki wzorzec jest tu wypisany jawnie i policzony w wyniku -- lista
dopuszczen, ktorej nie widac, po kilku iteracjach przepuszcza wszystko.

O TOLERANCJI
Zaokraglenie w dol do tej samej liczby miejsc po przecinku jest ostrzezeniem,
nie bledem: raport podaje 12.4321, model pisze 12.43 i to jest poprawne
cytowanie. Ale juz 12.5 bledem jest, bo czytelnik dostaje inna liczbe.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import StrEnum

from .prompt_builder import NodeReport, allowed_numbers


class Severity(StrEnum):
    ERROR = "ERROR"       # liczby nie ma w raportach
    WARN = "WARN"         # jest, ale model ja zaokraglil


#: Wzorce zdejmowane z tekstu przed szukaniem liczb. Kolejnosc ma znaczenie:
#: dluzsze i bardziej szczegolowe najpierw, inaczej krotszy wzorzec rozbije
#: dluzszy i zostawi ogon cyfr.
#: Uwaga o znakach: wzorce zawieraja MYSLNIK NIEROZDZIELAJACY (U+2011) obok
#: zwyklego oraz SPACJE NIEROZDZIELAJACA (U+00A0) i WASKA NIEROZDZIELAJACA
#: (U+202F) obok zwyklej. To nie sa literowki. Modele formatuja sygnatury spraw
#: i separatory tysiecy wlasnie tymi znakami, a wzorzec, ktory zna tylko wersje
#: ASCII, przepuszcza `32 911` jako liczbe nieznana i podnosi falszywy alarm.
EXEMPTIONS: tuple[tuple[str, str], ...] = (
    ("odcisk snapshotu", r"sha256:[0-9a-fA-F]+"),
    ("identyfikator runu", r"\brun[_-][0-9A-Za-z_-]+|\b\d{8}T\d{6}\b"),
    ("data ISO", r"\b\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2})?(?:[+-]\d{2}:?\d{2}|Z)?)?"),
    ("godzina", r"\b\d{1,2}:\d{2}(?::\d{2})?\b"),
    ("sygnatura TSUE", r"\bC[-‑]\d{1,4}/\d{2,4}\b"),
    ("rozporzadzenie EU261", r"\bEU[ -]?261(?:/\d{4})?\b"),
    ("akt prawny", r"\b\d{2,4}/\d{4}(?:/\w+)?\b"),
    ("artykul", r"\bArt(?:\.|ykul|ykule|ykulu)?\s*\d+[a-z]?(?:\s*ust\.\s*\d+)?"),
    ("numer rejsu", r"\b(?:znak:)?(?:LO|LOT)[ -]?\d{1,4}[A-Z]{0,3}\b"),
    ("znak rejestracyjny", r"\bSP[-‑][A-Z]{2,3}\b"),
    ("typ statku", r"\b(?:B7\d{2}|B3\d[A-Z]|A\d{3}|E\d{2}[A-Z]?|DH\d[A-Z]?)\b"),
    ("identyfikator node", r"\bnode\s*\d{2}[a-z]?\b|\[\d{2}[a-z]?\]"),
    ("wersja", r"\bv?\d+\.\d+(?:\.\d+)+\b"),
    ("identyfikator rekordu", r"\b(?:PAX|OD|ROT|OPT)[-_]?\d+\b"),
    ("numeracja listy", r"(?m)^\s{0,6}\d{1,2}[.)]\s"),
    ("naglowek struktury", r"(?m)^#{1,6}\s*\d{1,2}[.)]?\s"),
)

#: Liczba w tekscie: opcjonalny minus, cyfry z separatorem tysiecy (spacja,
#: spacja nierozdzielajaca albo apostrof), opcjonalna czesc dziesietna.
_NUMBER = re.compile(r"-?\d{1,3}(?:[   ']\d{3})+(?:[.,]\d+)?|-?\d+(?:[.,]\d+)?")


@dataclass(frozen=True, slots=True)
class Violation:
    severity: Severity
    value: float
    text: str
    context: str

    def as_dict(self) -> dict[str, object]:
        return {"severity": self.severity.value, "value": self.value,
                "text": self.text, "context": self.context}


@dataclass(slots=True)
class GuardResult:
    checked: int = 0
    exempted: dict[str, int] = field(default_factory=dict)
    violations: list[Violation] = field(default_factory=list)
    allowed_count: int = 0

    @property
    def errors(self) -> list[Violation]:
        return [v for v in self.violations if v.severity is Severity.ERROR]

    @property
    def warnings(self) -> list[Violation]:
        return [v for v in self.violations if v.severity is Severity.WARN]

    @property
    def clean(self) -> bool:
        return not self.errors

    def summary(self) -> str:
        if not self.checked:
            return "Odpowiedz nie zawiera zadnej liczby do sprawdzenia."
        if self.clean and not self.warnings:
            return f"Wszystkie {self.checked} liczb pochodzi z raportow."
        parts = [f"sprawdzono {self.checked} liczb"]
        if self.errors:
            parts.append(f"{len(self.errors)} spoza raportow")
        if self.warnings:
            parts.append(f"{len(self.warnings)} zaokraglonych")
        return ", ".join(parts) + "."

    def as_dict(self) -> dict[str, object]:
        return {
            "clean": self.clean,
            "checked": self.checked,
            "allowed_pool": self.allowed_count,
            "exempted": dict(sorted(self.exempted.items())),
            "errors": [v.as_dict() for v in self.errors],
            "warnings": [v.as_dict() for v in self.warnings],
            "summary": self.summary(),
        }


def strip_exemptions(text: str) -> tuple[str, dict[str, int]]:
    """Zdejmuje z tekstu to, co nie jest wynikiem obliczen. Zwraca (tekst, licznik)."""
    counts: dict[str, int] = {}
    out = text
    for label, pattern in EXEMPTIONS:
        out, hits = re.subn(pattern, " ", out)
        if hits:
            counts[label] = counts.get(label, 0) + hits
    return out, counts


def parse_number(token: str) -> float | None:
    """`'32 911'` -> 32911.0, `'12,43'` -> 12.43. Zwraca None dla smieci."""
    cleaned = token.replace(" ", "").replace(" ", "")
    cleaned = cleaned.replace(" ", "").replace("'", "")
    if cleaned.count(",") and cleaned.count("."):
        # 1.234,56 (pl) albo 1,234.56 (en) -- ostatni separator jest dziesietny
        last = max(cleaned.rfind(","), cleaned.rfind("."))
        cleaned = re.sub(r"[.,]", "", cleaned[:last]) + "." + cleaned[last + 1:]
    else:
        cleaned = cleaned.replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


def check(answer: str, reports: tuple[NodeReport, ...],
          extra_allowed: set[float] | None = None) -> GuardResult:
    """Porownaj liczby z odpowiedzi z liczbami z raportow."""
    allowed = allowed_numbers(reports)
    if extra_allowed:
        allowed = allowed | extra_allowed

    stripped, exempted = strip_exemptions(answer)
    result = GuardResult(exempted=exempted, allowed_count=len(allowed))

    # Zaokraglenia liczymy raz na komplet raportow, nie raz na liczbe.
    rounded: dict[int, set[float]] = {}
    for places in range(4):
        rounded[places] = {round(v, places) for v in allowed}

    seen: set[str] = set()
    for match in _NUMBER.finditer(stripped):
        token = match.group(0)
        value = parse_number(token)
        if value is None:
            continue
        result.checked += 1
        if value in allowed:
            continue

        places = len(token.partition(".")[2]) if "." in token else \
            len(token.partition(",")[2]) if "," in token else 0
        places = min(places, 3)

        key = f"{value}|{places}"
        if key in seen:
            continue
        seen.add(key)

        context = _context(stripped, match.start(), match.end())
        if value in rounded[places]:
            result.violations.append(
                Violation(Severity.WARN, value, token, context))
        else:
            result.violations.append(
                Violation(Severity.ERROR, value, token, context))
    return result


def annotate(answer: str, result: GuardResult) -> str:
    """Doklej do odpowiedzi adnotacje straznika.

    Odpowiedz z naruszeniem nie jest kasowana -- jest oznaczana. Czlowiek ma
    zobaczyc, co model napisal i czego w raporcie nie bylo; ciche skasowanie
    odebraloby mu te informacje.
    """
    lines = [answer.rstrip(), "", "---", "", "## Kontrola straznika liczb", "",
             result.summary()]
    if result.errors:
        lines += ["", "**Liczby, ktorych nie ma w raportach tego runu:**", ""]
        lines += [f"- `{v.text}` -- {v.context}" for v in result.errors]
        lines += ["", "Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku."]
    if result.warnings:
        lines += ["", "**Zaokraglone wzgledem raportu (dopuszczalne, warto sprawdzic):**", ""]
        lines += [f"- `{v.text}` -- {v.context}" for v in result.warnings]
    if result.exempted:
        exempt = ", ".join(f"{k}: {n}" for k, n in sorted(result.exempted.items()))
        lines += ["", f"_Zdjete przed skanem jako nieobliczeniowe -- {exempt}._"]
    return "\n".join(lines) + "\n"


def _context(text: str, start: int, end: int, width: int = 40) -> str:
    left = text[max(0, start - width):start].replace("\n", " ")
    right = text[end:end + width].replace("\n", " ")
    return f"...{left.strip()} [{text[start:end]}] {right.strip()}...".replace("  ", " ")
