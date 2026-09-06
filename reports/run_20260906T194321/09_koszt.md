# [09] COST ENGINE

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **15.08 ms**

Wyceniono 4 opcji. Kategoria EU261: C (2580.00 PLN na pasazera), prog opieki 240 min, p(odszkodowanie) = 1.0. Najtansza `HOLD` (20640.00 PLN), najdrozsza `REBOOK-OAL` (1248100.80 PLN).

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
| `koszt_najdrozszej` | 1248100.80 PLN | PLN |

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
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 124 810 080
      - **currency:** PLN
      - **major:** 1248100.80
    - **najwieksze**
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 63 446 500
        - **currency:** PLN
        - **major:** 634465.00
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 58 566 000
        - **currency:** PLN
        - **major:** 585660.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 2 147 420
        - **currency:** PLN
        - **major:** 21474.20
    - **pasazerow_z_odszkodowaniem:** 227
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 95 610 506
      - **currency:** PLN
      - **major:** 956105.06
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 58 566 000
        - **currency:** PLN
        - **major:** 585660.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 22 206 275
        - **currency:** PLN
        - **major:** 222062.75
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 13 738 721
        - **currency:** PLN
        - **major:** 137387.21
    - **pasazerow_z_odszkodowaniem:** 227
    - **noclegow:** 227
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 74 049 231
      - **currency:** PLN
      - **major:** 740492.31
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 58 566 000
        - **currency:** PLN
        - **major:** 585660.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 13 738 721
        - **currency:** PLN
        - **major:** 137387.21
      - **pozycja:** roszczenia_mc99
      - **kwota**
        - **minor:** 650 160
        - **currency:** PLN
        - **major:** 6501.60
    - **pasazerow_z_odszkodowaniem:** 227
    - **noclegow:** 227
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
