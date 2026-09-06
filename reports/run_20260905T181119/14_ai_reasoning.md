# [14] AI REASONING

**Status:** degraded · **run:** `20260905T181119` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **28.22 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 3 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 3 | szt |
| `rekomendacja` | REBOOK-OWN | - |
| `przewaga_nad_druga` | 5448.90 PLN | PLN |

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
  - **REBOOK-OWN**
    - **powod:** zakladane oczekiwanie [190] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
  - **CANCEL**
    - **powod:** zakladane oczekiwanie [190] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
  - **SPLIT**
    - **powod:** zakladane oczekiwanie [190] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
- **uzasadnienie**
  - **wybrana:** REBOOK-OWN
  - **label:** Przenies na wlasny rejs LO3852 (+190 min)
  - **strata**
    - **minor:** 8 810 399
    - **currency:** PLN
    - **major:** 88103.99
  - **widelki**
    - **min**
      - **minor:** 8 259 749
      - **currency:** PLN
      - **major:** 82597.49
    - **max**
      - **minor:** 11 380 099
      - **currency:** PLN
      - **major:** 113800.99
  - **najwieksze_skladniki_kosztu**
    - odszkodowanie_art7: 59125.00 PLN
    - rebooking_wlasny_spill: 7449.75 PLN
    - opieka_art9: 3311.00 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** 8 349 849
    - **currency:** PLN
    - **major:** 83498.49
  - **alternatywa**
    - **id:** CANCEL
    - **strata**
      - **minor:** 9 355 289
      - **currency:** PLN
      - **major:** 93552.89
    - **roznica**
      - **minor:** 544 890
      - **currency:** PLN
      - **major:** 5448.90
  - **czolowka_blisko:** 1
  - **uwaga_polityki:** 22 utraconych przesiadek; szerokie widelki

## Ostrzezenia

- anomalia w `REBOOK-OWN`: zakladane oczekiwanie [190] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
- anomalia w `CANCEL`: zakladane oczekiwanie [190] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
- anomalia w `SPLIT`: zakladane oczekiwanie [190] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
