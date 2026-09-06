# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T191046` · **snapshot:** `sha256:f3c290f4e6930407` · **3.89 ms**

Policzono przychod 4 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (620518.87 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 4 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 620518.87 PLN | PLN |
| `baseline_doby` | 30490348.49 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **revenue_opcji**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 258
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **revenue_opcji**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 258
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **revenue_opcji**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 258
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **zwroty**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **pasazerow:** 258
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
