# [08] REVENUE ENGINE

**Status:** ok · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **3.96 ms**

Policzono przychod 6 opcji. Najmniej traci `SWAP-SP-LRF` (0.00 PLN), najwiecej `CANCEL` (425734.81 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_wycenionych` | 6 | szt |
| `najmniejszy_revenue_at_risk` | 0.00 PLN | PLN |
| `najwiekszy_revenue_at_risk` | 425734.81 PLN | PLN |
| `baseline_doby` | 30490348.49 PLN | PLN |

## Co ten node ustalil

- rebooking na obcego przewoznika zachowuje przychod z biletu; rozliczenie interline jest kosztem, nie utrata przychodu
- revenue at risk to wynik odejmowania, nie osobna wielkosc

## Szczegoly

- **revenue_opcji**
  - **HOLD**
    - **baseline_dotknietych**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **revenue_opcji**
      - **minor:** 42 318 765
      - **currency:** PLN
      - **major:** 423187.65
    - **revenue_at_risk**
      - **minor:** 254 716
      - **currency:** PLN
      - **major:** 2547.16
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 242
  - **SWAP-SP-LRF**
    - **baseline_dotknietych**
      - **minor:** 93 397 199
      - **currency:** PLN
      - **major:** 933971.99
    - **revenue_opcji**
      - **minor:** 93 397 199
      - **currency:** PLN
      - **major:** 933971.99
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 242
  - **SWAP-SP-LSC**
    - **baseline_dotknietych**
      - **minor:** 97 273 623
      - **currency:** PLN
      - **major:** 972736.23
    - **revenue_opcji**
      - **minor:** 97 273 623
      - **currency:** PLN
      - **major:** 972736.23
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 242
  - **REBOOK-OAL**
    - **baseline_dotknietych**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **revenue_opcji**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 242
  - **OVERNIGHT**
    - **baseline_dotknietych**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **revenue_opcji**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **zwroty**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **pasazerow:** 242
  - **CANCEL**
    - **baseline_dotknietych**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **revenue_opcji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **revenue_at_risk**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **zwroty**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **pasazerow:** 242
- **zasada**
  - **revenue_at_risk:** baseline dotknietych rejsow minus revenue opcji
  - **rebooking_na_OAL:** zachowuje przychod, generuje koszt rozliczenia w node 09
  - **zwrot:** kasuje przychod w calosci

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
