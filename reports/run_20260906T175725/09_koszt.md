# [09] COST ENGINE

**Status:** ok · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **17.32 ms**

Wyceniono 6 opcji. Kategoria EU261: C (2580.00 PLN na pasazera), prog opieki 240 min, p(odszkodowanie) = 0.5. Najtansza `HOLD` (19166.00 PLN), najdrozsza `REBOOK-OAL` (1284385.92 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | C | - |
| `odszkodowanie_na_pasazera` | 2580.00 PLN | PLN |
| `prog_opieki` | 240 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 0.50 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 19166.00 PLN | PLN |
| `koszt_najdrozszej` | 1284385.92 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 240 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 0.5
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 1 916 600
      - **currency:** PLN
      - **major:** 19166.00
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 1 798 350
        - **currency:** PLN
        - **major:** 17983.50
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 118 250
        - **currency:** PLN
        - **major:** 1182.50
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LSB**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 9 138 542
      - **currency:** PLN
      - **major:** 91385.42
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 10 245 140
        - **currency:** PLN
        - **major:** 102451.40
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 708 067
        - **currency:** PLN
        - **major:** 7080.67
      - **pozycja:** roznica_kosztu_typu
      - **kwota**
        - **minor:** -1 814 665
        - **currency:** PLN
        - **major:** -18146.65
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LSG**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 10 021 352
      - **currency:** PLN
      - **major:** 100213.52
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 10 245 140
        - **currency:** PLN
        - **major:** 102451.40
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 708 067
        - **currency:** PLN
        - **major:** 7080.67
      - **pozycja:** roznica_kosztu_typu
      - **kwota**
        - **minor:** -931 855
        - **currency:** PLN
        - **major:** -9318.55
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 128 438 592
      - **currency:** PLN
      - **major:** 1284385.92
    - **najwieksze**
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 67 359 500
        - **currency:** PLN
        - **major:** 673595.00
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 31 089 000
        - **currency:** PLN
        - **major:** 310890.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
    - **pasazerow_z_odszkodowaniem:** 241
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 93 847 988
      - **currency:** PLN
      - **major:** 938479.88
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 31 089 000
        - **currency:** PLN
        - **major:** 310890.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 23 575 825
        - **currency:** PLN
        - **major:** 235758.25
    - **pasazerow_z_odszkodowaniem:** 241
    - **noclegow:** 241
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 70 917 163
      - **currency:** PLN
      - **major:** 709171.63
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 31 089 000
        - **currency:** PLN
        - **major:** 310890.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 11 023 581
        - **currency:** PLN
        - **major:** 110235.81
    - **pasazerow_z_odszkodowaniem:** 241
    - **noclegow:** 241
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
