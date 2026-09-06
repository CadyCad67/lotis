# [17] WYNIK RZECZYWISTY

**Status:** ok · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **0.1 ms**

Rejs LO6: prognoza 37149.50 PLN, rzeczywistosc 46740.70 PLN, blad +25.8%. Klasyfikacja: BLAD_MODELU. Wynik miesci sie w widelkach.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcja_wykonana` | HOLD | - |
| `opoznienie_prognozowane` | 30 | min |
| `opoznienie_rzeczywiste` | 46 | min |
| `strata_prognozowana` | 37149.50 PLN | PLN |
| `strata_rzeczywista` | 46740.70 PLN | PLN |
| `blad` | 9591.20 PLN | PLN |
| `blad_procentowo` | 25.82 | % |
| `w_widelkach` | 1 | - |
| `rodzaj_bledu` | BLAD_MODELU | - |

## Co ten node ustalil

- wycena rozminela sie o +25.8% przy poprawnym wykonaniu i przyjetej rekomendacji
- blad modelu, blad wykonania i odstepstwo czlowieka sa liczone osobno -- mieszanie ich uczy model na cudzych pomylkach
- kalibracja z tlumieniem 20%: jedna doba nie przestawia modelu

## Szczegoly

- **klasyfikacja**
  - **rodzaj:** BLAD_MODELU
  - **opis:** wycena rozminela sie o +25.8% przy poprawnym wykonaniu i przyjetej rekomendacji
  - **blad_modelu:** 1
  - **blad_wykonania:** 0
  - **odstepstwo_czlowieka:** 0
- **zrodlo_rzeczywistosci**
  - **poziom:** rejs
  - **p25:** 33.00
  - **mediana:** 46.00
  - **p90:** 121.00
- **kalibracja**
  - **poprawki**
    - **parametr:** koszt_minuty_opoznienia
    - **kierunek:** w gore
    - **sugerowana_zmiana_pct:** 5.16
    - **podstawa:** roznica miedzy strata prognozowana a rzeczywista
    - **parametr:** szacunek_opoznienia
    - **kierunek:** w gore
    - **sugerowana_zmiana_pct:** 10.67
    - **podstawa:** prognoza 30 min wobec rzeczywistych 46 min
  - **tlumienie:** 0.20
  - **zasada:** poprawka wchodzi z waga 20% -- potrzeba kilkunastu zgodnych obserwacji
- **wykonanie**
  - **opcja:** HOLD
  - **kroki**
    - **nowy_slot**
      - **wykonawca:** Slot Coordination / EUROCONTROL
      - **opis:** wystapienie o nowe okno startowe
      - **odwracalny:** 0
      - **krytyczny:** 1
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
