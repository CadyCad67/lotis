# [14] AI REASONING

**Status:** degraded · **run:** `20260906T190133` · **snapshot:** `sha256:f3c290f4e6930407` · **33.51 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 1 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 1 | szt |
| `rekomendacja` | REBOOK-OWN | - |
| `przewaga_nad_druga` | 3278.63 PLN | PLN |

## Co ten node ustalil

- opcje `REBOOK-OWN` i `CANCEL` sa blisko -- rekomendacja nie jest jednoznaczna i czlowiek powinien to zobaczyc
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
  - **wybrana:** REBOOK-OWN
  - **label:** Przenies na wlasny rejs LO3994 (+560 min)
  - **strata**
    - **minor:** 8 771 613
    - **currency:** PLN
    - **major:** 87716.13
  - **widelki**
    - **min**
      - **minor:** 7 949 275
      - **currency:** PLN
      - **major:** 79492.75
    - **max**
      - **minor:** 10 599 032
      - **currency:** PLN
      - **major:** 105990.32
  - **najwieksze_skladniki_kosztu**
    - odszkodowanie_art7: 65575.00 PLN
    - rebooking_wlasny_spill: 8262.45 PLN
    - opieka_art9: 5770.60 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 5 644 521
    - **currency:** PLN
    - **major:** 56445.21
  - **alternatywa**
    - **id:** CANCEL
    - **strata**
      - **minor:** 9 099 476
      - **currency:** PLN
      - **major:** 90994.76
    - **roznica**
      - **minor:** 327 863
      - **currency:** PLN
      - **major:** 3278.63
  - **czolowka_blisko:** 1
  - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki

## Ostrzezenia

- anomalia w `HOLD`: zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
