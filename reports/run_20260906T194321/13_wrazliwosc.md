# [13] WRAZLIWOSC

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **0.43 ms**

Ranking koncowy 3 dopuszczalnych opcji. Rekomendacja: `OVERNIGHT` (1213890.06 PLN), oszczednosc wobec opcji domyslnej `REBOOK-OAL`: 291995.74 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | OVERNIGHT | - |
| `strata_rekomendacji` | 1213890.06 PLN | PLN |
| `widelki_min` | 1140320.97 PLN | PLN |
| `widelki_max` | 2452303.15 PLN | PLN |
| `opcja_domyslna` | REBOOK-OAL | - |
| `strata_opcji_domyslnej` | 1505885.80 PLN | PLN |
| `oszczednosc` | 291995.74 PLN | PLN |
| `prog_oplacalnosci` | 120 | min |
| `opcji_w_rankingu` | 3 | szt |

## Co ten node ustalil

- opcja domyslna to `REBOOK-OAL` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `OVERNIGHT` pozostaje najlepsza w calym badanym zakresie do +120 min
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie

## Szczegoly

- **ranking_koncowy**
  - **OVERNIGHT**
    - **pozycja:** 1
    - **strata**
      - **minor:** 121 389 006
      - **currency:** PLN
      - **major:** 1213890.06
    - **min**
      - **minor:** 114 032 097
      - **currency:** PLN
      - **major:** 1140320.97
    - **max**
      - **minor:** 245 230 315
      - **currency:** PLN
      - **major:** 2452303.15
    - **oszczednosc**
      - **minor:** 29 199 574
      - **currency:** PLN
      - **major:** 291995.74
    - **wskaznik:** 138 894 526.80
    - **uwaga_polityki:** 105 utraconych przesiadek; szerokie widelki
  - **REBOOK-OAL**
    - **pozycja:** 2
    - **strata**
      - **minor:** 150 588 580
      - **currency:** PLN
      - **major:** 1505885.80
    - **min**
      - **minor:** 141 462 000
      - **currency:** PLN
      - **major:** 1414620.00
    - **max**
      - **minor:** 304 219 353
      - **currency:** PLN
      - **major:** 3042193.53
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 172 304 974.31
    - **uwaga_polityki:** 105 utraconych przesiadek; szerokie widelki
  - **CANCEL**
    - **pozycja:** 3
    - **strata**
      - **minor:** 169 173 593
      - **currency:** PLN
      - **major:** 1691735.93
    - **min**
      - **minor:** 158 920 648
      - **currency:** PLN
      - **major:** 1589206.48
    - **max**
      - **minor:** 341 764 834
      - **currency:** PLN
      - **major:** 3417648.34
    - **oszczednosc**
      - **minor:** -18 585 013
      - **currency:** PLN
      - **major:** -185850.13
    - **wskaznik:** 193 570 133.93
    - **uwaga_polityki:** 105 utraconych przesiadek; szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** OVERNIGHT
  - **ranking**
    - **OVERNIGHT**
      - **strata**
        - **minor:** 121 389 006
        - **currency:** PLN
        - **major:** 1213890.06
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 150 588 580
        - **currency:** PLN
        - **major:** 1505885.80
    - **CANCEL**
      - **strata**
        - **minor:** 169 173 593
        - **currency:** PLN
        - **major:** 1691735.93
  - **krok_min:** 60
  - **lider:** OVERNIGHT
  - **ranking**
    - **OVERNIGHT**
      - **strata**
        - **minor:** 121 389 006
        - **currency:** PLN
        - **major:** 1213890.06
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 150 588 580
        - **currency:** PLN
        - **major:** 1505885.80
    - **CANCEL**
      - **strata**
        - **minor:** 169 173 593
        - **currency:** PLN
        - **major:** 1691735.93
  - **krok_min:** 120
  - **lider:** OVERNIGHT
  - **ranking**
    - **OVERNIGHT**
      - **strata**
        - **minor:** 121 389 006
        - **currency:** PLN
        - **major:** 1213890.06
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 150 588 580
        - **currency:** PLN
        - **major:** 1505885.80
    - **CANCEL**
      - **strata**
        - **minor:** 169 173 593
        - **currency:** PLN
        - **major:** 1691735.93
- **prog_oplacalnosci**
  - **do_minut:** 120
  - **przejmuje:** 
  - **opis:** `OVERNIGHT` pozostaje najlepsza w calym badanym zakresie do +120 min
- **wagi_polityki**
  - **rot:** 1.00
  - **trf:** 1.00
  - **vuln:** 1.00
  - **unc:** 1.00
  - **cx:** 1.00
  - **crew:** 1.00
- **opcje_odrzucone_przez_prawo**
  - **HOLD**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
- **karta_wykonania**
  - **option_id:** OVERNIGHT
  - **label:** Nocleg i rejs nastepnego dnia
  - **what_changes**
    - LO82: rejs odwolany
    - 227 pasazerow na wlasny rejs -- oczekiwanie 840 min
    - 227 pasazerow z noclegiem na koszt przewoznika (Art. 9)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX000236:** wlasny rejs
    - **PAX000237:** wlasny rejs
    - **PAX000238:** wlasny rejs
    - **PAX000239:** wlasny rejs
    - **PAX000240:** wlasny rejs
    - **PAX000241:** wlasny rejs
    - **PAX000242:** wlasny rejs
    - **PAX000243:** wlasny rejs
    - **PAX000244:** wlasny rejs
    - **PAX000245:** wlasny rejs
    - **PAX000246:** wlasny rejs
    - **PAX000247:** wlasny rejs
    - **PAX000248:** wlasny rejs
    - **PAX000249:** wlasny rejs
    - **PAX000250:** wlasny rejs
    - **PAX000251:** wlasny rejs
    - **PAX000252:** wlasny rejs
    - **PAX000253:** wlasny rejs
    - **PAX000254:** wlasny rejs
    - **PAX000255:** wlasny rejs
  - **crew_actions**
    - nocleg zalogi poza baza
  - **valid_until:** 2026-08-24T01:15:00+00:00
  - **cost_low**
    - **minor:** 114 032 097
    - **currency:** PLN
    - **major:** 1140320.97
  - **cost_expected**
    - **minor:** 121 389 006
    - **currency:** PLN
    - **major:** 1213890.06
  - **cost_high**
    - **minor:** 245 230 315
    - **currency:** PLN
    - **major:** 2452303.15
  - **threshold_note:** `OVERNIGHT` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Director Network Operations
  - **second_signature:** 1

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
