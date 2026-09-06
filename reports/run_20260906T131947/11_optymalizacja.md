# [11] OPTIMIZATION ENGINE

**Status:** ok · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **0.24 ms**

Ranking wstepny 7 opcji. Najmniejsza strata: `HOLD` (22108.70 PLN), najwieksza: `REBOOK-OAL` (2200256.68 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 22108.70 PLN | PLN |
| `strata_najgorszej` | 2200256.68 PLN | PLN |
| `rozpietosc_rankingu` | 2178147.98 PLN | PLN |
| `wspolczynnik_dolny` | 0.95 | - |
| `wspolczynnik_gorny` | 1.32 | - |
| `opcji` | 7 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt

## Szczegoly

- **ranking_wstepny**
  - **HOLD**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 2 210 870
      - **currency:** PLN
      - **major:** 22108.70
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 2 210 870
      - **currency:** PLN
      - **major:** 22108.70
    - **widelki_min**
      - **minor:** 2 092 431
      - **currency:** PLN
      - **major:** 20924.31
    - **widelki_max**
      - **minor:** 2 912 733
      - **currency:** PLN
      - **major:** 29127.33
    - **rozpietosc**
      - **minor:** 820 302
      - **currency:** PLN
      - **major:** 8203.02
    - **pozycja_wstepna:** 1
  - **SWAP-SP-LSC**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 12 508 318
      - **currency:** PLN
      - **major:** 125083.18
    - **propagacja**
      - **minor:** 2 092 620
      - **currency:** PLN
      - **major:** 20926.20
    - **strata**
      - **minor:** 14 600 938
      - **currency:** PLN
      - **major:** 146009.38
    - **widelki_min**
      - **minor:** 13 818 745
      - **currency:** PLN
      - **major:** 138187.45
    - **widelki_max**
      - **minor:** 19 236 156
      - **currency:** PLN
      - **major:** 192361.56
    - **rozpietosc**
      - **minor:** 5 417 411
      - **currency:** PLN
      - **major:** 54174.11
    - **pozycja_wstepna:** 2
  - **SWAP-SP-LRD**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 5 522 202
      - **currency:** PLN
      - **major:** 55222.02
    - **koszty**
      - **minor:** 16 900 483
      - **currency:** PLN
      - **major:** 169004.83
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 22 422 685
      - **currency:** PLN
      - **major:** 224226.85
    - **widelki_min**
      - **minor:** 21 221 470
      - **currency:** PLN
      - **major:** 212214.70
    - **widelki_max**
      - **minor:** 29 540 997
      - **currency:** PLN
      - **major:** 295409.97
    - **rozpietosc**
      - **minor:** 8 319 527
      - **currency:** PLN
      - **major:** 83195.27
    - **pozycja_wstepna:** 3
  - **SWAP-SP-LRG**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 5 522 202
      - **currency:** PLN
      - **major:** 55222.02
    - **koszty**
      - **minor:** 19 892 228
      - **currency:** PLN
      - **major:** 198922.28
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 25 414 430
      - **currency:** PLN
      - **major:** 254144.30
    - **widelki_min**
      - **minor:** 24 052 943
      - **currency:** PLN
      - **major:** 240529.43
    - **widelki_max**
      - **minor:** 33 482 503
      - **currency:** PLN
      - **major:** 334825.03
    - **rozpietosc**
      - **minor:** 9 429 560
      - **currency:** PLN
      - **major:** 94295.60
    - **pozycja_wstepna:** 4
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 148 203 504
      - **currency:** PLN
      - **major:** 1482035.04
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 148 203 504
      - **currency:** PLN
      - **major:** 1482035.04
    - **widelki_min**
      - **minor:** 140 264 031
      - **currency:** PLN
      - **major:** 1402640.31
    - **widelki_max**
      - **minor:** 195 252 235
      - **currency:** PLN
      - **major:** 1952522.35
    - **rozpietosc**
      - **minor:** 54 988 204
      - **currency:** PLN
      - **major:** 549882.04
    - **pozycja_wstepna:** 5
  - **CANCEL**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 65 097 982
      - **currency:** PLN
      - **major:** 650979.82
    - **koszty**
      - **minor:** 121 359 679
      - **currency:** PLN
      - **major:** 1213596.79
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 186 457 661
      - **currency:** PLN
      - **major:** 1864576.61
    - **widelki_min**
      - **minor:** 176 468 858
      - **currency:** PLN
      - **major:** 1764688.58
    - **widelki_max**
      - **minor:** 245 650 569
      - **currency:** PLN
      - **major:** 2456505.69
    - **rozpietosc**
      - **minor:** 69 181 711
      - **currency:** PLN
      - **major:** 691817.11
    - **pozycja_wstepna:** 6
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 220 025 668
      - **currency:** PLN
      - **major:** 2200256.68
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 220 025 668
      - **currency:** PLN
      - **major:** 2200256.68
    - **widelki_min**
      - **minor:** 208 238 579
      - **currency:** PLN
      - **major:** 2082385.79
    - **widelki_max**
      - **minor:** 289 875 086
      - **currency:** PLN
      - **major:** 2898750.86
    - **rozpietosc**
      - **minor:** 81 636 507
      - **currency:** PLN
      - **major:** 816365.07
    - **pozycja_wstepna:** 7
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 39
  - **p25:** 33.00
  - **mediana:** 42.00
  - **p90:** 82.00
  - **punktualnosc15:** 0.00

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
