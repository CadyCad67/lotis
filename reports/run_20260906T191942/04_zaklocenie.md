# [04] ZAKLOCENIE

**Status:** ok · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **12.16 ms**

Usterka techniczna na rejsie LO6 WAW-JFK, szacowane opoznienie 20 min i nadsprzedaz 17. Decyzja do 12:10 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO6 | - |
| `relacja` | WAW-JFK | - |
| `typ_zaklocenia` | TECHNICAL | - |
| `opoznienie_szacowane` | 20 | min |
| `nadsprzedaz` | 17 | rezerwacji |
| `ponad_pojemnosc` | 7 | osob |
| `kod_opoznienia` | 12 | - |
| `klasa_kodu` | c | - |
| `p_odszkodowania` | 1.00 | - |
| `okno_decyzji` | 45 | min |
| `iteracja` | 0 | szt |
| `powod_wejscia` | INITIAL | - |
| `odcinkow_ponizej` | 1 | szt |
| `pasazerow_na_rejsie` | 242 | osob |

## Co ten node ustalil

- klasa kodu `c` daje prawdopodobienstwo odszkodowania 1.0 -- node 09 mnozy przez nie kwote z Art. 7

## Szczegoly

- **rejs**
  - **id:** LO6-2026-08-21
  - **numer:** LO6
  - **z:** WAW
  - **do:** JFK
  - **std:** 2026-08-21T12:10:00+00:00
  - **sta:** 2026-08-21T21:40:00+00:00
  - **typ:** B788
  - **maszyna:** SP-LRE
  - **rotacja:** ROT-SP-LRE-2026-08-21
- **kod_opoznienia**
  - **kod:** 12
  - **opis:** Pozna odprawa, tlok w strefie odpraw
  - **grupa:** Pasazerowie i bagaz
  - **orzecznictwo_tsue:** 0
- **odcinki_ponizej**
  - **LO7-2026-08-21**
    - **numer:** LO7
    - **z:** JFK
    - **do:** WAW

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `opoznienie szacowane` | policy | 0.50 | wartosc podana przy zgloszeniu, nie zmierzona |

## Ostrzezenia

- nadsprzedaz: 7 pasazerow nie miesci sie w kabinie (259 na 252 miejsc)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
