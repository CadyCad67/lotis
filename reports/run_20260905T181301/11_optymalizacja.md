# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260905T181301` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **3.66 ms**

Ranking wstepny 6 opcji. Najmniejsza strata: `REBOOK-OWN` (88103.99 PLN), najwieksza: `HOLD` (171602.48 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `najlepsza_opcja` | REBOOK-OWN | - |
| `strata_najlepszej` | 88103.99 PLN | PLN |
| `strata_najgorszej` | 171602.48 PLN | PLN |
| `rozpietosc_rankingu` | 83498.49 PLN | PLN |
| `wspolczynnik_dolny` | 0.94 | - |
| `wspolczynnik_gorny` | 1.29 | - |
| `opcji` | 6 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt
- przy zachodzacych widelkach o wyborze decyduja kryteria poza kosztem: node 13 dokłada wage polityki firmy

## Szczegoly

- **ranking_wstepny**
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 7 124 799
      - **currency:** PLN
      - **major:** 71247.99
    - **propagacja**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **strata**
      - **minor:** 8 810 399
      - **currency:** PLN
      - **major:** 88103.99
    - **widelki_min**
      - **minor:** 8 259 749
      - **currency:** PLN
      - **major:** 82597.49
    - **widelki_max**
      - **minor:** 11 380 099
      - **currency:** PLN
      - **major:** 113800.99
    - **rozpietosc**
      - **minor:** 3 120 350
      - **currency:** PLN
      - **major:** 31203.50
    - **pozycja_wstepna:** 1
  - **CANCEL**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 1 289 865
      - **currency:** PLN
      - **major:** 12898.65
    - **koszty**
      - **minor:** 6 379 824
      - **currency:** PLN
      - **major:** 63798.24
    - **propagacja**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **strata**
      - **minor:** 9 355 289
      - **currency:** PLN
      - **major:** 93552.89
    - **widelki_min**
      - **minor:** 8 770 583
      - **currency:** PLN
      - **major:** 87705.83
    - **widelki_max**
      - **minor:** 12 083 915
      - **currency:** PLN
      - **major:** 120839.15
    - **rozpietosc**
      - **minor:** 3 313 332
      - **currency:** PLN
      - **major:** 33133.32
    - **pozycja_wstepna:** 2
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 7 925 459
      - **currency:** PLN
      - **major:** 79254.59
    - **propagacja**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **strata**
      - **minor:** 9 611 059
      - **currency:** PLN
      - **major:** 96110.59
    - **widelki_min**
      - **minor:** 9 010 368
      - **currency:** PLN
      - **major:** 90103.68
    - **widelki_max**
      - **minor:** 12 414 285
      - **currency:** PLN
      - **major:** 124142.85
    - **rozpietosc**
      - **minor:** 3 403 917
      - **currency:** PLN
      - **major:** 34039.17
    - **pozycja_wstepna:** 3
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 8 697 524
      - **currency:** PLN
      - **major:** 86975.24
    - **propagacja**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **strata**
      - **minor:** 10 383 124
      - **currency:** PLN
      - **major:** 103831.24
    - **widelki_min**
      - **minor:** 9 734 179
      - **currency:** PLN
      - **major:** 97341.79
    - **widelki_max**
      - **minor:** 13 411 535
      - **currency:** PLN
      - **major:** 134115.35
    - **rozpietosc**
      - **minor:** 3 677 356
      - **currency:** PLN
      - **major:** 36773.56
    - **pozycja_wstepna:** 4
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 9 694 614
      - **currency:** PLN
      - **major:** 96946.14
    - **propagacja**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **strata**
      - **minor:** 11 380 214
      - **currency:** PLN
      - **major:** 113802.14
    - **widelki_min**
      - **minor:** 10 668 951
      - **currency:** PLN
      - **major:** 106689.51
    - **widelki_max**
      - **minor:** 14 699 443
      - **currency:** PLN
      - **major:** 146994.43
    - **rozpietosc**
      - **minor:** 4 030 492
      - **currency:** PLN
      - **major:** 40304.92
    - **pozycja_wstepna:** 5
  - **HOLD**
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 10 617 264
      - **currency:** PLN
      - **major:** 106172.64
    - **propagacja**
      - **minor:** 6 542 984
      - **currency:** PLN
      - **major:** 65429.84
    - **strata**
      - **minor:** 17 160 248
      - **currency:** PLN
      - **major:** 171602.48
    - **widelki_min**
      - **minor:** 16 087 733
      - **currency:** PLN
      - **major:** 160877.33
    - **widelki_max**
      - **minor:** 22 165 320
      - **currency:** PLN
      - **major:** 221653.20
    - **rozpietosc**
      - **minor:** 6 077 587
      - **currency:** PLN
      - **major:** 60775.87
    - **pozycja_wstepna:** 6
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 16
  - **p25:** 6.00
  - **mediana:** 8.00
  - **p90:** 15.00
  - **punktualnosc15:** 93.80

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

## Ostrzezenia

- widelki opcji `REBOOK-OWN` i `CANCEL` zachodza na siebie -- roznica miedzy nimi nie jest istotna statystycznie

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
