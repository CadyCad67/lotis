# [17] WYNIK RZECZYWISTY

**Status:** degraded · **run:** `20260906T190325` · **snapshot:** `sha256:f3c290f4e6930407` · **0.09 ms**

Rejs LO3981: prognoza 12035.06 PLN, rzeczywistosc 82590.74 PLN, blad +586.2%. Klasyfikacja: BLAD_MODELU. Wynik POZA widelkami prognozy.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcja_wykonana` | SWAP-SP-LIO | - |
| `opoznienie_prognozowane` | 0 | min |
| `opoznienie_rzeczywiste` | 14 | min |
| `strata_prognozowana` | 12035.06 PLN | PLN |
| `strata_rzeczywista` | 82590.74 PLN | PLN |
| `blad` | 70555.68 PLN | PLN |
| `blad_procentowo` | 586.25 | % |
| `w_widelkach` | 0 | - |
| `rodzaj_bledu` | BLAD_MODELU | - |

## Co ten node ustalil

- wycena rozminela sie o +586.2% przy poprawnym wykonaniu i przyjetej rekomendacji
- blad modelu, blad wykonania i odstepstwo czlowieka sa liczone osobno -- mieszanie ich uczy model na cudzych pomylkach
- kalibracja z tlumieniem 20%: jedna doba nie przestawia modelu

## Szczegoly

- **klasyfikacja**
  - **rodzaj:** BLAD_MODELU
  - **opis:** wycena rozminela sie o +586.2% przy poprawnym wykonaniu i przyjetej rekomendacji
  - **blad_modelu:** 1
  - **blad_wykonania:** 0
  - **odstepstwo_czlowieka:** 0
- **zrodlo_rzeczywistosci**
  - **poziom:** rejs
  - **p25:** 8.00
  - **mediana:** 14.00
  - **p90:** 19.00
- **kalibracja**
  - **poprawki**
    - **parametr:** koszt_minuty_opoznienia
    - **kierunek:** w gore
    - **sugerowana_zmiana_pct:** 117.25
    - **podstawa:** roznica miedzy strata prognozowana a rzeczywista
  - **tlumienie:** 0.20
  - **zasada:** poprawka wchodzi z waga 20% -- potrzeba kilkunastu zgodnych obserwacji
- **wykonanie**
  - **opcja:** SWAP-SP-LIO
  - **kroki**
    - **przydzial_maszyny**
      - **wykonawca:** OCC / Maintenance Control
      - **opis:** przepiecie rejsow miedzy maszynami
      - **odwracalny:** 1
      - **krytyczny:** 0
      - **status:** wykonany
    - **obsluga_naziemna**
      - **wykonawca:** Handling
      - **opis:** przestawienie sprzetu i bagazu
      - **odwracalny:** 1
      - **krytyczny:** 0
      - **status:** wykonany
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
