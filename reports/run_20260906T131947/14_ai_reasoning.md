# [14] AI REASONING

**Status:** degraded · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **39.61 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 3 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 3 | szt |
| `rekomendacja` | HOLD | - |
| `przewaga_nad_druga` | 123900.68 PLN | PLN |

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
  - **SWAP-SP-LRD**
    - **powod:** zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 302075.00 PLN kosztu.
  - **SWAP-SP-LRG**
    - **powod:** zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 302075.00 PLN kosztu.
  - **SWAP-SP-LSC**
    - **powod:** zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 302075.00 PLN kosztu.
- **uzasadnienie**
  - **wybrana:** HOLD
  - **label:** Wstrzymaj odlot o 30 min
  - **strata**
    - **minor:** 2 210 870
    - **currency:** PLN
    - **major:** 22108.70
  - **widelki**
    - **min**
      - **minor:** 2 092 431
      - **currency:** PLN
      - **major:** 20924.31
    - **max**
      - **minor:** 2 912 733
      - **currency:** PLN
      - **major:** 29127.33
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 20926.20 PLN
    - zaloga: 1182.50 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** SWAP-SP-LSC
    - **strata**
      - **minor:** 14 600 938
      - **currency:** PLN
      - **major:** 146009.38
    - **roznica**
      - **minor:** 12 390 068
      - **currency:** PLN
      - **major:** 123900.68
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** szerokie widelki

## Ostrzezenia

- anomalia w `SWAP-SP-LRD`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 302075.00 PLN kosztu.
- anomalia w `SWAP-SP-LRG`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 302075.00 PLN kosztu.
- anomalia w `SWAP-SP-LSC`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 302075.00 PLN kosztu.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
