# [13] WRAZLIWOSC

**Status:** ok · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **0.53 ms**

Ranking koncowy 4 dopuszczalnych opcji. Rekomendacja: `HOLD` (22108.70 PLN), oszczednosc wobec opcji domyslnej `HOLD`: 0.00 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | HOLD | - |
| `strata_rekomendacji` | 22108.70 PLN | PLN |
| `widelki_min` | 20924.31 PLN | PLN |
| `widelki_max` | 29127.33 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 22108.70 PLN | PLN |
| `oszczednosc` | 0.00 PLN | PLN |
| `prog_oplacalnosci` | 120 | min |
| `opcji_w_rankingu` | 4 | szt |

## Co ten node ustalil

- opcja domyslna to `HOLD` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie

## Szczegoly

- **ranking_koncowy**
  - **HOLD**
    - **pozycja:** 1
    - **strata**
      - **minor:** 2 210 870
      - **currency:** PLN
      - **major:** 22108.70
    - **min**
      - **minor:** 2 092 431
      - **currency:** PLN
      - **major:** 20924.31
    - **max**
      - **minor:** 2 912 733
      - **currency:** PLN
      - **major:** 29127.33
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 2 227 276.04
    - **uwaga_polityki:** szerokie widelki
  - **SWAP-SP-LSC**
    - **pozycja:** 2
    - **strata**
      - **minor:** 14 600 938
      - **currency:** PLN
      - **major:** 146009.38
    - **min**
      - **minor:** 13 818 745
      - **currency:** PLN
      - **major:** 138187.45
    - **max**
      - **minor:** 19 236 156
      - **currency:** PLN
      - **major:** 192361.56
    - **oszczednosc**
      - **minor:** -12 390 068
      - **currency:** PLN
      - **major:** -123900.68
    - **wskaznik:** 15 077 018.38
    - **uwaga_polityki:** propagacja 30 min (waga rotacji 1.0); szerokie widelki
  - **OVERNIGHT**
    - **pozycja:** 3
    - **strata**
      - **minor:** 148 203 504
      - **currency:** PLN
      - **major:** 1482035.04
    - **min**
      - **minor:** 140 264 031
      - **currency:** PLN
      - **major:** 1402640.31
    - **max**
      - **minor:** 195 252 235
      - **currency:** PLN
      - **major:** 1952522.35
    - **oszczednosc**
      - **minor:** -145 992 634
      - **currency:** PLN
      - **major:** -1459926.34
    - **wskaznik:** 149 303 268.08
    - **uwaga_polityki:** szerokie widelki
  - **CANCEL**
    - **pozycja:** 4
    - **strata**
      - **minor:** 186 457 661
      - **currency:** PLN
      - **major:** 1864576.61
    - **min**
      - **minor:** 176 468 858
      - **currency:** PLN
      - **major:** 1764688.58
    - **max**
      - **minor:** 245 650 569
      - **currency:** PLN
      - **major:** 2456505.69
    - **oszczednosc**
      - **minor:** -184 246 791
      - **currency:** PLN
      - **major:** -1842467.91
    - **wskaznik:** 187 841 295.22
    - **uwaga_polityki:** szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 2 375 870
        - **currency:** PLN
        - **major:** 23758.70
    - **SWAP-SP-LSC**
      - **strata**
        - **minor:** 14 636 938
        - **currency:** PLN
        - **major:** 146369.38
    - **OVERNIGHT**
      - **strata**
        - **minor:** 148 203 504
        - **currency:** PLN
        - **major:** 1482035.04
    - **CANCEL**
      - **strata**
        - **minor:** 186 457 661
        - **currency:** PLN
        - **major:** 1864576.61
  - **krok_min:** 60
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 2 540 870
        - **currency:** PLN
        - **major:** 25408.70
    - **SWAP-SP-LSC**
      - **strata**
        - **minor:** 14 672 938
        - **currency:** PLN
        - **major:** 146729.38
    - **OVERNIGHT**
      - **strata**
        - **minor:** 148 203 504
        - **currency:** PLN
        - **major:** 1482035.04
    - **CANCEL**
      - **strata**
        - **minor:** 186 457 661
        - **currency:** PLN
        - **major:** 1864576.61
  - **krok_min:** 120
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 2 870 870
        - **currency:** PLN
        - **major:** 28708.70
    - **SWAP-SP-LSC**
      - **strata**
        - **minor:** 14 744 938
        - **currency:** PLN
        - **major:** 147449.38
    - **OVERNIGHT**
      - **strata**
        - **minor:** 148 203 504
        - **currency:** PLN
        - **major:** 1482035.04
    - **CANCEL**
      - **strata**
        - **minor:** 186 457 661
        - **currency:** PLN
        - **major:** 1864576.61
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
  - **SWAP-SP-LRD**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
  - **SWAP-SP-LRG**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
  - **REBOOK-OAL**
    - **reguly**
      - Art. 9 EU261
- **karta_wykonania**
  - **option_id:** HOLD
  - **label:** Wstrzymaj odlot o 30 min
  - **what_changes**
    - LO21: odlot pozniej o 30 min (z 11:20 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO21 pozostaje na sluzbie +30 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-26T11:20:00+00:00
  - **cost_low**
    - **minor:** 2 092 431
    - **currency:** PLN
    - **major:** 20924.31
  - **cost_expected**
    - **minor:** 2 210 870
    - **currency:** PLN
    - **major:** 22108.70
  - **cost_high**
    - **minor:** 2 912 733
    - **currency:** PLN
    - **major:** 29127.33
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Dyzurny OCC
  - **second_signature:** 0

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
