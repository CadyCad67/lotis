# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260906T130726` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **0.3 ms**

Ranking wstepny 9 opcji. Najmniejsza strata: `SWAP-SP-LDH` (60783.55 PLN), najwieksza: `REBOOK-OAL` (99907.92 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `najlepsza_opcja` | SWAP-SP-LDH | - |
| `strata_najlepszej` | 60783.55 PLN | PLN |
| `strata_najgorszej` | 99907.92 PLN | PLN |
| `rozpietosc_rankingu` | 39124.37 PLN | PLN |
| `wspolczynnik_dolny` | 0.94 | - |
| `wspolczynnik_gorny` | 1.28 | - |
| `opcji` | 9 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt
- przy zachodzacych widelkach o wyborze decyduja kryteria poza kosztem: node 13 dokłada wage polityki firmy

## Szczegoly

- **ranking_wstepny**
  - **SWAP-SP-LDH**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 3 243 271
      - **currency:** PLN
      - **major:** 32432.71
    - **propagacja**
      - **minor:** 2 835 084
      - **currency:** PLN
      - **major:** 28350.84
    - **strata**
      - **minor:** 6 078 355
      - **currency:** PLN
      - **major:** 60783.55
    - **widelki_min**
      - **minor:** 5 698 458
      - **currency:** PLN
      - **major:** 56984.58
    - **widelki_max**
      - **minor:** 7 800 555
      - **currency:** PLN
      - **major:** 78005.55
    - **rozpietosc**
      - **minor:** 2 102 097
      - **currency:** PLN
      - **major:** 21020.97
    - **pozycja_wstepna:** 1
  - **SWAP-SP-LIK**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 3 492 916
      - **currency:** PLN
      - **major:** 34929.16
    - **propagacja**
      - **minor:** 2 905 772
      - **currency:** PLN
      - **major:** 29057.72
    - **strata**
      - **minor:** 6 398 688
      - **currency:** PLN
      - **major:** 63986.88
    - **widelki_min**
      - **minor:** 5 998 770
      - **currency:** PLN
      - **major:** 59987.70
    - **widelki_max**
      - **minor:** 8 211 649
      - **currency:** PLN
      - **major:** 82116.49
    - **rozpietosc**
      - **minor:** 2 212 879
      - **currency:** PLN
      - **major:** 22128.79
    - **pozycja_wstepna:** 2
  - **SWAP-SP-LIL**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 3 492 916
      - **currency:** PLN
      - **major:** 34929.16
    - **propagacja**
      - **minor:** 2 905 772
      - **currency:** PLN
      - **major:** 29057.72
    - **strata**
      - **minor:** 6 398 688
      - **currency:** PLN
      - **major:** 63986.88
    - **widelki_min**
      - **minor:** 5 998 770
      - **currency:** PLN
      - **major:** 59987.70
    - **widelki_max**
      - **minor:** 8 211 649
      - **currency:** PLN
      - **major:** 82116.49
    - **rozpietosc**
      - **minor:** 2 212 879
      - **currency:** PLN
      - **major:** 22128.79
    - **pozycja_wstepna:** 3
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 6 245 492
      - **currency:** PLN
      - **major:** 62454.92
    - **propagacja**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **strata**
      - **minor:** 7 810 692
      - **currency:** PLN
      - **major:** 78106.92
    - **widelki_min**
      - **minor:** 7 322 524
      - **currency:** PLN
      - **major:** 73225.24
    - **widelki_max**
      - **minor:** 10 023 721
      - **currency:** PLN
      - **major:** 100237.21
    - **rozpietosc**
      - **minor:** 2 701 197
      - **currency:** PLN
      - **major:** 27011.97
    - **pozycja_wstepna:** 4
  - **HOLD**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 6 243 292
      - **currency:** PLN
      - **major:** 62432.92
    - **propagacja**
      - **minor:** 2 532 768
      - **currency:** PLN
      - **major:** 25327.68
    - **strata**
      - **minor:** 8 776 060
      - **currency:** PLN
      - **major:** 87760.60
    - **widelki_min**
      - **minor:** 8 227 557
      - **currency:** PLN
      - **major:** 82275.57
    - **widelki_max**
      - **minor:** 11 262 610
      - **currency:** PLN
      - **major:** 112626.10
    - **rozpietosc**
      - **minor:** 3 035 053
      - **currency:** PLN
      - **major:** 30350.53
    - **pozycja_wstepna:** 5
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 7 335 542
      - **currency:** PLN
      - **major:** 73355.42
    - **propagacja**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **strata**
      - **minor:** 8 900 742
      - **currency:** PLN
      - **major:** 89007.42
    - **widelki_min**
      - **minor:** 8 344 446
      - **currency:** PLN
      - **major:** 83444.46
    - **widelki_max**
      - **minor:** 11 422 618
      - **currency:** PLN
      - **major:** 114226.18
    - **rozpietosc**
      - **minor:** 3 078 172
      - **currency:** PLN
      - **major:** 30781.72
    - **pozycja_wstepna:** 6
  - **CANCEL**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 2 234 302
      - **currency:** PLN
      - **major:** 22343.02
    - **koszty**
      - **minor:** 5 716 592
      - **currency:** PLN
      - **major:** 57165.92
    - **propagacja**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **strata**
      - **minor:** 9 516 094
      - **currency:** PLN
      - **major:** 95160.94
    - **widelki_min**
      - **minor:** 8 921 339
      - **currency:** PLN
      - **major:** 89213.39
    - **widelki_max**
      - **minor:** 12 212 320
      - **currency:** PLN
      - **major:** 122123.20
    - **rozpietosc**
      - **minor:** 3 290 981
      - **currency:** PLN
      - **major:** 32909.81
    - **pozycja_wstepna:** 7
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 8 295 504
      - **currency:** PLN
      - **major:** 82955.04
    - **propagacja**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **strata**
      - **minor:** 9 860 704
      - **currency:** PLN
      - **major:** 98607.04
    - **widelki_min**
      - **minor:** 9 244 410
      - **currency:** PLN
      - **major:** 92444.10
    - **widelki_max**
      - **minor:** 12 654 570
      - **currency:** PLN
      - **major:** 126545.70
    - **rozpietosc**
      - **minor:** 3 410 160
      - **currency:** PLN
      - **major:** 34101.60
    - **pozycja_wstepna:** 8
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 8 425 592
      - **currency:** PLN
      - **major:** 84255.92
    - **propagacja**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **strata**
      - **minor:** 9 990 792
      - **currency:** PLN
      - **major:** 99907.92
    - **widelki_min**
      - **minor:** 9 366 368
      - **currency:** PLN
      - **major:** 93663.68
    - **widelki_max**
      - **minor:** 12 821 516
      - **currency:** PLN
      - **major:** 128215.16
    - **rozpietosc**
      - **minor:** 3 455 148
      - **currency:** PLN
      - **major:** 34551.48
    - **pozycja_wstepna:** 9
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 17
  - **p25:** 15.00
  - **mediana:** 20.00
  - **p90:** 37.00
  - **punktualnosc15:** 35.30

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

## Ostrzezenia

- widelki opcji `SWAP-SP-LDH` i `SWAP-SP-LIK` zachodza na siebie -- roznica miedzy nimi nie jest istotna statystycznie

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
