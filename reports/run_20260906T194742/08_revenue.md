# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T194742` · **snapshot:** `sha256:6c790f69f87c3591` · **1.58 ms**

Policzono przychod 9 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (27241.41 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 9 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 27241.41 PLN | PLN |
| `baseline_doby` | 30084400.12 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **revenue_opcji**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 79
  - **SWAP-SP-LIC**
    - **baseline_dotknietych**
      - **minor:** 5 274 850
      - **currency:** PLN
      - **major:** 52748.50
    - **revenue_opcji**
      - **minor:** 5 274 850
      - **currency:** PLN
      - **major:** 52748.50
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 79
  - **SWAP-SP-LID**
    - **baseline_dotknietych**
      - **minor:** 5 613 682
      - **currency:** PLN
      - **major:** 56136.82
    - **revenue_opcji**
      - **minor:** 5 613 682
      - **currency:** PLN
      - **major:** 56136.82
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 79
  - **SWAP-SP-LII**
    - **baseline_dotknietych**
      - **minor:** 4 131 480
      - **currency:** PLN
      - **major:** 41314.80
    - **revenue_opcji**
      - **minor:** 4 131 480
      - **currency:** PLN
      - **major:** 41314.80
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 79
  - **REBOOK-OWN**
    - **baseline_dotknietych**
      - **minor:** 5 924 058
      - **currency:** PLN
      - **major:** 59240.58
    - **revenue_opcji**
      - **minor:** 5 924 058
      - **currency:** PLN
      - **major:** 59240.58
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 79
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **revenue_opcji**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 79
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **revenue_opcji**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 79
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **zwroty**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **pasazerow:** 79
  - **SPLIT**
    - **baseline_dotknietych**
      - **minor:** 5 924 058
      - **currency:** PLN
      - **major:** 59240.58
    - **revenue_opcji**
      - **minor:** 5 924 058
      - **currency:** PLN
      - **major:** 59240.58
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 79
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
