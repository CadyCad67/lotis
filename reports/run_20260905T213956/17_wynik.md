# [17] WYNIK RZECZYWISTY

**Status:** ok · **run:** `20260905T213956` · **snapshot:** `sha256:f3c290f4e6930407` · **0.08 ms**

Rejs LO3996: prognoza 87716.13 PLN, rzeczywistosc 87716.13 PLN, blad +0.0%. Klasyfikacja: ZGODNY. Wynik miesci sie w widelkach.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcja_wykonana` | REBOOK-OWN | - |
| `opoznienie_prognozowane` | 180 | min |
| `opoznienie_rzeczywiste` | 8 | min |
| `strata_prognozowana` | 87716.13 PLN | PLN |
| `strata_rzeczywista` | 87716.13 PLN | PLN |
| `blad` | 0.00 PLN | PLN |
| `blad_procentowo` | 0.00 | % |
| `w_widelkach` | 1 | - |
| `rodzaj_bledu` | ZGODNY | - |

## Co ten node ustalil

- prognoza zgodna z rzeczywistoscia w granicach +0.0%
- blad modelu, blad wykonania i odstepstwo czlowieka sa liczone osobno -- mieszanie ich uczy model na cudzych pomylkach
- blad +0.0% miesci sie w szumie (5%) -- bez poprawek

## Szczegoly

- **klasyfikacja**
  - **rodzaj:** ZGODNY
  - **opis:** prognoza zgodna z rzeczywistoscia w granicach +0.0%
  - **blad_modelu:** 0
  - **blad_wykonania:** 0
  - **odstepstwo_czlowieka:** 0
- **zrodlo_rzeczywistosci**
  - **poziom:** rejs
  - **p25:** 5.00
  - **mediana:** 8.00
  - **p90:** 13.00
- **kalibracja**
  - **poprawki:** -
  - **powod_pominiecia:** rodzaj `ZGODNY` nie kalibruje modelu
  - **tlumienie:** 0.20
- **wykonanie**
  - **opcja:** REBOOK-OWN
  - **kroki**
    - **kasacja_w_systemie**
      - **wykonawca:** System rezerwacyjny
      - **opis:** odwolanie rejsu i zwolnienie miejsc
      - **odwracalny:** 0
      - **krytyczny:** 1
      - **status:** wykonany
    - **przepisanie_wlasne**
      - **wykonawca:** System rezerwacyjny
      - **opis:** przepisanie pasazerow na wlasny rejs
      - **odwracalny:** 1
      - **krytyczny:** 0
      - **status:** wykonany
    - **powiadomienie_pax**
      - **wykonawca:** Komunikacja
      - **opis:** wyslanie SMS i e-mail do pasazerow
      - **odwracalny:** 1
      - **krytyczny:** 0
      - **status:** wykonany
    - **brief_zalogi**
      - **wykonawca:** Crew Control
      - **opis:** poinformowanie zalogi o zmianie
      - **odwracalny:** 1
      - **krytyczny:** 0
      - **status:** wykonany
  - **udane:** 1

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `rzeczywiste opoznienie` | real | 0.90 | mediana rozkladu z 6374 operacji |

## Braki danych

- rzeczywisty koszt operacji nie jest w zadnym ze zrodel -- porownanie opiera sie na opoznieniu, nie na fakturach

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
