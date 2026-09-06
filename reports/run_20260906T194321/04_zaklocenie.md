# [04] ZAKLOCENIE

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **12.65 ms**

Zdarzenie pasazerskie na rejsie LO82 NRT-WAW, nadsprzedaz 33 rezerwacji. Decyzja do 01:15 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO82 | - |
| `relacja` | NRT-WAW | - |
| `typ_zaklocenia` | PAX | - |
| `opoznienie_szacowane` | 0 | min |
| `nadsprzedaz` | 33 | rezerwacji |
| `ponad_pojemnosc` | 8 | osob |
| `kod_opoznienia` | 14 | - |
| `klasa_kodu` | c | - |
| `p_odszkodowania` | 1.00 | - |
| `okno_decyzji` | 45 | min |
| `iteracja` | 0 | szt |
| `powod_wejscia` | INITIAL | - |
| `odcinkow_ponizej` | 2 | szt |
| `pasazerow_na_rejsie` | 227 | osob |

## Co ten node ustalil

- klasa kodu `c` daje prawdopodobienstwo odszkodowania 1.0 -- node 09 mnozy przez nie kwote z Art. 7

## Szczegoly

- **rejs**
  - **id:** LO82-2026-08-24
  - **numer:** LO82
  - **z:** NRT
  - **do:** WAW
  - **std:** 2026-08-24T01:15:00+00:00
  - **sta:** 2026-08-24T15:30:00+00:00
  - **typ:** B788
  - **maszyna:** SP-LRE
  - **rotacja:** ROT-SP-LRE-2026-08-24
- **kod_opoznienia**
  - **kod:** 14
  - **opis:** Nadsprzedaz, bledy rezerwacji
  - **grupa:** Pasazerowie i bagaz
  - **orzecznictwo_tsue:** 0
- **odcinki_ponizej**
  - **LO4-2026-08-24**
    - **numer:** LO4
    - **z:** ORD
    - **do:** WAW
  - **LO3-2026-08-24**
    - **numer:** LO3
    - **z:** WAW
    - **do:** ORD

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `opoznienie szacowane` | policy | 0.50 | wartosc podana przy zgloszeniu, nie zmierzona |

## Ostrzezenia

- nadsprzedaz: 8 pasazerow nie miesci sie w kabinie (260 na 252 miejsc)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
