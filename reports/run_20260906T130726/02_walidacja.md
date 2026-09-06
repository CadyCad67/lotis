# [02] DATA ENGINE

**Status:** ok · **run:** `20260906T130726` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **10.73 ms**

Sprawdzono 6 rodzin niezmiennikow na 350 rejsach. Zadne pole nie schodzi do UNKNOWN. Osobno: 39 operacji w oknie ciszy nocnej typu 1 -- to rozklad, nie blad danych.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `porty_rejsow_bledow` | 0 | szt |
| `typy_statkow_bledow` | 0 | szt |
| `ciaglosc_rotacji_bledow` | 3 | szt |
| `zapas_fdp_bledow` | 0 | szt |
| `obsadzenie_bledow` | 0 | szt |
| `kwalifikacje_zalogi_bledow` | 0 | szt |
| `operacje_w_ciszy_nocnej` | 39 | szt |
| `rejsy_bez_numeru_handlowego` | 2 | szt |
| `pol_znanych` | 9 | szt |
| `pol_szacowanych` | 4 | szt |
| `pol_nieznanych` | 0 | szt |

## Co ten node ustalil

- 39 operacji lezy w oknie zakazu planowania -- node 05 traktuje je jako istniejace, ale nie wolno na nich planowac nowych
- manifest pasazerski dla tych rejsow jest niepewny: lot techniczny nie ma pasazerow, a wiec nie ma tez ekspozycji z Art. 7 EU261
- pole `ciaglosc_rotacji` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `crew` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `fares` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `passengers` liczone jako ESTIMATED -- node 11 rozszerza widelki

## Szczegoly

- **ciaglosc_rotacji**
  - **ROT-SP-LRG-2026-08-25**
    - **z:** LO24-2026-08-25
    - **do:** LO23-2026-08-25
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LSB-2026-08-25**
    - **z:** LO2098-2026-08-25
    - **do:** LO1-2026-08-25
    - **konczy_w:** KRK
    - **zaczyna_w:** WAW
  - **ROT-SP-LSD-2026-08-25**
    - **z:** LO42-2026-08-25
    - **do:** LO72-2026-08-25
    - **konczy_w:** WAW
    - **zaczyna_w:** DEL
- **operacje_w_ciszy_nocnej**
  - **LO149-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:05
  - **LO151-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO195-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO197-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:40
  - **LO234-2026-08-25**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:35
  - **LO268-2026-08-25**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO280-2026-08-25**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO320-2026-08-25**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO336-2026-08-25**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:00
  - **LO355-2026-08-25**
    - **pole:** przylot
    - **port:** MUC
    - **lokalnie:** 00:20
  - **LO380-2026-08-25**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO3803-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:10
  - **LO3827-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO3849-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3860-2026-08-25**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:25
  - **LO3879-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3911-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO3941-2026-08-25**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:40
  - **LO397-2026-08-25**
    - **pole:** przylot
    - **port:** HAM
    - **lokalnie:** 00:15
  - **LO3986-2026-08-25**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:30
- **operacje_w_ciszy_nocnej_pominietych:** 19
- **rejsy_bez_numeru_handlowego**
  - **znak:LOT1HF-2026-08-25**
    - **znak:** znak:LOT1HF
    - **z:** KGS
    - **do:** WAW
    - **maszyna:** SP-LYJ
  - **znak:LOT6KM-2026-08-25**
    - **znak:** znak:LOT6KM
    - **z:** WAW
    - **do:** KGS
    - **maszyna:** SP-LYJ
- **poziomy_pewnosci**
  - **aircraft_types:** KNOWN
  - **airports:** KNOWN
  - **ciaglosc_rotacji:** ESTIMATED
  - **crew:** ESTIMATED
  - **fares:** ESTIMATED
  - **flights:** KNOWN
  - **kwalifikacje_zalogi:** KNOWN
  - **obsadzenie:** KNOWN
  - **passengers:** ESTIMATED
  - **porty_rejsow:** KNOWN
  - **rotations:** KNOWN
  - **typy_statkow:** KNOWN
  - **zapas_fdp:** KNOWN

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `zaloga` | derived | 0.70 | sklad i limity FDP wyliczone z tabel EASA, nie z grafiku operatora |
| `obsadzenie` | synthetic | 0.60 | manifest z rozkladow bazy, tozsamosci pasazerow modelowane |

## Braki danych

- 2 rejsow ma tylko znak wywolawczy, bez numeru handlowego -- zrodlo nie rozstrzyga, czy to loty techniczne (dolot, przebazowanie), czy rejsy handlowe, ktorym eksport zgubil numer

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
