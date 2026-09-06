# [11] OPTIMIZATION ENGINE

**Status:** degraded · **run:** `20260906T191132` · **snapshot:** `sha256:f3c290f4e6930407` · **0.48 ms**

Ranking wstepny 4 opcji, priorytet 50. Najmniejsza strata: `HOLD` (805722.60 PLN), najwieksza: `CANCEL` (1719112.11 PLN).

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `priorytet` | 50 | 0 finanse, 100 pasazer |
| `najlepsza_opcja` | HOLD | - |
| `strata_najlepszej` | 805722.60 PLN | PLN |
| `strata_najgorszej` | 1719112.11 PLN | PLN |
| `rozpietosc_rankingu` | 913389.51 PLN | PLN |
| `wspolczynnik_dolny` | 0.91 | - |
| `wspolczynnik_gorny` | 1.74 | - |
| `opcji` | 4 | szt |

## Co ten node ustalil

- strata = (baseline - revenue opcji) + koszty + propagacja
- najlepsza opcja to najmniejsza strata, nie najmniejszy koszt
- przy zachodzacych widelkach o wyborze decyduja kryteria poza kosztem: node 13 dokłada wage polityki firmy

## Szczegoly

- **ranking_wstepny**
  - **HOLD**
    - **indeks_pax:** 3.00
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 80 572 260
      - **currency:** PLN
      - **major:** 805722.60
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 80 572 260
      - **currency:** PLN
      - **major:** 805722.60
    - **widelki_min**
      - **minor:** 73 484 886
      - **currency:** PLN
      - **major:** 734848.86
    - **widelki_max**
      - **minor:** 140 255 415
      - **currency:** PLN
      - **major:** 1402554.15
    - **rozpietosc**
      - **minor:** 66 770 529
      - **currency:** PLN
      - **major:** 667705.29
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
      - **minor:** 135 098 174
      - **currency:** PLN
      - **major:** 1350981.74
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 135 098 174
      - **currency:** PLN
      - **major:** 1350981.74
    - **widelki_min**
      - **minor:** 123 214 539
      - **currency:** PLN
      - **major:** 1232145.39
    - **widelki_max**
      - **minor:** 235 170 895
      - **currency:** PLN
      - **major:** 2351708.95
    - **rozpietosc**
      - **minor:** 111 956 356
      - **currency:** PLN
      - **major:** 1119563.56
    - **wynik_wazony:** 0.66
    - **pozycja_wstepna:** 2
  - **REBOOK-OAL**
    - **indeks_pax:** 18.42
    - **tryb:** RESTRUCTURING
    - **revenue_at_risk**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **koszty**
      - **minor:** 168 346 720
      - **currency:** PLN
      - **major:** 1683467.20
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 168 346 720
      - **currency:** PLN
      - **major:** 1683467.20
    - **widelki_min**
      - **minor:** 153 538 444
      - **currency:** PLN
      - **major:** 1535384.44
    - **widelki_max**
      - **minor:** 293 047 994
      - **currency:** PLN
      - **major:** 2930479.94
    - **rozpietosc**
      - **minor:** 139 509 550
      - **currency:** PLN
      - **major:** 1395095.50
    - **wynik_wazony:** 0.85
    - **pozycja_wstepna:** 3
  - **CANCEL**
    - **indeks_pax:** 24.00
    - **tryb:** MODIFYING
    - **revenue_at_risk**
      - **minor:** 62 051 887
      - **currency:** PLN
      - **major:** 620518.87
    - **koszty**
      - **minor:** 109 859 324
      - **currency:** PLN
      - **major:** 1098593.24
    - **propagacja**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **strata**
      - **minor:** 171 911 211
      - **currency:** PLN
      - **major:** 1719112.11
    - **widelki_min**
      - **minor:** 156 789 392
      - **currency:** PLN
      - **major:** 1567893.92
    - **widelki_max**
      - **minor:** 299 252 848
      - **currency:** PLN
      - **major:** 2992528.48
    - **rozpietosc**
      - **minor:** 142 463 456
      - **currency:** PLN
      - **major:** 1424634.56
    - **wynik_wazony:** 1.00
    - **pozycja_wstepna:** 4
- **zrodlo_widelek**
  - **poziom:** rejs
  - **obserwacji:** 42
  - **p25:** 35.00
  - **mediana:** 54.00
  - **p90:** 174.00
  - **punktualnosc15:** 2.40

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `widelki` | real | 0.80 | kwantyle p25/mediana/p90 z rzeczywistych operacji tej siatki |
| `kurs EUR/PLN` | policy | 0.50 | 4.3 -- placeholder - kurs do ustawienia w Konfiguracji |

## Ostrzezenia

- widelki opcji `HOLD` i `OVERNIGHT` zachodza na siebie -- roznica miedzy nimi nie jest istotna statystycznie

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
