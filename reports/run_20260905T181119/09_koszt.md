# [09] COST ENGINE

**Status:** ok · **run:** `20260905T181119` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **5.2 ms**

Wyceniono 6 opcji. Kategoria EU261: A (1075.00 PLN na pasazera), prog opieki 120 min, p(odszkodowanie) = 1.0. Najtansza `CANCEL` (63798.24 PLN), najdrozsza `HOLD` (106172.64 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | A | - |
| `odszkodowanie_na_pasazera` | 1075.00 PLN | PLN |
| `prog_opieki` | 120 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 63798.24 PLN | PLN |
| `koszt_najdrozszej` | 106172.64 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 120 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 10 617 264
      - **currency:** PLN
      - **major:** 106172.64
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 5 912 500
        - **currency:** PLN
        - **major:** 59125.00
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 3 618 240
        - **currency:** PLN
        - **major:** 36182.40
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 520 300
        - **currency:** PLN
        - **major:** 5203.00
    - **pasazerow_z_odszkodowaniem:** 55
    - **noclegow:** 0
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 7 124 799
      - **currency:** PLN
      - **major:** 71247.99
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 5 912 500
        - **currency:** PLN
        - **major:** 59125.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 744 975
        - **currency:** PLN
        - **major:** 7449.75
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 331 100
        - **currency:** PLN
        - **major:** 3311.00
    - **pasazerow_z_odszkodowaniem:** 55
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 8 697 524
      - **currency:** PLN
      - **major:** 86975.24
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 5 912 500
        - **currency:** PLN
        - **major:** 59125.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 2 128 500
        - **currency:** PLN
        - **major:** 21285.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 520 300
        - **currency:** PLN
        - **major:** 5203.00
    - **pasazerow_z_odszkodowaniem:** 55
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 9 694 614
      - **currency:** PLN
      - **major:** 96946.14
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 5 912 500
        - **currency:** PLN
        - **major:** 59125.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 2 737 515
        - **currency:** PLN
        - **major:** 27375.15
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 744 975
        - **currency:** PLN
        - **major:** 7449.75
    - **pasazerow_z_odszkodowaniem:** 55
    - **noclegow:** 55
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 6 379 824
      - **currency:** PLN
      - **major:** 63798.24
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 5 912 500
        - **currency:** PLN
        - **major:** 59125.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 331 100
        - **currency:** PLN
        - **major:** 3311.00
      - **pozycja:** roszczenia_mc99
      - **kwota**
        - **minor:** 136 224
        - **currency:** PLN
        - **major:** 1362.24
    - **pasazerow_z_odszkodowaniem:** 55
    - **noclegow:** 0
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 7 925 459
      - **currency:** PLN
      - **major:** 79254.59
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 5 912 500
        - **currency:** PLN
        - **major:** 59125.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 1 083 600
        - **currency:** PLN
        - **major:** 10836.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 427 420
        - **currency:** PLN
        - **major:** 4274.20
    - **pasazerow_z_odszkodowaniem:** 55
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
