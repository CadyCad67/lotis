# [14] AI REASONING

**Status:** degraded · **run:** `20260906T193758` · **snapshot:** `sha256:6c790f69f87c3591` · **48.01 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 2 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 2 | szt |
| `rekomendacja` | HOLD | - |
| `przewaga_nad_druga` | 179006.34 PLN | PLN |

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
- **anomalie**
  - **SWAP-SP-LSA**
    - **powod:** zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 292400.00 PLN kosztu.
  - **SWAP-SP-LSE**
    - **powod:** zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 292400.00 PLN kosztu.
- **uzasadnienie**
  - **wybrana:** HOLD
  - **label:** Wstrzymaj odlot o 30 min
  - **strata**
    - **minor:** 4 303 490
    - **currency:** PLN
    - **major:** 43034.90
  - **widelki**
    - **min**
      - **minor:** 3 999 440
      - **currency:** PLN
      - **major:** 39994.40
    - **max**
      - **minor:** 6 642 343
      - **currency:** PLN
      - **major:** 66423.43
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 20926.20 PLN
    - zaloga: 1182.50 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** SWAP-SP-LSA
    - **strata**
      - **minor:** 22 204 124
      - **currency:** PLN
      - **major:** 222041.24
    - **roznica**
      - **minor:** 17 900 634
      - **currency:** PLN
      - **major:** 179006.34
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** propagacja 30 min (waga rotacji 1.0); szerokie widelki

## Ostrzezenia

- anomalia w `SWAP-SP-LSA`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 292400.00 PLN kosztu.
- anomalia w `SWAP-SP-LSE`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 292400.00 PLN kosztu.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
