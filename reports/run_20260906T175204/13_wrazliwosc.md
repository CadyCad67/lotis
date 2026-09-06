# [13] WRAZLIWOSC

**Status:** ok · **run:** `20260906T175204` · **snapshot:** `sha256:91cb2a4af61a3714` · **0.56 ms**

Ranking koncowy 5 dopuszczalnych opcji. Rekomendacja: `HOLD` (148598.00 PLN), oszczednosc wobec opcji domyslnej `HOLD`: 0.00 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | HOLD | - |
| `strata_rekomendacji` | 148598.00 PLN | PLN |
| `widelki_min` | 138099.23 PLN | PLN |
| `widelki_max` | 229357.78 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 148598.00 PLN | PLN |
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
      - **minor:** 14 859 800
      - **currency:** PLN
      - **major:** 148598.00
    - **min**
      - **minor:** 13 809 923
      - **currency:** PLN
      - **major:** 138099.23
    - **max**
      - **minor:** 22 935 778
      - **currency:** PLN
      - **major:** 229357.78
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 16 546 548.81
    - **uwaga_polityki:** propagacja 120 min (waga rotacji 1.0); szerokie widelki
  - **SWAP-SP-LSB**
    - **pozycja:** 2
    - **strata**
      - **minor:** 23 568 922
      - **currency:** PLN
      - **major:** 235689.22
    - **min**
      - **minor:** 21 903 727
      - **currency:** PLN
      - **major:** 219037.27
    - **max**
      - **minor:** 36 378 118
      - **currency:** PLN
      - **major:** 363781.18
    - **oszczednosc**
      - **minor:** -8 709 122
      - **currency:** PLN
      - **major:** -87091.22
    - **wskaznik:** 29 749 846.48
    - **uwaga_polityki:** propagacja 136 min (waga rotacji 1.0); 114 utraconych przesiadek; szerokie widelki
  - **SWAP-SP-LSG**
    - **pozycja:** 3
    - **strata**
      - **minor:** 24 451 732
      - **currency:** PLN
      - **major:** 244517.32
    - **min**
      - **minor:** 22 724 164
      - **currency:** PLN
      - **major:** 227241.64
    - **max**
      - **minor:** 37 740 716
      - **currency:** PLN
      - **major:** 377407.16
    - **oszczednosc**
      - **minor:** -9 591 932
      - **currency:** PLN
      - **major:** -95919.32
    - **wskaznik:** 30 864 172.47
    - **uwaga_polityki:** propagacja 136 min (waga rotacji 1.0); 114 utraconych przesiadek; szerokie widelki
  - **OVERNIGHT**
    - **pozycja:** 4
    - **strata**
      - **minor:** 149 296 488
      - **currency:** PLN
      - **major:** 1492964.88
    - **min**
      - **minor:** 138 748 367
      - **currency:** PLN
      - **major:** 1387483.67
    - **max**
      - **minor:** 230 435 883
      - **currency:** PLN
      - **major:** 2304358.83
    - **oszczednosc**
      - **minor:** -134 436 688
      - **currency:** PLN
      - **major:** -1344366.88
    - **wskaznik:** 169 265 866.92
    - **uwaga_polityki:** 114 utraconych przesiadek; szerokie widelki
  - **CANCEL**
    - **pozycja:** 5
    - **strata**
      - **minor:** 178 598 859
      - **currency:** PLN
      - **major:** 1785988.59
    - **min**
      - **minor:** 165 980 462
      - **currency:** PLN
      - **major:** 1659804.62
    - **max**
      - **minor:** 275 663 456
      - **currency:** PLN
      - **major:** 2756634.56
    - **oszczednosc**
      - **minor:** -163 739 059
      - **currency:** PLN
      - **major:** -1637390.59
    - **wskaznik:** 202 487 621.15
    - **uwaga_polityki:** 114 utraconych przesiadek; szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 15 024 800
        - **currency:** PLN
        - **major:** 150248.00
    - **SWAP-SP-LSB**
      - **strata**
        - **minor:** 23 604 922
        - **currency:** PLN
        - **major:** 236049.22
    - **SWAP-SP-LSG**
      - **strata**
        - **minor:** 24 487 732
        - **currency:** PLN
        - **major:** 244877.32
    - **OVERNIGHT**
      - **strata**
        - **minor:** 149 296 488
        - **currency:** PLN
        - **major:** 1492964.88
    - **CANCEL**
      - **strata**
        - **minor:** 178 598 859
        - **currency:** PLN
        - **major:** 1785988.59
  - **krok_min:** 60
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 15 189 800
        - **currency:** PLN
        - **major:** 151898.00
    - **SWAP-SP-LSB**
      - **strata**
        - **minor:** 23 640 922
        - **currency:** PLN
        - **major:** 236409.22
    - **SWAP-SP-LSG**
      - **strata**
        - **minor:** 24 523 732
        - **currency:** PLN
        - **major:** 245237.32
    - **OVERNIGHT**
      - **strata**
        - **minor:** 149 296 488
        - **currency:** PLN
        - **major:** 1492964.88
    - **CANCEL**
      - **strata**
        - **minor:** 178 598 859
        - **currency:** PLN
        - **major:** 1785988.59
  - **krok_min:** 120
  - **lider:** HOLD
  - **ranking**
    - **HOLD**
      - **strata**
        - **minor:** 15 519 800
        - **currency:** PLN
        - **major:** 155198.00
    - **SWAP-SP-LSB**
      - **strata**
        - **minor:** 23 712 922
        - **currency:** PLN
        - **major:** 237129.22
    - **SWAP-SP-LSG**
      - **strata**
        - **minor:** 24 595 732
        - **currency:** PLN
        - **major:** 245957.32
    - **OVERNIGHT**
      - **strata**
        - **minor:** 149 296 488
        - **currency:** PLN
        - **major:** 1492964.88
    - **CANCEL**
      - **strata**
        - **minor:** 178 598 859
        - **currency:** PLN
        - **major:** 1785988.59
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
  - **label:** Wstrzymaj odlot o 120 min
  - **what_changes**
    - LO6: odlot pozniej o 120 min (z 12:10 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO6 pozostaje na sluzbie +120 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-22T12:10:00+00:00
  - **cost_low**
    - **minor:** 13 809 923
    - **currency:** PLN
    - **major:** 138099.23
  - **cost_expected**
    - **minor:** 14 859 800
    - **currency:** PLN
    - **major:** 148598.00
  - **cost_high**
    - **minor:** 22 935 778
    - **currency:** PLN
    - **major:** 229357.78
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Duty Manager OCC
  - **second_signature:** 1

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
