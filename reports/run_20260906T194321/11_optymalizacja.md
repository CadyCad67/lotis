# [11] OPTIMIZATION ENGINE

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **0.44 ms**

Ranking wstepny 4 opcji, priorytet 0. Najmniejsza strata: `HOLD` (33975.27 PLN), najwieksza: `CANCEL` (1691735.93 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 0 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 33975.27 PLN | PLN |
| `strata_najgorszej` | 1691735.93 PLN | PLN |
| `rozpietosc_rankingu` | 1657760.66 PLN | PLN |
| `wspolczynnik_dolny` | 0.94 | - |
| `wspolczynnik_gorny` | 2.02 | - |
| `opcji` | 4 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt

## Szczegoly

- **ranking_wstepny**
  - **HOLD**
    - **indeks_pax:** 0.35
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 1 333 527
      - **currency:** PLN
      - **major:** 13335.27
    - **koszty**
      - **minor:** 2 064 000
      - **currency:** PLN
      - **major:** 20640.00
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 3 397 527
      - **currency:** PLN
      - **major:** 33975.27
    - **widelki_min**
      - **minor:** 3 191 617
      - **currency:** PLN
      - **major:** 31916.17
    - **widelki_max**
      - **minor:** 6 863 690
      - **currency:** PLN
      - **major:** 68636.90
    - **rozpietosc**
      - **minor:** 3 672 073
      - **currency:** PLN
      - **major:** 36720.73
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 1
  - **OVERNIGHT**
    - **indeks_pax:** 18.00
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 95 610 506
      - **currency:** PLN
      - **major:** 956105.06
    - **propagacja**
      - **minor:** 25 778 500
      - **currency:** PLN
      - **major:** 257785.00
    - **strata**
      - **minor:** 121 389 006
      - **currency:** PLN
      - **major:** 1213890.06
    - **widelki_min**
      - **minor:** 114 032 097
      - **currency:** PLN
      - **major:** 1140320.97
    - **widelki_max**
      - **minor:** 245 230 315
      - **currency:** PLN
      - **major:** 2452303.15
    - **rozpietosc**
      - **minor:** 131 198 218
      - **currency:** PLN
      - **major:** 1311982.18
    - **wynik_wazony:** 0.71
    - **pozycja_wstepna:** 2
  - **REBOOK-OAL**
    - **indeks_pax:** 13.42
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 124 810 080
      - **currency:** PLN
      - **major:** 1248100.80
    - **propagacja**
      - **minor:** 25 778 500
      - **currency:** PLN
      - **major:** 257785.00
    - **strata**
      - **minor:** 150 588 580
      - **currency:** PLN
      - **major:** 1505885.80
    - **widelki_min**
      - **minor:** 141 462 000
      - **currency:** PLN
      - **major:** 1414620.00
    - **widelki_max**
      - **minor:** 304 219 353
      - **currency:** PLN
      - **major:** 3042193.53
    - **rozpietosc**
      - **minor:** 162 757 353
      - **currency:** PLN
      - **major:** 1627573.53
    - **wynik_wazony:** 0.89
    - **pozycja_wstepna:** 3
  - **CANCEL**
    - **indeks_pax:** 24.00
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 69 345 862
      - **currency:** PLN
      - **major:** 693458.62
    - **koszty**
      - **minor:** 74 049 231
      - **currency:** PLN
      - **major:** 740492.31
    - **propagacja**
      - **minor:** 25 778 500
      - **currency:** PLN
      - **major:** 257785.00
    - **strata**
      - **minor:** 169 173 593
      - **currency:** PLN
      - **major:** 1691735.93
    - **widelki_min**
      - **minor:** 158 920 648
      - **currency:** PLN
      - **major:** 1589206.48
    - **widelki_max**
      - **minor:** 341 764 834
      - **currency:** PLN
      - **major:** 3417648.34
    - **rozpietosc**
      - **minor:** 182 844 186
      - **currency:** PLN
      - **major:** 1828441.86
    - **wynik_wazony:** 1.00
    - **pozycja_wstepna:** 4
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 19
  - **p25:** 25.00
  - **mediana:** 33.00
  - **p90:** 134.00
  - **punktualnosc15:** 0.00

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
