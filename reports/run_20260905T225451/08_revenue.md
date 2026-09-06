# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260905T225451` · **snapshot:** `sha256:f3c290f4e6930407` · **1.12 ms**

Policzono przychod 6 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (11541.08 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 6 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 11541.08 PLN | PLN |
| `baseline_doby` | 30490348.49 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **revenue_opcji**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 61
  - **REBOOK-OWN**
    - **baseline_dotknietych**
      - **minor:** 1 864 710
      - **currency:** PLN
      - **major:** 18647.10
    - **revenue_opcji**
      - **minor:** 1 864 710
      - **currency:** PLN
      - **major:** 18647.10
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 61
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **revenue_opcji**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 61
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **revenue_opcji**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 61
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **zwroty**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **pasazerow:** 61
  - **SPLIT**
    - **baseline_dotknietych**
      - **minor:** 1 864 710
      - **currency:** PLN
      - **major:** 18647.10
    - **revenue_opcji**
      - **minor:** 1 864 710
      - **currency:** PLN
      - **major:** 18647.10
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 61
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
