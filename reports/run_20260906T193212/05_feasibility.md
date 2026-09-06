# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T193212` · **snapshot:** `sha256:6c790f69f87c3591` · **10.12 ms**

Cztery bramki na rejsie LO6 przy opoznieniu 0 min. Odpadly: zaloga.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | przeszla | - |
| `dopuszczonych_rodzajow` | 7 | szt |
| `nowy_std` | 2026-08-24T12:10:00+00:00 | - |
| `nowy_sta` | 2026-08-24T21:40:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 11 osob przekracza FDP przy opoznieniu 0 min (najgorszy zapas -485 min) -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 5 maszyn do podmiany w WAW
    - **kandydaci:** 5
    - **lista**
      - **reg:** SP-LRH
      - **typ:** B788
      - **reg:** SP-LSA
      - **typ:** B789
      - **reg:** SP-LSE
      - **typ:** B789
      - **reg:** SP-LSF
      - **typ:** B789
      - **reg:** SP-LSG
      - **typ:** B789
    - **minimalny_postoj_min:** 139
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 11 osob przekracza FDP przy opoznieniu 0 min (najgorszy zapas -485 min)
    - **przekroczen:** 11
    - **lista**
      - **SP-LSC-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 265
        - **limit_min:** 780
        - **zapas_min:** -485
      - **SP-LSC-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 265
        - **limit_min:** 780
        - **zapas_min:** -485
      - **SP-LSC-FIR2**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 265
        - **limit_min:** 780
        - **zapas_min:** -485
      - **SP-LSC-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 250
        - **limit_min:** 795
        - **zapas_min:** -455
      - **SP-LSC-CAB4**
        - **rola:** CABIN
        - **potrzeba_min:** 1 250
        - **limit_min:** 795
        - **zapas_min:** -455
      - **SP-LSC-CAB5**
        - **rola:** CABIN
        - **potrzeba_min:** 1 250
        - **limit_min:** 795
        - **zapas_min:** -455
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 1
    - **powod:** 19 wolnych miejsc na 1 wlasnych rejsach
    - **wolnych_miejsc:** 19
    - **rejsow:** 1
    - **lista**
      - **LO26-2026-08-24**
        - **numer:** LO26
        - **std:** 2026-08-24T16:50:00+00:00
        - **wolnych:** 19
- **dopuszczone_rodzaje_opcji**
  - **HOLD:** 0
  - **DEPART:** 1
  - **SWAP:** 1
  - **REBOOK-OWN:** 1
  - **REBOOK-OAL:** 1
  - **OVERNIGHT:** 1
  - **SPLIT:** 1
  - **CANCEL:** 1

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `MEL i ETOPS` | policy | 0.40 | brak biezacego statusu technicznego floty w zrodlach |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
