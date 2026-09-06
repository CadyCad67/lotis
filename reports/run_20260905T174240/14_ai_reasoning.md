# [14] AI REASONING

**Status:** ok · **run:** `20260905T174240` · **snapshot:** `sha256:f3c290f4e6930407` · **34.83 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 0 | szt |
| `rekomendacja` | HOLD | - |
| `przewaga_nad_druga` | 53962.47 PLN | PLN |

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
- **anomalie:** -
- **uzasadnienie**
  - **wybrana:** HOLD
  - **label:** Wstrzymaj odlot o 90 min
  - **strata**
    - **minor:** 3 375 366
    - **currency:** PLN
    - **major:** 33753.66
  - **widelki**
    - **min**
      - **minor:** 3 058 925
      - **currency:** PLN
      - **major:** 30589.25
    - **max**
      - **minor:** 4 078 567
      - **currency:** PLN
      - **major:** 40785.67
  - **najwieksze_skladniki_kosztu**
    - opoznienie_w_siatce: 12687.30 PLN
    - zaloga: 1612.50 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** REBOOK-OWN
    - **strata**
      - **minor:** 8 771 613
      - **currency:** PLN
      - **major:** 87716.13
    - **roznica**
      - **minor:** 5 396 247
      - **currency:** PLN
      - **major:** 53962.47
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** propagacja 138 min (waga rotacji 1.0); 24 utraconych przesiadek; szerokie widelki

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
