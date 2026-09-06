# [17] WYNIK RZECZYWISTY

**Status:** degraded · **run:** `20260906T130726` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **0.09 ms**

Rejs LO417: prognoza 60783.55 PLN, rzeczywistosc 33404.03 PLN, blad -45.0%. Klasyfikacja: BLAD_WYKONANIA. Wynik POZA widelkami prognozy.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcja_wykonana` | SWAP-SP-LDH | - |
| `opoznienie_prognozowane` | 180 | min |
| `opoznienie_rzeczywiste` | 20 | min |
| `strata_prognozowana` | 60783.55 PLN | PLN |
| `strata_rzeczywista` | 33404.03 PLN | PLN |
| `blad` | -27379.52 PLN | PLN |
| `blad_procentowo` | -45.04 | % |
| `w_widelkach` | 0 | - |
| `rodzaj_bledu` | BLAD_WYKONANIA | - |

## Co ten node ustalil

- wykonanie nie powiodlo sie na kroku `nowy_slot` (Slot Coordination / EUROCONTROL nie potwierdzil kroku `wystapienie o nowe okno startowe`) -- model nie ponosi za to odpowiedzialnosci
- blad modelu, blad wykonania i odstepstwo czlowieka sa liczone osobno -- mieszanie ich uczy model na cudzych pomylkach
- blad -45.0% miesci sie w szumie (5%) -- bez poprawek

## Szczegoly

- **klasyfikacja**
  - **rodzaj:** BLAD_WYKONANIA
  - **opis:** wykonanie nie powiodlo sie na kroku `nowy_slot` (Slot Coordination / EUROCONTROL nie potwierdzil kroku `wystapienie o nowe okno startowe`) -- model nie ponosi za to odpowiedzialnosci
  - **blad_modelu:** 0
  - **blad_wykonania:** 1
  - **odstepstwo_czlowieka:** 0
- **zrodlo_rzeczywistosci**
  - **poziom:** rejs
  - **p25:** 15.00
  - **mediana:** 20.00
  - **p90:** 37.00
- **kalibracja**
  - **poprawki:** -
  - **powod_pominiecia:** rodzaj `BLAD_WYKONANIA` nie kalibruje modelu
  - **tlumienie:** 0.20
- **wykonanie**
  - **udane:** 0
  - **powod**
    - **step:** nowy_slot
    - **reason:** Slot Coordination / EUROCONTROL nie potwierdzil kroku `wystapienie o nowe okno startowe`
    - **recoverable:** 1

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `rzeczywiste opoznienie` | real | 0.90 | mediana rozkladu z 6374 operacji |

## Braki danych

- rzeczywisty koszt operacji nie jest w zadnym ze zrodel -- porownanie opiera sie na opoznieniu, nie na fakturach

## Ostrzezenia

- rzeczywistosc wypadla poza widelkami prognozy -- widelki byly za waskie albo model pominal skladnik

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
