# [01] DANE

**Status:** degraded · **run:** `20260905T213940` · **snapshot:** `sha256:f3c290f4e6930407` · **1814.68 ms**

Zamrozony stan piątek 2026-08-21: 390 rejsow LOT-u na 86 lancuchach, 32911 pasazerow na 32911 podrozach.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `doba` | 2026-08-21 | - |
| `dzien_tygodnia` | piątek | - |
| `rejsy` | 390 | szt |
| `rotacje` | 86 | szt |
| `rotacje_przerwane` | 1 | szt |
| `maszyny` | 94 | szt |
| `zaloga` | 536 | osob |
| `pasazerowie` | 32 911 | osob |
| `podroze` | 32 911 | szt |
| `udzial_transferowych` | 31.00 | % |
| `porty` | 148 | szt |
| `typy_statkow` | 11 | szt |
| `odcisk` | sha256:f3c290f4e6930407fb2bcad856fc671f | - |

## Co ten node ustalil

- snapshot sha256:f3c290f4e6930407fb2bcad856fc671f jest podstawa calego runu
- horyzont propagacji konczy sie na dobie operacyjnej 2026-08-21 albo na powrocie maszyny do WAW, co nastapi pierwsze

## Szczegoly

- **zasieg_doby**
  - **pierwszy_odlot_utc:** 2026-08-21T00:10:00+00:00
  - **ostatni_przylot_utc:** 2026-08-22T11:25:00+00:00
  - **rozpietosc_h:** 35.20
- **najwieksze_porty**
  - **WAW**
    - **operacji:** 360
  - **KRK**
    - **operacji:** 27
  - **GDN**
    - **operacji:** 17
  - **WRO**
    - **operacji:** 14
  - **POZ**
    - **operacji:** 12
  - **VNO**
    - **operacji:** 12
  - **KTW**
    - **operacji:** 11
  - **RZE**
    - **operacji:** 11
- **flota_wg_typu**
  - **B38M:** 124
  - **E195:** 74
  - **E75S:** 70
  - **E190:** 47
  - **B738:** 24
  - **E170:** 17
  - **B788:** 13
  - **E295:** 11
  - **B789:** 10
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

- 1 przerw w lancuchach rotacji (1 maszyn) -- okno eksportu, nie blad

## Ostrzezenia

- 1 maszyn ma przerwany lancuch doby -- czesc odcinkow wypadla poza okno eksportu

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
