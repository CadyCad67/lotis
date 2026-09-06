# [09] COST ENGINE

**Status:** ok · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **18.2 ms**

Wyceniono 7 opcji. Kategoria EU261: C (2580.00 PLN na pasazera), prog opieki 240 min, p(odszkodowanie) = 1.0. Najtansza `HOLD` (0.00 PLN), najdrozsza `REBOOK-OAL` (2026985.60 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | C | - |
| `odszkodowanie_na_pasazera` | 2580.00 PLN | PLN |
| `prog_opieki` | 240 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 0.00 PLN | PLN |
| `koszt_najdrozszej` | 2026985.60 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 240 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **najwieksze:** -
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LRC**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 8 799 268
      - **currency:** PLN
      - **major:** 87992.68
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 9 695 806
        - **currency:** PLN
        - **major:** 96958.06
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 1 032 000
        - **currency:** PLN
        - **major:** 10320.00
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 719 892
        - **currency:** PLN
        - **major:** 7198.92
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LRD**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 11 791 013
      - **currency:** PLN
      - **major:** 117910.13
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 9 695 806
        - **currency:** PLN
        - **major:** 96958.06
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 1 032 000
        - **currency:** PLN
        - **major:** 10320.00
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 719 892
        - **currency:** PLN
        - **major:** 7198.92
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LRH**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 9 976 348
      - **currency:** PLN
      - **major:** 99763.48
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 9 695 806
        - **currency:** PLN
        - **major:** 96958.06
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 1 032 000
        - **currency:** PLN
        - **major:** 10320.00
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 719 892
        - **currency:** PLN
        - **major:** 7198.92
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 202 698 560
      - **currency:** PLN
      - **major:** 2026985.60
    - **najwieksze**
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 100 172 800
        - **currency:** PLN
        - **major:** 1001728.00
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 66 048 000
        - **currency:** PLN
        - **major:** 660480.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 34 056 000
        - **currency:** PLN
        - **major:** 340560.00
    - **pasazerow_z_odszkodowaniem:** 256
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 137 306 246
      - **currency:** PLN
      - **major:** 1373062.46
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 66 048 000
        - **currency:** PLN
        - **major:** 660480.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 34 056 000
        - **currency:** PLN
        - **major:** 340560.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 25 043 200
        - **currency:** PLN
        - **major:** 250432.00
    - **pasazerow_z_odszkodowaniem:** 256
    - **noclegow:** 256
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 112 908 046
      - **currency:** PLN
      - **major:** 1129080.46
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 66 048 000
        - **currency:** PLN
        - **major:** 660480.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 34 056 000
        - **currency:** PLN
        - **major:** 340560.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 11 709 696
        - **currency:** PLN
        - **major:** 117096.96
    - **pasazerow_z_odszkodowaniem:** 256
    - **noclegow:** 256
- **tryby_liczenia**
  - **MODIFYING:** roznica wobec sytuacji bez zaklocenia
  - **RESTRUCTURING:** pelny nowy zestaw kosztow minus stary

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |
| `stawki K.care` | policy | 0.60 | estimate |
| `stawki K.reb` | policy | 0.60 | estimate |
| `stawki K.crew` | policy | 0.60 | estimate |
| `stawki K.grd` | policy | 0.60 | estimate |
| `stawki K.cxl` | policy | 0.60 | estimate |
| `stawki K.div` | policy | 0.60 | estimate |
| `stawki K.mc99` | policy | 0.60 | estimate |

## Braki danych

- odsetek ochotnikow przy odmowie przyjecia (PoC) nie jest w bazie -- opcje z offloadem liczone sciezka 'wbrew woli', czyli najdrozsza

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
