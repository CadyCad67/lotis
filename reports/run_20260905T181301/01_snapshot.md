# [01] DANE

**Status:** degraded · **run:** `20260905T181301` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **1597.67 ms**

Zamrozony stan wtorek 2026-08-25: 350 rejsow LOT-u na 81 lancuchach, 29673 pasazerow na 29673 podrozach.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `doba` | 2026-08-25 | - |
| `dzien_tygodnia` | wtorek | - |
| `rejsy` | 350 | szt |
| `rotacje` | 81 | szt |
| `rotacje_przerwane` | 2 | szt |
| `maszyny` | 94 | szt |
| `zaloga` | 494 | osob |
| `pasazerowie` | 29 673 | osob |
| `podroze` | 29 673 | szt |
| `udzial_transferowych` | 31.50 | % |
| `porty` | 148 | szt |
| `typy_statkow` | 11 | szt |
| `odcisk` | sha256:44a9b3ee12dd2f2588d143e4b9546c90 | - |

## Co ten node ustalil

- snapshot sha256:44a9b3ee12dd2f2588d143e4b9546c90 jest podstawa calego runu
- horyzont propagacji konczy sie na dobie operacyjnej 2026-08-25 albo na powrocie maszyny do WAW, co nastapi pierwsze

## Szczegoly

- **zasieg_doby**
  - **pierwszy_odlot_utc:** 2026-08-25T00:10:00+00:00
  - **ostatni_przylot_utc:** 2026-08-26T11:25:00+00:00
  - **rozpietosc_h:** 35.20
- **najwieksze_porty**
  - **WAW**
    - **operacji:** 336
  - **KRK**
    - **operacji:** 19
  - **RZE**
    - **operacji:** 12
  - **WRO**
    - **operacji:** 12
  - **GDN**
    - **operacji:** 11
  - **KTW**
    - **operacji:** 10
  - **VNO**
    - **operacji:** 10
  - **OTP**
    - **operacji:** 9
- **flota_wg_typu**
  - **B38M:** 111
  - **E75S:** 71
  - **E195:** 59
  - **E190:** 32
  - **B738:** 21
  - **E295:** 20
  - **E170:** 15
  - **B789:** 11
  - **B788:** 10
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

- 2 przerw w lancuchach rotacji (2 maszyn) -- okno eksportu, nie blad

## Ostrzezenia

- 2 maszyn ma przerwany lancuch doby -- czesc odcinkow wypadla poza okno eksportu

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
