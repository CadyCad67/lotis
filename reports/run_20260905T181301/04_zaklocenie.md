# [04] ZAKLOCENIE

**Status:** ok · **run:** `20260905T181301` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **13.66 ms**

Usterka techniczna na rejsie LO3850 WRO-WAW, szacowane opoznienie 240 min. Decyzja do 05:35 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO3850 | - |
| `relacja` | WRO-WAW | - |
| `typ_zaklocenia` | TECHNICAL | - |
| `opoznienie_szacowane` | 240 | min |
| `kod_opoznienia` | 41 | - |
| `klasa_kodu` | c | - |
| `p_odszkodowania` | 1.00 | - |
| `okno_decyzji` | 45 | min |
| `iteracja` | 0 | szt |
| `powod_wejscia` | INITIAL | - |
| `odcinkow_ponizej` | 8 | szt |
| `pasazerow_na_rejsie` | 55 | osob |

## Co ten node ustalil

- klasa kodu `c` daje prawdopodobienstwo odszkodowania 1.0 -- node 09 mnozy przez nie kwote z Art. 7

## Szczegoly

- **rejs**
  - **id:** LO3850-2026-08-25
  - **numer:** LO3850
  - **z:** WRO
  - **do:** WAW
  - **std:** 2026-08-25T05:35:00+00:00
  - **sta:** 2026-08-25T06:30:00+00:00
  - **typ:** E75S
  - **maszyna:** SP-LIM
  - **rotacja:** ROT-SP-LIM-2026-08-25
- **kod_opoznienia**
  - **kod:** 41
  - **opis:** Usterka techniczna samolotu
  - **grupa:** Techniczne
  - **orzecznictwo_tsue:** 1
- **odcinki_ponizej**
  - **LO417-2026-08-25**
    - **numer:** LO417
    - **z:** WAW
    - **do:** GVA
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
