# [04] ZAKLOCENIE

**Status:** ok · **run:** `20260906T190327` · **snapshot:** `sha256:f3c290f4e6930407` · **11.42 ms**

Usterka techniczna na rejsie LO3981 WAW-IEG, szacowane opoznienie 180 min. Decyzja do 07:05 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO3981 | - |
| `relacja` | WAW-IEG | - |
| `typ_zaklocenia` | TECHNICAL | - |
| `opoznienie_szacowane` | 180 | min |
| `nadsprzedaz` | 0 | rezerwacji |
| `ponad_pojemnosc` | 0 | osob |
| `kod_opoznienia` | 41 | - |
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
  - **id:** LO3981-2026-08-21
  - **numer:** LO3981
  - **z:** WAW
  - **do:** IEG
  - **std:** 2026-08-21T07:05:00+00:00
  - **sta:** 2026-08-21T08:05:00+00:00
  - **typ:** E75S
  - **maszyna:** SP-LIC
  - **rotacja:** ROT-SP-LIC-2026-08-21
- **kod_opoznienia**
  - **kod:** 41
  - **opis:** Usterka techniczna samolotu
  - **grupa:** Techniczne
  - **orzecznictwo_tsue:** 1
- **odcinki_ponizej**
  - **LO3982-2026-08-21**
    - **numer:** LO3982
    - **z:** IEG
    - **do:** WAW
  - **LO3853-2026-08-21**
    - **numer:** LO3853
    - **z:** WAW
    - **do:** WRO
  - **LO3854-2026-08-21**
    - **numer:** LO3854
    - **z:** WRO
    - **do:** WAW
  - **LO237-2026-08-21**
    - **numer:** LO237
    - **z:** WAW
    - **do:** BRU
  - **LO238-2026-08-21**
    - **numer:** LO238
    - **z:** BRU
    - **do:** WAW
  - **LO485-2026-08-21**
    - **numer:** LO485
    - **z:** WAW
    - **do:** OSL

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `opoznienie szacowane` | policy | 0.50 | wartosc podana przy zgloszeniu, nie zmierzona |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
