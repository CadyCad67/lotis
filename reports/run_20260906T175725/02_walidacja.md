# [02] DATA ENGINE

**Status:** ok · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **12.14 ms**

Sprawdzono 6 rodzin niezmiennikow na 348 rejsach. Zadne pole nie schodzi do UNKNOWN. Osobno: 35 operacji w oknie ciszy nocnej typu 1 -- to rozklad, nie blad danych.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `porty_rejsow_bledow` | 0 | szt |
| `typy_statkow_bledow` | 0 | szt |
| `ciaglosc_rotacji_bledow` | 5 | szt |
| `zapas_fdp_bledow` | 0 | szt |
| `obsadzenie_bledow` | 0 | szt |
| `kwalifikacje_zalogi_bledow` | 0 | szt |
| `operacje_w_ciszy_nocnej` | 35 | szt |
| `rejsy_bez_numeru_handlowego` | 3 | szt |
| `pol_znanych` | 9 | szt |
| `pol_szacowanych` | 4 | szt |
| `pol_nieznanych` | 0 | szt |

## Co ten node ustalil

- 35 operacji lezy w oknie zakazu planowania -- node 05 traktuje je jako istniejace, ale nie wolno na nich planowac nowych
- manifest pasazerski dla tych rejsow jest niepewny: lot techniczny nie ma pasazerow, a wiec nie ma tez ekspozycji z Art. 7 EU261
- pole `ciaglosc_rotacji` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `crew` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `fares` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `passengers` liczone jako ESTIMATED -- node 11 rozszerza widelki

## Szczegoly

- **ciaglosc_rotacji**
  - **ROT-SP-LRC-2026-08-22**
    - **z:** LO22-2026-08-22
    - **do:** LO21-2026-08-22
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LRD-2026-08-22**
    - **z:** LO38-2026-08-22
    - **do:** LO37-2026-08-22
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LSD-2026-08-22**
    - **z:** LO2-2026-08-22
    - **do:** LO2097-2026-08-22
    - **konczy_w:** WAW
    - **zaczyna_w:** KRK
  - **ROT-SP-LSF-2026-08-22**
    - **z:** LO12-2026-08-22
    - **do:** LO2083-2026-08-22
    - **konczy_w:** WAW
    - **zaczyna_w:** KRK
  - **ROT-SP-LYA-2026-08-22**
    - **z:** LO195-2026-08-22
    - **do:** LO190-2026-08-22
    - **konczy_w:** NQZ
    - **zaczyna_w:** TAS
- **operacje_w_ciszy_nocnej**
  - **LO151-2026-08-22**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO1729-2026-08-22**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:15
  - **LO173-2026-08-22**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:30
  - **LO195-2026-08-22**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO197-2026-08-22**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:40
  - **LO234-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:35
  - **LO268-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO280-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO304-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:30
  - **LO320-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO336-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:00
  - **LO344-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:00
  - **LO355-2026-08-22**
    - **pole:** przylot
    - **port:** MUC
    - **lokalnie:** 00:20
  - **LO380-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO3827-2026-08-22**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO3849-2026-08-22**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3860-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:25
  - **LO3911-2026-08-22**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO408-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:35
  - **LO410-2026-08-22**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
- **operacje_w_ciszy_nocnej_pominietych:** 15
- **rejsy_bez_numeru_handlowego**
  - **znak:LOT2VM-2026-08-22**
    - **znak:** znak:LOT2VM
    - **z:** AYT
    - **do:** WAW
    - **maszyna:** SP-LVN
  - **znak:LOT6RP-2026-08-22**
    - **znak:** znak:LOT6RP
    - **z:** WAW
    - **do:** AYT
    - **maszyna:** SP-LVN
  - **znak:LOT7KX-2026-08-22**
    - **znak:** znak:LOT7KX
    - **z:** KGS
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

- 3 rejsow ma tylko znak wywolawczy, bez numeru handlowego -- zrodlo nie rozstrzyga, czy to loty techniczne (dolot, przebazowanie), czy rejsy handlowe, ktorym eksport zgubil numer

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
