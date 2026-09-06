# [13] WRAZLIWOSC

**Status:** degraded · **run:** `20260905T181301` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **0.35 ms**

Ranking koncowy 6 dopuszczalnych opcji. Rekomendacja: `REBOOK-OWN` (88103.99 PLN), oszczednosc wobec opcji domyslnej `HOLD`: 83498.49 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | REBOOK-OWN | - |
| `strata_rekomendacji` | 88103.99 PLN | PLN |
| `widelki_min` | 82597.49 PLN | PLN |
| `widelki_max` | 113800.99 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 171602.48 PLN | PLN |
| `oszczednosc` | 83498.49 PLN | PLN |
| `prog_oplacalnosci` | 120 | min |
| `opcji_w_rankingu` | 6 | szt |

## Co ten node ustalil

- opcja domyslna to `HOLD` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `REBOOK-OWN` pozostaje najlepsza w calym badanym zakresie do +120 min
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie
- przy bliskiej czolowce decyzja nalezy do czlowieka, nie do rankingu

## Szczegoly

- **ranking_koncowy**
  - **REBOOK-OWN**
    - **pozycja:** 1
    - **strata**
      - **minor:** 8 810 399
      - **currency:** PLN
      - **major:** 88103.99
    - **min**
      - **minor:** 8 259 749
      - **currency:** PLN
      - **major:** 82597.49
    - **max**
      - **minor:** 11 380 099
      - **currency:** PLN
      - **major:** 113800.99
    - **oszczednosc**
      - **minor:** 8 349 849
      - **currency:** PLN
      - **major:** 83498.49
    - **wskaznik:** 9 458 411.20
    - **uwaga_polityki:** 22 utraconych przesiadek; szerokie widelki
  - **CANCEL**
    - **pozycja:** 2
    - **strata**
      - **minor:** 9 355 289
      - **currency:** PLN
      - **major:** 93552.89
    - **min**
      - **minor:** 8 770 583
      - **currency:** PLN
      - **major:** 87705.83
    - **max**
      - **minor:** 12 083 915
      - **currency:** PLN
      - **major:** 120839.15
    - **oszczednosc**
      - **minor:** 7 804 959
      - **currency:** PLN
      - **major:** 78049.59
    - **wskaznik:** 10 043 378.31
    - **uwaga_polityki:** 22 utraconych przesiadek; szerokie widelki
  - **SPLIT**
    - **pozycja:** 3
    - **strata**
      - **minor:** 9 611 059
      - **currency:** PLN
      - **major:** 96110.59
    - **min**
      - **minor:** 9 010 368
      - **currency:** PLN
      - **major:** 90103.68
    - **max**
      - **minor:** 12 414 285
      - **currency:** PLN
      - **major:** 124142.85
    - **oszczednosc**
      - **minor:** 7 549 189
      - **currency:** PLN
      - **major:** 75491.89
    - **wskaznik:** 10 317 960.40
    - **uwaga_polityki:** 22 utraconych przesiadek; szerokie widelki
  - **REBOOK-OAL**
    - **pozycja:** 4
    - **strata**
      - **minor:** 10 383 124
      - **currency:** PLN
      - **major:** 103831.24
    - **min**
      - **minor:** 9 734 179
      - **currency:** PLN
      - **major:** 97341.79
    - **max**
      - **minor:** 13 411 535
      - **currency:** PLN
      - **major:** 134115.35
    - **oszczednosc**
      - **minor:** 6 777 124
      - **currency:** PLN
      - **major:** 67771.24
    - **wskaznik:** 11 146 811.41
    - **uwaga_polityki:** 22 utraconych przesiadek; szerokie widelki
  - **OVERNIGHT**
    - **pozycja:** 5
    - **strata**
      - **minor:** 11 380 214
      - **currency:** PLN
      - **major:** 113802.14
    - **min**
      - **minor:** 10 668 951
      - **currency:** PLN
      - **major:** 106689.51
    - **max**
      - **minor:** 14 699 443
      - **currency:** PLN
      - **major:** 146994.43
    - **oszczednosc**
      - **minor:** 5 780 034
      - **currency:** PLN
      - **major:** 57800.34
    - **wskaznik:** 12 217 238.21
    - **uwaga_polityki:** 22 utraconych przesiadek; szerokie widelki
  - **HOLD**
    - **pozycja:** 6
    - **strata**
      - **minor:** 17 160 248
      - **currency:** PLN
      - **major:** 171602.48
    - **min**
      - **minor:** 16 087 733
      - **currency:** PLN
      - **major:** 160877.33
    - **max**
      - **minor:** 22 165 320
      - **currency:** PLN
      - **major:** 221653.20
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 22 106 878.23
    - **uwaga_polityki:** propagacja 434 min (waga rotacji 1.0); 22 utraconych przesiadek; szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** REBOOK-OWN
  - **ranking**
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 810 399
        - **currency:** PLN
        - **major:** 88103.99
    - **CANCEL**
      - **strata**
        - **minor:** 9 355 289
        - **currency:** PLN
        - **major:** 93552.89
    - **SPLIT**
      - **strata**
        - **minor:** 9 611 059
        - **currency:** PLN
        - **major:** 96110.59
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 10 383 124
        - **currency:** PLN
        - **major:** 103831.24
    - **OVERNIGHT**
      - **strata**
        - **minor:** 11 380 214
        - **currency:** PLN
        - **major:** 113802.14
    - **HOLD**
      - **strata**
        - **minor:** 17 325 248
        - **currency:** PLN
        - **major:** 173252.48
  - **krok_min:** 60
  - **lider:** REBOOK-OWN
  - **ranking**
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 810 399
        - **currency:** PLN
        - **major:** 88103.99
    - **CANCEL**
      - **strata**
        - **minor:** 9 355 289
        - **currency:** PLN
        - **major:** 93552.89
    - **SPLIT**
      - **strata**
        - **minor:** 9 611 059
        - **currency:** PLN
        - **major:** 96110.59
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 10 383 124
        - **currency:** PLN
        - **major:** 103831.24
    - **OVERNIGHT**
      - **strata**
        - **minor:** 11 380 214
        - **currency:** PLN
        - **major:** 113802.14
    - **HOLD**
      - **strata**
        - **minor:** 17 490 248
        - **currency:** PLN
        - **major:** 174902.48
  - **krok_min:** 120
  - **lider:** REBOOK-OWN
  - **ranking**
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 810 399
        - **currency:** PLN
        - **major:** 88103.99
    - **CANCEL**
      - **strata**
        - **minor:** 9 355 289
        - **currency:** PLN
        - **major:** 93552.89
    - **SPLIT**
      - **strata**
        - **minor:** 9 611 059
        - **currency:** PLN
        - **major:** 96110.59
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 10 383 124
        - **currency:** PLN
        - **major:** 103831.24
    - **OVERNIGHT**
      - **strata**
        - **minor:** 11 380 214
        - **currency:** PLN
        - **major:** 113802.14
    - **HOLD**
      - **strata**
        - **minor:** 17 820 248
        - **currency:** PLN
        - **major:** 178202.48
