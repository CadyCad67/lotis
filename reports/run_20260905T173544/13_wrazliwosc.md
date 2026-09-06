# [13] WRAZLIWOSC

**Status:** degraded · **run:** `20260905T173544` · **snapshot:** `sha256:f3c290f4e6930407` · **0.29 ms**

Ranking koncowy 6 dopuszczalnych opcji. Rekomendacja: `REBOOK-OWN` (87716.13 PLN), oszczednosc wobec opcji domyslnej `HOLD`: 56445.21 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | REBOOK-OWN | - |
| `strata_rekomendacji` | 87716.13 PLN | PLN |
| `widelki_min` | 79492.74 PLN | PLN |
| `widelki_max` | 105990.32 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 144161.34 PLN | PLN |
| `oszczednosc` | 56445.21 PLN | PLN |
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
      - **minor:** 8 771 613
      - **currency:** PLN
      - **major:** 87716.13
    - **min**
      - **minor:** 7 949 274
      - **currency:** PLN
      - **major:** 79492.74
    - **max**
      - **minor:** 10 599 032
      - **currency:** PLN
      - **major:** 105990.32
    - **oszczednosc**
      - **minor:** 5 644 521
      - **currency:** PLN
      - **major:** 56445.21
    - **wskaznik:** 9 459 979.95
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **CANCEL**
    - **pozycja:** 2
    - **strata**
      - **minor:** 9 241 722
      - **currency:** PLN
      - **major:** 92417.22
    - **min**
      - **minor:** 8 375 311
      - **currency:** PLN
      - **major:** 83753.11
    - **max**
      - **minor:** 11 167 081
      - **currency:** PLN
      - **major:** 111670.81
    - **oszczednosc**
      - **minor:** 5 174 412
      - **currency:** PLN
      - **major:** 51744.12
    - **wskaznik:** 9 966 981.53
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **SPLIT**
    - **pozycja:** 3
    - **strata**
      - **minor:** 9 551 418
      - **currency:** PLN
      - **major:** 95514.18
    - **min**
      - **minor:** 8 655 973
      - **currency:** PLN
      - **major:** 86559.73
    - **max**
      - **minor:** 11 541 297
      - **currency:** PLN
      - **major:** 115412.97
    - **oszczednosc**
      - **minor:** 4 864 716
      - **currency:** PLN
      - **major:** 48647.16
    - **wskaznik:** 10 300 981.44
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **REBOOK-OAL**
    - **pozycja:** 4
    - **strata**
      - **minor:** 10 306 068
      - **currency:** PLN
      - **major:** 103060.68
    - **min**
      - **minor:** 9 339 874
      - **currency:** PLN
      - **major:** 93398.74
    - **max**
      - **minor:** 12 453 165
      - **currency:** PLN
      - **major:** 124531.65
    - **oszczednosc**
      - **minor:** 4 110 066
      - **currency:** PLN
      - **major:** 41100.66
    - **wskaznik:** 11 114 853.86
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **OVERNIGHT**
    - **pozycja:** 5
    - **strata**
      - **minor:** 11 394 106
      - **currency:** PLN
      - **major:** 113941.06
    - **min**
      - **minor:** 10 325 909
      - **currency:** PLN
      - **major:** 103259.09
    - **max**
      - **minor:** 13 767 878
      - **currency:** PLN
      - **major:** 137678.78
    - **oszczednosc**
      - **minor:** 3 022 028
      - **currency:** PLN
      - **major:** 30220.28
    - **wskaznik:** 12 288 277.45
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **HOLD**
    - **pozycja:** 6
    - **strata**
      - **minor:** 14 416 134
      - **currency:** PLN
      - **major:** 144161.34
    - **min**
      - **minor:** 13 064 621
      - **currency:** PLN
      - **major:** 130646.21
    - **max**
      - **minor:** 17 419 495
      - **currency:** PLN
      - **major:** 174194.95
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 18 656 956.98
    - **uwaga_polityki:** propagacja 318 min (waga rotacji 1.0); 24 utraconych przesiadek; szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** REBOOK-OWN
  - **ranking**
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 771 613
        - **currency:** PLN
        - **major:** 87716.13
    - **CANCEL**
      - **strata**
        - **minor:** 9 241 722
        - **currency:** PLN
        - **major:** 92417.22
    - **SPLIT**
      - **strata**
        - **minor:** 9 551 418
        - **currency:** PLN
        - **major:** 95514.18
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 10 306 068
        - **currency:** PLN
        - **major:** 103060.68
    - **OVERNIGHT**
      - **strata**
        - **minor:** 11 394 106
        - **currency:** PLN
        - **major:** 113941.06
    - **HOLD**
      - **strata**
        - **minor:** 14 581 134
        - **currency:** PLN
        - **major:** 145811.34
  - **krok_min:** 60
  - **lider:** REBOOK-OWN
  - **ranking**
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 771 613
        - **currency:** PLN
        - **major:** 87716.13
    - **CANCEL**
      - **strata**
        - **minor:** 9 241 722
        - **currency:** PLN
        - **major:** 92417.22
    - **SPLIT**
      - **strata**
        - **minor:** 9 551 418
        - **currency:** PLN
        - **major:** 95514.18
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 10 306 068
        - **currency:** PLN
        - **major:** 103060.68
    - **OVERNIGHT**
      - **strata**
        - **minor:** 11 394 106
        - **currency:** PLN
        - **major:** 113941.06
    - **HOLD**
      - **strata**
        - **minor:** 14 746 134
        - **currency:** PLN
        - **major:** 147461.34
  - **krok_min:** 120
  - **lider:** REBOOK-OWN
  - **ranking**
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 771 613
        - **currency:** PLN
        - **major:** 87716.13
    - **CANCEL**
      - **strata**
        - **minor:** 9 241 722
        - **currency:** PLN
        - **major:** 92417.22
    - **SPLIT**
      - **strata**
        - **minor:** 9 551 418
        - **currency:** PLN
        - **major:** 95514.18
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 10 306 068
        - **currency:** PLN
        - **major:** 103060.68
    - **OVERNIGHT**
      - **strata**
        - **minor:** 11 394 106
        - **currency:** PLN
        - **major:** 113941.06
    - **HOLD**
      - **strata**
        - **minor:** 15 076 134
        - **currency:** PLN
        - **major:** 150761.34
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
  - **label:** Przenies na wlasny rejs LO3994 (+560 min)
  - **what_changes**
    - LO3996: rejs odwolany
    - 61 pasazerow na wlasny rejs (LO3994, odlot 14:55 UTC) -- oczekiwanie 560 min
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX003776:** wlasny rejs
    - **PAX003777:** wlasny rejs
    - **PAX003778:** wlasny rejs
    - **PAX003779:** wlasny rejs
    - **PAX003780:** wlasny rejs
    - **PAX003781:** wlasny rejs
    - **PAX003782:** wlasny rejs
    - **PAX003783:** wlasny rejs
    - **PAX003784:** wlasny rejs
    - **PAX003785:** wlasny rejs
    - **PAX003786:** wlasny rejs
    - **PAX003787:** wlasny rejs
    - **PAX003788:** wlasny rejs
    - **PAX003789:** wlasny rejs
    - **PAX003790:** wlasny rejs
    - **PAX003791:** wlasny rejs
    - **PAX003792:** wlasny rejs
    - **PAX003793:** wlasny rejs
    - **PAX003794:** wlasny rejs
    - **PAX003795:** wlasny rejs
  - **crew_actions**
    - bez zmian dla zalogi
  - **valid_until:** 2026-08-21T05:35:00+00:00
  - **cost_low**
    - **minor:** 7 949 274
    - **currency:** PLN
    - **major:** 79492.74
  - **cost_expected**
    - **minor:** 8 771 613
    - **currency:** PLN
    - **major:** 87716.13
  - **cost_high**
    - **minor:** 10 599 032
    - **currency:** PLN
    - **major:** 105990.32
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
