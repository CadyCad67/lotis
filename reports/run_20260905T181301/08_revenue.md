# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260905T181301` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **2.85 ms**

Policzono przychod 6 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (12898.65 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 6 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 12898.65 PLN | PLN |
| `baseline_doby` | 27314843.25 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 1 152 756
      - **currency:** PLN
      - **major:** 11527.56
    - **revenue_opcji**
      - **minor:** 1 152 756
      - **currency:** PLN
      - **major:** 11527.56
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 55
  - **REBOOK-OWN**
    - **baseline_dotknietych**
      - **minor:** 2 524 247
      - **currency:** PLN
      - **major:** 25242.47
    - **revenue_opcji**
      - **minor:** 2 524 247
      - **currency:** PLN
      - **major:** 25242.47
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 55
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 1 152 756
      - **currency:** PLN
      - **major:** 11527.56
    - **revenue_opcji**
      - **minor:** 1 152 756
      - **currency:** PLN
      - **major:** 11527.56
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 55
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 1 152 756
      - **currency:** PLN
      - **major:** 11527.56
    - **revenue_opcji**
      - **minor:** 1 152 756
      - **currency:** PLN
      - **major:** 11527.56
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 55
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 1 152 756
      - **currency:** PLN
      - **major:** 11527.56
    - **revenue_opcji**
      - **minor:** -137 109
      - **currency:** PLN
      - **major:** -1371.09
    - **revenue_at_risk**
      - **minor:** 1 289 865
      - **currency:** PLN
      - **major:** 12898.65
    - **zwroty**
      - **minor:** 1 289 865
      - **currency:** PLN
      - **major:** 12898.65
    - **pasazerow:** 55
  - **SPLIT**
    - **baseline_dotknietych**
      - **minor:** 2 524 247
      - **currency:** PLN
      - **major:** 25242.47
    - **revenue_opcji**
      - **minor:** 2 524 247
      - **currency:** PLN
      - **major:** 25242.47
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 55
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
