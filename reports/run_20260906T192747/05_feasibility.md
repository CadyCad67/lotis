# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T192747` · **snapshot:** `sha256:f3c290f4e6930407` · **10.48 ms**

Cztery bramki na rejsie LO3931 przy opoznieniu 20 min. Odpadly: zaloga.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | przeszla | - |
| `dopuszczonych_rodzajow` | 7 | szt |
| `nowy_std` | 2026-08-21T07:25:00+00:00 | - |
| `nowy_sta` | 2026-08-21T08:30:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 4 osob przekracza FDP przy opoznieniu 20 min (najgorszy zapas -545 min) -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 13 maszyn do podmiany w WAW
    - **kandydaci:** 13
    - **lista**
      - **reg:** SP-LDH
      - **typ:** E170
      - **reg:** SP-LIC
      - **typ:** E75S
      - **reg:** SP-LID
      - **typ:** E75S
      - **reg:** SP-LIO
      - **typ:** E75S
      - **reg:** SP-LIQ
      - **typ:** E75S
      - **reg:** SP-LMC
      - **typ:** E190
    - **minimalny_postoj_min:** 36
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 4 osob przekracza FDP przy opoznieniu 20 min (najgorszy zapas -545 min)
    - **przekroczen:** 4
    - **lista**
      - **SP-LII-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 145
        - **limit_min:** 600
        - **zapas_min:** -545
      - **SP-LII-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 145
        - **limit_min:** 600
        - **zapas_min:** -545
      - **SP-LII-CAB2**
        - **rola:** CABIN
        - **potrzeba_min:** 1 130
        - **limit_min:** 615
        - **zapas_min:** -515
      - **SP-LII-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 130
        - **limit_min:** 615
        - **zapas_min:** -515
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 1
    - **powod:** 53 wolnych miejsc na 2 wlasnych rejsach
    - **wolnych_miejsc:** 53
    - **rejsow:** 2
    - **lista**
      - **LO3933-2026-08-21**
        - **numer:** LO3933
        - **std:** 2026-08-21T11:55:00+00:00
        - **wolnych:** 23
      - **LO3935-2026-08-21**
        - **numer:** LO3935
        - **std:** 2026-08-21T19:35:00+00:00
        - **wolnych:** 30
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
