# [09] COST ENGINE

**Status:** ok · **run:** `20260906T192747` · **snapshot:** `sha256:f3c290f4e6930407` · **7.15 ms**

Wyceniono 10 opcji. Kategoria EU261: A (1075.00 PLN na pasazera), prog opieki 120 min, p(odszkodowanie) = 1.0. Najtansza `SWAP-SP-LIC` (9915.76 PLN), najdrozsza `REBOOK-OAL` (153238.24 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kategoria_eu261` | A | - |
| `odszkodowanie_na_pasazera` | 1075.00 PLN | PLN |
| `prog_opieki` | 120 | min |
| `prog_odszkodowania` | 180 | min |
| `p_odszkodowania` | 1.00 | - |
| `kurs_eur_pln` | 4.30 | - |
| `koszt_najtanszej` | 9915.76 PLN | PLN |
| `koszt_najdrozszej` | 153238.24 PLN | PLN |

## Co ten node ustalil

- opieka z Art. 9 wchodzi do kazdej opcji od 120 min NIEZALEZNIE od przyczyny -- to koszt pewny
- odszkodowanie z Art. 7 wchodzi jako koszt oczekiwany: kwota x liczba pax x 1.0
- filtr prawny NIE dopisuje ceny do opcji -- ten node liczy ekspozycje, node 12 usuwa opcje niedopuszczalne

## Szczegoly

- **koszty_opcji**
  - **HOLD**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 1 000 673
      - **currency:** PLN
      - **major:** 10006.73
    - **najwieksze**
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 752 500
        - **currency:** PLN
        - **major:** 7525.00
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 212 340
        - **currency:** PLN
        - **major:** 2123.40
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 35 833
        - **currency:** PLN
        - **major:** 358.33
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **REBOOK-SPILL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 1 669 452
      - **currency:** PLN
      - **major:** 16694.52
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 752 500
        - **currency:** PLN
        - **major:** 7525.00
      - **pozycja:** roszczenia_mc99
      - **kwota**
        - **minor:** 507 744
        - **currency:** PLN
        - **major:** 5077.44
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 212 340
        - **currency:** PLN
        - **major:** 2123.40
    - **pasazerow_z_odszkodowaniem:** 7
    - **noclegow:** 0
  - **SWAP-SP-LDH**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 1 608 111
      - **currency:** PLN
      - **major:** 16081.11
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 741 296
        - **currency:** PLN
        - **major:** 7412.96
      - **pozycja:** odmowa_przyjecia_art4
      - **kwota**
        - **minor:** 645 000
        - **currency:** PLN
        - **major:** 6450.00
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 236 500
        - **currency:** PLN
        - **major:** 2365.00
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LIC**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 991 576
      - **currency:** PLN
      - **major:** 9915.76
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 755 076
        - **currency:** PLN
        - **major:** 7550.76
      - **pozycja:** zaloga
      - **kwota**
        - **minor:** 236 500
        - **currency:** PLN
        - **major:** 2365.00
    - **pasazerow_z_odszkodowaniem:** 0
    - **noclegow:** 0
  - **SWAP-SP-LIO**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 991 576
      - **currency:** PLN
      - **major:** 9915.76
    - **najwieksze**
      - **pozycja:** opoznienie_w_siatce
      - **kwota**
        - **minor:** 755 076
        - **currency:** PLN
        - **major:** 7550.76
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
      - **minor:** 11 991 754
      - **currency:** PLN
      - **major:** 119917.54
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 815 000
        - **currency:** PLN
        - **major:** 88150.00
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 1 110 690
        - **currency:** PLN
        - **major:** 11106.90
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 782 600
        - **currency:** PLN
        - **major:** 7826.00
    - **pasazerow_z_odszkodowaniem:** 82
    - **noclegow:** 0
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 15 323 824
      - **currency:** PLN
      - **major:** 153238.24
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 815 000
        - **currency:** PLN
        - **major:** 88150.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 4 442 760
        - **currency:** PLN
        - **major:** 44427.60
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 782 600
        - **currency:** PLN
        - **major:** 7826.00
    - **pasazerow_z_odszkodowaniem:** 82
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 15 130 196
      - **currency:** PLN
      - **major:** 151301.96
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 815 000
        - **currency:** PLN
        - **major:** 88150.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 3 750 762
        - **currency:** PLN
        - **major:** 37507.62
      - **pozycja:** rebooking_wlasny_spill
      - **kwota**
        - **minor:** 1 110 690
        - **currency:** PLN
        - **major:** 11106.90
    - **pasazerow_z_odszkodowaniem:** 82
    - **noclegow:** 82
  - **CANCEL**
    - **tryb:** MODIFYING
    - **koszt**
      - **minor:** 11 526 064
      - **currency:** PLN
      - **major:** 115260.64
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 815 000
        - **currency:** PLN
        - **major:** 88150.00
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 782 600
        - **currency:** PLN
        - **major:** 7826.00
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 775 720
        - **currency:** PLN
        - **major:** 7757.20
    - **pasazerow_z_odszkodowaniem:** 82
    - **noclegow:** 0
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 13 657 789
      - **currency:** PLN
      - **major:** 136577.89
    - **najwieksze**
      - **pozycja:** odszkodowanie_art7
      - **kwota**
        - **minor:** 8 815 000
        - **currency:** PLN
        - **major:** 88150.00
      - **pozycja:** rozliczenie_interline
      - **kwota**
        - **minor:** 2 221 380
        - **currency:** PLN
        - **major:** 22213.80
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 782 600
        - **currency:** PLN
        - **major:** 7826.00
    - **pasazerow_z_odszkodowaniem:** 82
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
