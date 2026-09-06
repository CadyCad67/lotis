# [14] AI REASONING

**Status:** degraded · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **36.44 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 5 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 5 | szt |
| `rekomendacja` | HOLD | - |
| `przewaga_nad_druga` | 1373062.46 PLN | PLN |

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
  - **HOLD**
    - **powod:** strata bliska zeru (0.00 PLN) mimo 256 dotknietych pasazerow
  - **HOLD**
    - **powod:** opcja dotyka pasazerow, a nie ma zadnego skladnika kosztu
  - **SWAP-SP-LRC**
    - **powod:** zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 275200.00 PLN kosztu.
  - **SWAP-SP-LRD**
    - **powod:** zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 275200.00 PLN kosztu.
  - **SWAP-SP-LRH**
    - **powod:** zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 275200.00 PLN kosztu.
- **uzasadnienie**
  - **wybrana:** HOLD
  - **label:** Wstrzymaj odlot o 0 min
  - **strata**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **widelki**
    - **min**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **max**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
  - **najwieksze_skladniki_kosztu:** -
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** OVERNIGHT
    - **strata**
      - **minor:** 137 306 246
      - **currency:** PLN
      - **major:** 1373062.46
    - **roznica**
      - **minor:** 137 306 246
      - **currency:** PLN
      - **major:** 1373062.46
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** 

## Ostrzezenia

- anomalia w `HOLD`: strata bliska zeru (0.00 PLN) mimo 256 dotknietych pasazerow
- anomalia w `HOLD`: opcja dotyka pasazerow, a nie ma zadnego skladnika kosztu
- anomalia w `SWAP-SP-LRC`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 275200.00 PLN kosztu.
- anomalia w `SWAP-SP-LRD`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 275200.00 PLN kosztu.
- anomalia w `SWAP-SP-LRH`: zakladane oczekiwanie [139] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 41 min dodaje okolo 275200.00 PLN kosztu.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
