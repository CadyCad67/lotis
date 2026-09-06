"""Nodes -- po jednym pliku na box tablicy.

Osiemnascie plikow: siedemnascie boxow pionu ARCHITEKTURA plus `15b WYKONANIE`,
ktorego na tablicy nie bylo (luka 1). Kazdy dziedziczy po `kernel.Node`,
dostaje `RunContext`, oddaje `NodeOutput` i zapisuje pare raportow. Klasa
bazowa mierzy czas, sprawdza wejscia i lapie wyjatki dziedzinowe, wiec plik
node zawiera wylacznie logike.

    01  DANE                 zamraza stan swiata
    02  DATA ENGINE          mowi, ktorym polom wolno ufac
    03  BASELINE REVENUE     punkt odniesienia sprzed zaklocenia
    04  ZAKLOCENIE           co, kiedy, czego dotyczy, do kiedy decyzja
    05  FEASIBILITY          cztery bramki: samolot, zaloga, port, miejsca
    06  REZERWACJA ZASOBU    co jest do wziecia i co jest sporne
    07  SCENARIO ENGINE      generuje opcje z katalogu SZ bazy
    08  REVENUE ENGINE       ile z baseline'u przetrwalo
    09  COST ENGINE          skladniki kosztu, dwa tryby liczenia
    10  NETWORK IMPACT       propagacja do konca doby albo do bazy
    11  OPTIMIZATION ENGINE  strata, widelki, ranking wstepny
    12  FILTR PRAWNY         USUWA opcje, nigdy ich nie przecenia
    13  WRAZLIWOSC           +30/+60/+120, prog, ranking koncowy, karta
    14  AI REASONING         deterministyczna kontrola spojnosci wyniku
    15  PRACOWNIK            Accept / Modify / Reject + progi autoryzacji
    15b WYKONANIE            kto realizuje i co, gdy sie nie uda (luka 1)
    16  LOG                  co policzono, co odrzucono i dlaczego
    17  WYNIK RZECZYWISTY    blad modelu / wykonania / odstepstwo + kalibracja

Kolejnosc nie jest przypadkowa i nie da sie jej przestawic: kazdy node
deklaruje w `consumes`, czego potrzebuje, a klasa bazowa blokuje go z jawnym
komunikatem, gdy wejscia brakuje.
"""

from .n01_snapshot import SnapshotNode
from .n02_walidacja import WalidacjaNode
from .n03_baseline import BaselineNode
from .n04_zaklocenie import ZaklocenieNode
from .n05_feasibility import FeasibilityNode
from .n06_zasoby import ZasobyNode
from .n07_scenariusze import ScenariuszeNode
from .n08_revenue import RevenueNode
from .n09_koszt import KosztNode
from .n10_siec import SiecNode
from .n11_optymalizacja import OptymalizacjaNode
from .n12_filtr_prawny import FiltrPrawnyNode
from .n13_wrazliwosc import WrazliwoscNode
from .n14_ai_reasoning import AiReasoningNode
from .n15_pracownik import Decision, PracownikNode
from .n15b_wykonanie import WykonanieNode
from .n16_log import LogNode
from .n17_wynik import WynikNode

#: Klasy w kolejnosci tablicy. Node bezargumentowy da sie zbudowac wprost;
#: te z parametrami (04, 15, 15b, 17) buduje `build_pipeline`.
NODE_CLASSES = (
    SnapshotNode, WalidacjaNode, BaselineNode, ZaklocenieNode, FeasibilityNode,
    ZasobyNode, ScenariuszeNode, RevenueNode, KosztNode, SiecNode,
    OptymalizacjaNode, FiltrPrawnyNode, WrazliwoscNode, AiReasoningNode,
    PracownikNode, WykonanieNode, LogNode, WynikNode,
)


def build_pipeline(
    *,
    weekday: int = 4,
    seed: int = 2026,
    flight_id: str | None = None,
    delay_min: int = 180,
    delay_code: str = "41",
    decision: Decision = Decision.ACCEPT,
    chosen_option: str | None = None,
    reason_code: str = "",
    fail_step: str | None = None,
    actual_delay_min: int | None = None,
) -> list:
    """Pelny przeplyw osiemnastu nodes, w kolejnosci tablicy.

    Parametry ida do czterech nodes, ktore reprezentuja wejscie z zewnatrz:
    zaklocenie (04), decyzje czlowieka (15), przebieg wykonania (15b)
    i rzeczywisty wynik (17). Reszta liczy sie sama ze snapshotu.
    """
    return [
        SnapshotNode(weekday=weekday, seed=seed),
        WalidacjaNode(),
        BaselineNode(),
        ZaklocenieNode(flight_id=flight_id, delay_min=delay_min, delay_code=delay_code),
        FeasibilityNode(),
        ZasobyNode(),
        ScenariuszeNode(),
        RevenueNode(),
        KosztNode(),
        SiecNode(),
        OptymalizacjaNode(),
        FiltrPrawnyNode(),
        WrazliwoscNode(),
        AiReasoningNode(),
        PracownikNode(decision=decision, chosen_option=chosen_option,
                      reason_code=reason_code),
        WykonanieNode(fail_step=fail_step),
        LogNode(),
        WynikNode(actual_delay_min=actual_delay_min),
    ]


__all__ = [
    "NODE_CLASSES",
    "AiReasoningNode",
    "BaselineNode",
    "Decision",
    "FeasibilityNode",
    "FiltrPrawnyNode",
    "KosztNode",
    "LogNode",
    "OptymalizacjaNode",
    "PracownikNode",
    "RevenueNode",
    "ScenariuszeNode",
    "SiecNode",
    "SnapshotNode",
    "WalidacjaNode",
    "WrazliwoscNode",
    "WykonanieNode",
    "WynikNode",
    "ZaklocenieNode",
    "ZasobyNode",
    "build_pipeline",
]
