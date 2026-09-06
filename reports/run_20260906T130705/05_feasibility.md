# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T130705` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **9.19 ms**

Cztery bramki na rejsie LO417 przy opoznieniu 180 min. Odpadly: zaloga.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | przeszla | - |
| `dopuszczonych_rodzajow` | 7 | szt |
| `nowy_std` | 2026-08-25T10:20:00+00:00 | - |
| `nowy_sta` | 2026-08-25T12:40:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 4 osob przekracza FDP przy opoznieniu 180 min (najgorszy zapas -685 min) -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 19 maszyn do podmiany w WAW
    - **kandydaci:** 19
    - **lista**
      - **reg:** SP-LDF
      - **typ:** E170
      - **reg:** SP-LDH
      - **typ:** E170
      - **reg:** SP-LIK
      - **typ:** E75S
      - **reg:** SP-LIL
      - **typ:** E75S
      - **reg:** SP-LIN
      - **typ:** E75S
      - **reg:** SP-LIO
      - **typ:** E75S
    - **minimalny_postoj_min:** 36
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 4 osob przekracza FDP przy opoznieniu 180 min (najgorszy zapas -685 min)
    - **przekroczen:** 4
    - **lista**
      - **SP-LIM-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 255
        - **limit_min:** 570
        - **zapas_min:** -685
      - **SP-LIM-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 255
        - **limit_min:** 570
        - **zapas_min:** -685
      - **SP-LIM-CAB2**
        - **rola:** CABIN
        - **potrzeba_min:** 1 255
        - **limit_min:** 630
        - **zapas_min:** -625
      - **SP-LIM-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 255
        - **limit_min:** 630
        - **zapas_min:** -625
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 1
    - **powod:** 16 wolnych miejsc na 1 wlasnych rejsach
    - **wolnych_miejsc:** 16
    - **rejsow:** 1
    - **lista**
      - **LO415-2026-08-25**
        - **numer:** LO415
        - **std:** 2026-08-25T16:30:00+00:00
        - **wolnych:** 16
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
