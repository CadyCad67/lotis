# [11] OPTIMIZATION ENGINE

**Status:** ok · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **0.24 ms**

Ranking wstepny 6 opcji. Najmniejsza strata: `HOLD` (37149.50 PLN), najwieksza: `REBOOK-OAL` (1527980.92 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 37149.50 PLN | PLN |
| `strata_najgorszej` | 1527980.92 PLN | PLN |
| `rozpietosc_rankingu` | 1490831.42 PLN | PLN |
| `wspolczynnik_dolny` | 0.93 | - |
| `wspolczynnik_gorny` | 1.54 | - |
| `opcji` | 6 | szt |

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
      - **minor:** 1 916 600
      - **currency:** PLN
      - **major:** 19166.00
    - **propagacja**
      - **minor:** 1 798 350
      - **currency:** PLN
      - **major:** 17983.50
    - **strata**
      - **minor:** 3 714 950
      - **currency:** PLN
      - **major:** 37149.50
    - **widelki_min**
      - **minor:** 3 452 481
      - **currency:** PLN
      - **major:** 34524.81
    - **widelki_max**
      - **minor:** 5 733 944
      - **currency:** PLN
      - **major:** 57339.44
    - **rozpietosc**
      - **minor:** 2 281 463
      - **currency:** PLN
      - **major:** 22814.63
    - **pozycja_wstepna:** 1
  - **SWAP-SP-LSB**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 9 138 542
      - **currency:** PLN
      - **major:** 91385.42
    - **propagacja**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **strata**
      - **minor:** 17 291 062
      - **currency:** PLN
      - **major:** 172910.62
    - **widelki_min**
      - **minor:** 16 069 411
      - **currency:** PLN
      - **major:** 160694.11
    - **widelki_max**
      - **minor:** 26 688 378
      - **currency:** PLN
      - **major:** 266883.78
    - **rozpietosc**
      - **minor:** 10 618 967
      - **currency:** PLN
      - **major:** 106189.67
    - **pozycja_wstepna:** 2
  - **SWAP-SP-LSG**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 10 021 352
      - **currency:** PLN
      - **major:** 100213.52
    - **propagacja**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **strata**
      - **minor:** 18 173 872
      - **currency:** PLN
      - **major:** 181738.72
    - **widelki_min**
      - **minor:** 16 889 849
      - **currency:** PLN
      - **major:** 168898.49
    - **widelki_max**
      - **minor:** 28 050 976
      - **currency:** PLN
      - **major:** 280509.76
    - **rozpietosc**
      - **minor:** 11 161 127
      - **currency:** PLN
      - **major:** 111611.27
    - **pozycja_wstepna:** 3
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 93 847 988
      - **currency:** PLN
      - **major:** 938479.88
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 118 207 488
      - **currency:** PLN
      - **major:** 1182074.88
    - **widelki_min**
      - **minor:** 109 855 873
      - **currency:** PLN
      - **major:** 1098558.73
    - **widelki_max**
      - **minor:** 182 450 688
      - **currency:** PLN
      - **major:** 1824506.88
    - **rozpietosc**
      - **minor:** 72 594 815
      - **currency:** PLN
      - **major:** 725948.15
    - **pozycja_wstepna:** 4
  - **CANCEL**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **koszty**
      - **minor:** 70 917 163
      - **currency:** PLN
      - **major:** 709171.63
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 147 509 859
      - **currency:** PLN
      - **major:** 1475098.59
    - **widelki_min**
      - **minor:** 137 087 967
      - **currency:** PLN
      - **major:** 1370879.67
    - **widelki_max**
      - **minor:** 227 678 260
      - **currency:** PLN
      - **major:** 2276782.60
    - **rozpietosc**
      - **minor:** 90 590 293
      - **currency:** PLN
      - **major:** 905902.93
    - **pozycja_wstepna:** 5
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 128 438 592
      - **currency:** PLN
      - **major:** 1284385.92
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 152 798 092
      - **currency:** PLN
      - **major:** 1527980.92
    - **widelki_min**
      - **minor:** 142 002 575
      - **currency:** PLN
      - **major:** 1420025.75
    - **widelki_max**
      - **minor:** 235 840 533
      - **currency:** PLN
      - **major:** 2358405.33
    - **rozpietosc**
      - **minor:** 93 837 958
      - **currency:** PLN
      - **major:** 938379.58
    - **pozycja_wstepna:** 6
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 57
  - **p25:** 33.00
  - **mediana:** 46.00
  - **p90:** 121.00
  - **punktualnosc15:** 0.00

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
