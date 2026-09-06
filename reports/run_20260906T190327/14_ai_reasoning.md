# [14] AI REASONING

**Status:** degraded · **run:** `20260906T190327` · **snapshot:** `sha256:f3c290f4e6930407` · **38.27 ms**

Sprawdzono 5 niezmiennikow wyniku. Wszystkie przeszly. Wykryto 2 anomalii.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `kontroli` | 5 | szt |
| `kontroli_nieudanych` | 0 | szt |
| `anomalii` | 2 | szt |
| `rekomendacja` | OVERNIGHT | - |
| `przewaga_nad_druga` | 1936.28 PLN | PLN |

## Co ten node ustalil

- opcje `OVERNIGHT` i `REBOOK-OAL` sa blisko -- rekomendacja nie jest jednoznaczna i czlowiek powinien to zobaczyc
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
  - **wybrana:** OVERNIGHT
  - **label:** Nocleg i rejs nastepnego dnia
  - **strata**
    - **minor:** 15 732 196
    - **currency:** PLN
    - **major:** 157321.96
  - **widelki**
    - **min**
      - **minor:** 14 046 604
      - **currency:** PLN
      - **major:** 140466.04
    - **max**
      - **minor:** 17 605 076
      - **currency:** PLN
      - **major:** 176050.76
  - **najwieksze_skladniki_kosztu**
    - odszkodowanie_art7: 88150.00 PLN
    - opieka_art9: 37507.62 PLN
    - rebooking_wlasny_spill: 11106.90 PLN
  - **oszczednosc_wobec_domyslnej**
    - **minor:** -271 484
    - **currency:** PLN
    - **major:** -2714.84
  - **alternatywa**
    - **id:** REBOOK-OAL
    - **strata**
      - **minor:** 15 925 824
      - **currency:** PLN
      - **major:** 159258.24
    - **roznica**
      - **minor:** 193 628
      - **currency:** PLN
      - **major:** 1936.28
  - **czolowka_blisko:** 1
  - **uwaga_polityki:** szerokie widelki; priorytet 0, indeks pasazerski 18.00

## Ostrzezenia

- anomalia w `HOLD`: zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.
- anomalia w `SWAP-SP-LDH`: zakladane oczekiwanie [180] min lezy w promieniu 45 min od progu 180 min z Art. 7. Opcja jest powyzej progu i nalicza pelne odszkodowanie.

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
