# [01] DANE

**Status:** degraded · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **1693.62 ms**

Zamrozony stan środa 2026-08-26: 381 rejsow LOT-u na 83 lancuchach, 31684 pasazerow na 31684 podrozach.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `doba` | 2026-08-26 | - |
| `dzien_tygodnia` | środa | - |
| `rejsy` | 381 | szt |
| `rotacje` | 83 | szt |
| `rotacje_przerwane` | 1 | szt |
| `maszyny` | 94 | szt |
| `zaloga` | 511 | osob |
| `pasazerowie` | 31 684 | osob |
| `podroze` | 31 684 | szt |
| `udzial_transferowych` | 31.00 | % |
| `porty` | 148 | szt |
| `typy_statkow` | 11 | szt |
| `odcisk` | sha256:3b1d18402faf79f0e77fd3d167817e01 | - |

## Co ten node ustalil

- snapshot sha256:3b1d18402faf79f0e77fd3d167817e01 jest podstawa calego runu
- horyzont propagacji konczy sie na dobie operacyjnej 2026-08-26 albo na powrocie maszyny do WAW, co nastapi pierwsze

## Szczegoly

- **zasieg_doby**
  - **pierwszy_odlot_utc:** 2026-08-26T00:10:00+00:00
  - **ostatni_przylot_utc:** 2026-08-27T11:25:00+00:00
  - **rozpietosc_h:** 35.20
- **najwieksze_porty**
  - **WAW**
    - **operacji:** 356
  - **KRK**
    - **operacji:** 23
  - **GDN**
    - **operacji:** 19
  - **WRO**
    - **operacji:** 14
  - **AYT**
    - **operacji:** 12
  - **POZ**
    - **operacji:** 12
  - **KTW**
    - **operacji:** 11
  - **RZE**
    - **operacji:** 11
- **flota_wg_typu**
  - **B38M:** 113
  - **E75S:** 75
  - **E195:** 63
  - **E190:** 47
  - **B738:** 22
  - **E295:** 20
  - **E170:** 19
  - **B788:** 13
  - **B789:** 9
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
