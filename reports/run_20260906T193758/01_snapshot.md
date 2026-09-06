# [01] DANE

**Status:** degraded · **run:** `20260906T193758` · **snapshot:** `sha256:6c790f69f87c3591` · **1791.98 ms**

Zamrozony stan poniedziałek 2026-08-24: 380 rejsow LOT-u na 86 lancuchach, 32534 pasazerow na 32534 podrozach.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `doba` | 2026-08-24 | - |
| `dzien_tygodnia` | poniedziałek | - |
| `rejsy` | 380 | szt |
| `rotacje` | 86 | szt |
| `rotacje_przerwane` | 3 | szt |
| `maszyny` | 94 | szt |
| `zaloga` | 529 | osob |
| `pasazerowie` | 32 534 | osob |
| `podroze` | 32 534 | szt |
| `udzial_transferowych` | 31.20 | % |
| `porty` | 148 | szt |
| `typy_statkow` | 11 | szt |
| `odcisk` | sha256:6c790f69f87c359132b1de878467789b | - |

## Co ten node ustalil

- snapshot sha256:6c790f69f87c359132b1de878467789b jest podstawa calego runu
- horyzont propagacji konczy sie na dobie operacyjnej 2026-08-24 albo na powrocie maszyny do WAW, co nastapi pierwsze

## Szczegoly

- **zasieg_doby**
  - **pierwszy_odlot_utc:** 2026-08-24T00:10:00+00:00
  - **ostatni_przylot_utc:** 2026-08-25T11:25:00+00:00
  - **rozpietosc_h:** 35.20
- **najwieksze_porty**
  - **WAW**
    - **operacji:** 351
  - **KRK**
    - **operacji:** 26
  - **GDN**
    - **operacji:** 18
  - **RZE**
    - **operacji:** 12
  - **WRO**
    - **operacji:** 12
  - **AYT**
    - **operacji:** 10
  - **BRU**
    - **operacji:** 10
  - **VNO**
    - **operacji:** 10
- **flota_wg_typu**
  - **B38M:** 121
  - **E75S:** 68
  - **E195:** 67
  - **E190:** 43
  - **B738:** 24
  - **E295:** 18
  - **B788:** 16
  - **E170:** 15
  - **B789:** 8
- **pewnosc_pol**
  - **flights:** KNOWN
  - **rotations:** KNOWN
  - **airports:** KNOWN
  - **aircraft_types:** KNOWN
  - **crew:** ESTIMATED
  - **passengers:** ESTIMATED
  - **fares:** ESTIMATED

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `manifest` | synthetic | 0.60 | rozklad klas rezerwacyjnych w obrebie kabiny (baza podaje mnozniki, nie udzialy) |
| `manifest` | synthetic | 0.60 | ancillary jako ulamek taryfy |
| `manifest` | synthetic | 0.60 | moment zakupu skorelowany z elastycznoscia klasy |
| `manifest` | synthetic | 0.60 | zaloga wyliczona z tabel FDP EASA, nie z grafiku operatora |
| `rozklad` | real | 1.00 | siedem rzeczywistych dob operacyjnych, nie generator |
| `porty i prawo` | real | 1.00 | baza parametryczna loops.jsx |

## Braki danych

- 4 przerw w lancuchach rotacji (3 maszyn) -- okno eksportu, nie blad

## Ostrzezenia

- 3 maszyn ma przerwany lancuch doby -- czesc odcinkow wypadla poza okno eksportu

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
