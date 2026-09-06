# [09] COST ENGINE

**Status:** ok · **run:** `20260906T192705` · **snapshot:** `sha256:f3c290f4e6930407` · **6.59 ms**

Wyceniono 7 opcji. Kategoria EU261: A (1075.00 PLN na pasazera), prog opieki 120 min, p(odszkodowanie) = 1.0. Najtansza `SWAP-SP-LIO` (9915.76 PLN), najdrozsza `REBOOK-OAL` (152636.24 PLN).

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
| `koszt_najdrozszej` | 152636.24 PLN | PLN |

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
  - **SWAP-SP-LDH**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 1 613 006
      - **currency:** PLN
      - **major:** 16130.06
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
  - **SWAP-SP-LIQ**
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
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 15 263 624
      - **currency:** PLN
      - **major:** 152636.24
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
      - **pozycja:** opieka_art9
      - **kwota**
        - **minor:** 775 720
        - **currency:** PLN
        - **major:** 7757.20
    - **pasazerow_z_odszkodowaniem:** 82
    - **noclegow:** 0
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **koszt**
      - **minor:** 15 069 996
      - **currency:** PLN
      - **major:** 150699.96
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
      - **minor:** 14 604 306
      - **currency:** PLN
      - **major:** 146043.06
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
      - **pozycja:** pozycjonowanie
      - **kwota**
        - **minor:** 722 400
        - **currency:** PLN
        - **major:** 7224.00
    - **pasazerow_z_odszkodowaniem:** 82
    - **noclegow:** 82
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
