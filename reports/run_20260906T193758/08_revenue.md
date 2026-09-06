# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T193758` · **snapshot:** `sha256:6c790f69f87c3591` · **4.66 ms**

Policzono przychod 8 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (544059.74 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 8 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 544059.74 PLN | PLN |
| `baseline_doby` | 30084400.12 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **revenue_opcji**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 272
  - **SWAP-SP-LSA**
    - **baseline_dotknietych**
      - **minor:** 97 394 991
      - **currency:** PLN
      - **major:** 973949.91
    - **revenue_opcji**
      - **minor:** 97 394 991
      - **currency:** PLN
      - **major:** 973949.91
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 272
  - **SWAP-SP-LSE**
    - **baseline_dotknietych**
      - **minor:** 115 780 951
      - **currency:** PLN
      - **major:** 1157809.51
    - **revenue_opcji**
      - **minor:** 115 780 951
      - **currency:** PLN
      - **major:** 1157809.51
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 272
  - **REBOOK-OWN**
    - **baseline_dotknietych**
      - **minor:** 107 327 690
      - **currency:** PLN
      - **major:** 1073276.90
    - **revenue_opcji**
      - **minor:** 107 327 690
      - **currency:** PLN
      - **major:** 1073276.90
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 272
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **revenue_opcji**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 272
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **revenue_opcji**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 272
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **zwroty**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **pasazerow:** 272
  - **SPLIT**
    - **baseline_dotknietych**
      - **minor:** 107 327 690
      - **currency:** PLN
      - **major:** 1073276.90
    - **revenue_opcji**
      - **minor:** 107 327 690
      - **currency:** PLN
      - **major:** 1073276.90
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 272
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
