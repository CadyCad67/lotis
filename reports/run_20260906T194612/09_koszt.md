# [09] COST ENGINE

**Status:** ok · **run:** `20260906T194612` · **snapshot:** `sha256:6c790f69f87c3591` · **6.98 ms**

Wyceniono 10 opcji. Kategoria EU261: A (1075.00 PLN na pasazera), prog opieki 120 min, p(odszkodowanie) = 1.0. Najtansza `HOLD` (16197.90 PLN), najdrozsza `REBOOK-OAL` (177835.96 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | A | - |
| `odszkodowanie_na_pasazera` | 1075.00 PLN | PLN |
| `prog_opieki` | 120 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 16197.90 PLN | PLN |
| `koszt_najdrozszej` | 177835.96 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 120 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 1 619 790
      - **currency:** PLN
      - **major:** 16197.90
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 1 174 740
        - **currency:** PLN
        - **major:** 11747.40
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 322 500
        - **currency:** PLN
        - **major:** 3225.00
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 122 550
        - **currency:** PLN
        - **major:** 1225.50
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **REBOOK-SPILL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 1 982 151
      - **currency:** PLN
      - **major:** 19821.51
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 1 174 740
        - **currency:** PLN
        - **major:** 11747.40
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 322 500
        - **currency:** PLN
        - **major:** 3225.00
      - **pozycja:** roszczenia_mc99
      - **kwota**
        - **minor:** 266 256
        - **currency:** PLN
        - **major:** 2662.56
    - **pasazerow_z_odszkodowaniem:** 3
    - **noclegow:** 0
  - **SWAP-SP-LIC**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 1 895 496
      - **currency:** PLN
      - **major:** 18954.96
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 1 707 299
        - **currency:** PLN
        - **major:** 17072.99
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 255 742
        - **currency:** PLN
        - **major:** 2557.42
      - **pozycja:** roznica_kosztu_typu
      - **kwota**
        - **minor:** -67 545
        - **currency:** PLN
        - **major:** -675.45
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LID**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 1 940 526
      - **currency:** PLN
      - **major:** 19405.26
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 1 707 299
        - **currency:** PLN
        - **major:** 17072.99
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 255 742
        - **currency:** PLN
        - **major:** 2557.42
      - **pozycja:** roznica_kosztu_typu
      - **kwota**
        - **minor:** -22 515
        - **currency:** PLN
        - **major:** -225.15
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LII**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 1 760 406
      - **currency:** PLN
      - **major:** 17604.06
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 1 707 299
        - **currency:** PLN
        - **major:** 17072.99
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 255 742
        - **currency:** PLN
        - **major:** 2557.42
      - **pozycja:** roznica_kosztu_typu
      - **kwota**
        - **minor:** -202 635
        - **currency:** PLN
        - **major:** -2026.35
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 12 433 321
      - **currency:** PLN
      - **major:** 124333.21
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 492 500
        - **currency:** PLN
        - **major:** 84925.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 1 783 425
        - **currency:** PLN
        - **major:** 17834.25
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 143 800
        - **currency:** PLN
        - **major:** 11438.00
    - **pasazerow_z_odszkodowaniem:** 79
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 17 783 596
      - **currency:** PLN
      - **major:** 177835.96
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 492 500
        - **currency:** PLN
        - **major:** 84925.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 7 133 700
        - **currency:** PLN
        - **major:** 71337.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 143 800
        - **currency:** PLN
        - **major:** 11438.00
    - **pasazerow_z_odszkodowaniem:** 79
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 15 503 770
      - **currency:** PLN
      - **major:** 155037.70
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 492 500
        - **currency:** PLN
        - **major:** 84925.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 3 613 539
        - **currency:** PLN
        - **major:** 36135.39
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 1 783 425
        - **currency:** PLN
        - **major:** 17834.25
    - **pasazerow_z_odszkodowaniem:** 79
    - **noclegow:** 79
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 11 294 896
      - **currency:** PLN
      - **major:** 112948.96
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 492 500
        - **currency:** PLN
        - **major:** 84925.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 143 800
        - **currency:** PLN
        - **major:** 11438.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 747 340
        - **currency:** PLN
        - **major:** 7473.40
    - **pasazerow_z_odszkodowaniem:** 79
    - **noclegow:** 0
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 15 142 321
      - **currency:** PLN
      - **major:** 151423.21
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 492 500
        - **currency:** PLN
        - **major:** 84925.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 3 612 000
        - **currency:** PLN
        - **major:** 36120.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 1 143 800
        - **currency:** PLN
        - **major:** 11438.00
    - **pasazerow_z_odszkodowaniem:** 79
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
