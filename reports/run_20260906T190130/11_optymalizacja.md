# [11] OPTIMIZATION ENGINE

**Status:** ok · **run:** `20260906T190130` · **snapshot:** `sha256:f3c290f4e6930407` · **3.67 ms**

Ranking wstepny 6 opcji, priorytet 50. Najmniejsza strata: `HOLD` (12553.59 PLN), najwieksza: `OVERNIGHT` (113941.06 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 50 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 12553.59 PLN | PLN |
| `strata_najgorszej` | 113941.06 PLN | PLN |
| `rozpietosc_rankingu` | 101387.47 PLN | PLN |
| `wspolczynnik_dolny` | 0.91 | - |
| `wspolczynnik_gorny` | 1.21 | - |
| `opcji` | 6 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt

## Szczegoly

- **ranking_wstepny**
  - **HOLD**
    - **indeks_pax:** 1.64
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 180 359
      - **currency:** PLN
      - **major:** 1803.59
    - **koszty**
      - **minor:** 1 075 000
      - **currency:** PLN
      - **major:** 10750.00
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 1 255 359
      - **currency:** PLN
      - **major:** 12553.59
    - **widelki_min**
      - **minor:** 1 137 670
      - **currency:** PLN
      - **major:** 11376.70
    - **widelki_max**
      - **minor:** 1 516 892
      - **currency:** PLN
      - **major:** 15168.92
    - **rozpietosc**
      - **minor:** 379 222
      - **currency:** PLN
      - **major:** 3792.22
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 1
  - **REBOOK-OWN**
    - **indeks_pax:** 11.33
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
      - **minor:** 7 949 275
      - **currency:** PLN
      - **major:** 79492.75
    - **widelki_max**
      - **minor:** 10 599 032
      - **currency:** PLN
      - **major:** 105990.32
    - **rozpietosc**
      - **minor:** 2 649 757
      - **currency:** PLN
      - **major:** 26497.57
    - **wynik_wazony:** 0.67
    - **pozycja_wstepna:** 2
  - **SPLIT**
    - **indeks_pax:** 12.39
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
      - **minor:** 11 541 296
      - **currency:** PLN
      - **major:** 115412.96
    - **rozpietosc**
      - **minor:** 2 885 323
      - **currency:** PLN
      - **major:** 28853.23
    - **wynik_wazony:** 0.74
    - **pozycja_wstepna:** 3
  - **REBOOK-OAL**
    - **indeks_pax:** 13.42
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
      - **minor:** 9 339 875
      - **currency:** PLN
      - **major:** 93398.75
    - **widelki_max**
      - **minor:** 12 453 165
      - **currency:** PLN
      - **major:** 124531.65
    - **rozpietosc**
      - **minor:** 3 113 290
      - **currency:** PLN
      - **major:** 31132.90
    - **wynik_wazony:** 0.81
    - **pozycja_wstepna:** 4
  - **CANCEL**
    - **indeks_pax:** 17.33
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 1 154 108
      - **currency:** PLN
      - **major:** 11541.08
    - **koszty**
      - **minor:** 7 283 168
      - **currency:** PLN
      - **major:** 72831.68
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 9 099 476
      - **currency:** PLN
      - **major:** 90994.76
    - **widelki_min**
      - **minor:** 8 246 401
      - **currency:** PLN
      - **major:** 82464.01
    - **widelki_max**
      - **minor:** 10 995 200
      - **currency:** PLN
      - **major:** 109952.00
    - **rozpietosc**
      - **minor:** 2 748 799
      - **currency:** PLN
      - **major:** 27487.99
    - **wynik_wazony:** 0.87
    - **pozycja_wstepna:** 5
  - **OVERNIGHT**
    - **indeks_pax:** 18.00
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
    - **wynik_wazony:** 1.00
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
