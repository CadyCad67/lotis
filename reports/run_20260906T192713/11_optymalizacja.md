# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260906T192713` · **snapshot:** `sha256:f3c290f4e6930407` · **0.43 ms**

Ranking wstepny 7 opcji, priorytet 100. Najmniejsza strata: `SWAP-SP-LIO` (14158.46 PLN), najwieksza: `CANCEL` (170081.09 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 100 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | SWAP-SP-LIO | - |
| `strata_najlepszej` | 14158.46 PLN | PLN |
| `strata_najgorszej` | 170081.09 PLN | PLN |
| `rozpietosc_rankingu` | 155922.63 PLN | PLN |
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
      - **minor:** 991 576
      - **currency:** PLN
      - **major:** 9915.76
    - **propagacja**
      - **minor:** 424 270
      - **currency:** PLN
      - **major:** 4242.70
    - **strata**
      - **minor:** 1 415 846
      - **currency:** PLN
      - **major:** 14158.46
    - **widelki_min**
      - **minor:** 1 264 149
      - **currency:** PLN
      - **major:** 12641.49
    - **widelki_max**
      - **minor:** 1 584 399
      - **currency:** PLN
      - **major:** 15843.99
    - **rozpietosc**
      - **minor:** 320 250
      - **currency:** PLN
      - **major:** 3202.50
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
      - **minor:** 991 576
      - **currency:** PLN
      - **major:** 9915.76
    - **propagacja**
      - **minor:** 523 733
      - **currency:** PLN
      - **major:** 5237.33
    - **strata**
      - **minor:** 1 515 309
      - **currency:** PLN
      - **major:** 15153.09
    - **widelki_min**
      - **minor:** 1 352 955
      - **currency:** PLN
      - **major:** 13529.55
    - **widelki_max**
      - **minor:** 1 695 702
      - **currency:** PLN
      - **major:** 16957.02
    - **rozpietosc**
      - **minor:** 342 747
      - **currency:** PLN
      - **major:** 3427.47
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 2
  - **HOLD**
    - **indeks_pax:** 1.16
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 83 258
      - **currency:** PLN
      - **major:** 832.58
    - **koszty**
      - **minor:** 1 000 673
      - **currency:** PLN
      - **major:** 10006.73
    - **propagacja**
      - **minor:** 99 463
      - **currency:** PLN
      - **major:** 994.63
    - **strata**
      - **minor:** 1 183 394
      - **currency:** PLN
      - **major:** 11833.94
    - **widelki_min**
      - **minor:** 1 056 602
      - **currency:** PLN
      - **major:** 10566.02
    - **widelki_max**
      - **minor:** 1 324 274
      - **currency:** PLN
      - **major:** 13242.74
    - **rozpietosc**
      - **minor:** 267 672
      - **currency:** PLN
      - **major:** 2676.72
    - **wynik_wazony:** 0.02
    - **pozycja_wstepna:** 3
  - **SWAP-SP-LDH**
    - **indeks_pax:** 1.31
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 125 373
      - **currency:** PLN
      - **major:** 1253.73
    - **koszty**
      - **minor:** 1 613 006
      - **currency:** PLN
      - **major:** 16130.06
    - **propagacja**
      - **minor:** 622 830
      - **currency:** PLN
      - **major:** 6228.30
    - **strata**
      - **minor:** 2 361 209
      - **currency:** PLN
      - **major:** 23612.09
    - **widelki_min**
      - **minor:** 2 108 223
      - **currency:** PLN
      - **major:** 21082.23
    - **widelki_max**
      - **minor:** 2 642 305
      - **currency:** PLN
      - **major:** 26423.05
    - **rozpietosc**
      - **minor:** 534 082
      - **currency:** PLN
      - **major:** 5340.82
    - **wynik_wazony:** 0.03
    - **pozycja_wstepna:** 4
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
    - **wynik_wazony:** 0.55
    - **pozycja_wstepna:** 5
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
    - **wynik_wazony:** 0.74
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

- przy priorytecie 100 ranking wskazuje `SWAP-SP-LIO`, a najtansza jest `HOLD` (11833.94 PLN)
- widelki opcji `SWAP-SP-LIO` i `SWAP-SP-LIQ` zachodza na siebie -- roznica miedzy nimi nie jest istotna statystycznie

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
