# [13] WRAZLIWOSC

**Status:** ok · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **0.55 ms**

Ranking koncowy 5 dopuszczalnych opcji. Rekomendacja: `HOLD` (37149.50 PLN), oszczednosc wobec opcji domyslnej `HOLD`: 0.00 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | HOLD | - |
| `strata_rekomendacji` | 37149.50 PLN | PLN |
| `widelki_min` | 34524.81 PLN | PLN |
| `widelki_max` | 57339.44 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 37149.50 PLN | PLN |
| `oszczednosc` | 0.00 PLN | PLN |
| `prog_oplacalnosci` | 120 | min |
| `opcji_w_rankingu` | 5 | szt |

## Co ten node ustalil

- opcja domyslna to `HOLD` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie

## Szczegoly

- **ranking_koncowy**
  - **HOLD**
    - **pozycja:** 1
    - **strata**
      - **minor:** 3 714 950
      - **currency:** PLN
      - **major:** 37149.50
    - **min**
      - **minor:** 3 452 481
      - **currency:** PLN
      - **major:** 34524.81
    - **max**
      - **minor:** 5 733 944
      - **currency:** PLN
      - **major:** 57339.44
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 3 854 593.74
    - **uwaga_polityki:** propagacja 30 min (waga rotacji 1.0); szerokie widelki
  - **SWAP-SP-LSB**
    - **pozycja:** 2
    - **strata**
      - **minor:** 17 291 062
      - **currency:** PLN
      - **major:** 172910.62
    - **min**
      - **minor:** 16 069 411
      - **currency:** PLN
      - **major:** 160694.11
    - **max**
      - **minor:** 26 688 378
      - **currency:** PLN
      - **major:** 266883.78
    - **oszczednosc**
      - **minor:** -13 576 112
      - **currency:** PLN
      - **major:** -135761.12
    - **wskaznik:** 21 825 624.45
    - **uwaga_polityki:** propagacja 136 min (waga rotacji 1.0); 114 utraconych przesiadek; szerokie widelki
  - **SWAP-SP-LSG**
    - **pozycja:** 3
    - **strata**
      - **minor:** 18 173 872
      - **currency:** PLN
      - **major:** 181738.72
    - **min**
      - **minor:** 16 889 849
      - **currency:** PLN
      - **major:** 168898.49
    - **max**
      - **minor:** 28 050 976
      - **currency:** PLN
      - **major:** 280509.76
    - **oszczednosc**
      - **minor:** -14 458 922
      - **currency:** PLN
      - **major:** -144589.22
    - **wskaznik:** 22 939 950.42
    - **uwaga_polityki:** propagacja 136 min (waga rotacji 1.0); 114 utraconych przesiadek; szerokie widelki
  - **OVERNIGHT**
    - **pozycja:** 4
    - **strata**
      - **minor:** 118 207 488
      - **currency:** PLN
      - **major:** 1182074.88
    - **min**
      - **minor:** 109 855 873
      - **currency:** PLN
      - **major:** 1098558.73
    - **max**
      - **minor:** 182 450 688
      - **currency:** PLN
      - **major:** 1824506.88
    - **oszczednosc**
      - **minor:** -114 492 538
      - **currency:** PLN
      - **major:** -1144925.38
    - **wskaznik:** 134 018 510.42
    - **uwaga_polityki:** 114 utraconych przesiadek; szerokie widelki
  - **CANCEL**
    - **pozycja:** 5
    - **strata**
      - **minor:** 147 509 859
      - **currency:** PLN
      - **major:** 1475098.59
    - **min**
      - **minor:** 137 087 967
      - **currency:** PLN
      - **major:** 1370879.67
    - **max**
      - **minor:** 227 678 260
      - **currency:** PLN
      - **major:** 2276782.60
    - **oszczednosc**
      - **minor:** -143 794 909
      - **currency:** PLN
      - **major:** -1437949.09
    - **wskaznik:** 167 240 264.64
    - **uwaga_polityki:** 114 utraconych przesiadek; szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 3 879 950
        - **currency:** PLN
        - **major:** 38799.50
    - **SWAP-SP-LSB**
      - **strata**
        - **minor:** 17 327 062
        - **currency:** PLN
        - **major:** 173270.62
    - **SWAP-SP-LSG**
      - **strata**
        - **minor:** 18 209 872
        - **currency:** PLN
        - **major:** 182098.72
    - **OVERNIGHT**
      - **strata**
        - **minor:** 118 207 488
        - **currency:** PLN
        - **major:** 1182074.88
    - **CANCEL**
      - **strata**
        - **minor:** 147 509 859
        - **currency:** PLN
        - **major:** 1475098.59
  - **krok_min:** 60
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 4 044 950
        - **currency:** PLN
        - **major:** 40449.50
    - **SWAP-SP-LSB**
      - **strata**
        - **minor:** 17 363 062
        - **currency:** PLN
        - **major:** 173630.62
    - **SWAP-SP-LSG**
      - **strata**
        - **minor:** 18 245 872
        - **currency:** PLN
        - **major:** 182458.72
    - **OVERNIGHT**
      - **strata**
        - **minor:** 118 207 488
        - **currency:** PLN
        - **major:** 1182074.88
    - **CANCEL**
      - **strata**
        - **minor:** 147 509 859
        - **currency:** PLN
        - **major:** 1475098.59
  - **krok_min:** 120
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 4 374 950
        - **currency:** PLN
        - **major:** 43749.50
    - **SWAP-SP-LSB**
      - **strata**
        - **minor:** 17 435 062
        - **currency:** PLN
        - **major:** 174350.62
    - **SWAP-SP-LSG**
      - **strata**
        - **minor:** 18 317 872
        - **currency:** PLN
        - **major:** 183178.72
    - **OVERNIGHT**
      - **strata**
        - **minor:** 118 207 488
        - **currency:** PLN
        - **major:** 1182074.88
    - **CANCEL**
      - **strata**
        - **minor:** 147 509 859
        - **currency:** PLN
        - **major:** 1475098.59
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
  - **label:** Wstrzymaj odlot o 30 min
  - **what_changes**
    - LO6: odlot pozniej o 30 min (z 12:10 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO6 pozostaje na sluzbie +30 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-22T12:10:00+00:00
  - **cost_low**
    - **minor:** 3 452 481
    - **currency:** PLN
    - **major:** 34524.81
  - **cost_expected**
    - **minor:** 3 714 950
    - **currency:** PLN
    - **major:** 37149.50
  - **cost_high**
    - **minor:** 5 733 944
    - **currency:** PLN
    - **major:** 57339.44
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Supervisor OCC
  - **second_signature:** 0

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