- **prog_oplacalnosci**
  - **do_minut:** 120
  - **przejmuje:** 
  - **opis:** `REBOOK-OWN` pozostaje najlepsza w calym badanym zakresie do +120 min
- **wagi_polityki**
  - **rot:** 1.00
  - **trf:** 1.00
  - **vuln:** 1.00
  - **unc:** 1.00
  - **cx:** 1.00
  - **crew:** 1.00
- **opcje_odrzucone_przez_prawo:** -
- **karta_wykonania**
  - **option_id:** REBOOK-OWN
  - **label:** Przenies na wlasny rejs LO3852 (+190 min)
  - **what_changes**
    - LO3850: rejs odwolany
    - 55 pasazerow na wlasny rejs (LO3852, odlot 08:45 UTC) -- oczekiwanie 190 min
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX003129:** wlasny rejs
    - **PAX003130:** wlasny rejs
    - **PAX003131:** wlasny rejs
    - **PAX003132:** wlasny rejs
    - **PAX003133:** wlasny rejs
    - **PAX003134:** wlasny rejs
    - **PAX003135:** wlasny rejs
    - **PAX003136:** wlasny rejs
    - **PAX003137:** wlasny rejs
    - **PAX003138:** wlasny rejs
    - **PAX003139:** wlasny rejs
    - **PAX003140:** wlasny rejs
    - **PAX003141:** wlasny rejs
    - **PAX003142:** wlasny rejs
    - **PAX003143:** wlasny rejs
    - **PAX003144:** wlasny rejs
    - **PAX003145:** wlasny rejs
    - **PAX003146:** wlasny rejs
    - **PAX003147:** wlasny rejs
    - **PAX003148:** wlasny rejs
  - **crew_actions**
    - bez zmian dla zalogi
  - **valid_until:** 2026-08-25T05:35:00+00:00
  - **cost_low**
    - **minor:** 8 259 749
    - **currency:** PLN
    - **major:** 82597.49
  - **cost_expected**
    - **minor:** 8 810 399
    - **currency:** PLN
    - **major:** 88103.99
  - **cost_high**
    - **minor:** 11 380 099
    - **currency:** PLN
    - **major:** 113800.99
  - **threshold_note:** `REBOOK-OWN` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Supervisor OCC
  - **second_signature:** 0

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

## Ostrzezenia

- opcje `REBOOK-OWN` i `CANCEL` roznia sie o mniej niz 10% -- roznica moze byc szumem

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
