# [13] WRAZLIWOSC

**Status:** degraded · **run:** `20260906T192713` · **snapshot:** `sha256:f3c290f4e6930407` · **0.4 ms**

Ranking koncowy 5 dopuszczalnych opcji. Rekomendacja: `SWAP-SP-LIO` (14158.46 PLN), oszczednosc wobec opcji domyslnej `SWAP-SP-LIO`: 0.00 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | SWAP-SP-LIO | - |
| `strata_rekomendacji` | 14158.46 PLN | PLN |
| `widelki_min` | 12641.49 PLN | PLN |
| `widelki_max` | 15843.99 PLN | PLN |
| `opcja_domyslna` | SWAP-SP-LIO | - |
| `strata_opcji_domyslnej` | 14158.46 PLN | PLN |
| `oszczednosc` | 0.00 PLN | PLN |
| `prog_oplacalnosci` | 120 | min |
| `opcji_w_rankingu` | 5 | szt |

## Co ten node ustalil

- opcja domyslna to `SWAP-SP-LIO` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `SWAP-SP-LIO` pozostaje najlepsza w calym badanym zakresie do +120 min
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie
- przy bliskiej czolowce decyzja nalezy do czlowieka, nie do rankingu

## Szczegoly

- **ranking_koncowy**
  - **SWAP-SP-LIO**
    - **pozycja:** 1
    - **strata**
      - **minor:** 1 415 846
      - **currency:** PLN
      - **major:** 14158.46
    - **min**
      - **minor:** 1 264 149
      - **currency:** PLN
      - **major:** 12641.49
    - **max**
      - **minor:** 1 584 399
      - **currency:** PLN
      - **major:** 15843.99
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 1 762 512.70
    - **uwaga_polityki:** propagacja 29 min (waga rotacji 1.0); szerokie widelki; priorytet 100, indeks pasazerski 0.60
  - **SWAP-SP-LIQ**
    - **pozycja:** 2
    - **strata**
      - **minor:** 1 515 309
      - **currency:** PLN
      - **major:** 15153.09
    - **min**
      - **minor:** 1 352 955
      - **currency:** PLN
      - **major:** 13529.55
    - **max**
      - **minor:** 1 695 702
      - **currency:** PLN
      - **major:** 16957.02
    - **oszczednosc**
      - **minor:** -99 463
      - **currency:** PLN
      - **major:** -994.63
    - **wskaznik:** 1 906 282.01
    - **uwaga_polityki:** propagacja 42 min (waga rotacji 1.0); szerokie widelki; priorytet 100, indeks pasazerski 0.60
  - **OVERNIGHT**
    - **pozycja:** 3
    - **strata**
      - **minor:** 15 732 196
      - **currency:** PLN
      - **major:** 157321.96
    - **min**
      - **minor:** 14 046 604
      - **currency:** PLN
      - **major:** 140466.04
    - **max**
      - **minor:** 17 605 076
      - **currency:** PLN
      - **major:** 176050.76
    - **oszczednosc**
      - **minor:** -14 316 350
      - **currency:** PLN
      - **major:** -143163.50
    - **wskaznik:** 48 990 432.86
    - **uwaga_polityki:** szerokie widelki; priorytet 100, indeks pasazerski 18.00
  - **REBOOK-OAL**
    - **pozycja:** 4
    - **strata**
      - **minor:** 15 925 824
      - **currency:** PLN
      - **major:** 159258.24
    - **min**
      - **minor:** 14 219 486
      - **currency:** PLN
      - **major:** 142194.86
    - **max**
      - **minor:** 17 821 755
      - **currency:** PLN
      - **major:** 178217.55
    - **oszczednosc**
      - **minor:** -14 509 978
      - **currency:** PLN
      - **major:** -145099.78
    - **wskaznik:** 49 593 395.08
    - **uwaga_polityki:** szerokie widelki; priorytet 100, indeks pasazerski 13.42
  - **CANCEL**
    - **pozycja:** 5
    - **strata**
      - **minor:** 17 008 109
      - **currency:** PLN
      - **major:** 170081.09
    - **min**
      - **minor:** 15 185 812
      - **currency:** PLN
      - **major:** 151858.12
    - **max**
      - **minor:** 19 032 883
      - **currency:** PLN
      - **major:** 190328.83
    - **oszczednosc**
      - **minor:** -15 592 263
      - **currency:** PLN
      - **major:** -155922.63
    - **wskaznik:** 52 963 656.30
    - **uwaga_polityki:** szerokie widelki; priorytet 100, indeks pasazerski 24.00
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** SWAP-SP-LIO
  - **ranking**
    - **SWAP-SP-LIO**
      - **strata**
        - **minor:** 1 451 846
        - **currency:** PLN
        - **major:** 14518.46
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 1 551 309
        - **currency:** PLN
        - **major:** 15513.09
    - **OVERNIGHT**
      - **strata**
        - **minor:** 15 732 196
        - **currency:** PLN
        - **major:** 157321.96
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 15 925 824
        - **currency:** PLN
        - **major:** 159258.24
    - **CANCEL**
      - **strata**
        - **minor:** 17 008 109
        - **currency:** PLN
        - **major:** 170081.09
  - **krok_min:** 60
  - **lider:** SWAP-SP-LIO
  - **ranking**
    - **SWAP-SP-LIO**
      - **strata**
        - **minor:** 1 487 846
        - **currency:** PLN
        - **major:** 14878.46
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 1 587 309
        - **currency:** PLN
        - **major:** 15873.09
    - **OVERNIGHT**
      - **strata**
        - **minor:** 15 732 196
        - **currency:** PLN
        - **major:** 157321.96
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 15 925 824
        - **currency:** PLN
        - **major:** 159258.24
    - **CANCEL**
      - **strata**
        - **minor:** 17 008 109
        - **currency:** PLN
        - **major:** 170081.09
  - **krok_min:** 120
  - **lider:** SWAP-SP-LIO
  - **ranking**
    - **SWAP-SP-LIO**
      - **strata**
        - **minor:** 1 559 846
        - **currency:** PLN
        - **major:** 15598.46
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 1 659 309
        - **currency:** PLN
        - **major:** 16593.09
    - **OVERNIGHT**
      - **strata**
        - **minor:** 15 732 196
        - **currency:** PLN
        - **major:** 157321.96
    - **REBOOK-OAL**
      - **strata**
        - **minor:** 15 925 824
        - **currency:** PLN
        - **major:** 159258.24
    - **CANCEL**
      - **strata**
        - **minor:** 17 008 109
        - **currency:** PLN
        - **major:** 170081.09
