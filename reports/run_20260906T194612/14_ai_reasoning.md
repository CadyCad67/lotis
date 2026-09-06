# [14] AI REASONING

**Status:** ok · **run:** `20260906T194612` · **snapshot:** `sha256:6c790f69f87c3591` · **60.87 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 0 | szt |
| `rekomendacja` | REBOOK-SPILL | - |
| `przewaga_nad_druga` | 2052.82 PLN | PLN |

## Co ten node ustalil

- opcje `REBOOK-SPILL` i `SWAP-SP-LII` sa blisko -- rekomendacja nie jest jednoznaczna i czlowiek powinien to zobaczyc
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
  - **wybrana:** REBOOK-SPILL
  - **label:** Przenies 3 nadmiarowych na LO393 (+480 min)
  - **strata**
    - **minor:** 3 019 838
    - **currency:** PLN
    - **major:** 30198.38
  - **widelki**
    - **min**
      - **minor:** 2 705 272
      - **currency:** PLN
      - **major:** 27052.72
    - **max**
      - **minor:** 4 152 277
      - **currency:** PLN
      - **major:** 41522.77
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 11747.40 PLN
    - odszkodowanie_art7: 3225.00 PLN
    - roszczenia_mc99: 2662.56 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** SWAP-SP-LII
    - **strata**
      - **minor:** 3 225 120
      - **currency:** PLN
      - **major:** 32251.20
    - **roznica**
      - **minor:** 205 282
      - **currency:** PLN
      - **major:** 2052.82
  - **czolowka_blisko:** 1
  - **uwaga_polityki:** propagacja 53 min (waga rotacji 1.0); 23 utraconych przesiadek; szerokie widelki

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
