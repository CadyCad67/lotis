# [04] ZAKLOCENIE

**Status:** ok · **run:** `20260906T194612` · **snapshot:** `sha256:6c790f69f87c3591` · **12.24 ms**

Usterka techniczna na rejsie LO395 WAW-HAM, szacowane opoznienie 60 min i nadsprzedaz 30. Decyzja do 09:05 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO395 | - |
| `relacja` | WAW-HAM | - |
| `typ_zaklocenia` | TECHNICAL | - |
| `opoznienie_szacowane` | 60 | min |
| `nadsprzedaz` | 30 | rezerwacji |
| `ponad_pojemnosc` | 3 | osob |
| `kod_opoznienia` | 22 | - |
| `klasa_kodu` | c | - |
| `p_odszkodowania` | 1.00 | - |
| `okno_decyzji` | 45 | min |
| `iteracja` | 0 | szt |
| `powod_wejscia` | INITIAL | - |
| `odcinkow_ponizej` | 5 | szt |
| `pasazerow_na_rejsie` | 79 | osob |

## Co ten node ustalil

- klasa kodu `c` daje prawdopodobienstwo odszkodowania 1.0 -- node 09 mnozy przez nie kwote z Art. 7

## Szczegoly

- **rejs**
  - **id:** LO395-2026-08-24
  - **numer:** LO395
  - **z:** WAW
  - **do:** HAM
  - **std:** 2026-08-24T09:05:00+00:00
  - **sta:** 2026-08-24T10:40:00+00:00
  - **typ:** E190
  - **maszyna:** SP-LMA
  - **rotacja:** ROT-SP-LMA-2026-08-24
- **kod_opoznienia**
  - **kod:** 22
  - **opis:** Pozne podstawienie ladunku
  - **grupa:** Cargo i poczta
  - **orzecznictwo_tsue:** 0
- **odcinki_ponizej**
  - **LO396-2026-08-24**
    - **numer:** LO396
    - **z:** HAM
    - **do:** WAW
  - **LO3801-2026-08-24**
    - **numer:** LO3801
    - **z:** WAW
    - **do:** RZE
  - **LO3802-2026-08-24**
    - **numer:** LO3802
    - **z:** RZE
    - **do:** WAW
  - **LO461-2026-08-24**
    - **numer:** LO461
    - **z:** WAW
    - **do:** CPH
  - **LO462-2026-08-24**
    - **numer:** LO462
    - **z:** CPH
    - **do:** WAW

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `opoznienie szacowane` | policy | 0.50 | wartosc podana przy zgloszeniu, nie zmierzona |

## Ostrzezenia

- nadsprzedaz: 3 pasazerow nie miesci sie w kabinie (109 na 106 miejsc)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
