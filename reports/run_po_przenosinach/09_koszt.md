# [09] COST ENGINE

**Status:** ok · **run:** `po_przenosinach` · **snapshot:** `sha256:f3c290f4e6930407` · **5.56 ms**

Wyceniono 6 opcji. Kategoria EU261: A (1075.00 PLN na pasazera), prog opieki 120 min, p(odszkodowanie) = 1.0. Najtansza `CANCEL` (72831.68 PLN), najdrozsza `OVERNIGHT` (107319.06 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | A | - |
| `odszkodowanie_na_pasazera` | 1075.00 PLN | PLN |
| `prog_opieki` | 120 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 72831.68 PLN | PLN |
| `koszt_najdrozszej` | 107319.06 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 120 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 9 933 288
      - **currency:** PLN
      - **major:** 99332.88
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 6 557 500
        - **currency:** PLN
        - **major:** 65575.00
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 2 537 460
        - **currency:** PLN
        - **major:** 25374.60
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 367 220
        - **currency:** PLN
        - **major:** 3672.20
    - **pasazerow_z_odszkodowaniem:** 61
    - **noclegow:** 0
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 8 109 413
      - **currency:** PLN
      - **major:** 81094.13
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 6 557 500
        - **currency:** PLN
        - **major:** 65575.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 826 245
        - **currency:** PLN
        - **major:** 8262.45
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 577 060
        - **currency:** PLN
        - **major:** 5770.60
    - **pasazerow_z_odszkodowaniem:** 61
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 9 643 868
      - **currency:** PLN
      - **major:** 96438.68
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 6 557 500
        - **currency:** PLN
        - **major:** 65575.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 2 360 700
        - **currency:** PLN
        - **major:** 23607.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 577 060
        - **currency:** PLN
        - **major:** 5770.60
    - **pasazerow_z_odszkodowaniem:** 61
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 10 731 906
      - **currency:** PLN
      - **major:** 107319.06
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 6 557 500
        - **currency:** PLN
        - **major:** 65575.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 3 036 153
        - **currency:** PLN
        - **major:** 30361.53
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 826 245
        - **currency:** PLN
        - **major:** 8262.45
    - **pasazerow_z_odszkodowaniem:** 61
    - **noclegow:** 61
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 7 283 168
      - **currency:** PLN
      - **major:** 72831.68
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 6 557 500
        - **currency:** PLN
        - **major:** 65575.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 577 060
        - **currency:** PLN
        - **major:** 5770.60
      - **pozycja:** roszczenia_mc99
      - **kwota**
        - **minor:** 148 608
        - **currency:** PLN
        - **major:** 1486.08
    - **pasazerow_z_odszkodowaniem:** 61
    - **noclegow:** 0
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 8 889 218
      - **currency:** PLN
      - **major:** 88892.18
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 6 557 500
        - **currency:** PLN
        - **major:** 65575.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 1 199 700
        - **currency:** PLN
        - **major:** 11997.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 577 060
        - **currency:** PLN
        - **major:** 5770.60
    - **pasazerow_z_odszkodowaniem:** 61
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
