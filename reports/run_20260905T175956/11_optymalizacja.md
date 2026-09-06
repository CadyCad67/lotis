# [11] OPTIMIZATION ENGINE

**Status:** ok · **run:** `20260905T175956` · **snapshot:** `sha256:f3c290f4e6930407` · **0.28 ms**

Ranking wstepny 6 opcji. Najmniejsza strata: `HOLD` (33753.66 PLN), najwieksza: `OVERNIGHT` (113941.06 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 33753.66 PLN | PLN |
| `strata_najgorszej` | 113941.06 PLN | PLN |
| `rozpietosc_rankingu` | 80187.40 PLN | PLN |
| `wspolczynnik_dolny` | 0.91 | - |
| `wspolczynnik_gorny` | 1.21 | - |
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
      - **minor:** 1 429 980
      - **currency:** PLN
      - **major:** 14299.80
    - **propagacja**
      - **minor:** 1 945 386
      - **currency:** PLN
      - **major:** 19453.86
    - **strata**
      - **minor:** 3 375 366
      - **currency:** PLN
      - **major:** 33753.66
    - **widelki_min**
      - **minor:** 3 058 925
      - **currency:** PLN
      - **major:** 30589.25
    - **widelki_max**
      - **minor:** 4 078 567
      - **currency:** PLN
      - **major:** 40785.67
    - **rozpietosc**
      - **minor:** 1 019 642
      - **currency:** PLN
      - **major:** 10196.42
    - **pozycja_wstepna:** 1
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 8 109 413
      - **currency:** PLN
      - **major:** 81094.13
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 8 771 613
      - **currency:** PLN
      - **major:** 87716.13
    - **widelki_min**
      - **minor:** 7 949 274
      - **currency:** PLN
      - **major:** 79492.74
    - **widelki_max**
      - **minor:** 10 599 032
      - **currency:** PLN
      - **major:** 105990.32
    - **rozpietosc**
      - **minor:** 2 649 758
      - **currency:** PLN
      - **major:** 26497.58
    - **pozycja_wstepna:** 2
  - **CANCEL**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 1 296 354
      - **currency:** PLN
      - **major:** 12963.54
    - **koszty**
      - **minor:** 7 283 168
      - **currency:** PLN
      - **major:** 72831.68
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 9 241 722
      - **currency:** PLN
      - **major:** 92417.22
    - **widelki_min**
      - **minor:** 8 375 311
      - **currency:** PLN
      - **major:** 83753.11
    - **widelki_max**
      - **minor:** 11 167 081
      - **currency:** PLN
      - **major:** 111670.81
    - **rozpietosc**
      - **minor:** 2 791 770
      - **currency:** PLN
      - **major:** 27917.70
    - **pozycja_wstepna:** 3
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 8 889 218
      - **currency:** PLN
      - **major:** 88892.18
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 9 551 418
      - **currency:** PLN
      - **major:** 95514.18
    - **widelki_min**
      - **minor:** 8 655 973
      - **currency:** PLN
      - **major:** 86559.73
    - **widelki_max**
      - **minor:** 11 541 297
      - **currency:** PLN
      - **major:** 115412.97
    - **rozpietosc**
      - **minor:** 2 885 324
      - **currency:** PLN
      - **major:** 28853.24
    - **pozycja_wstepna:** 4
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 9 643 868
      - **currency:** PLN
      - **major:** 96438.68
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 10 306 068
      - **currency:** PLN
      - **major:** 103060.68
    - **widelki_min**
      - **minor:** 9 339 874
      - **currency:** PLN
      - **major:** 93398.74
    - **widelki_max**
      - **minor:** 12 453 165
      - **currency:** PLN
      - **major:** 124531.65
    - **rozpietosc**
      - **minor:** 3 113 291
      - **currency:** PLN
      - **major:** 31132.91
    - **pozycja_wstepna:** 5
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 10 731 906
      - **currency:** PLN
      - **major:** 107319.06
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 11 394 106
      - **currency:** PLN
      - **major:** 113941.06
    - **widelki_min**
      - **minor:** 10 325 909
      - **currency:** PLN
      - **major:** 103259.09
    - **widelki_max**
      - **minor:** 13 767 878
      - **currency:** PLN
      - **major:** 137678.78
    - **rozpietosc**
      - **minor:** 3 441 969
      - **currency:** PLN
      - **major:** 34419.69
    - **pozycja_wstepna:** 6
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 14
  - **p25:** 5.00
  - **mediana:** 8.00
  - **p90:** 13.00
  - **punktualnosc15:** 92.90

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
