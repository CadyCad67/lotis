# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **10.53 ms**

Cztery bramki na rejsie LO6 przy opoznieniu 20 min. Odpadly: zaloga, miejsca.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | odpadla | - |
| `dopuszczonych_rodzajow` | 5 | szt |
| `nowy_std` | 2026-08-21T12:30:00+00:00 | - |
| `nowy_sta` | 2026-08-21T22:00:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 11 osob przekracza FDP przy opoznieniu 20 min (najgorszy zapas -505 min) -- opcje od niej zalezne odpadaja
- bramka miejsca: brak pozniejszego wlasnego rejsu WAW-JFK z wolnymi miejscami -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 4 maszyn do podmiany w WAW
    - **kandydaci:** 4
    - **lista**
      - **reg:** SP-LRA
      - **typ:** B788
      - **reg:** SP-LRF
      - **typ:** B788
      - **reg:** SP-LSA
      - **typ:** B789
      - **reg:** SP-LSC
      - **typ:** B789
    - **minimalny_postoj_min:** 136
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 11 osob przekracza FDP przy opoznieniu 20 min (najgorszy zapas -505 min)
    - **przekroczen:** 11
    - **lista**
      - **SP-LRE-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 285
        - **limit_min:** 780
        - **zapas_min:** -505
      - **SP-LRE-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 285
        - **limit_min:** 780
        - **zapas_min:** -505
      - **SP-LRE-FIR2**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 285
        - **limit_min:** 780
        - **zapas_min:** -505
      - **SP-LRE-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 270
        - **limit_min:** 795
        - **zapas_min:** -475
      - **SP-LRE-CAB4**
        - **rola:** CABIN
        - **potrzeba_min:** 1 270
        - **limit_min:** 795
        - **zapas_min:** -475
      - **SP-LRE-CAB5**
        - **rola:** CABIN
        - **potrzeba_min:** 1 270
        - **limit_min:** 795
        - **zapas_min:** -475
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 0
    - **powod:** brak pozniejszego wlasnego rejsu WAW-JFK z wolnymi miejscami
    - **wolnych_miejsc:** 0
    - **rejsow:** 0
- **dopuszczone_rodzaje_opcji**
  - **HOLD:** 0
  - **DEPART:** 1
  - **SWAP:** 1
  - **REBOOK-OWN:** 0
  - **REBOOK-OAL:** 1
  - **OVERNIGHT:** 1
  - **SPLIT:** 0
  - **CANCEL:** 1

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `MEL i ETOPS` | policy | 0.40 | brak biezacego statusu technicznego floty w zrodlach |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
