# [13] WRAZLIWOSC

**Status:** ok · **run:** `20260905T231516` · **snapshot:** `sha256:f3c290f4e6930407` · **0.27 ms**

Ranking koncowy 6 dopuszczalnych opcji. Rekomendacja: `HOLD` (33753.66 PLN), oszczednosc wobec opcji domyslnej `HOLD`: 0.00 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | HOLD | - |
| `strata_rekomendacji` | 33753.66 PLN | PLN |
| `widelki_min` | 30589.26 PLN | PLN |
| `widelki_max` | 40785.67 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 33753.66 PLN | PLN |
| `oszczednosc` | 0.00 PLN | PLN |
| `prog_oplacalnosci` | 120 | min |
| `opcji_w_rankingu` | 6 | szt |

## Co ten node ustalil

- opcja domyslna to `HOLD` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie

## Szczegoly

- **ranking_koncowy**
  - **HOLD**
    - **pozycja:** 1
    - **strata**
      - **minor:** 3 375 366
      - **currency:** PLN
      - **major:** 33753.66
    - **min**
      - **minor:** 3 058 926
      - **currency:** PLN
      - **major:** 30589.26
    - **max**
      - **minor:** 4 078 567
      - **currency:** PLN
      - **major:** 40785.67
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 4 058 882.60
    - **uwaga_polityki:** propagacja 138 min (waga rotacji 1.0); 24 utraconych przesiadek; szerokie widelki
  - **REBOOK-OWN**
    - **pozycja:** 2
    - **strata**
      - **minor:** 8 771 613
      - **currency:** PLN
      - **major:** 87716.13
    - **min**
      - **minor:** 7 949 275
      - **currency:** PLN
      - **major:** 79492.75
    - **max**
      - **minor:** 10 599 032
      - **currency:** PLN
      - **major:** 105990.32
    - **oszczednosc**
      - **minor:** -5 396 247
      - **currency:** PLN
      - **major:** -53962.47
    - **wskaznik:** 9 459 979.93
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **CANCEL**
    - **pozycja:** 3
    - **strata**
      - **minor:** 9 099 476
      - **currency:** PLN
      - **major:** 90994.76
    - **min**
      - **minor:** 8 246 401
      - **currency:** PLN
      - **major:** 82464.01
    - **max**
      - **minor:** 10 995 200
      - **currency:** PLN
      - **major:** 109952.00
    - **oszczednosc**
      - **minor:** -5 724 110
      - **currency:** PLN
      - **major:** -57241.10
    - **wskaznik:** 9 813 572.52
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **SPLIT**
    - **pozycja:** 4
    - **strata**
      - **minor:** 9 551 418
      - **currency:** PLN
      - **major:** 95514.18
    - **min**
      - **minor:** 8 655 973
      - **currency:** PLN
      - **major:** 86559.73
    - **max**
      - **minor:** 11 541 296
      - **currency:** PLN
      - **major:** 115412.96
    - **oszczednosc**
      - **minor:** -6 176 052
      - **currency:** PLN
      - **major:** -61760.52
    - **wskaznik:** 10 300 981.42
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **REBOOK-OAL**
    - **pozycja:** 5
    - **strata**
      - **minor:** 10 306 068
      - **currency:** PLN
      - **major:** 103060.68
    - **min**
      - **minor:** 9 339 875
      - **currency:** PLN
      - **major:** 93398.75
    - **max**
      - **minor:** 12 453 165
      - **currency:** PLN
      - **major:** 124531.65
    - **oszczednosc**
      - **minor:** -6 930 702
      - **currency:** PLN
      - **major:** -69307.02
    - **wskaznik:** 11 114 853.83
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
  - **OVERNIGHT**
    - **pozycja:** 6
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
      - **minor:** -8 018 740
      - **currency:** PLN
      - **major:** -80187.40
    - **wskaznik:** 12 288 277.45
    - **uwaga_polityki:** 24 utraconych przesiadek; szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 3 540 366
        - **currency:** PLN
        - **major:** 35403.66
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 771 613
        - **currency:** PLN
        - **major:** 87716.13
    - **CANCEL**
      - **strata**
        - **minor:** 9 099 476
        - **currency:** PLN
        - **major:** 90994.76
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
  - **krok_min:** 60
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 3 705 366
        - **currency:** PLN
        - **major:** 37053.66
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 771 613
        - **currency:** PLN
        - **major:** 87716.13
    - **CANCEL**
      - **strata**
        - **minor:** 9 099 476
        - **currency:** PLN
        - **major:** 90994.76
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
  - **krok_min:** 120
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 4 035 366
        - **currency:** PLN
        - **major:** 40353.66
    - **REBOOK-OWN**
      - **strata**
        - **minor:** 8 771 613
        - **currency:** PLN
        - **major:** 87716.13
    - **CANCEL**
      - **strata**
        - **minor:** 9 099 476
        - **currency:** PLN
        - **major:** 90994.76
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
- **prog_oplacalnosci**
  - **do_minut:** 120
  - **przejmuje:** 
  - **opis:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
- **wagi_polityki**
  - **rot:** 1.00
  - **trf:** 1.00
  - **vuln:** 1.00
  - **unc:** 1.00
  - **cx:** 1.00
  - **crew:** 1.00
- **opcje_odrzucone_przez_prawo:** -
- **karta_wykonania**
  - **option_id:** HOLD
  - **label:** Wstrzymaj odlot o 90 min
  - **what_changes**
    - LO3996: odlot pozniej o 90 min (z 05:35 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO3996 pozostaje na sluzbie +90 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-21T05:35:00+00:00
  - **cost_low**
    - **minor:** 3 058 926
    - **currency:** PLN
    - **major:** 30589.26
  - **cost_expected**
    - **minor:** 3 375 366
    - **currency:** PLN
    - **major:** 33753.66
  - **cost_high**
    - **minor:** 4 078 567
    - **currency:** PLN
    - **major:** 40785.67
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Dyzurny OCC
  - **second_signature:** 0

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
