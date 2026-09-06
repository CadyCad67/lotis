# [11] OPTIMIZATION ENGINE

**Status:** ok · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **1.03 ms**

Ranking wstepny 6 opcji, priorytet 0. Najmniejsza strata: `HOLD` (38377.09 PLN), najwieksza: `REBOOK-OAL` (1844835.88 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 0 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 38377.09 PLN | PLN |
| `strata_najgorszej` | 1844835.88 PLN | PLN |
| `rozpietosc_rankingu` | 1806458.79 PLN | PLN |
| `wspolczynnik_dolny` | 0.93 | - |
| `wspolczynnik_gorny` | 1.54 | - |
| `opcji` | 6 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt

## Szczegoly

- **ranking_wstepny**
  - **HOLD**
    - **indeks_pax:** 0.61
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 254 716
      - **currency:** PLN
      - **major:** 2547.16
    - **koszty**
      - **minor:** 2 733 913
      - **currency:** PLN
      - **major:** 27339.13
    - **propagacja**
      - **minor:** 849 080
      - **currency:** PLN
      - **major:** 8490.80
    - **strata**
      - **minor:** 3 837 709
      - **currency:** PLN
      - **major:** 38377.09
    - **widelki_min**
      - **minor:** 3 566 567
      - **currency:** PLN
      - **major:** 35665.67
    - **widelki_max**
      - **minor:** 5 923 420
      - **currency:** PLN
      - **major:** 59234.20
    - **rozpietosc**
      - **minor:** 2 356 853
      - **currency:** PLN
      - **major:** 23568.53
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 1
  - **SWAP-SP-LSC**
    - **indeks_pax:** 2.27
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 8 033 942
      - **currency:** PLN
      - **major:** 80339.42
    - **propagacja**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **strata**
      - **minor:** 16 186 462
      - **currency:** PLN
      - **major:** 161864.62
    - **widelki_min**
      - **minor:** 15 042 854
      - **currency:** PLN
      - **major:** 150428.54
    - **widelki_max**
      - **minor:** 24 983 452
      - **currency:** PLN
      - **major:** 249834.52
    - **rozpietosc**
      - **minor:** 9 940 598
      - **currency:** PLN
      - **major:** 99405.98
    - **wynik_wazony:** 0.07
    - **pozycja_wstepna:** 2
  - **SWAP-SP-LRF**
    - **indeks_pax:** 2.27
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 9 709 667
      - **currency:** PLN
      - **major:** 97096.67
    - **propagacja**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **strata**
      - **minor:** 17 862 187
      - **currency:** PLN
      - **major:** 178621.87
    - **widelki_min**
      - **minor:** 16 600 185
      - **currency:** PLN
      - **major:** 166001.85
    - **widelki_max**
      - **minor:** 27 569 897
      - **currency:** PLN
      - **major:** 275698.97
    - **rozpietosc**
      - **minor:** 10 969 712
      - **currency:** PLN
      - **major:** 109697.12
    - **wynik_wazony:** 0.08
    - **pozycja_wstepna:** 3
  - **OVERNIGHT**
    - **indeks_pax:** 18.00
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 125 388 090
      - **currency:** PLN
      - **major:** 1253880.90
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 149 747 590
      - **currency:** PLN
      - **major:** 1497475.90
    - **widelki_min**
      - **minor:** 139 167 598
      - **currency:** PLN
      - **major:** 1391675.98
    - **widelki_max**
      - **minor:** 231 132 149
      - **currency:** PLN
      - **major:** 2311321.49
    - **rozpietosc**
      - **minor:** 91 964 551
      - **currency:** PLN
      - **major:** 919645.51
    - **wynik_wazony:** 0.81
    - **pozycja_wstepna:** 4
  - **CANCEL**
    - **indeks_pax:** 24.00
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 42 573 481
      - **currency:** PLN
      - **major:** 425734.81
    - **koszty**
      - **minor:** 102 359 440
      - **currency:** PLN
      - **major:** 1023594.40
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 169 292 421
      - **currency:** PLN
      - **major:** 1692924.21
    - **widelki_min**
      - **minor:** 157 331 544
      - **currency:** PLN
      - **major:** 1573315.44
    - **widelki_max**
      - **minor:** 261 299 171
      - **currency:** PLN
      - **major:** 2612991.71
    - **rozpietosc**
      - **minor:** 103 967 627
      - **currency:** PLN
      - **major:** 1039676.27
    - **wynik_wazony:** 0.92
    - **pozycja_wstepna:** 5
  - **REBOOK-OAL**
    - **indeks_pax:** 18.42
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 160 124 088
      - **currency:** PLN
      - **major:** 1601240.88
    - **propagacja**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **strata**
      - **minor:** 184 483 588
      - **currency:** PLN
      - **major:** 1844835.88
    - **widelki_min**
      - **minor:** 171 449 422
      - **currency:** PLN
      - **major:** 1714494.22
    - **widelki_max**
      - **minor:** 284 746 407
      - **currency:** PLN
      - **major:** 2847464.07
    - **rozpietosc**
      - **minor:** 113 296 985
      - **currency:** PLN
      - **major:** 1132969.85
    - **wynik_wazony:** 1.00
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

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
