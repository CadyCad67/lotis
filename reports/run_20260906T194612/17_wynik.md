# [17] WYNIK RZECZYWISTY

**Status:** degraded · **run:** `20260906T194612` · **snapshot:** `sha256:6c790f69f87c3591` · **0.09 ms**

Rejs LO395: prognoza 30198.38 PLN, rzeczywistosc 23149.94 PLN, blad -23.3%. Klasyfikacja: BLAD_MODELU. Wynik POZA widelkami prognozy.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcja_wykonana` | REBOOK-SPILL | - |
| `opoznienie_prognozowane` | 60 | min |
| `opoznienie_rzeczywiste` | 24 | min |
| `strata_prognozowana` | 30198.38 PLN | PLN |
| `strata_rzeczywista` | 23149.94 PLN | PLN |
| `blad` | -7048.44 PLN | PLN |
| `blad_procentowo` | -23.34 | % |
| `w_widelkach` | 0 | - |
| `rodzaj_bledu` | BLAD_MODELU | - |

## Co ten node ustalil

- wycena rozminela sie o -23.3% przy poprawnym wykonaniu i przyjetej rekomendacji
- blad modelu, blad wykonania i odstepstwo czlowieka sa liczone osobno -- mieszanie ich uczy model na cudzych pomylkach
- kalibracja z tlumieniem 20%: jedna doba nie przestawia modelu

## Szczegoly

- **klasyfikacja**
  - **rodzaj:** BLAD_MODELU
  - **opis:** wycena rozminela sie o -23.3% przy poprawnym wykonaniu i przyjetej rekomendacji
  - **blad_modelu:** 1
  - **blad_wykonania:** 0
  - **odstepstwo_czlowieka:** 0
- **zrodlo_rzeczywistosci**
  - **poziom:** rejs
  - **p25:** 14.00
  - **mediana:** 24.00
  - **p90:** 51.00
- **kalibracja**
  - **poprawki**
    - **parametr:** koszt_minuty_opoznienia
    - **kierunek:** w dol
    - **sugerowana_zmiana_pct:** -4.67
    - **podstawa:** roznica miedzy strata prognozowana a rzeczywista
    - **parametr:** szacunek_opoznienia
    - **kierunek:** w dol
    - **sugerowana_zmiana_pct:** -12.00
    - **podstawa:** prognoza 60 min wobec rzeczywistych 24 min
  - **tlumienie:** 0.20
  - **zasada:** poprawka wchodzi z waga 20% -- potrzeba kilkunastu zgodnych obserwacji
- **wykonanie**
  - **opcja:** REBOOK-SPILL
  - **kroki**
    - **nowy_slot**
      - **wykonawca:** Slot Coordination / EUROCONTROL
      - **opis:** wystapienie o nowe okno startowe
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

## Ostrzezenia

- rzeczywistosc wypadla poza widelkami prognozy -- widelki byly za waskie albo model pominal skladnik

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
