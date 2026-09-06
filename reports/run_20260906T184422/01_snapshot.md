# [01] DANE

**Status:** degraded · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **1638.67 ms**

Zamrozony stan niedziela 2026-08-23: 371 rejsow LOT-u na 87 lancuchach, 31966 pasazerow na 31966 podrozach.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `doba` | 2026-08-23 | - |
| `dzien_tygodnia` | niedziela | - |
| `rejsy` | 371 | szt |
| `rotacje` | 87 | szt |
| `rotacje_przerwane` | 4 | szt |
| `maszyny` | 94 | szt |
| `zaloga` | 542 | osob |
| `pasazerowie` | 31 966 | osob |
| `podroze` | 31 966 | szt |
| `udzial_transferowych` | 30.80 | % |
| `porty` | 148 | szt |
| `typy_statkow` | 11 | szt |
| `odcisk` | sha256:d7806668b46167a39f400ef7880d14c4 | - |

## Co ten node ustalil

- snapshot sha256:d7806668b46167a39f400ef7880d14c4 jest podstawa calego runu
- horyzont propagacji konczy sie na dobie operacyjnej 2026-08-23 albo na powrocie maszyny do WAW, co nastapi pierwsze

## Szczegoly

- **zasieg_doby**
  - **pierwszy_odlot_utc:** 2026-08-23T00:10:00+00:00
  - **ostatni_przylot_utc:** 2026-08-24T11:25:00+00:00
  - **rozpietosc_h:** 35.20
- **najwieksze_porty**
  - **WAW**
    - **operacji:** 343
  - **KRK**
    - **operacji:** 25
  - **GDN**
    - **operacji:** 18
  - **WRO**
    - **operacji:** 14
  - **KTW**
    - **operacji:** 11
  - **IST**
    - **operacji:** 10
  - **POZ**
    - **operacji:** 10
  - **VNO**
    - **operacji:** 10
- **flota_wg_typu**
  - **B38M:** 134
  - **E195:** 66
  - **E75S:** 60
  - **E190:** 37
  - **B738:** 24
  - **E170:** 15
  - **B788:** 12
  - **E295:** 12
  - **B789:** 11
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

- 4 przerw w lancuchach rotacji (4 maszyn) -- okno eksportu, nie blad

## Ostrzezenia

- 4 maszyn ma przerwany lancuch doby -- czesc odcinkow wypadla poza okno eksportu

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
