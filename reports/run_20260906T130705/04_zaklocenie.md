# [04] ZAKLOCENIE

**Status:** ok · **run:** `20260906T130705` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **5.51 ms**

Usterka techniczna na rejsie LO417 WAW-GVA, szacowane opoznienie 180 min. Decyzja do 07:20 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO417 | - |
| `relacja` | WAW-GVA | - |
| `typ_zaklocenia` | TECHNICAL | - |
| `opoznienie_szacowane` | 180 | min |
| `kod_opoznienia` | 93 | - |
| `klasa_kodu` | d | - |
| `p_odszkodowania` | 0.50 | - |
| `okno_decyzji` | 45 | min |
| `iteracja` | 0 | szt |
| `powod_wejscia` | INITIAL | - |
| `odcinkow_ponizej` | 7 | szt |
| `pasazerow_na_rejsie` | 52 | osob |

## Co ten node ustalil

- klasa kodu `d` daje prawdopodobienstwo odszkodowania 0.5 -- node 09 mnozy przez nie kwote z Art. 7

## Szczegoly

- **rejs**
  - **id:** LO417-2026-08-25
  - **numer:** LO417
  - **z:** WAW
  - **do:** GVA
  - **std:** 2026-08-25T07:20:00+00:00
  - **sta:** 2026-08-25T09:40:00+00:00
  - **typ:** E75S
  - **maszyna:** SP-LIM
  - **rotacja:** ROT-SP-LIM-2026-08-25
- **kod_opoznienia**
  - **kod:** 93
  - **opis:** Rotacja: pozny przylot maszyny z poprzedniego odcinka
  - **grupa:** Rotacja
  - **orzecznictwo_tsue:** 1
- **odcinki_ponizej**
  - **LO418-2026-08-25**
    - **numer:** LO418
    - **z:** GVA
    - **do:** WAW
  - **LO3943-2026-08-25**
    - **numer:** LO3943
    - **z:** WAW
    - **do:** POZ
  - **LO3944-2026-08-25**
    - **numer:** LO3944
    - **z:** POZ
    - **do:** WAW
  - **LO3923-2026-08-25**
    - **numer:** LO3923
    - **z:** WAW
    - **do:** KRK
  - **LO3924-2026-08-25**
    - **numer:** LO3924
    - **z:** KRK
    - **do:** WAW
  - **LO3985-2026-08-25**
    - **numer:** LO3985
    - **z:** WAW
    - **do:** IEG
  - **LO3986-2026-08-25**
    - **numer:** LO3986
    - **z:** IEG
    - **do:** WAW

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `opoznienie szacowane` | policy | 0.50 | wartosc podana przy zgloszeniu, nie zmierzona |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
