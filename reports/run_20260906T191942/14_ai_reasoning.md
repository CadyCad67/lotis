# [14] AI REASONING

**Status:** degraded · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **34.06 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 2 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 2 | szt |
| `rekomendacja` | OVERNIGHT | - |
| `przewaga_nad_druga` | 195448.31 PLN | PLN |

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
  - **SWAP-SP-LRF**
    - **powod:** zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 260150.00 PLN kosztu.
  - **SWAP-SP-LSC**
    - **powod:** zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 260150.00 PLN kosztu.
- **uzasadnienie**
  - **wybrana:** OVERNIGHT
  - **label:** Nocleg i rejs nastepnego dnia
  - **strata**
    - **minor:** 149 747 590
    - **currency:** PLN
    - **major:** 1497475.90
  - **widelki**
    - **min**
      - **minor:** 139 167 598
      - **currency:** PLN
      - **major:** 1391675.98
    - **max**
      - **minor:** 231 132 149
      - **currency:** PLN
      - **major:** 2311321.49
  - **najwieksze_skladniki_kosztu**
    - odszkodowanie_art7: 624360.00 PLN
    - pozycjonowanie: 269610.00 PLN
    - rebooking_wlasny_spill: 236736.50 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** -131 885 403
    - **currency:** PLN
    - **major:** -1318854.03
  - **alternatywa**
    - **id:** CANCEL
    - **strata**
      - **minor:** 169 292 421
      - **currency:** PLN
      - **major:** 1692924.21
    - **roznica**
      - **minor:** 19 544 831
      - **currency:** PLN
      - **major:** 195448.31
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** 99 utraconych przesiadek; szerokie widelki; priorytet 0, indeks pasazerski 18.00

## Ostrzezenia

- anomalia w `SWAP-SP-LRF`: zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 260150.00 PLN kosztu.
- anomalia w `SWAP-SP-LSC`: zakladane oczekiwanie [136] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest PONIZEJ progu, wiec nie nalicza odszkodowania; przesuniecie o 44 min dodaje okolo 260150.00 PLN kosztu.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
