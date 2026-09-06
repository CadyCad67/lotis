# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T194612` · **snapshot:** `sha256:6c790f69f87c3591` · **10.88 ms**

Cztery bramki na rejsie LO395 przy opoznieniu 60 min. Odpadly: zaloga.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | przeszla | - |
| `dopuszczonych_rodzajow` | 7 | szt |
| `nowy_std` | 2026-08-24T10:05:00+00:00 | - |
| `nowy_sta` | 2026-08-24T11:40:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 5 osob przekracza FDP przy opoznieniu 60 min (najgorszy zapas -400 min) -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 15 maszyn do podmiany w WAW
    - **kandydaci:** 15
    - **lista**
      - **reg:** SP-LDF
      - **typ:** E170
      - **reg:** SP-LIC
      - **typ:** E75S
      - **reg:** SP-LID
      - **typ:** E75S
      - **reg:** SP-LII
      - **typ:** E75S
      - **reg:** SP-LIM
      - **typ:** E75S
      - **reg:** SP-LMC
      - **typ:** E190
    - **minimalny_postoj_min:** 41
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 5 osob przekracza FDP przy opoznieniu 60 min (najgorszy zapas -400 min)
    - **przekroczen:** 5
    - **lista**
      - **SP-LMA-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 030
        - **limit_min:** 630
        - **zapas_min:** -400
      - **SP-LMA-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 030
        - **limit_min:** 630
        - **zapas_min:** -400
      - **SP-LMA-CAB2**
        - **rola:** CABIN
        - **potrzeba_min:** 1 015
        - **limit_min:** 645
        - **zapas_min:** -370
      - **SP-LMA-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 015
        - **limit_min:** 645
        - **zapas_min:** -370
      - **SP-LMA-CAB4**
        - **rola:** CABIN
        - **potrzeba_min:** 1 015
        - **limit_min:** 645
        - **zapas_min:** -370
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 1
    - **powod:** 39 wolnych miejsc na 2 wlasnych rejsach
    - **wolnych_miejsc:** 39
    - **rejsow:** 2
    - **lista**
      - **LO393-2026-08-24**
        - **numer:** LO393
        - **std:** 2026-08-24T17:05:00+00:00
        - **wolnych:** 11
      - **LO397-2026-08-24**
        - **numer:** LO397
        - **std:** 2026-08-24T20:35:00+00:00
        - **wolnych:** 28
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
