# [13] WRAZLIWOSC

**Status:** degraded · **run:** `20260906T190327` · **snapshot:** `sha256:f3c290f4e6930407` · **0.48 ms**

Ranking koncowy 6 dopuszczalnych opcji. Rekomendacja: `OVERNIGHT` (157321.96 PLN), oszczednosc wobec opcji domyslnej `HOLD`: -2714.84 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | OVERNIGHT | - |
| `strata_rekomendacji` | 157321.96 PLN | PLN |
| `widelki_min` | 140466.04 PLN | PLN |
| `widelki_max` | 176050.76 PLN | PLN |
| `opcja_domyslna` | HOLD | - |
| `strata_opcji_domyslnej` | 154607.12 PLN | PLN |
| `oszczednosc` | -2714.84 PLN | PLN |
| `prog_oplacalnosci` | 30 | min |
| `opcji_w_rankingu` | 6 | szt |

## Co ten node ustalil

- opcja domyslna to `HOLD` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `OVERNIGHT` jest najlepsza do okolo +30 min dodatkowego opoznienia; powyzej przejmuje `SWAP-SP-LIO`
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie
- przy bliskiej czolowce decyzja nalezy do czlowieka, nie do rankingu

## Szczegoly

- **ranking_koncowy**
  - **OVERNIGHT**
    - **pozycja:** 1
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
      - **minor:** -271 484
      - **currency:** PLN
      - **major:** -2714.84
    - **wskaznik:** 632 134.62
    - **uwaga_polityki:** szerokie widelki; priorytet 0, indeks pasazerski 18.00
  - **REBOOK-OAL**
    - **pozycja:** 2
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
      - **minor:** -465 112
      - **currency:** PLN
      - **major:** -4651.12
    - **wskaznik:** 639 914.78
    - **uwaga_polityki:** szerokie widelki; priorytet 0, indeks pasazerski 13.42
  - **CANCEL**
    - **pozycja:** 3
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
      - **minor:** -1 547 397
      - **currency:** PLN
      - **major:** -15473.97
    - **wskaznik:** 683 402.02
    - **uwaga_polityki:** szerokie widelki; priorytet 0, indeks pasazerski 24.00
  - **SWAP-SP-LIO**
    - **pozycja:** 4
    - **strata**
      - **minor:** 6 299 194
      - **currency:** PLN
      - **major:** 62991.94
    - **min**
      - **minor:** 5 624 281
      - **currency:** PLN
      - **major:** 56242.81
    - **max**
      - **minor:** 7 049 098
      - **currency:** PLN
      - **major:** 70490.98
    - **oszczednosc**
      - **minor:** 9 161 518
      - **currency:** PLN
      - **major:** 91615.18
    - **wskaznik:** 6 611 634.90
    - **uwaga_polityki:** propagacja 187 min (waga rotacji 1.0); szerokie widelki; priorytet 0, indeks pasazerski 0.60
  - **SWAP-SP-LIQ**
    - **pozycja:** 5
    - **strata**
      - **minor:** 6 525 334
      - **currency:** PLN
      - **major:** 65253.34
    - **min**
      - **minor:** 5 826 192
      - **currency:** PLN
      - **major:** 58261.92
    - **max**
      - **minor:** 7 302 159
      - **currency:** PLN
      - **major:** 73021.59
    - **oszczednosc**
      - **minor:** 8 935 378
      - **currency:** PLN
      - **major:** 89353.78
    - **wskaznik:** 6 923 061.30
    - **uwaga_polityki:** propagacja 202 min (waga rotacji 1.0); szerokie widelki; priorytet 0, indeks pasazerski 0.60
  - **HOLD**
    - **pozycja:** 6
    - **strata**
      - **minor:** 15 460 712
      - **currency:** PLN
      - **major:** 154607.12
    - **min**
      - **minor:** 13 804 208
      - **currency:** PLN
      - **major:** 138042.08
    - **max**
      - **minor:** 17 301 272
      - **currency:** PLN
      - **major:** 173012.72
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 9 240 221.01
    - **uwaga_polityki:** propagacja 173 min (waga rotacji 1.0); szerokie widelki; priorytet 0, indeks pasazerski 3.00
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** SWAP-SP-LIO
  - **ranking**
    - **SWAP-SP-LIO**
      - **strata**
        - **minor:** 6 335 194
        - **currency:** PLN
        - **major:** 63351.94
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 6 561 334
        - **currency:** PLN
        - **major:** 65613.34
    - **HOLD**
      - **strata**
        - **minor:** 15 625 712
        - **currency:** PLN
        - **major:** 156257.12
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
        - **minor:** 6 371 194
        - **currency:** PLN
        - **major:** 63711.94
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 6 597 334
        - **currency:** PLN
        - **major:** 65973.34
    - **OVERNIGHT**
      - **strata**
        - **minor:** 15 732 196
        - **currency:** PLN
        - **major:** 157321.96
    - **HOLD**
      - **strata**
        - **minor:** 15 790 712
        - **currency:** PLN
        - **major:** 157907.12
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
        - **minor:** 6 443 194
        - **currency:** PLN
        - **major:** 64431.94
    - **SWAP-SP-LIQ**
      - **strata**
        - **minor:** 6 669 334
        - **currency:** PLN
        - **major:** 66693.34
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
    - **HOLD**
      - **strata**
        - **minor:** 16 120 712
        - **currency:** PLN
        - **major:** 161207.12
    - **CANCEL**
      - **strata**
        - **minor:** 17 008 109
        - **currency:** PLN
        - **major:** 170081.09
