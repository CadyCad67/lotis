# [14] AI REASONING

**Status:** degraded · **run:** `20260906T190330` · **snapshot:** `sha256:f3c290f4e6930407` · **39.13 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 2 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 2 | szt |
| `rekomendacja` | SWAP-SP-LIO | - |
| `przewaga_nad_druga` | 2261.40 PLN | PLN |

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
- **anomalie**
  - **HOLD**
    - **powod:** zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
  - **SWAP-SP-LDH**
    - **powod:** zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
- **uzasadnienie**
  - **wybrana:** SWAP-SP-LIO
  - **label:** Podmien maszyne na SP-LIO (E75S)
  - **strata**
    - **minor:** 6 299 194
    - **currency:** PLN
    - **major:** 62991.94
  - **widelki**
    - **min**
      - **minor:** 5 624 281
      - **currency:** PLN
      - **major:** 56242.81
    - **max**
      - **minor:** 7 049 098
      - **currency:** PLN
      - **major:** 70490.98
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 32564.16 PLN
    - zaloga: 2365.00 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 9 161 518
    - **currency:** PLN
    - **major:** 91615.18
  - **alternatywa**
    - **id:** SWAP-SP-LIQ
    - **strata**
      - **minor:** 6 525 334
      - **currency:** PLN
      - **major:** 65253.34
    - **roznica**
      - **minor:** 226 140
      - **currency:** PLN
      - **major:** 2261.40
  - **czolowka_blisko:** 1
  - **uwaga_polityki:** propagacja 187 min (waga rotacji 1.0); szerokie widelki; priorytet 100, indeks pasazerski 0.60

## Ostrzezenia

- anomalia w `HOLD`: zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
- anomalia w `SWAP-SP-LDH`: zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
