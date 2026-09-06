# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T192747` · **snapshot:** `sha256:f3c290f4e6930407` · **1.94 ms**

Policzono przychod 10 opcji. Najmniej traci `REBOOK-SPILL` (0.00 PLN), najwiecej `CANCEL` (23944.56 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 10 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 23944.56 PLN | PLN |
| `baseline_doby` | 30490348.49 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 2 394 456
      - **currency:** PLN
      - **major:** 23944.56
    - **revenue_opcji**
      - **minor:** 2 232 593
      - **currency:** PLN
      - **major:** 22325.93
    - **revenue_at_risk**
      - **minor:** 161 863
      - **currency:** PLN
      - **major:** 1618.63
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **REBOOK-SPILL**
    - **baseline_dotknietych**
      - **minor:** 3 821 155
      - **currency:** PLN
      - **major:** 38211.55
    - **revenue_opcji**
      - **minor:** 3 821 155
      - **currency:** PLN
      - **major:** 38211.55
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
      - **minor:** 3 444 913
      - **currency:** PLN
      - **major:** 34449.13
    - **revenue_opcji**
      - **minor:** 3 324 157
      - **currency:** PLN
      - **major:** 33241.57
    - **revenue_at_risk**
      - **minor:** 120 756
      - **currency:** PLN
      - **major:** 1207.56
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **SWAP-SP-LIC**
    - **baseline_dotknietych**
      - **minor:** 3 242 181
      - **currency:** PLN
      - **major:** 32421.81
    - **revenue_opcji**
      - **minor:** 3 242 181
      - **currency:** PLN
      - **major:** 32421.81
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **SWAP-SP-LIO**
    - **baseline_dotknietych**
      - **minor:** 5 454 187
      - **currency:** PLN
      - **major:** 54541.87
    - **revenue_opcji**
      - **minor:** 5 454 187
      - **currency:** PLN
      - **major:** 54541.87
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 82
  - **REBOOK-OWN**
    - **baseline_dotknietych**
      - **minor:** 3 821 155
      - **currency:** PLN
      - **major:** 38211.55
    - **revenue_opcji**
      - **minor:** 3 821 155
      - **currency:** PLN
      - **major:** 38211.55
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
      - **minor:** 2 394 456
      - **currency:** PLN
      - **major:** 23944.56
    - **revenue_opcji**
      - **minor:** 2 394 456
      - **currency:** PLN
      - **major:** 23944.56
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
      - **minor:** 2 394 456
      - **currency:** PLN
      - **major:** 23944.56
    - **revenue_opcji**
      - **minor:** 2 394 456
      - **currency:** PLN
      - **major:** 23944.56
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
      - **minor:** 2 394 456
      - **currency:** PLN
      - **major:** 23944.56
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 2 394 456
      - **currency:** PLN
      - **major:** 23944.56
    - **zwroty**
      - **minor:** 2 394 456
      - **currency:** PLN
      - **major:** 23944.56
    - **pasazerow:** 82
  - **SPLIT**
    - **baseline_dotknietych**
      - **minor:** 3 821 155
      - **currency:** PLN
      - **major:** 38211.55
    - **revenue_opcji**
      - **minor:** 3 821 155
      - **currency:** PLN
      - **major:** 38211.55
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
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
