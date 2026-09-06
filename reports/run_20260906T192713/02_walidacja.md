# [02] DATA ENGINE

**Status:** ok · **run:** `20260906T192713` · **snapshot:** `sha256:f3c290f4e6930407` · **11.9 ms**

Sprawdzono 6 rodzin niezmiennikow na 390 rejsach. Zadne pole nie schodzi do UNKNOWN. Osobno: 47 operacji w oknie ciszy nocnej typu 1 -- to rozklad, nie blad danych.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `porty_rejsow_bledow` | 0 | szt |
| `typy_statkow_bledow` | 0 | szt |
| `ciaglosc_rotacji_bledow` | 6 | szt |
| `zapas_fdp_bledow` | 0 | szt |
| `obsadzenie_bledow` | 0 | szt |
| `kwalifikacje_zalogi_bledow` | 0 | szt |
| `operacje_w_ciszy_nocnej` | 47 | szt |
| `rejsy_bez_numeru_handlowego` | 2 | szt |
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
  - **ROT-SP-LMD-2026-08-21**
    - **z:** LO456-2026-08-21
    - **do:** LO395-2026-08-21
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LMF-2026-08-21**
    - **z:** LO462-2026-08-21
    - **do:** LO3951-2026-08-21
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LNG-2026-08-21**
    - **z:** LO524-2026-08-21
    - **do:** LO783-2026-08-21
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LNK-2026-08-21**
    - **z:** LO460-2026-08-21
    - **do:** LO453-2026-08-21
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LSD-2026-08-21**
    - **z:** LO2084-2026-08-21
    - **do:** LO11-2026-08-21
    - **konczy_w:** KRK
    - **zaczyna_w:** WAW
  - **ROT-SP-LSG-2026-08-21**
    - **z:** LO22-2026-08-21
    - **do:** LO21-2026-08-21
    - **problem:** odlot przed przylotem poprzedniego odcinka
- **operacje_w_ciszy_nocnej**
  - **LO1155-2026-08-21**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:15
  - **LO151-2026-08-21**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO195-2026-08-21**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO234-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:35
  - **LO254-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO268-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO280-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO304-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:30
  - **LO320-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO336-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:05
  - **LO344-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:00
  - **LO348-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:40
  - **LO355-2026-08-21**
    - **pole:** przylot
    - **port:** MUC
    - **lokalnie:** 00:20
  - **LO374-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:30
  - **LO380-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO3803-2026-08-21**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:10
  - **LO3827-2026-08-21**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO3849-2026-08-21**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3860-2026-08-21**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:25
  - **LO3879-2026-08-21**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
- **operacje_w_ciszy_nocnej_pominietych:** 27
- **rejsy_bez_numeru_handlowego**
  - **znak:LOT3AD-2026-08-21**
    - **znak:** znak:LOT3AD
    - **z:** WAW
    - **do:** BOJ
    - **maszyna:** SP-LVN
  - **znak:LOT7LP-2026-08-21**
    - **znak:** znak:LOT7LP
    - **z:** WAW
    - **do:** VAR
    - **maszyna:** SP-LYL
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
