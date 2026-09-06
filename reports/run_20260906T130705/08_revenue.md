# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T130705` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **1.03 ms**

Policzono przychod 9 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (22343.02 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 9 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 22343.02 PLN | PLN |
| `baseline_doby` | 27314843.25 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **revenue_opcji**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 52
  - **SWAP-SP-LDH**
    - **baseline_dotknietych**
      - **minor:** 5 217 758
      - **currency:** PLN
      - **major:** 52177.58
    - **revenue_opcji**
      - **minor:** 5 217 758
      - **currency:** PLN
      - **major:** 52177.58
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 52
  - **SWAP-SP-LIK**
    - **baseline_dotknietych**
      - **minor:** 3 395 688
      - **currency:** PLN
      - **major:** 33956.88
    - **revenue_opcji**
      - **minor:** 3 395 688
      - **currency:** PLN
      - **major:** 33956.88
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 52
  - **SWAP-SP-LIL**
    - **baseline_dotknietych**
      - **minor:** 4 636 239
      - **currency:** PLN
      - **major:** 46362.39
    - **revenue_opcji**
      - **minor:** 4 636 239
      - **currency:** PLN
      - **major:** 46362.39
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 52
  - **REBOOK-OWN**
    - **baseline_dotknietych**
      - **minor:** 6 958 509
      - **currency:** PLN
      - **major:** 69585.09
    - **revenue_opcji**
      - **minor:** 6 958 509
      - **currency:** PLN
      - **major:** 69585.09
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 52
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **revenue_opcji**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 52
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **revenue_opcji**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 52
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **zwroty**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **pasazerow:** 52
  - **SPLIT**
    - **baseline_dotknietych**
      - **minor:** 6 958 509
      - **currency:** PLN
      - **major:** 69585.09
    - **revenue_opcji**
      - **minor:** 6 958 509
      - **currency:** PLN
      - **major:** 69585.09
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 52
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
