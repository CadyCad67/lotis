# [14] AI REASONING

**Status:** degraded · **run:** `20260906T191046` · **snapshot:** `sha256:f3c290f4e6930407` · **23.02 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 1 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 1 | szt |
| `rekomendacja` | HOLD | - |
| `przewaga_nad_druga` | 545259.14 PLN | PLN |

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
    - **powod:** zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
- **uzasadnienie**
  - **wybrana:** HOLD
  - **label:** Wstrzymaj odlot o 180 min
  - **strata**
    - **minor:** 80 572 260
    - **currency:** PLN
    - **major:** 805722.60
  - **widelki**
    - **min**
      - **minor:** 73 484 886
      - **currency:** PLN
      - **major:** 734848.86
    - **max**
      - **minor:** 140 255 415
      - **currency:** PLN
      - **major:** 1402554.15
  - **najwieksze_skladniki_kosztu**
    - odszkodowanie_art7: 665640.00 PLN
    - opoznienie_w_siatce: 125557.20 PLN
    - roszczenia_mc99: 7430.40 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **alternatywa**
    - **id:** OVERNIGHT
    - **strata**
      - **minor:** 135 098 174
      - **currency:** PLN
      - **major:** 1350981.74
    - **roznica**
      - **minor:** 54 525 914
      - **currency:** PLN
      - **major:** 545259.14
  - **czolowka_blisko:** 0
  - **uwaga_polityki:** 70 utraconych przesiadek; szerokie widelki

## Ostrzezenia

- anomalia w `HOLD`: zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
