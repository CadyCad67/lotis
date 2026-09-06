# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260906T190325` · **snapshot:** `sha256:f3c290f4e6930407` · **3.66 ms**

Ranking wstepny 7 opcji, priorytet 50. Najmniejsza strata: `SWAP-SP-LIO` (12035.06 PLN), najwieksza: `CANCEL` (170081.09 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 50 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | SWAP-SP-LIO | - |
| `strata_najlepszej` | 12035.06 PLN | PLN |
| `strata_najgorszej` | 170081.09 PLN | PLN |
| `rozpietosc_rankingu` | 158046.03 PLN | PLN |
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
      - **minor:** 779 236
      - **currency:** PLN
      - **major:** 7792.36
    - **propagacja**
      - **minor:** 424 270
      - **currency:** PLN
      - **major:** 4242.70
    - **strata**
      - **minor:** 1 203 506
      - **currency:** PLN
      - **major:** 12035.06
    - **widelki_min**
      - **minor:** 1 074 559
      - **currency:** PLN
      - **major:** 10745.59
    - **widelki_max**
      - **minor:** 1 346 780
      - **currency:** PLN
      - **major:** 13467.80
    - **rozpietosc**
      - **minor:** 272 221
      - **currency:** PLN
      - **major:** 2722.21
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
      - **minor:** 779 236
      - **currency:** PLN
      - **major:** 7792.36
    - **propagacja**
      - **minor:** 424 270
      - **currency:** PLN
      - **major:** 4242.70
    - **strata**
      - **minor:** 1 203 506
      - **currency:** PLN
      - **major:** 12035.06
    - **widelki_min**
      - **minor:** 1 074 559
      - **currency:** PLN
      - **major:** 10745.59
    - **widelki_max**
      - **minor:** 1 346 780
      - **currency:** PLN
      - **major:** 13467.80
    - **rozpietosc**
      - **minor:** 272 221
      - **currency:** PLN
      - **major:** 2722.21
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 2
  - **SWAP-SP-LDH**
    - **indeks_pax:** 1.29
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 125 373
      - **currency:** PLN
      - **major:** 1253.73
    - **koszty**
      - **minor:** 1 414 446
      - **currency:** PLN
      - **major:** 14144.46
    - **propagacja**
      - **minor:** 424 270
      - **currency:** PLN
      - **major:** 4242.70
    - **strata**
      - **minor:** 1 964 089
      - **currency:** PLN
      - **major:** 19640.89
    - **widelki_min**
      - **minor:** 1 753 651
      - **currency:** PLN
      - **major:** 17536.51
    - **widelki_max**
      - **minor:** 2 197 909
      - **currency:** PLN
      - **major:** 21979.09
    - **rozpietosc**
      - **minor:** 444 258
      - **currency:** PLN
      - **major:** 4442.58
    - **wynik_wazony:** 0.04
    - **pozycja_wstepna:** 3
  - **HOLD**
    - **indeks_pax:** 4.88
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 735 933
      - **currency:** PLN
      - **major:** 7359.33
    - **koszty**
      - **minor:** 4 300 000
      - **currency:** PLN
      - **major:** 43000.00
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 5 035 933
      - **currency:** PLN
      - **major:** 50359.33
    - **widelki_min**
      - **minor:** 4 496 369
      - **currency:** PLN
      - **major:** 44963.69
    - **widelki_max**
      - **minor:** 5 635 448
      - **currency:** PLN
      - **major:** 56354.48
    - **rozpietosc**
      - **minor:** 1 139 079
      - **currency:** PLN
      - **major:** 11390.79
    - **wynik_wazony:** 0.21
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
    - **wynik_wazony:** 0.74
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
    - **wynik_wazony:** 0.83
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
