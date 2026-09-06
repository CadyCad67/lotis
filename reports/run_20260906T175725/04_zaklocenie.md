# [04] ZAKLOCENIE

**Status:** degraded · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **5.98 ms**

Usterka techniczna na rejsie LO6 WAW-JFK, szacowane opoznienie 30 min. Decyzja do 12:10 UTC (45 min).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rejs` | LO6 | - |
| `relacja` | WAW-JFK | - |
| `typ_zaklocenia` | TECHNICAL | - |
| `opoznienie_szacowane` | 30 | min |
| `kod_opoznienia` | ZZZ | - |
| `klasa_kodu` | ? | - |
| `p_odszkodowania` | 0.50 | - |
| `okno_decyzji` | 45 | min |
| `iteracja` | 0 | szt |
| `powod_wejscia` | INITIAL | - |
| `odcinkow_ponizej` | 1 | szt |
| `pasazerow_na_rejsie` | 241 | osob |

## Co ten node ustalil

- klasa kodu `?` daje prawdopodobienstwo odszkodowania 0.5 -- node 09 mnozy przez nie kwote z Art. 7

## Szczegoly

- **rejs**
  - **id:** LO6-2026-08-22
  - **numer:** LO6
  - **z:** WAW
  - **do:** JFK
  - **std:** 2026-08-22T12:10:00+00:00
  - **sta:** 2026-08-22T21:40:00+00:00
  - **typ:** B788
  - **maszyna:** SP-LRG
  - **rotacja:** ROT-SP-LRG-2026-08-22
- **odcinki_ponizej**
  - **LO7-2026-08-22**
    - **numer:** LO7
    - **z:** JFK
    - **do:** WAW

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `opoznienie szacowane` | policy | 0.50 | wartosc podana przy zgloszeniu, nie zmierzona |

## Ostrzezenia

- kod ZZZ nie ma klasy w bazie -- przyjeto p=0.5, czyli srodek miedzy odpowiedzialnoscia a okolicznoscia nadzwyczajna

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
