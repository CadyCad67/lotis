# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **4.75 ms**

Policzono przychod 7 opcji. Najmniej traci `HOLD` (0.00 PLN), najwiecej `CANCEL` (650979.82 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 7 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 650979.82 PLN | PLN |
| `baseline_doby` | 29220703.02 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **revenue_opcji**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 281
  - **SWAP-SP-LRD**
    - **baseline_dotknietych**
      - **minor:** 120 789 712
      - **currency:** PLN
      - **major:** 1207897.12
    - **revenue_opcji**
      - **minor:** 115 267 510
      - **currency:** PLN
      - **major:** 1152675.10
    - **revenue_at_risk**
      - **minor:** 5 522 202
      - **currency:** PLN
      - **major:** 55222.02
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 281
  - **SWAP-SP-LRG**
    - **baseline_dotknietych**
      - **minor:** 110 279 276
      - **currency:** PLN
      - **major:** 1102792.76
    - **revenue_opcji**
      - **minor:** 104 757 074
      - **currency:** PLN
      - **major:** 1047570.74
    - **revenue_at_risk**
      - **minor:** 5 522 202
      - **currency:** PLN
      - **major:** 55222.02
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 281
  - **SWAP-SP-LSC**
    - **baseline_dotknietych**
      - **minor:** 127 532 537
      - **currency:** PLN
      - **major:** 1275325.37
    - **revenue_opcji**
      - **minor:** 127 532 537
      - **currency:** PLN
      - **major:** 1275325.37
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 281
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **revenue_opcji**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 281
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **revenue_opcji**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 281
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **zwroty**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **pasazerow:** 281
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
