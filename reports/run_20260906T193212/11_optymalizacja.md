# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260906T193212` · **snapshot:** `sha256:6c790f69f87c3591` · **4.32 ms**

Ranking wstepny 9 opcji, priorytet 0. Najmniejsza strata: `HOLD` (28810.32 PLN), najwieksza: `REBOOK-OAL` (2009914.60 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 0 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 28810.32 PLN | PLN |
| `strata_najgorszej` | 2009914.60 PLN | PLN |
| `rozpietosc_rankingu` | 1981104.28 PLN | PLN |
| `wspolczynnik_dolny` | 0.93 | - |
| `wspolczynnik_gorny` | 1.54 | - |
| `opcji` | 9 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt
- przy zachodzacych widelkach o wyborze decyduja kryteria poza kosztem: node 13 dokłada wage polityki firmy

## Szczegoly

- **ranking_wstepny**
  - **HOLD**
    - **indeks_pax:** 0.29
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 817 032
      - **currency:** PLN
      - **major:** 8170.32
    - **koszty**
      - **minor:** 2 064 000
      - **currency:** PLN
      - **major:** 20640.00
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 2 881 032
      - **currency:** PLN
      - **major:** 28810.32
    - **widelki_min**
      - **minor:** 2 677 481
      - **currency:** PLN
      - **major:** 26774.81
    - **widelki_max**
      - **minor:** 4 446 810
      - **currency:** PLN
      - **major:** 44468.10
    - **rozpietosc**
      - **minor:** 1 769 329
      - **currency:** PLN
      - **major:** 17693.29
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 1
  - **REBOOK-SPILL**
    - **indeks_pax:** 0.20
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 3 820 120
      - **currency:** PLN
      - **major:** 38201.20
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 3 820 120
      - **currency:** PLN
      - **major:** 38201.20
    - **widelki_min**
      - **minor:** 3 550 221
      - **currency:** PLN
      - **major:** 35502.21
    - **widelki_max**
      - **minor:** 5 896 272
      - **currency:** PLN
      - **major:** 58962.72
    - **rozpietosc**
      - **minor:** 2 346 051
      - **currency:** PLN
      - **major:** 23460.51
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 2
  - **SWAP-SP-LSA**
    - **indeks_pax:** 2.32
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 10 415 698
      - **currency:** PLN
      - **major:** 104156.98
    - **propagacja**
      - **minor:** 9 695 806
      - **currency:** PLN
      - **major:** 96958.06
    - **strata**
      - **minor:** 20 111 504
      - **currency:** PLN
      - **major:** 201115.04
    - **widelki_min**
      - **minor:** 18 690 583
      - **currency:** PLN
      - **major:** 186905.83
    - **widelki_max**
      - **minor:** 31 041 669
      - **currency:** PLN
      - **major:** 310416.69
    - **rozpietosc**
      - **minor:** 12 351 086
      - **currency:** PLN
      - **major:** 123510.86
    - **wynik_wazony:** 0.09
    - **pozycja_wstepna:** 3
  - **SWAP-SP-LSE**
    - **indeks_pax:** 2.32
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 10 415 698
      - **currency:** PLN
      - **major:** 104156.98
    - **propagacja**
      - **minor:** 9 695 806
      - **currency:** PLN
      - **major:** 96958.06
    - **strata**
      - **minor:** 20 111 504
      - **currency:** PLN
      - **major:** 201115.04
    - **widelki_min**
      - **minor:** 18 690 583
      - **currency:** PLN
      - **major:** 186905.83
    - **widelki_max**
      - **minor:** 31 041 669
      - **currency:** PLN
      - **major:** 310416.69
    - **rozpietosc**
      - **minor:** 12 351 086
      - **currency:** PLN
      - **major:** 123510.86
    - **wynik_wazony:** 0.09
    - **pozycja_wstepna:** 4
  - **REBOOK-OWN**
    - **indeks_pax:** 6.67
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 127 216 360
      - **currency:** PLN
      - **major:** 1272163.60
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 151 575 860
      - **currency:** PLN
      - **major:** 1515758.60
    - **widelki_min**
      - **minor:** 140 866 696
      - **currency:** PLN
      - **major:** 1408666.96
    - **widelki_max**
      - **minor:** 233 954 044
      - **currency:** PLN
      - **major:** 2339540.44
    - **rozpietosc**
      - **minor:** 93 087 348
      - **currency:** PLN
      - **major:** 930873.48
    - **wynik_wazony:** 0.75
    - **pozycja_wstepna:** 5
  - **OVERNIGHT**
    - **indeks_pax:** 18.00
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 137 534 142
      - **currency:** PLN
      - **major:** 1375341.42
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 161 893 642
      - **currency:** PLN
      - **major:** 1618936.42
    - **widelki_min**
      - **minor:** 150 455 505
      - **currency:** PLN
      - **major:** 1504555.05
    - **widelki_max**
      - **minor:** 249 879 317
      - **currency:** PLN
      - **major:** 2498793.17
    - **rozpietosc**
      - **minor:** 99 423 812
      - **currency:** PLN
      - **major:** 994238.12
    - **wynik_wazony:** 0.80
    - **pozycja_wstepna:** 6
  - **SPLIT**
    - **indeks_pax:** 10.04
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 151 924 160
      - **currency:** PLN
      - **major:** 1519241.60
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 176 283 660
      - **currency:** PLN
      - **major:** 1762836.60
    - **widelki_min**
      - **minor:** 163 828 837
      - **currency:** PLN
      - **major:** 1638288.37
    - **widelki_max**
      - **minor:** 272 089 996
      - **currency:** PLN
      - **major:** 2720899.96
    - **rozpietosc**
      - **minor:** 108 261 159
      - **currency:** PLN
      - **major:** 1082611.59
    - **wynik_wazony:** 0.88
    - **pozycja_wstepna:** 7
  - **CANCEL**
    - **indeks_pax:** 12.67
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 54 405 974
      - **currency:** PLN
      - **major:** 544059.74
    - **koszty**
      - **minor:** 101 252 960
      - **currency:** PLN
      - **major:** 1012529.60
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 180 018 434
      - **currency:** PLN
      - **major:** 1800184.34
    - **widelki_min**
      - **minor:** 167 299 741
      - **currency:** PLN
      - **major:** 1672997.41
    - **widelki_max**
      - **minor:** 277 854 539
      - **currency:** PLN
      - **major:** 2778545.39
    - **rozpietosc**
      - **minor:** 110 554 798
      - **currency:** PLN
      - **major:** 1105547.98
    - **wynik_wazony:** 0.89
    - **pozycja_wstepna:** 8
  - **REBOOK-OAL**
    - **indeks_pax:** 13.42
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 176 631 960
      - **currency:** PLN
      - **major:** 1766319.60
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 200 991 460
      - **currency:** PLN
      - **major:** 2009914.60
    - **widelki_min**
      - **minor:** 186 790 977
      - **currency:** PLN
      - **major:** 1867909.77
    - **widelki_max**
      - **minor:** 310 225 949
      - **currency:** PLN
      - **major:** 3102259.49
    - **rozpietosc**
      - **minor:** 123 434 972
      - **currency:** PLN
      - **major:** 1234349.72
    - **wynik_wazony:** 1.00
    - **pozycja_wstepna:** 9
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

- widelki opcji `HOLD` i `REBOOK-SPILL` zachodza na siebie -- roznica miedzy nimi nie jest istotna statystycznie

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
