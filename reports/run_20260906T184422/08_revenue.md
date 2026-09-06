# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **3.78 ms**

Policzono przychod 7 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (655600.25 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 7 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 655600.25 PLN | PLN |
| `baseline_doby` | 30287600.48 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **revenue_opcji**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 256
  - **SWAP-SP-LRC**
    - **baseline_dotknietych**
      - **minor:** 114 480 748
      - **currency:** PLN
      - **major:** 1144807.48
    - **revenue_opcji**
      - **minor:** 113 720 066
      - **currency:** PLN
      - **major:** 1137200.66
    - **revenue_at_risk**
      - **minor:** 760 682
      - **currency:** PLN
      - **major:** 7606.82
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 256
  - **SWAP-SP-LRD**
    - **baseline_dotknietych**
      - **minor:** 116 017 158
      - **currency:** PLN
      - **major:** 1160171.58
    - **revenue_opcji**
      - **minor:** 115 256 476
      - **currency:** PLN
      - **major:** 1152564.76
    - **revenue_at_risk**
      - **minor:** 760 682
      - **currency:** PLN
      - **major:** 7606.82
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 256
  - **SWAP-SP-LRH**
    - **baseline_dotknietych**
      - **minor:** 110 694 753
      - **currency:** PLN
      - **major:** 1106947.53
    - **revenue_opcji**
      - **minor:** 109 934 071
      - **currency:** PLN
      - **major:** 1099340.71
    - **revenue_at_risk**
      - **minor:** 760 682
      - **currency:** PLN
      - **major:** 7606.82
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 256
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **revenue_opcji**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 256
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **revenue_opcji**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 256
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **zwroty**
      - **minor:** 65 560 025
      - **currency:** PLN
      - **major:** 655600.25
    - **pasazerow:** 256
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
