# [13] WRAZLIWOSC

**Status:** ok · **run:** `20260906T191132` · **snapshot:** `sha256:f3c290f4e6930407` · **0.41 ms**

Ranking koncowy 3 dopuszczalnych opcji. Rekomendacja: `HOLD` (805722.60 PLN), oszczednosc wobec opcji domyslnej `HOLD`: 0.00 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | HOLD | - |
| `strata_rekomendacji` | 805722.60 PLN | PLN |
| `widelki_min` | 734848.86 PLN | PLN |
| `widelki_max` | 1402554.15 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 805722.60 PLN | PLN |
| `oszczednosc` | 0.00 PLN | PLN |
| `prog_oplacalnosci` | 120 | min |
| `opcji_w_rankingu` | 3 | szt |

## Co ten node ustalil

- opcja domyslna to `HOLD` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie

## Szczegoly

- **ranking_koncowy**
  - **HOLD**
    - **pozycja:** 1
    - **strata**
      - **minor:** 80 572 260
      - **currency:** PLN
      - **major:** 805722.60
    - **min**
      - **minor:** 73 484 886
      - **currency:** PLN
      - **major:** 734848.86
    - **max**
      - **minor:** 140 255 415
      - **currency:** PLN
      - **major:** 1402554.15
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 91 736 591.05
    - **uwaga_polityki:** 70 utraconych przesiadek; szerokie widelki
  - **OVERNIGHT**
    - **pozycja:** 2
    - **strata**
      - **minor:** 135 098 174
      - **currency:** PLN
      - **major:** 1350981.74
    - **min**
      - **minor:** 123 214 539
      - **currency:** PLN
      - **major:** 1232145.39
    - **max**
      - **minor:** 235 170 895
      - **currency:** PLN
      - **major:** 2351708.95
    - **oszczednosc**
      - **minor:** -54 525 914
      - **currency:** PLN
      - **major:** -545259.14
    - **wskaznik:** 153 817 777.25
    - **uwaga_polityki:** 120 utraconych przesiadek; szerokie widelki
  - **CANCEL**
    - **pozycja:** 3
    - **strata**
      - **minor:** 171 911 211
      - **currency:** PLN
      - **major:** 1719112.11
    - **min**
      - **minor:** 156 789 392
      - **currency:** PLN
      - **major:** 1567893.92
    - **max**
      - **minor:** 299 252 848
      - **currency:** PLN
      - **major:** 2992528.48
    - **oszczednosc**
      - **minor:** -91 338 951
      - **currency:** PLN
      - **major:** -913389.51
    - **wskaznik:** 195 731 737.73
    - **uwaga_polityki:** 120 utraconych przesiadek; szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 80 737 260
        - **currency:** PLN
        - **major:** 807372.60
    - **OVERNIGHT**
      - **strata**
        - **minor:** 135 098 174
        - **currency:** PLN
        - **major:** 1350981.74
    - **CANCEL**
      - **strata**
        - **minor:** 171 911 211
        - **currency:** PLN
        - **major:** 1719112.11
  - **krok_min:** 60
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 80 902 260
        - **currency:** PLN
        - **major:** 809022.60
    - **OVERNIGHT**
      - **strata**
        - **minor:** 135 098 174
        - **currency:** PLN
        - **major:** 1350981.74
    - **CANCEL**
      - **strata**
        - **minor:** 171 911 211
        - **currency:** PLN
        - **major:** 1719112.11
  - **krok_min:** 120
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 81 232 260
        - **currency:** PLN
        - **major:** 812322.60
    - **OVERNIGHT**
      - **strata**
        - **minor:** 135 098 174
        - **currency:** PLN
        - **major:** 1350981.74
    - **CANCEL**
      - **strata**
        - **minor:** 171 911 211
        - **currency:** PLN
        - **major:** 1719112.11
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
- **opcje_odrzucone_przez_prawo**
  - **REBOOK-OAL**
    - **reguly**
      - Art. 9 EU261
- **karta_wykonania**
  - **option_id:** HOLD
  - **label:** Wstrzymaj odlot o 180 min
  - **what_changes**
    - LO2098: odlot pozniej o 180 min (z 00:10 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO2098 pozostaje na sluzbie +180 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-21T00:10:00+00:00
  - **cost_low**
    - **minor:** 73 484 886
    - **currency:** PLN
    - **major:** 734848.86
  - **cost_expected**
    - **minor:** 80 572 260
    - **currency:** PLN
    - **major:** 805722.60
  - **cost_high**
    - **minor:** 140 255 415
    - **currency:** PLN
    - **major:** 1402554.15
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Director Network Operations
  - **second_signature:** 1

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
