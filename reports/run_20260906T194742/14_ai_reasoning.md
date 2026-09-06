# [14] AI REASONING

**Status:** ok · **run:** `20260906T194742` · **snapshot:** `sha256:6c790f69f87c3591` · **56.3 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 0 | szt |
| `rekomendacja` | REBOOK-OWN | - |
| `przewaga_nad_druga` | 15857.16 PLN | PLN |

## Co ten node ustalil

- karta wykonania powstala deterministycznie w node 13; model jezykowy dopisuje komentarz obok i nie ma sciezki zapisu do jej srodka
- warstwa AI jest osobnym wyjsciem systemu, nie etapem przeplywu -- silnik konczy run bez niej

## Szczegoly

- **kontrole**
  - **kolejnosc_rankingu**
    - **ok:** 1
    - **powod:** 
  - **widelki**
    - **ok:** 1
    - **powod:** 
  - **karta_wykonania**
    - **ok:** 1
    - **powod:** 
  - **suma_skladnikow**
    - **ok:** 1
    - **powod:** 
  - **kompletnosc_pasazerow**
    - **ok:** 1
    - **powod:** 
- **anomalie:** -
- **uzasadnienie**
  - **wybrana:** REBOOK-OWN
  - **label:** Przenies na wlasny rejs LO393 (+480 min)
  - **strata**
    - **minor:** 13 516 921
    - **currency:** PLN
    - **major:** 135169.21
  - **widelki**
    - **min**
      - **minor:** 12 108 909
      - **currency:** PLN
      - **major:** 121089.09
    - **max**
      - **minor:** 18 585 766
      - **currency:** PLN
      - **major:** 185857.66
  - **najwieksze_skladniki_kosztu**
    - odszkodowanie_art7: 84925.00 PLN
    - rebooking_wlasny_spill: 17834.25 PLN
    - pozycjonowanie: 11438.00 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 9 668 229
    - **currency:** PLN
    - **major:** 96682.29
  - **alternatywa**
    - **id:** CANCEL
    - **strata**
      - **minor:** 15 102 637
      - **currency:** PLN
      - **major:** 151026.37
    - **roznica**
      - **minor:** 1 585 716
      - **currency:** PLN
      - **major:** 15857.16
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** 23 utraconych przesiadek; szerokie widelki

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
