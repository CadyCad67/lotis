# [14] AI REASONING

**Status:** degraded · **run:** `20260906T130705` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **44.59 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 1 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 1 | szt |
| `rekomendacja` | SWAP-SP-LDH | - |
| `przewaga_nad_druga` | 3203.33 PLN | PLN |

## Co ten node ustalil

- opcje `SWAP-SP-LDH` i `SWAP-SP-LIK` sa blisko -- rekomendacja nie jest jednoznaczna i czlowiek powinien to zobaczyc
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
- **uzasadnienie**
  - **wybrana:** SWAP-SP-LDH
  - **label:** Podmien maszyne na SP-LDH (E170)
  - **strata**
    - **minor:** 6 078 355
    - **currency:** PLN
    - **major:** 60783.55
  - **widelki**
    - **min**
      - **minor:** 5 698 458
      - **currency:** PLN
      - **major:** 56984.58
    - **max**
      - **minor:** 7 800 555
      - **currency:** PLN
      - **major:** 78005.55
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 30801.96 PLN
    - zaloga: 2365.00 PLN
    - roznica_kosztu_typu: -734.25 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 2 697 705
    - **currency:** PLN
    - **major:** 26977.05
  - **alternatywa**
    - **id:** SWAP-SP-LIK
    - **strata**
      - **minor:** 6 398 688
      - **currency:** PLN
      - **major:** 63986.88
    - **roznica**
      - **minor:** 320 333
      - **currency:** PLN
      - **major:** 3203.33
  - **czolowka_blisko:** 1
  - **uwaga_polityki:** propagacja 204 min (waga rotacji 1.0); szerokie widelki

## Ostrzezenia

- anomalia w `HOLD`: zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
