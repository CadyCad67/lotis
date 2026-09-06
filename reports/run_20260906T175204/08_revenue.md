# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T175204` · **snapshot:** `sha256:91cb2a4af61a3714` · **3.99 ms**

Policzono przychod 6 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (522331.96 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 6 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 522331.96 PLN | PLN |
| `baseline_doby` | 30254879.34 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **revenue_opcji**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 241
  - **SWAP-SP-LSB**
    - **baseline_dotknietych**
      - **minor:** 109 247 334
      - **currency:** PLN
      - **major:** 1092473.34
    - **revenue_opcji**
      - **minor:** 109 247 334
      - **currency:** PLN
      - **major:** 1092473.34
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 241
  - **SWAP-SP-LSG**
    - **baseline_dotknietych**
      - **minor:** 109 679 521
      - **currency:** PLN
      - **major:** 1096795.21
    - **revenue_opcji**
      - **minor:** 109 679 521
      - **currency:** PLN
      - **major:** 1096795.21
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 241
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **revenue_opcji**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 241
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **revenue_opcji**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 241
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **zwroty**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **pasazerow:** 241
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
