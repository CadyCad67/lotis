# [17] WYNIK RZECZYWISTY

**Status:** degraded · **run:** `20260906T191046` · **snapshot:** `sha256:f3c290f4e6930407` · **0.1 ms**

Rejs LO2098: prognoza 805722.60 PLN, rzeczywistosc 717832.56 PLN, blad -10.9%. Klasyfikacja: BLAD_MODELU. Wynik POZA widelkami prognozy.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcja_wykonana` | HOLD | - |
| `opoznienie_prognozowane` | 180 | min |
| `opoznienie_rzeczywiste` | 54 | min |
| `strata_prognozowana` | 805722.60 PLN | PLN |
| `strata_rzeczywista` | 717832.56 PLN | PLN |
| `blad` | -87890.04 PLN | PLN |
| `blad_procentowo` | -10.91 | % |
| `w_widelkach` | 0 | - |
| `rodzaj_bledu` | BLAD_MODELU | - |

## Co ten node ustalil

- wycena rozminela sie o -10.9% przy poprawnym wykonaniu i przyjetej rekomendacji
- blad modelu, blad wykonania i odstepstwo czlowieka sa liczone osobno -- mieszanie ich uczy model na cudzych pomylkach
- kalibracja z tlumieniem 20%: jedna doba nie przestawia modelu

## Szczegoly

- **klasyfikacja**
  - **rodzaj:** BLAD_MODELU
  - **opis:** wycena rozminela sie o -10.9% przy poprawnym wykonaniu i przyjetej rekomendacji
  - **blad_modelu:** 1
  - **blad_wykonania:** 0
  - **odstepstwo_czlowieka:** 0
- **zrodlo_rzeczywistosci**
  - **poziom:** rejs
  - **p25:** 35.00
  - **mediana:** 54.00
  - **p90:** 174.00
- **kalibracja**
  - **poprawki**
    - **parametr:** koszt_minuty_opoznienia
    - **kierunek:** w dol
    - **sugerowana_zmiana_pct:** -2.18
    - **podstawa:** roznica miedzy strata prognozowana a rzeczywista
    - **parametr:** szacunek_opoznienia
    - **kierunek:** w dol
    - **sugerowana_zmiana_pct:** -14.00
    - **podstawa:** prognoza 180 min wobec rzeczywistych 54 min
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

## Ostrzezenia

- rzeczywistosc wypadla poza widelkami prognozy -- widelki byly za waskie albo model pominal skladnik

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
