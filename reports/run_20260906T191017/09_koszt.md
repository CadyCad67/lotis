# [09] COST ENGINE

**Status:** ok · **run:** `20260906T191017` · **snapshot:** `sha256:f3c290f4e6930407` · **17.11 ms**

Wyceniono 4 opcji. Kategoria EU261: C (2580.00 PLN na pasazera), prog opieki 240 min, p(odszkodowanie) = 1.0. Najtansza `HOLD` (805722.60 PLN), najdrozsza `REBOOK-OAL` (1683467.20 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | C | - |
| `odszkodowanie_na_pasazera` | 2580.00 PLN | PLN |
| `prog_opieki` | 240 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 805722.60 PLN | PLN |
| `koszt_najdrozszej` | 1683467.20 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 240 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 80 572 260
      - **currency:** PLN
      - **major:** 805722.60
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 66 564 000
        - **currency:** PLN
        - **major:** 665640.00
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 12 555 720
        - **currency:** PLN
        - **major:** 125557.20
      - **pozycja:** roszczenia_mc99
      - **kwota**
        - **minor:** 743 040
        - **currency:** PLN
        - **major:** 7430.40
    - **pasazerow_z_odszkodowaniem:** 258
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 168 346 720
      - **currency:** PLN
      - **major:** 1683467.20
    - **najwieksze**
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 72 111 000
        - **currency:** PLN
        - **major:** 721110.00
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 66 564 000
        - **currency:** PLN
        - **major:** 665640.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 488 000
        - **currency:** PLN
        - **major:** 264880.00
    - **pasazerow_z_odszkodowaniem:** 258
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 135 098 174
      - **currency:** PLN
      - **major:** 1350981.74
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 66 564 000
        - **currency:** PLN
        - **major:** 665640.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 488 000
        - **currency:** PLN
        - **major:** 264880.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 25 238 850
        - **currency:** PLN
        - **major:** 252388.50
    - **pasazerow_z_odszkodowaniem:** 258
    - **noclegow:** 258
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 109 859 324
      - **currency:** PLN
      - **major:** 1098593.24
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 66 564 000
        - **currency:** PLN
        - **major:** 665640.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 26 488 000
        - **currency:** PLN
        - **major:** 264880.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 15 614 934
        - **currency:** PLN
        - **major:** 156149.34
    - **pasazerow_z_odszkodowaniem:** 258
    - **noclegow:** 258
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
