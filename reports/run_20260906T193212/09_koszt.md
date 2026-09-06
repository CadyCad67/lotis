# [09] COST ENGINE

**Status:** ok · **run:** `20260906T193212` · **snapshot:** `sha256:6c790f69f87c3591` · **21.45 ms**

Wyceniono 9 opcji. Kategoria EU261: C (2580.00 PLN na pasazera), prog opieki 240 min, p(odszkodowanie) = 1.0. Najtansza `HOLD` (20640.00 PLN), najdrozsza `REBOOK-OAL` (1766319.60 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | C | - |
| `odszkodowanie_na_pasazera` | 2580.00 PLN | PLN |
| `prog_opieki` | 240 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 20640.00 PLN | PLN |
| `koszt_najdrozszej` | 1766319.60 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 240 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 2 064 000
      - **currency:** PLN
      - **major:** 20640.00
    - **najwieksze**
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 2 064 000
        - **currency:** PLN
        - **major:** 20640.00
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **REBOOK-SPILL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 3 820 120
      - **currency:** PLN
      - **major:** 38201.20
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 2 064 000
        - **currency:** PLN
        - **major:** 20640.00
      - **pozycja:** roszczenia_mc99
      - **kwota**
        - **minor:** 897 840
        - **currency:** PLN
        - **major:** 8978.40
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 782 600
        - **currency:** PLN
        - **major:** 7826.00
    - **pasazerow_z_odszkodowaniem:** 8
    - **noclegow:** 0
  - **SWAP-SP-LSA**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 10 415 698
      - **currency:** PLN
      - **major:** 104156.98
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 9 695 806
        - **currency:** PLN
        - **major:** 96958.06
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 719 892
        - **currency:** PLN
        - **major:** 7198.92
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LSE**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 10 415 698
      - **currency:** PLN
      - **major:** 104156.98
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 9 695 806
        - **currency:** PLN
        - **major:** 96958.06
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 719 892
        - **currency:** PLN
        - **major:** 7198.92
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 127 216 360
      - **currency:** PLN
      - **major:** 1272163.60
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 70 176 000
        - **currency:** PLN
        - **major:** 701760.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 26 608 400
        - **currency:** PLN
        - **major:** 266084.00
    - **pasazerow_z_odszkodowaniem:** 272
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 176 631 960
      - **currency:** PLN
      - **major:** 1766319.60
    - **najwieksze**
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 76 024 000
        - **currency:** PLN
        - **major:** 760240.00
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 70 176 000
        - **currency:** PLN
        - **major:** 701760.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
    - **pasazerow_z_odszkodowaniem:** 272
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 137 534 142
      - **currency:** PLN
      - **major:** 1375341.42
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 70 176 000
        - **currency:** PLN
        - **major:** 701760.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 26 608 400
        - **currency:** PLN
        - **major:** 266084.00
    - **pasazerow_z_odszkodowaniem:** 272
    - **noclegow:** 272
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 101 252 960
      - **currency:** PLN
      - **major:** 1012529.60
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 70 176 000
        - **currency:** PLN
        - **major:** 701760.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 2 573 120
        - **currency:** PLN
        - **major:** 25731.20
    - **pasazerow_z_odszkodowaniem:** 272
    - **noclegow:** 0
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 151 924 160
      - **currency:** PLN
      - **major:** 1519241.60
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 70 176 000
        - **currency:** PLN
        - **major:** 701760.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 38 012 000
        - **currency:** PLN
        - **major:** 380120.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 961 000
        - **currency:** PLN
        - **major:** 269610.00
    - **pasazerow_z_odszkodowaniem:** 272
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
