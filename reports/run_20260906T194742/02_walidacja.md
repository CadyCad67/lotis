# [02] DATA ENGINE

**Status:** ok · **run:** `20260906T194742` · **snapshot:** `sha256:6c790f69f87c3591` · **12.26 ms**

Sprawdzono 6 rodzin niezmiennikow na 380 rejsach. Zadne pole nie schodzi do UNKNOWN. Osobno: 43 operacji w oknie ciszy nocnej typu 1 -- to rozklad, nie blad danych.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `porty_rejsow_bledow` | 0 | szt |
| `typy_statkow_bledow` | 0 | szt |
| `ciaglosc_rotacji_bledow` | 6 | szt |
| `zapas_fdp_bledow` | 0 | szt |
| `obsadzenie_bledow` | 0 | szt |
| `kwalifikacje_zalogi_bledow` | 0 | szt |
| `operacje_w_ciszy_nocnej` | 43 | szt |
| `rejsy_bez_numeru_handlowego` | 4 | szt |
| `pol_znanych` | 9 | szt |
| `pol_szacowanych` | 4 | szt |
| `pol_nieznanych` | 0 | szt |

## Co ten node ustalil

- 43 operacji lezy w oknie zakazu planowania -- node 05 traktuje je jako istniejace, ale nie wolno na nich planowac nowych
- manifest pasazerski dla tych rejsow jest niepewny: lot techniczny nie ma pasazerow, a wiec nie ma tez ekspozycji z Art. 7 EU261
- pole `ciaglosc_rotacji` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `crew` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `fares` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `passengers` liczone jako ESTIMATED -- node 11 rozszerza widelki

## Szczegoly

- **ciaglosc_rotacji**
  - **ROT-SP-LRA-2026-08-24**
    - **z:** LO2-2026-08-24
    - **do:** LO2097-2026-08-24
    - **konczy_w:** WAW
    - **zaczyna_w:** KRK
  - **ROT-SP-LRB-2026-08-24**
    - **z:** LO12-2026-08-24
    - **do:** LO2081-2026-08-24
    - **konczy_w:** WAW
    - **zaczyna_w:** RZE
  - **ROT-SP-LRB-2026-08-24**
    - **z:** LO2081-2026-08-24
    - **do:** LO9001-2026-08-24
    - **konczy_w:** EWR
    - **zaczyna_w:** WAW
  - **ROT-SP-LRE-2026-08-24**
    - **z:** LO82-2026-08-24
    - **do:** LO4-2026-08-24
    - **konczy_w:** WAW
    - **zaczyna_w:** ORD
  - **ROT-SP-LRG-2026-08-24**
    - **z:** LO22-2026-08-24
    - **do:** LO21-2026-08-24
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LSD-2026-08-24**
    - **z:** LO100-2026-08-24
    - **do:** LO71-2026-08-24
    - **problem:** odlot przed przylotem poprzedniego odcinka
- **operacje_w_ciszy_nocnej**
  - **LO151-2026-08-24**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO195-2026-08-24**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO234-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:55
  - **LO254-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO268-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO280-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO304-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:30
  - **LO320-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO336-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:05
  - **LO355-2026-08-24**
    - **pole:** przylot
    - **port:** MUC
    - **lokalnie:** 00:20
  - **LO380-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO3803-2026-08-24**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:10
  - **LO3827-2026-08-24**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO3849-2026-08-24**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3860-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:25
  - **LO3879-2026-08-24**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3922-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:20
  - **LO3936-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:25
  - **LO397-2026-08-24**
    - **pole:** przylot
    - **port:** HAM
    - **lokalnie:** 00:15
  - **LO3986-2026-08-24**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:30
- **operacje_w_ciszy_nocnej_pominietych:** 23
- **rejsy_bez_numeru_handlowego**
  - **znak:LOT2HP-2026-08-24**
    - **znak:** znak:LOT2HP
    - **z:** DLM
    - **do:** WAW
    - **maszyna:** SP-LVO
  - **znak:LOT3AT-2026-08-24**
    - **znak:** znak:LOT3AT
    - **z:** WAW
    - **do:** DLM
    - **maszyna:** SP-LVO
  - **znak:LOT7NB-2026-08-24**
    - **znak:** znak:LOT7NB
    - **z:** WAW
    - **do:** AYT
    - **maszyna:** SP-LYL
  - **znak:LOT7PA-2026-08-24**
    - **znak:** znak:LOT7PA
    - **z:** LEI
    - **do:** WAW
    - **maszyna:** SP-LYM
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

- 4 rejsow ma tylko znak wywolawczy, bez numeru handlowego -- zrodlo nie rozstrzyga, czy to loty techniczne (dolot, przebazowanie), czy rejsy handlowe, ktorym eksport zgubil numer

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
