# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T190327` · **snapshot:** `sha256:f3c290f4e6930407` · **1.73 ms**

Policzono przychod 7 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (17416.03 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 7 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 17416.03 PLN | PLN |
| `baseline_doby` | 30490348.49 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **revenue_opcji**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **SWAP-SP-LDH**
    - **baseline_dotknietych**
      - **minor:** 2 792 060
      - **currency:** PLN
      - **major:** 27920.60
    - **revenue_opcji**
      - **minor:** 2 666 687
      - **currency:** PLN
      - **major:** 26666.87
    - **revenue_at_risk**
      - **minor:** 125 373
      - **currency:** PLN
      - **major:** 1253.73
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **SWAP-SP-LIO**
    - **baseline_dotknietych**
      - **minor:** 4 801 334
      - **currency:** PLN
      - **major:** 48013.34
    - **revenue_opcji**
      - **minor:** 4 801 334
      - **currency:** PLN
      - **major:** 48013.34
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **SWAP-SP-LIQ**
    - **baseline_dotknietych**
      - **minor:** 4 268 973
      - **currency:** PLN
      - **major:** 42689.73
    - **revenue_opcji**
      - **minor:** 4 268 973
      - **currency:** PLN
      - **major:** 42689.73
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **revenue_opcji**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **revenue_opcji**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **zwroty**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **pasazerow:** 82
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
