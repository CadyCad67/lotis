# [14] AI REASONING

**Status:** degraded · **run:** `20260906T175204` · **snapshot:** `sha256:91cb2a4af61a3714` · **32.47 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 2 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 2 | szt |
| `rekomendacja` | HOLD | - |
| `przewaga_nad_druga` | 87091.22 PLN | PLN |

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
  - **label:** Wstrzymaj odlot o 120 min
  - **strata**
    - **minor:** 14 859 800
    - **currency:** PLN
    - **major:** 148598.00
  - **widelki**
    - **min**
      - **minor:** 13 809 923
      - **currency:** PLN
      - **major:** 138099.23
    - **max**
      - **minor:** 22 935 778
      - **currency:** PLN
      - **major:** 229357.78
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 71934.00 PLN
    - zaloga: 4730.00 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** SWAP-SP-LSB
    - **strata**
      - **minor:** 23 568 922
      - **currency:** PLN
      - **major:** 235689.22
    - **roznica**
      - **minor:** 8 709 122
      - **currency:** PLN
      - **major:** 87091.22
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** propagacja 120 min (waga rotacji 1.0); szerokie widelki

## Ostrzezenia

- anomalia w `SWAP-SP-LSB`: zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 259075.00 PLN kosztu.
- anomalia w `SWAP-SP-LSG`: zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 259075.00 PLN kosztu.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
