# [13] WRAZLIWOSC

**Status:** degraded · **run:** `20260906T190325` · **snapshot:** `sha256:f3c290f4e6930407` · **0.34 ms**

Ranking koncowy 5 dopuszczalnych opcji. Rekomendacja: `SWAP-SP-LIO` (12035.06 PLN), oszczednosc wobec opcji domyslnej `SWAP-SP-LIO`: 0.00 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | SWAP-SP-LIO | - |
| `strata_rekomendacji` | 12035.06 PLN | PLN |
| `widelki_min` | 10745.59 PLN | PLN |
| `widelki_max` | 13467.80 PLN | PLN |
| `opcja_domyslna` | SWAP-SP-LIO | - |
| `strata_opcji_domyslnej` | 12035.06 PLN | PLN |
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
      - **minor:** 1 203 506
      - **currency:** PLN
      - **major:** 12035.06
    - **min**
      - **minor:** 1 074 559
      - **currency:** PLN
      - **major:** 10745.59
    - **max**
      - **minor:** 1 346 780
      - **currency:** PLN
      - **major:** 13467.80
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 1 238 166.72
    - **uwaga_polityki:** propagacja 29 min (waga rotacji 1.0); szerokie widelki
  - **SWAP-SP-LIQ**
    - **pozycja:** 2
    - **strata**
      - **minor:** 1 203 506
      - **currency:** PLN
      - **major:** 12035.06
    - **min**
      - **minor:** 1 074 559
      - **currency:** PLN
      - **major:** 10745.59
    - **max**
      - **minor:** 1 346 780
      - **currency:** PLN
      - **major:** 13467.80
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 1 238 166.72
    - **uwaga_polityki:** propagacja 29 min (waga rotacji 1.0); szerokie widelki
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
      - **minor:** -14 528 690
      - **currency:** PLN
      - **major:** -145286.90
    - **wskaznik:** 15 803 365.44
    - **uwaga_polityki:** szerokie widelki
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
      - **minor:** -14 722 318
      - **currency:** PLN
      - **major:** -147223.18
    - **wskaznik:** 15 997 869.38
    - **uwaga_polityki:** szerokie widelki
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
      - **minor:** -15 804 603
      - **currency:** PLN
      - **major:** -158046.03
    - **wskaznik:** 17 085 050.42
    - **uwaga_polityki:** szerokie widelki
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** SWAP-SP-LIO
  - **ranking**
    - **SWAP-SP-LIO**
      - **strata**
        - **minor:** 1 239 506
        - **currency:** PLN
        - **major:** 12395.06
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 1 239 506
        - **currency:** PLN
        - **major:** 12395.06
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
        - **minor:** 1 275 506
        - **currency:** PLN
        - **major:** 12755.06
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 1 275 506
        - **currency:** PLN
        - **major:** 12755.06
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
        - **minor:** 1 347 506
        - **currency:** PLN
        - **major:** 13475.06
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 1 347 506
        - **currency:** PLN
        - **major:** 13475.06
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
    - LO3981: odlot pozniej o 36 min (z 07:05 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO3981 pozostaje na sluzbie +36 min -- sprawdzic FDP przed odlotem
    - wezwanie zalogi z rezerwy dla rejsu przejmujacego maszyne
  - **valid_until:** 2026-08-21T07:05:00+00:00
  - **cost_low**
    - **minor:** 1 074 559
    - **currency:** PLN
    - **major:** 10745.59
  - **cost_expected**
    - **minor:** 1 203 506
    - **currency:** PLN
    - **major:** 12035.06
  - **cost_high**
    - **minor:** 1 346 780
    - **currency:** PLN
    - **major:** 13467.80
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
