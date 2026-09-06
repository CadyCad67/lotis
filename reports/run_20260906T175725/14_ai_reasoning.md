# [14] AI REASONING

**Status:** degraded · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **34.76 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 2 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 2 | szt |
| `rekomendacja` | HOLD | - |
| `przewaga_nad_druga` | 135761.12 PLN | PLN |

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
  - **SWAP-SP-LSB**
    - **powod:** zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 259075.00 PLN kosztu.
  - **SWAP-SP-LSG**
    - **powod:** zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 259075.00 PLN kosztu.
- **uzasadnienie**
  - **wybrana:** HOLD
  - **label:** Wstrzymaj odlot o 30 min
  - **strata**
    - **minor:** 3 714 950
    - **currency:** PLN
    - **major:** 37149.50
  - **widelki**
    - **min**
      - **minor:** 3 452 481
      - **currency:** PLN
      - **major:** 34524.81
    - **max**
      - **minor:** 5 733 944
      - **currency:** PLN
      - **major:** 57339.44
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 17983.50 PLN
    - zaloga: 1182.50 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** SWAP-SP-LSB
    - **strata**
      - **minor:** 17 291 062
      - **currency:** PLN
      - **major:** 172910.62
    - **roznica**
      - **minor:** 13 576 112
      - **currency:** PLN
      - **major:** 135761.12
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** propagacja 30 min (waga rotacji 1.0); szerokie widelki

## Ostrzezenia

- anomalia w `SWAP-SP-LSB`: zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 259075.00 PLN kosztu.
- anomalia w `SWAP-SP-LSG`: zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 259075.00 PLN kosztu.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
