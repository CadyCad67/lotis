# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260906T194742` · **snapshot:** `sha256:6c790f69f87c3591` · **0.57 ms**

Ranking wstepny 9 opcji, priorytet 0. Najmniejsza strata: `REBOOK-OWN` (135169.21 PLN), najwieksza: `HOLD` (390334.03 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 0 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | REBOOK-OWN | - |
| `strata_najlepszej` | 135169.21 PLN | PLN |
| `strata_najgorszej` | 390334.03 PLN | PLN |
| `rozpietosc_rankingu` | 255164.82 PLN | PLN |
| `wspolczynnik_dolny` | 0.90 | - |
| `wspolczynnik_gorny` | 1.38 | - |
| `opcji` | 9 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt
- przy zachodzacych widelkach o wyborze decyduja kryteria poza kosztem: node 13 dokłada wage polityki firmy

## Szczegoly

- **ranking_wstepny**
  - **REBOOK-OWN**
    - **indeks_pax:** 10.00
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 12 433 321
      - **currency:** PLN
      - **major:** 124333.21
    - **propagacja**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **strata**
      - **minor:** 13 516 921
      - **currency:** PLN
      - **major:** 135169.21
    - **widelki_min**
      - **minor:** 12 108 909
      - **currency:** PLN
      - **major:** 121089.09
    - **widelki_max**
      - **minor:** 18 585 766
      - **currency:** PLN
      - **major:** 185857.66
    - **rozpietosc**
      - **minor:** 6 476 857
      - **currency:** PLN
      - **major:** 64768.57
    - **wynik_wazony:** 0.00
    - **pozycja_wstepna:** 1
  - **CANCEL**
    - **indeks_pax:** 16.00
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 2 724 141
      - **currency:** PLN
      - **major:** 27241.41
    - **koszty**
      - **minor:** 11 294 896
      - **currency:** PLN
      - **major:** 112948.96
    - **propagacja**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **strata**
      - **minor:** 15 102 637
      - **currency:** PLN
      - **major:** 151026.37
    - **widelki_min**
      - **minor:** 13 529 446
      - **currency:** PLN
      - **major:** 135294.46
    - **widelki_max**
      - **minor:** 20 766 125
      - **currency:** PLN
      - **major:** 207661.25
    - **rozpietosc**
      - **minor:** 7 236 679
      - **currency:** PLN
      - **major:** 72366.79
    - **wynik_wazony:** 0.06
    - **pozycja_wstepna:** 2
  - **SPLIT**
    - **indeks_pax:** 10.21
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 15 142 321
      - **currency:** PLN
      - **major:** 151423.21
    - **propagacja**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **strata**
      - **minor:** 16 225 921
      - **currency:** PLN
      - **major:** 162259.21
    - **widelki_min**
      - **minor:** 14 535 721
      - **currency:** PLN
      - **major:** 145357.21
    - **widelki_max**
      - **minor:** 22 310 641
      - **currency:** PLN
      - **major:** 223106.41
    - **rozpietosc**
      - **minor:** 7 774 920
      - **currency:** PLN
      - **major:** 77749.20
    - **wynik_wazony:** 0.11
    - **pozycja_wstepna:** 3
  - **OVERNIGHT**
    - **indeks_pax:** 18.00
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 15 503 770
      - **currency:** PLN
      - **major:** 155037.70
    - **propagacja**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **strata**
      - **minor:** 16 587 370
      - **currency:** PLN
      - **major:** 165873.70
    - **widelki_min**
      - **minor:** 14 859 519
      - **currency:** PLN
      - **major:** 148595.19
    - **widelki_max**
      - **minor:** 22 807 633
      - **currency:** PLN
      - **major:** 228076.33
    - **rozpietosc**
      - **minor:** 7 948 114
      - **currency:** PLN
      - **major:** 79481.14
    - **wynik_wazony:** 0.12
    - **pozycja_wstepna:** 4
  - **REBOOK-OAL**
    - **indeks_pax:** 10.42
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 17 783 596
      - **currency:** PLN
      - **major:** 177835.96
    - **propagacja**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **strata**
      - **minor:** 18 867 196
      - **currency:** PLN
      - **major:** 188671.96
    - **widelki_min**
      - **minor:** 16 901 864
      - **currency:** PLN
      - **major:** 169018.64
    - **widelki_max**
      - **minor:** 25 942 394
      - **currency:** PLN
      - **major:** 259423.94
    - **rozpietosc**
      - **minor:** 9 040 530
      - **currency:** PLN
      - **major:** 90405.30
    - **wynik_wazony:** 0.21
    - **pozycja_wstepna:** 5
  - **SWAP-SP-LII**
    - **indeks_pax:** 0.68
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 11 710 566
      - **currency:** PLN
      - **major:** 117105.66
    - **propagacja**
      - **minor:** 11 414 874
      - **currency:** PLN
      - **major:** 114148.74
    - **strata**
      - **minor:** 23 125 440
      - **currency:** PLN
      - **major:** 231254.40
    - **widelki_min**
      - **minor:** 20 716 541
      - **currency:** PLN
      - **major:** 207165.41
    - **widelki_max**
      - **minor:** 31 797 480
      - **currency:** PLN
      - **major:** 317974.80
    - **rozpietosc**
      - **minor:** 11 080 939
      - **currency:** PLN
      - **major:** 110809.39
    - **wynik_wazony:** 0.38
    - **pozycja_wstepna:** 6
  - **SWAP-SP-LIC**
    - **indeks_pax:** 0.68
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 11 845 656
      - **currency:** PLN
      - **major:** 118456.56
    - **propagacja**
      - **minor:** 11 339 494
      - **currency:** PLN
      - **major:** 113394.94
    - **strata**
      - **minor:** 23 185 150
      - **currency:** PLN
      - **major:** 231851.50
    - **widelki_min**
      - **minor:** 20 770 031
      - **currency:** PLN
      - **major:** 207700.31
    - **widelki_max**
      - **minor:** 31 879 581
      - **currency:** PLN
      - **major:** 318795.81
    - **rozpietosc**
      - **minor:** 11 109 550
      - **currency:** PLN
      - **major:** 111095.50
    - **wynik_wazony:** 0.38
    - **pozycja_wstepna:** 7
  - **SWAP-SP-LID**
    - **indeks_pax:** 0.68
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 11 890 686
      - **currency:** PLN
      - **major:** 118906.86
    - **propagacja**
      - **minor:** 11 414 874
      - **currency:** PLN
      - **major:** 114148.74
    - **strata**
      - **minor:** 23 305 560
      - **currency:** PLN
      - **major:** 233055.60
    - **widelki_min**
      - **minor:** 20 877 898
      - **currency:** PLN
      - **major:** 208778.98
    - **widelki_max**
      - **minor:** 32 045 145
      - **currency:** PLN
      - **major:** 320451.45
    - **rozpietosc**
      - **minor:** 11 167 247
      - **currency:** PLN
      - **major:** 111672.47
    - **wynik_wazony:** 0.38
    - **pozycja_wstepna:** 8
  - **HOLD**
    - **indeks_pax:** 12.00
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 25 073 576
      - **currency:** PLN
      - **major:** 250735.76
    - **propagacja**
      - **minor:** 13 959 827
      - **currency:** PLN
      - **major:** 139598.27
    - **strata**
      - **minor:** 39 033 403
      - **currency:** PLN
      - **major:** 390334.03
    - **widelki_min**
      - **minor:** 34 967 424
      - **currency:** PLN
      - **major:** 349674.24
    - **widelki_max**
      - **minor:** 53 670 929
      - **currency:** PLN
      - **major:** 536709.29
    - **rozpietosc**
      - **minor:** 18 703 505
      - **currency:** PLN
      - **major:** 187035.05
    - **wynik_wazony:** 1.00
    - **pozycja_wstepna:** 9
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 19
  - **p25:** 14.00
  - **mediana:** 24.00
  - **p90:** 51.00
  - **punktualnosc15:** 26.30

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

## Ostrzezenia

- widelki opcji `REBOOK-OWN` i `CANCEL` zachodza na siebie -- roznica miedzy nimi nie jest istotna statystycznie

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
