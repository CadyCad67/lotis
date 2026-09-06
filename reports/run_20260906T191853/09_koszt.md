# [09] COST ENGINE

**Status:** ok · **run:** `20260906T191853` · **snapshot:** `sha256:f3c290f4e6930407` · **17.27 ms**

Wyceniono 6 opcji. Kategoria EU261: C (2580.00 PLN na pasazera), prog opieki 240 min, p(odszkodowanie) = 1.0. Najtansza `HOLD` (27339.13 PLN), najdrozsza `REBOOK-OAL` (1601240.88 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | C | - |
| `odszkodowanie_na_pasazera` | 2580.00 PLN | PLN |
| `prog_opieki` | 240 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 27339.13 PLN | PLN |
| `koszt_najdrozszej` | 1601240.88 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 240 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 2 733 913
      - **currency:** PLN
      - **major:** 27339.13
    - **najwieksze**
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 1 806 000
        - **currency:** PLN
        - **major:** 18060.00
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 849 080
        - **currency:** PLN
        - **major:** 8490.80
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 78 833
        - **currency:** PLN
        - **major:** 788.33
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LRF**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 9 709 667
      - **currency:** PLN
      - **major:** 97096.67
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 9 001 600
        - **currency:** PLN
        - **major:** 90016.00
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 708 067
        - **currency:** PLN
        - **major:** 7080.67
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LSC**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 8 033 942
      - **currency:** PLN
      - **major:** 80339.42
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 9 140 540
        - **currency:** PLN
        - **major:** 91405.40
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
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 160 124 088
      - **currency:** PLN
      - **major:** 1601240.88
    - **najwieksze**
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 67 639 000
        - **currency:** PLN
        - **major:** 676390.00
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 62 436 000
        - **currency:** PLN
        - **major:** 624360.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
    - **pasazerow_z_odszkodowaniem:** 242
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 125 388 090
      - **currency:** PLN
      - **major:** 1253880.90
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 62 436 000
        - **currency:** PLN
        - **major:** 624360.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 23 673 650
        - **currency:** PLN
        - **major:** 236736.50
    - **pasazerow_z_odszkodowaniem:** 242
    - **noclegow:** 242
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 102 359 440
      - **currency:** PLN
      - **major:** 1023594.40
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 62 436 000
        - **currency:** PLN
        - **major:** 624360.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 11 069 322
        - **currency:** PLN
        - **major:** 110693.22
    - **pasazerow_z_odszkodowaniem:** 242
    - **noclegow:** 242
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
