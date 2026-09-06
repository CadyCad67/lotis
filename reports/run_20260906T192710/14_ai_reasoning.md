# [14] AI REASONING

**Status:** ok · **run:** `20260906T192710` · **snapshot:** `sha256:f3c290f4e6930407` · **38.93 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 0 | szt |
| `rekomendacja` | SWAP-SP-LIO | - |
| `przewaga_nad_druga` | 994.63 PLN | PLN |

## Co ten node ustalil

- opcje `SWAP-SP-LIO` i `SWAP-SP-LIQ` sa blisko -- rekomendacja nie jest jednoznaczna i czlowiek powinien to zobaczyc
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
      - **minor:** 1 264 149
      - **currency:** PLN
      - **major:** 12641.49
    - **max**
      - **minor:** 1 584 399
      - **currency:** PLN
      - **major:** 15843.99
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 7550.76 PLN
    - zaloga: 2365.00 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** SWAP-SP-LIQ
    - **strata**
      - **minor:** 1 515 309
      - **currency:** PLN
      - **major:** 15153.09
    - **roznica**
      - **minor:** 99 463
      - **currency:** PLN
      - **major:** 994.63
  - **czolowka_blisko:** 1
  - **uwaga_polityki:** propagacja 29 min (waga rotacji 1.0); szerokie widelki; priorytet 50, indeks pasazerski 0.60

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
