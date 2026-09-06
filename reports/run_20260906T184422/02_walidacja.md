# [02] DATA ENGINE

**Status:** ok · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **11.88 ms**

Sprawdzono 6 rodzin niezmiennikow na 371 rejsach. Zadne pole nie schodzi do UNKNOWN. Osobno: 47 operacji w oknie ciszy nocnej typu 1 -- to rozklad, nie blad danych.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `porty_rejsow_bledow` | 0 | szt |
| `typy_statkow_bledow` | 0 | szt |
| `ciaglosc_rotacji_bledow` | 7 | szt |
| `zapas_fdp_bledow` | 0 | szt |
| `obsadzenie_bledow` | 0 | szt |
| `kwalifikacje_zalogi_bledow` | 0 | szt |
| `operacje_w_ciszy_nocnej` | 47 | szt |
| `rejsy_bez_numeru_handlowego` | 4 | szt |
| `pol_znanych` | 9 | szt |
| `pol_szacowanych` | 4 | szt |
| `pol_nieznanych` | 0 | szt |

## Co ten node ustalil

- 47 operacji lezy w oknie zakazu planowania -- node 05 traktuje je jako istniejace, ale nie wolno na nich planowac nowych
- manifest pasazerski dla tych rejsow jest niepewny: lot techniczny nie ma pasazerow, a wiec nie ma tez ekspozycji z Art. 7 EU261
- pole `ciaglosc_rotacji` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `crew` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `fares` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `passengers` liczone jako ESTIMATED -- node 11 rozszerza widelki

## Szczegoly

- **ciaglosc_rotacji**
  - **ROT-SP-LRA-2026-08-23**
    - **z:** LO2098-2026-08-23
    - **do:** LO1-2026-08-23
    - **konczy_w:** KRK
    - **zaczyna_w:** WAW
  - **ROT-SP-LRF-2026-08-23**
    - **z:** LO72-2026-08-23
    - **do:** LO4-2026-08-23
    - **konczy_w:** WAW
    - **zaczyna_w:** ORD
  - **ROT-SP-LSA-2026-08-23**
    - **z:** LO24-2026-08-23
    - **do:** LO23-2026-08-23
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LSE-2026-08-23**
    - **z:** LO36-2026-08-23
    - **do:** LO35-2026-08-23
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LSF-2026-08-23**
    - **z:** LO2082-2026-08-23
    - **do:** LO11-2026-08-23
    - **konczy_w:** RZE
    - **zaczyna_w:** WAW
  - **ROT-SP-LYE-2026-08-23**
    - **z:** LO436-2026-08-23
    - **do:** LO190-2026-08-23
    - **konczy_w:** WAW
    - **zaczyna_w:** TAS
  - **ROT-SP-LYE-2026-08-23**
    - **z:** LO190-2026-08-23
    - **do:** LO195-2026-08-23
    - **problem:** odlot przed przylotem poprzedniego odcinka
- **operacje_w_ciszy_nocnej**
  - **LO151-2026-08-23**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO173-2026-08-23**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:30
  - **LO191-2026-08-23**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO195-2026-08-23**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO197-2026-08-23**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:40
  - **LO234-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:35
  - **LO254-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO268-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO280-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO320-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO336-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:05
  - **LO344-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:00
  - **LO348-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:40
  - **LO355-2026-08-23**
    - **pole:** przylot
    - **port:** MUC
    - **lokalnie:** 00:20
  - **LO380-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:30
  - **LO3803-2026-08-23**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:10
  - **LO3826-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:20
  - **LO3827-2026-08-23**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO3849-2026-08-23**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3860-2026-08-23**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:25
- **operacje_w_ciszy_nocnej_pominietych:** 27
- **rejsy_bez_numeru_handlowego**
  - **znak:LOT4TJ-2026-08-23**
    - **znak:** znak:LOT4TJ
    - **z:** HER
    - **do:** WAW
    - **maszyna:** SP-LVH
  - **znak:LOT6CJ-2026-08-23**
    - **znak:** znak:LOT6CJ
    - **z:** AYT
    - **do:** WAW
    - **maszyna:** SP-LVI
  - **znak:LOT6EZ-2026-08-23**
    - **znak:** znak:LOT6EZ
    - **z:** AYT
    - **do:** WAW
    - **maszyna:** SP-LYH
  - **znak:LOT6VN-2026-08-23**
    - **znak:** znak:LOT6VN
    - **z:** WAW
    - **do:** AYT
    - **maszyna:** SP-LVI
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