- **prog_oplacalnosci**
  - **do_minut:** 120
  - **przejmuje:** 
  - **opis:** `SWAP-SP-LIO` pozostaje najlepsza w calym badanym zakresie do +120 min
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
  - **SWAP-SP-LDH**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
- **karta_wykonania**
  - **option_id:** SWAP-SP-LIO
  - **label:** Podmien maszyne na SP-LIO (E75S)
  - **what_changes**
    - podmiana maszyny miedzy LO3981 i LO265
    - LO265: odlot pozniej o 20 min (z 07:25 UTC)
    - LO3981: odlot pozniej o 36 min (z 07:05 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO3981 pozostaje na sluzbie +36 min -- sprawdzic FDP przed odlotem
    - wezwanie zalogi z rezerwy dla rejsu przejmujacego maszyne
  - **valid_until:** 2026-08-21T07:05:00+00:00
  - **cost_low**
    - **minor:** 1 264 149
    - **currency:** PLN
    - **major:** 12641.49
  - **cost_expected**
    - **minor:** 1 415 846
    - **currency:** PLN
    - **major:** 14158.46
  - **cost_high**
    - **minor:** 1 584 399
    - **currency:** PLN
    - **major:** 15843.99
  - **threshold_note:** `SWAP-SP-LIO` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Dyzurny OCC
  - **second_signature:** 0

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

## Ostrzezenia

- opcje `SWAP-SP-LIO` i `SWAP-SP-LIQ` roznia sie o mniej niz 10% -- roznica moze byc szumem

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
