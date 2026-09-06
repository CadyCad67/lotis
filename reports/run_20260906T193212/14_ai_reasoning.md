# [14] AI REASONING

**Status:** degraded · **run:** `20260906T193212` · **snapshot:** `sha256:6c790f69f87c3591` · **47.74 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 2 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 2 | szt |
| `rekomendacja` | REBOOK-SPILL | - |
| `przewaga_nad_druga` | 162913.84 PLN | PLN |

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
  - **wybrana:** REBOOK-SPILL
  - **label:** Przenies 8 nadmiarowych na LO26 (+280 min)
  - **strata**
    - **minor:** 3 820 120
    - **currency:** PLN
    - **major:** 38201.20
  - **widelki**
    - **min**
      - **minor:** 3 550 221
      - **currency:** PLN
      - **major:** 35502.21
    - **max**
      - **minor:** 5 896 272
      - **currency:** PLN
      - **major:** 58962.72
  - **najwieksze_skladniki_kosztu**
    - odszkodowanie_art7: 20640.00 PLN
    - roszczenia_mc99: 8978.40 PLN
    - rebooking_wlasny_spill: 7826.00 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** SWAP-SP-LSA
    - **strata**
      - **minor:** 20 111 504
      - **currency:** PLN
      - **major:** 201115.04
    - **roznica**
      - **minor:** 16 291 384
      - **currency:** PLN
      - **major:** 162913.84
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** szerokie widelki

## Ostrzezenia

- anomalia w `SWAP-SP-LSA`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 292400.00 PLN kosztu.
- anomalia w `SWAP-SP-LSE`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 292400.00 PLN kosztu.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
