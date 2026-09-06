# [02] WALIDACJA DANYCH

**Status:** ok · **run:** `20260904T165628` · **snapshot:** `sha256:3b1d18402faf79f0` · **10.57 ms**

Sprawdzono 6 rodzin niezmiennikow na 381 rejsach. Zadne pole nie schodzi do UNKNOWN. Osobno: 42 operacji w oknie ciszy nocnej typu 1 -- to rozklad, nie blad danych.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `porty_rejsow_bledow` | 0 | szt |
| `typy_statkow_bledow` | 0 | szt |
| `ciaglosc_rotacji_bledow` | 5 | szt |
| `zapas_fdp_bledow` | 0 | szt |
| `obsadzenie_bledow` | 0 | szt |
| `kwalifikacje_zalogi_bledow` | 0 | szt |
| `operacje_w_ciszy_nocnej` | 42 | szt |
| `pol_znanych` | 9 | szt |
| `pol_szacowanych` | 4 | szt |
| `pol_nieznanych` | 0 | szt |

## Co ten node ustalil

- 42 operacji lezy w oknie zakazu planowania -- node 05 traktuje je jako istniejace, ale nie wolno na nich planowac nowych
- pole `ciaglosc_rotacji` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `crew` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `fares` liczone jako ESTIMATED -- node 11 rozszerza widelki
- pole `passengers` liczone jako ESTIMATED -- node 11 rozszerza widelki

## Szczegoly

- **ciaglosc_rotacji**
  - **ROT-SP-LRF-2026-08-26**
    - **z:** LO30-2026-08-26
    - **do:** LO72-2026-08-26
    - **konczy_w:** WAW
    - **zaczyna_w:** DEL
  - **ROT-SP-LRF-2026-08-26**
    - **z:** LO72-2026-08-26
    - **do:** LO29-2026-08-26
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LSA-2026-08-26**
    - **z:** LO22-2026-08-26
    - **do:** LO21-2026-08-26
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LVI-2026-08-26**
    - **z:** LO584-2026-08-26
    - **do:** LO3919-2026-08-26
    - **problem:** odlot przed przylotem poprzedniego odcinka
  - **ROT-SP-LYK-2026-08-26**
    - **z:** LO286-2026-08-26
    - **do:** LO601-2026-08-26
    - **problem:** odlot przed przylotem poprzedniego odcinka
- **operacje_w_ciszy_nocnej**
  - **LO151-2026-08-26**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO195-2026-08-26**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:00
  - **LO234-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:35
  - **LO268-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO280-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:45
  - **LO304-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:30
  - **LO320-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:50
  - **LO336-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:05
  - **LO344-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:00
  - **LO348-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:40
  - **LO355-2026-08-26**
    - **pole:** przylot
    - **port:** MUC
    - **lokalnie:** 00:20
  - **LO380-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 23:35
  - **LO3803-2026-08-26**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 01:10
  - **LO3826-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:20
  - **LO3827-2026-08-26**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO3849-2026-08-26**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3860-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:25
  - **LO3879-2026-08-26**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:45
  - **LO3911-2026-08-26**
    - **pole:** wylot
    - **port:** WAW
    - **lokalnie:** 00:55
  - **LO3936-2026-08-26**
    - **pole:** przylot
    - **port:** WAW
    - **lokalnie:** 00:25
- **operacje_w_ciszy_nocnej_pominietych:** 22
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

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
