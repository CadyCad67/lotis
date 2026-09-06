# [01] DANE

**Status:** degraded · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **1741.64 ms**

Zamrozony stan sobota 2026-08-22: 348 rejsow LOT-u na 87 lancuchach, 30720 pasazerow na 30720 podrozach.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `doba` | 2026-08-22 | - |
| `dzien_tygodnia` | sobota | - |
| `rejsy` | 348 | szt |
| `rotacje` | 87 | szt |
| `rotacje_przerwane` | 3 | szt |
| `maszyny` | 94 | szt |
| `zaloga` | 549 | osob |
| `pasazerowie` | 30 720 | osob |
| `podroze` | 30 720 | szt |
| `udzial_transferowych` | 32.00 | % |
| `porty` | 148 | szt |
| `typy_statkow` | 11 | szt |
| `odcisk` | sha256:91cb2a4af61a3714f4c72ed8bbad9666 | - |

## Co ten node ustalil

- snapshot sha256:91cb2a4af61a3714f4c72ed8bbad9666 jest podstawa calego runu
- horyzont propagacji konczy sie na dobie operacyjnej 2026-08-22 albo na powrocie maszyny do WAW, co nastapi pierwsze

## Szczegoly

- **zasieg_doby**
  - **pierwszy_odlot_utc:** 2026-08-22T00:10:00+00:00
  - **ostatni_przylot_utc:** 2026-08-23T11:25:00+00:00
  - **rozpietosc_h:** 35.20
- **najwieksze_porty**
  - **WAW**
    - **operacji:** 329
  - **KRK**
    - **operacji:** 21
  - **AYT**
    - **operacji:** 14
  - **GDN**
    - **operacji:** 12
  - **WRO**
    - **operacji:** 11
  - **VNO**
    - **operacji:** 10
  - **KTW**
    - **operacji:** 9
  - **AMS**
    - **operacji:** 8
- **flota_wg_typu**
  - **B38M:** 125
  - **E195:** 70
  - **E75S:** 56
  - **E190:** 33
  - **B738:** 22
  - **B788:** 15
  - **E170:** 11
  - **B789:** 10
  - **E295:** 6
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

- 3 przerw w lancuchach rotacji (3 maszyn) -- okno eksportu, nie blad

## Ostrzezenia

- 3 maszyn ma przerwany lancuch doby -- czesc odcinkow wypadla poza okno eksportu

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