- **prog_oplacalnosci**
  - **do_minut:** 30
  - **przejmuje:** SWAP-SP-LIO
  - **opis:** `OVERNIGHT` jest najlepsza do okolo +30 min dodatkowego opoznienia; powyzej przejmuje `SWAP-SP-LIO`
- **wagi_polityki**
  - **rot:** 1.00
  - **trf:** 1.00
  - **vuln:** 1.00
  - **unc:** 1.00
  - **cx:** 1.00
  - **crew:** 1.00
- **opcje_odrzucone_przez_prawo**
  - **SWAP-SP-LDH**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
- **karta_wykonania**
  - **option_id:** OVERNIGHT
  - **label:** Nocleg i rejs nastepnego dnia
  - **what_changes**
    - LO3981: rejs odwolany
    - 82 pasazerow na wlasny rejs -- oczekiwanie 840 min
    - 82 pasazerow z noclegiem na koszt przewoznika (Art. 9)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX001266:** wlasny rejs
    - **PAX001293:** wlasny rejs
    - **PAX001320:** wlasny rejs
    - **PAX001328:** wlasny rejs
    - **PAX001373:** wlasny rejs
    - **PAX001379:** wlasny rejs
    - **PAX001387:** wlasny rejs
    - **PAX002053:** wlasny rejs
    - **PAX002084:** wlasny rejs
    - **PAX002086:** wlasny rejs
    - **PAX002089:** wlasny rejs
    - **PAX002097:** wlasny rejs
    - **PAX002105:** wlasny rejs
    - **PAX002130:** wlasny rejs
    - **PAX002136:** wlasny rejs
    - **PAX002137:** wlasny rejs
    - **PAX002156:** wlasny rejs
    - **PAX002163:** wlasny rejs
    - **PAX002169:** wlasny rejs
    - **PAX002171:** wlasny rejs
  - **crew_actions**
    - nocleg zalogi poza baza
  - **valid_until:** 2026-08-21T07:05:00+00:00
  - **cost_low**
    - **minor:** 14 046 604
    - **currency:** PLN
    - **major:** 140466.04
  - **cost_expected**
    - **minor:** 15 732 196
    - **currency:** PLN
    - **major:** 157321.96
  - **cost_high**
    - **minor:** 17 605 076
    - **currency:** PLN
    - **major:** 176050.76
  - **threshold_note:** `OVERNIGHT` jest najlepsza do okolo +30 min dodatkowego opoznienia; powyzej przejmuje `SWAP-SP-LIO`
  - **authorization_role:** Duty Manager OCC
  - **second_signature:** 1

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

## Ostrzezenia

- opcje `OVERNIGHT` i `REBOOK-OAL` roznia sie o mniej niz 10% -- roznica moze byc szumem

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
