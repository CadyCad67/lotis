# [14] AI REASONING

**Status:** ok · **run:** `20260906T192747` · **snapshot:** `sha256:f3c290f4e6930407` · **57.71 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 0 | szt |
| `rekomendacja` | SWAP-SP-LIO | - |
| `przewaga_nad_druga` | 1750.68 PLN | PLN |

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
  - **wybrana:** SWAP-SP-LIO
  - **label:** Podmien maszyne na SP-LIO (E75S)
  - **strata**
    - **minor:** 1 415 846
    - **currency:** PLN
    - **major:** 14158.46
  - **widelki**
    - **min**
      - **minor:** 1 228 455
      - **currency:** PLN
      - **major:** 12284.55
    - **max**
      - **minor:** 1 582 416
      - **currency:** PLN
      - **major:** 15824.16
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 7550.76 PLN
    - zaloga: 2365.00 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 353 069
    - **currency:** PLN
    - **major:** 3530.69
  - **alternatywa**
    - **id:** SWAP-SP-LIC
    - **strata**
      - **minor:** 1 590 914
      - **currency:** PLN
      - **major:** 15909.14
    - **roznica**
      - **minor:** 175 068
      - **currency:** PLN
      - **major:** 1750.68
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** propagacja 29 min (waga rotacji 1.0); szerokie widelki

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
