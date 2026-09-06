# [09] COST ENGINE

**Status:** ok · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **20.44 ms**

Wyceniono 7 opcji. Kategoria EU261: C (2580.00 PLN na pasazera), prog opieki 240 min, p(odszkodowanie) = 1.0. Najtansza `HOLD` (22108.70 PLN), najdrozsza `REBOOK-OAL` (2200256.68 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | C | - |
| `odszkodowanie_na_pasazera` | 2580.00 PLN | PLN |
| `prog_opieki` | 240 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 22108.70 PLN | PLN |
| `koszt_najdrozszej` | 2200256.68 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 240 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 2 210 870
      - **currency:** PLN
      - **major:** 22108.70
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 2 092 620
        - **currency:** PLN
        - **major:** 20926.20
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 118 250
        - **currency:** PLN
        - **major:** 1182.50
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LRD**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 16 900 483
      - **currency:** PLN
      - **major:** 169004.83
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 11 494 156
        - **currency:** PLN
        - **major:** 114941.56
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 7 482 000
        - **currency:** PLN
        - **major:** 74820.00
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 719 892
        - **currency:** PLN
        - **major:** 7198.92
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LRG**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 19 892 228
      - **currency:** PLN
      - **major:** 198922.28
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 11 494 156
        - **currency:** PLN
        - **major:** 114941.56
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 7 482 000
        - **currency:** PLN
        - **major:** 74820.00
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 719 892
        - **currency:** PLN
        - **major:** 7198.92
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LSC**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 12 508 318
      - **currency:** PLN
      - **major:** 125083.18
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 11 788 426
        - **currency:** PLN
        - **major:** 117884.26
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
      - **minor:** 220 025 668
      - **currency:** PLN
      - **major:** 2200256.68
    - **najwieksze**
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 109 955 300
        - **currency:** PLN
        - **major:** 1099553.00
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 72 498 000
        - **currency:** PLN
        - **major:** 724980.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 34 765 500
        - **currency:** PLN
        - **major:** 347655.00
    - **pasazerow_z_odszkodowaniem:** 281
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 148 203 504
      - **currency:** PLN
      - **major:** 1482035.04
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 72 498 000
        - **currency:** PLN
        - **major:** 724980.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 34 765 500
        - **currency:** PLN
        - **major:** 347655.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 27 488 825
        - **currency:** PLN
        - **major:** 274888.25
    - **pasazerow_z_odszkodowaniem:** 281
    - **noclegow:** 281
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 121 359 679
      - **currency:** PLN
      - **major:** 1213596.79
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 72 498 000
        - **currency:** PLN
        - **major:** 724980.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 34 765 500
        - **currency:** PLN
        - **major:** 347655.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 12 853 221
        - **currency:** PLN
        - **major:** 128532.21
    - **pasazerow_z_odszkodowaniem:** 281
    - **noclegow:** 281
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
