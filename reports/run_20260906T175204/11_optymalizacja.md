# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260906T175204` · **snapshot:** `sha256:91cb2a4af61a3714` · **0.28 ms**

Ranking wstepny 6 opcji. Najmniejsza strata: `HOLD` (148598.00 PLN), najwieksza: `REBOOK-OAL` (1838870.92 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 148598.00 PLN | PLN |
| `strata_najgorszej` | 1838870.92 PLN | PLN |
| `rozpietosc_rankingu` | 1690272.92 PLN | PLN |
| `wspolczynnik_dolny` | 0.93 | - |
| `wspolczynnik_gorny` | 1.54 | - |
| `opcji` | 6 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt
- przy zachodzacych widelkach o wyborze decyduja kryteria poza kosztem: node 13 dokłada wage polityki firmy

## Szczegoly

- **ranking_wstepny**
  - **HOLD**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 7 666 400
      - **currency:** PLN
      - **major:** 76664.00
    - **propagacja**
      - **minor:** 7 193 400
      - **currency:** PLN
      - **major:** 71934.00
    - **strata**
      - **minor:** 14 859 800
      - **currency:** PLN
      - **major:** 148598.00
    - **widelki_min**
      - **minor:** 13 809 923
      - **currency:** PLN
      - **major:** 138099.23
    - **widelki_max**
      - **minor:** 22 935 778
      - **currency:** PLN
      - **major:** 229357.78
    - **rozpietosc**
      - **minor:** 9 125 855
      - **currency:** PLN
      - **major:** 91258.55
    - **pozycja_wstepna:** 1
  - **SWAP-SP-LSB**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 15 416 402
      - **currency:** PLN
      - **major:** 154164.02
    - **propagacja**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **strata**
      - **minor:** 23 568 922
      - **currency:** PLN
      - **major:** 235689.22
    - **widelki_min**
      - **minor:** 21 903 727
      - **currency:** PLN
      - **major:** 219037.27
    - **widelki_max**
      - **minor:** 36 378 118
      - **currency:** PLN
      - **major:** 363781.18
    - **rozpietosc**
      - **minor:** 14 474 391
      - **currency:** PLN
      - **major:** 144743.91
    - **pozycja_wstepna:** 2
  - **SWAP-SP-LSG**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 16 299 212
      - **currency:** PLN
      - **major:** 162992.12
    - **propagacja**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **strata**
      - **minor:** 24 451 732
      - **currency:** PLN
      - **major:** 244517.32
    - **widelki_min**
      - **minor:** 22 724 164
      - **currency:** PLN
      - **major:** 227241.64
    - **widelki_max**
      - **minor:** 37 740 716
      - **currency:** PLN
      - **major:** 377407.16
    - **rozpietosc**
      - **minor:** 15 016 552
      - **currency:** PLN
      - **major:** 150165.52
    - **pozycja_wstepna:** 3
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 124 936 988
      - **currency:** PLN
      - **major:** 1249369.88
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 149 296 488
      - **currency:** PLN
      - **major:** 1492964.88
    - **widelki_min**
      - **minor:** 138 748 367
      - **currency:** PLN
      - **major:** 1387483.67
    - **widelki_max**
      - **minor:** 230 435 883
      - **currency:** PLN
      - **major:** 2304358.83
    - **rozpietosc**
      - **minor:** 91 687 516
      - **currency:** PLN
      - **major:** 916875.16
    - **pozycja_wstepna:** 4
  - **CANCEL**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 52 233 196
      - **currency:** PLN
      - **major:** 522331.96
    - **koszty**
      - **minor:** 102 006 163
      - **currency:** PLN
      - **major:** 1020061.63
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 178 598 859
      - **currency:** PLN
      - **major:** 1785988.59
    - **widelki_min**
      - **minor:** 165 980 462
      - **currency:** PLN
      - **major:** 1659804.62
    - **widelki_max**
      - **minor:** 275 663 456
      - **currency:** PLN
      - **major:** 2756634.56
    - **rozpietosc**
      - **minor:** 109 682 994
      - **currency:** PLN
      - **major:** 1096829.94
    - **pozycja_wstepna:** 5
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 159 527 592
      - **currency:** PLN
      - **major:** 1595275.92
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 183 887 092
      - **currency:** PLN
      - **major:** 1838870.92
    - **widelki_min**
      - **minor:** 170 895 070
      - **currency:** PLN
      - **major:** 1708950.70
    - **widelki_max**
      - **minor:** 283 825 728
      - **currency:** PLN
      - **major:** 2838257.28
    - **rozpietosc**
      - **minor:** 112 930 658
      - **currency:** PLN
      - **major:** 1129306.58
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

## Ostrzezenia

- widelki opcji `HOLD` i `SWAP-SP-LSB` zachodza na siebie -- roznica miedzy nimi nie jest istotna statystycznie

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
