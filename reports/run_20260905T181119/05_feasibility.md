# [05] FEASIBILITY

**Status:** ok · **run:** `20260905T181119` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **8.92 ms**

Cztery bramki na rejsie LO3850 przy opoznieniu 240 min. Odpadly: samolot, zaloga.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | odpadla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | przeszla | - |
| `dopuszczonych_rodzajow` | 6 | szt |
| `nowy_std` | 2026-08-25T09:35:00+00:00 | - |
| `nowy_sta` | 2026-08-25T10:30:00+00:00 | - |

## Co ten node ustalil

- bramka samolot: port WRO nie jest baza SWAP (baza dopuszcza WAW) -- opcje od niej zalezne odpadaja
- bramka zaloga: 4 osob przekracza FDP przy opoznieniu 240 min (najgorszy zapas -745 min) -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 0
    - **powod:** port WRO nie jest baza SWAP (baza dopuszcza WAW)
    - **kandydaci:** 0
    - **bazy_swap**
      - WAW
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 4 osob przekracza FDP przy opoznieniu 240 min (najgorszy zapas -745 min)
    - **przekroczen:** 4
    - **lista**
      - **SP-LIM-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 315
        - **limit_min:** 570
        - **zapas_min:** -745
      - **SP-LIM-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 315
        - **limit_min:** 570
        - **zapas_min:** -745
      - **SP-LIM-CAB2**
        - **rola:** CABIN
        - **potrzeba_min:** 1 315
        - **limit_min:** 630
        - **zapas_min:** -685
      - **SP-LIM-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 315
        - **limit_min:** 630
        - **zapas_min:** -685
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 0
    - **port_koordynowany:** 0
  - **miejsca**
    - **przeszla:** 1
    - **powod:** 161 wolnych miejsc na 5 wlasnych rejsach
    - **wolnych_miejsc:** 161
    - **rejsow:** 5
    - **lista**
      - **LO3852-2026-08-25**
        - **numer:** LO3852
        - **std:** 2026-08-25T08:45:00+00:00
        - **wolnych:** 41
      - **LO3854-2026-08-25**
        - **numer:** LO3854
        - **std:** 2026-08-25T12:10:00+00:00
        - **wolnych:** 27
      - **LO3844-2026-08-25**
        - **numer:** LO3844
        - **std:** 2026-08-25T14:55:00+00:00
        - **wolnych:** 25
      - **LO3848-2026-08-25**
        - **numer:** LO3848
        - **std:** 2026-08-25T18:15:00+00:00
        - **wolnych:** 39
      - **LO3860-2026-08-25**
        - **numer:** LO3860
        - **std:** 2026-08-25T21:30:00+00:00
        - **wolnych:** 29
- **dopuszczone_rodzaje_opcji**
  - **HOLD:** 0
  - **DEPART:** 1
  - **SWAP:** 0
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
