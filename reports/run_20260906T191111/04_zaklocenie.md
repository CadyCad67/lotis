# [04] ZAKLOCENIE

**Status:** ok · **run:** `20260906T191111` · **snapshot:** `sha256:f3c290f4e6930407` · **12.04 ms**

Usterka techniczna na rejsie LO2098 ORD-KRK, szacowane opoznienie 180 min. Decyzja do 00:10 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO2098 | - |
| `relacja` | ORD-KRK | - |
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
| `odcinkow_ponizej` | 1 | szt |
| `pasazerow_na_rejsie` | 258 | osob |

## Co ten node ustalil

- klasa kodu `c` daje prawdopodobienstwo odszkodowania 1.0 -- node 09 mnozy przez nie kwote z Art. 7

## Szczegoly

- **rejs**
  - **id:** LO2098-2026-08-21
  - **numer:** LO2098
  - **z:** ORD
  - **do:** KRK
  - **std:** 2026-08-21T00:10:00+00:00
  - **sta:** 2026-08-21T09:30:00+00:00
  - **typ:** B789
  - **maszyna:** SP-LSF
  - **rotacja:** ROT-SP-LSF-2026-08-21
- **kod_opoznienia**
  - **kod:** 41
  - **opis:** Usterka techniczna samolotu
  - **grupa:** Techniczne
  - **orzecznictwo_tsue:** 1
- **odcinki_ponizej**
  - **LO2097-2026-08-21**
    - **numer:** LO2097
    - **z:** KRK
    - **do:** ORD

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `opoznienie szacowane` | policy | 0.50 | wartosc podana przy zgloszeniu, nie zmierzona |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
