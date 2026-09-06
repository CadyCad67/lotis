# [09] COST ENGINE

**Status:** ok · **run:** `20260906T130705` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **5.53 ms**

Wyceniono 9 opcji. Kategoria EU261: A (1075.00 PLN na pasazera), prog opieki 120 min, p(odszkodowanie) = 0.5. Najtansza `SWAP-SP-LDH` (32432.71 PLN), najdrozsza `REBOOK-OAL` (84255.92 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | A | - |
| `odszkodowanie_na_pasazera` | 1075.00 PLN | PLN |
| `prog_opieki` | 120 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 0.50 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 32432.71 PLN | PLN |
| `koszt_najdrozszej` | 84255.92 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 120 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 0.5
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 6 243 292
      - **currency:** PLN
      - **major:** 62432.92
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 2 795 000
        - **currency:** PLN
        - **major:** 27950.00
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 2 713 680
        - **currency:** PLN
        - **major:** 27136.80
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 322 500
        - **currency:** PLN
        - **major:** 3225.00
    - **pasazerow_z_odszkodowaniem:** 52
    - **noclegow:** 0
  - **SWAP-SP-LDH**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 3 243 271
      - **currency:** PLN
      - **major:** 32432.71
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 3 080 196
        - **currency:** PLN
        - **major:** 30801.96
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 236 500
        - **currency:** PLN
        - **major:** 2365.00
      - **pozycja:** roznica_kosztu_typu
      - **kwota**
        - **minor:** -73 425
        - **currency:** PLN
        - **major:** -734.25
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LIK**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 3 492 916
      - **currency:** PLN
      - **major:** 34929.16
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 3 256 416
        - **currency:** PLN
        - **major:** 32564.16
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 236 500
        - **currency:** PLN
        - **major:** 2365.00
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LIL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 3 492 916
      - **currency:** PLN
      - **major:** 34929.16
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 3 256 416
        - **currency:** PLN
        - **major:** 32564.16
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 236 500
        - **currency:** PLN
        - **major:** 2365.00
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 6 245 492
      - **currency:** PLN
      - **major:** 62454.92
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 2 795 000
        - **currency:** PLN
        - **major:** 27950.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 685 600
        - **currency:** PLN
        - **major:** 16856.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 1 173 900
        - **currency:** PLN
        - **major:** 11739.00
    - **pasazerow_z_odszkodowaniem:** 52
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 8 425 592
      - **currency:** PLN
      - **major:** 84255.92
    - **najwieksze**
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 3 354 000
        - **currency:** PLN
        - **major:** 33540.00
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 2 795 000
        - **currency:** PLN
        - **major:** 27950.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 685 600
        - **currency:** PLN
        - **major:** 16856.00
    - **pasazerow_z_odszkodowaniem:** 52
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 8 295 504
      - **currency:** PLN
      - **major:** 82955.04
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 2 795 000
        - **currency:** PLN
        - **major:** 27950.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 2 378 532
        - **currency:** PLN
        - **major:** 23785.32
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 685 600
        - **currency:** PLN
        - **major:** 16856.00
    - **pasazerow_z_odszkodowaniem:** 52
    - **noclegow:** 52
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 5 716 592
      - **currency:** PLN
      - **major:** 57165.92
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 2 795 000
        - **currency:** PLN
        - **major:** 27950.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 685 600
        - **currency:** PLN
        - **major:** 16856.00
      - **pozycja:** ryzyko_serii_slotow
      - **kwota**
        - **minor:** 645 000
        - **currency:** PLN
        - **major:** 6450.00
    - **pasazerow_z_odszkodowaniem:** 52
    - **noclegow:** 0
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 7 335 542
      - **currency:** PLN
      - **major:** 73355.42
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 2 795 000
        - **currency:** PLN
        - **major:** 27950.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 685 600
        - **currency:** PLN
        - **major:** 16856.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 1 677 000
        - **currency:** PLN
        - **major:** 16770.00
    - **pasazerow_z_odszkodowaniem:** 52
    - **noclegow:** 0
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
