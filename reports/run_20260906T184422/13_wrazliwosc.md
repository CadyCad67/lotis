# [13] WRAZLIWOSC

**Status:** ok · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **0.44 ms**

Ranking koncowy 3 dopuszczalnych opcji. Rekomendacja: `HOLD` (0.00 PLN), oszczednosc wobec opcji domyslnej `HOLD`: 0.00 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | HOLD | - |
| `strata_rekomendacji` | 0.00 PLN | PLN |
| `widelki_min` | 0.00 PLN | PLN |
| `widelki_max` | 0.00 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 0.00 PLN | PLN |
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
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **min**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **max**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 0.00
    - **uwaga_polityki:** 
  - **OVERNIGHT**
    - **pozycja:** 2
    - **strata**
      - **minor:** 137 306 246
      - **currency:** PLN
      - **major:** 1373062.46
    - **min**
      - **minor:** 130 829 537
      - **currency:** PLN
      - **major:** 1308295.37
    - **max**
      - **minor:** 213 299 640
      - **currency:** PLN
      - **major:** 2132996.40
    - **oszczednosc**
      - **minor:** -137 306 246
      - **currency:** PLN
      - **major:** -1373062.46
    - **wskaznik:** 138 955 648.06
    - **uwaga_polityki:** szerokie widelki
  - **CANCEL**
    - **pozycja:** 3
    - **strata**
      - **minor:** 178 468 071
      - **currency:** PLN
      - **major:** 1784680.71
    - **min**
      - **minor:** 170 049 766
      - **currency:** PLN
      - **major:** 1700497.66
    - **max**
      - **minor:** 277 242 852
      - **currency:** PLN
      - **major:** 2772428.52
    - **oszczednosc**
      - **minor:** -178 468 071
      - **currency:** PLN
      - **major:** -1784680.71
    - **wskaznik:** 180 611 932.72
    - **uwaga_polityki:** szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 165 000
        - **currency:** PLN
        - **major:** 1650.00
    - **OVERNIGHT**
      - **strata**
        - **minor:** 137 306 246
        - **currency:** PLN
        - **major:** 1373062.46
    - **CANCEL**
      - **strata**
        - **minor:** 178 468 071
        - **currency:** PLN
        - **major:** 1784680.71
  - **krok_min:** 60
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 330 000
        - **currency:** PLN
        - **major:** 3300.00
    - **OVERNIGHT**
      - **strata**
        - **minor:** 137 306 246
        - **currency:** PLN
        - **major:** 1373062.46
    - **CANCEL**
      - **strata**
        - **minor:** 178 468 071
        - **currency:** PLN
        - **major:** 1784680.71
  - **krok_min:** 120
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 660 000
        - **currency:** PLN
        - **major:** 6600.00
    - **OVERNIGHT**
      - **strata**
        - **minor:** 137 306 246
        - **currency:** PLN
        - **major:** 1373062.46
    - **CANCEL**
      - **strata**
        - **minor:** 178 468 071
        - **currency:** PLN
        - **major:** 1784680.71
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
  - **SWAP-SP-LRC**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
  - **SWAP-SP-LRD**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
  - **SWAP-SP-LRH**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
  - **REBOOK-OAL**
    - **reguly**
      - Art. 9 EU261
- **karta_wykonania**
  - **option_id:** HOLD
  - **label:** Wstrzymaj odlot o 0 min
  - **what_changes**
    - bez zmian operacyjnych
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - bez zmian dla zalogi
  - **valid_until:** 2026-08-23T11:00:00+00:00
  - **cost_low**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **cost_expected**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **cost_high**
    - **minor:** 0
    - **currency:** PLN
    - **major:** 0.00
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Dyzurny OCC
  - **second_signature:** 0

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
