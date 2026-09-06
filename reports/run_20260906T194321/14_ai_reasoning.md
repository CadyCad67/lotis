# [14] AI REASONING

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **22.67 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 0 | szt |
| `rekomendacja` | OVERNIGHT | - |
| `przewaga_nad_druga` | 291995.74 PLN | PLN |

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
  - **wybrana:** OVERNIGHT
  - **label:** Nocleg i rejs nastepnego dnia
  - **strata**
    - **minor:** 121 389 006
    - **currency:** PLN
    - **major:** 1213890.06
  - **widelki**
    - **min**
      - **minor:** 114 032 097
      - **currency:** PLN
      - **major:** 1140320.97
    - **max**
      - **minor:** 245 230 315
      - **currency:** PLN
      - **major:** 2452303.15
  - **najwieksze_skladniki_kosztu**
    - odszkodowanie_art7: 585660.00 PLN
    - rebooking_wlasny_spill: 222062.75 PLN
    - opieka_art9: 137387.21 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 29 199 574
    - **currency:** PLN
    - **major:** 291995.74
  - **alternatywa**
    - **id:** REBOOK-OAL
    - **strata**
      - **minor:** 150 588 580
      - **currency:** PLN
      - **major:** 1505885.80
    - **roznica**
      - **minor:** 29 199 574
      - **currency:** PLN
      - **major:** 291995.74
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** 105 utraconych przesiadek; szerokie widelki

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
