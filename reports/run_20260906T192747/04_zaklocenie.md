# [04] ZAKLOCENIE

**Status:** ok · **run:** `20260906T192747` · **snapshot:** `sha256:f3c290f4e6930407` · **12.43 ms**

Usterka techniczna na rejsie LO3931 WAW-SZZ, szacowane opoznienie 20 min i nadsprzedaz 7. Decyzja do 07:05 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO3931 | - |
| `relacja` | WAW-SZZ | - |
| `typ_zaklocenia` | TECHNICAL | - |
| `opoznienie_szacowane` | 20 | min |
| `nadsprzedaz` | 7 | rezerwacji |
| `ponad_pojemnosc` | 7 | osob |
| `kod_opoznienia` | 13 | - |
| `klasa_kodu` | c | - |
| `p_odszkodowania` | 1.00 | - |
| `okno_decyzji` | 45 | min |
| `iteracja` | 0 | szt |
| `powod_wejscia` | INITIAL | - |
| `odcinkow_ponizej` | 6 | szt |
| `pasazerow_na_rejsie` | 82 | osob |

## Co ten node ustalil

- klasa kodu `c` daje prawdopodobienstwo odszkodowania 1.0 -- node 09 mnozy przez nie kwote z Art. 7

## Szczegoly

- **rejs**
  - **id:** LO3931-2026-08-21
  - **numer:** LO3931
  - **z:** WAW
  - **do:** SZZ
  - **std:** 2026-08-21T07:05:00+00:00
  - **sta:** 2026-08-21T08:10:00+00:00
  - **typ:** E75S
  - **maszyna:** SP-LII
  - **rotacja:** ROT-SP-LII-2026-08-21
- **kod_opoznienia**
  - **kod:** 13
  - **opis:** Blad odprawy pasazera lub bagazu
  - **grupa:** Pasazerowie i bagaz
  - **orzecznictwo_tsue:** 0
- **odcinki_ponizej**
  - **LO3932-2026-08-21**
    - **numer:** LO3932
    - **z:** SZZ
    - **do:** WAW
  - **LO3933-2026-08-21**
    - **numer:** LO3933
    - **z:** WAW
    - **do:** SZZ
  - **LO3934-2026-08-21**
    - **numer:** LO3934
    - **z:** SZZ
    - **do:** WAW
  - **LO613-2026-08-21**
    - **numer:** LO613
    - **z:** WAW
    - **do:** ZAG
  - **LO614-2026-08-21**
    - **numer:** LO614
    - **z:** ZAG
    - **do:** WAW
  - **LO459-2026-08-21**
    - **numer:** LO459
    - **z:** WAW
    - **do:** CPH

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `opoznienie szacowane` | policy | 0.50 | wartosc podana przy zgloszeniu, nie zmierzona |

## Ostrzezenia

- nadsprzedaz: 7 pasazerow nie miesci sie w kabinie (89 na 82 miejsc)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
