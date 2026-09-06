# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260906T190327` · **snapshot:** `sha256:f3c290f4e6930407` · **0.45 ms**

Ranking wstepny 7 opcji, priorytet 0. Najmniejsza strata: `SWAP-SP-LIO` (62991.94 PLN), najwieksza: `CANCEL` (170081.09 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 0 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | SWAP-SP-LIO | - |
| `strata_najlepszej` | 62991.94 PLN | PLN |
| `strata_najgorszej` | 170081.09 PLN | PLN |
| `rozpietosc_rankingu` | 107089.15 PLN | PLN |
| `wspolczynnik_dolny` | 0.89 | - |
| `wspolczynnik_gorny` | 1.12 | - |
| `opcji` | 7 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt
- przy zachodzacych widelkach o wyborze decyduja kryteria poza kosztem: node 13 dokłada wage polityki firmy

## Szczegoly

- **ranking_wstepny**
  - **SWAP-SP-LIO**
    - **indeks_pax:** 0.60
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
      - **minor:** 2 806 278
      - **currency:** PLN
      - **major:** 28062.78
    - **strata**
      - **minor:** 6 299 194
      - **currency:** PLN
      - **major:** 62991.94
    - **widelki_min**
      - **minor:** 5 624 281
      - **currency:** PLN
      - **major:** 56242.81
    - **widelki_max**
      - **minor:** 7 049 098
      - **currency:** PLN
      - **major:** 70490.98
    - **rozpietosc**
      - **minor:** 1 424 817
      - **currency:** PLN
      - **major:** 14248.17
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 1
  - **SWAP-SP-LIQ**
    - **indeks_pax:** 0.60
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
      - **minor:** 3 032 418
      - **currency:** PLN
      - **major:** 30324.18
    - **strata**
      - **minor:** 6 525 334
      - **currency:** PLN
      - **major:** 65253.34
    - **widelki_min**
      - **minor:** 5 826 192
      - **currency:** PLN
      - **major:** 58261.92
    - **widelki_max**
      - **minor:** 7 302 159
      - **currency:** PLN
      - **major:** 73021.59
    - **rozpietosc**
      - **minor:** 1 475 967
      - **currency:** PLN
      - **major:** 14759.67
    - **wynik_wazony:** 0.02
    - **pozycja_wstepna:** 2
  - **SWAP-SP-LDH**
    - **indeks_pax:** 1.51
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 125 373
      - **currency:** PLN
      - **major:** 1253.73
    - **koszty**
      - **minor:** 5 140 770
      - **currency:** PLN
      - **major:** 51407.70
    - **propagacja**
      - **minor:** 2 961 730
      - **currency:** PLN
      - **major:** 29617.30
    - **strata**
      - **minor:** 8 227 873
      - **currency:** PLN
      - **major:** 82278.73
    - **widelki_min**
      - **minor:** 7 346 316
      - **currency:** PLN
      - **major:** 73463.16
    - **widelki_max**
      - **minor:** 9 207 381
      - **currency:** PLN
      - **major:** 92073.81
    - **rozpietosc**
      - **minor:** 1 861 065
      - **currency:** PLN
      - **major:** 18610.65
    - **wynik_wazony:** 0.18
    - **pozycja_wstepna:** 3
  - **HOLD**
    - **indeks_pax:** 3.00
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 12 852 564
      - **currency:** PLN
      - **major:** 128525.64
    - **propagacja**
      - **minor:** 2 608 148
      - **currency:** PLN
      - **major:** 26081.48
    - **strata**
      - **minor:** 15 460 712
      - **currency:** PLN
      - **major:** 154607.12
    - **widelki_min**
      - **minor:** 13 804 208
      - **currency:** PLN
      - **major:** 138042.08
    - **widelki_max**
      - **minor:** 17 301 272
      - **currency:** PLN
      - **major:** 173012.72
    - **rozpietosc**
      - **minor:** 3 497 064
      - **currency:** PLN
      - **major:** 34970.64
    - **wynik_wazony:** 0.86
    - **pozycja_wstepna:** 4
  - **OVERNIGHT**
    - **indeks_pax:** 18.00
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 15 069 996
      - **currency:** PLN
      - **major:** 150699.96
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 15 732 196
      - **currency:** PLN
      - **major:** 157321.96
    - **widelki_min**
      - **minor:** 14 046 604
      - **currency:** PLN
      - **major:** 140466.04
    - **widelki_max**
      - **minor:** 17 605 076
      - **currency:** PLN
      - **major:** 176050.76
    - **rozpietosc**
      - **minor:** 3 558 472
      - **currency:** PLN
      - **major:** 35584.72
    - **wynik_wazony:** 0.88
    - **pozycja_wstepna:** 5
  - **REBOOK-OAL**
    - **indeks_pax:** 13.42
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 15 263 624
      - **currency:** PLN
      - **major:** 152636.24
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 15 925 824
      - **currency:** PLN
      - **major:** 159258.24
    - **widelki_min**
      - **minor:** 14 219 486
      - **currency:** PLN
      - **major:** 142194.86
    - **widelki_max**
      - **minor:** 17 821 755
      - **currency:** PLN
      - **major:** 178217.55
    - **rozpietosc**
      - **minor:** 3 602 269
      - **currency:** PLN
      - **major:** 36022.69
    - **wynik_wazony:** 0.90
    - **pozycja_wstepna:** 6
  - **CANCEL**
    - **indeks_pax:** 24.00
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 1 741 603
      - **currency:** PLN
      - **major:** 17416.03
    - **koszty**
      - **minor:** 14 604 306
      - **currency:** PLN
      - **major:** 146043.06
    - **propagacja**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **strata**
      - **minor:** 17 008 109
      - **currency:** PLN
      - **major:** 170081.09
    - **widelki_min**
      - **minor:** 15 185 812
      - **currency:** PLN
      - **major:** 151858.12
    - **widelki_max**
      - **minor:** 19 032 883
      - **currency:** PLN
      - **major:** 190328.83
    - **rozpietosc**
      - **minor:** 3 847 071
      - **currency:** PLN
      - **major:** 38470.71
    - **wynik_wazony:** 1.00
    - **pozycja_wstepna:** 7
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 11
  - **p25:** 8.00
  - **mediana:** 14.00
  - **p90:** 19.00
  - **punktualnosc15:** 63.60

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

## Ostrzezenia

- widelki opcji `SWAP-SP-LIO` i `SWAP-SP-LIQ` zachodza na siebie -- roznica miedzy nimi nie jest istotna statystycznie

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
