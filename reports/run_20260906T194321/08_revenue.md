# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **3.5 ms**

Policzono przychod 4 opcji. Najmniej traci `REBOOK-OAL` (0.00 PLN), najwiecej `CANCEL` (693458.62 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 4 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 693458.62 PLN | PLN |
| `baseline_doby` | 30084400.12 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **revenue_opcji**
      - **minor:** 68 012 335
      - **currency:** PLN
      - **major:** 680123.35
    - **revenue_at_risk**
      - **minor:** 1 333 527
      - **currency:** PLN
      - **major:** 13335.27
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 227
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **revenue_opcji**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 227
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **revenue_opcji**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 227
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **zwroty**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **pasazerow:** 227
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
