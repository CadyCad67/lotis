# [05] FEASIBILITY

**Status:** ok · **run:** `20260905T225451` · **snapshot:** `sha256:f3c290f4e6930407` · **9.91 ms**

Cztery bramki na rejsie LO3996 przy opoznieniu 90 min. Odpadly: samolot, zaloga.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | odpadla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | przeszla | - |
| `dopuszczonych_rodzajow` | 6 | szt |
| `nowy_std` | 2026-08-21T07:05:00+00:00 | - |
| `nowy_sta` | 2026-08-21T07:55:00+00:00 | - |

## Co ten node ustalil

- bramka samolot: port BZG nie jest baza SWAP (baza dopuszcza WAW) -- opcje od niej zalezne odpadaja
- bramka zaloga: 4 osob przekracza FDP przy opoznieniu 90 min (najgorszy zapas -700 min) -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 0
    - **powod:** port BZG nie jest baza SWAP (baza dopuszcza WAW)
    - **kandydaci:** 0
    - **bazy_swap**
      - WAW
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 4 osob przekracza FDP przy opoznieniu 90 min (najgorszy zapas -700 min)
    - **przekroczen:** 4
    - **lista**
      - **SP-LDI-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 240
        - **limit_min:** 540
        - **zapas_min:** -700
      - **SP-LDI-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 240
        - **limit_min:** 540
        - **zapas_min:** -700
      - **SP-LDI-CAB2**
        - **rola:** CABIN
        - **potrzeba_min:** 1 240
        - **limit_min:** 600
        - **zapas_min:** -640
      - **SP-LDI-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 240
        - **limit_min:** 600
        - **zapas_min:** -640
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 0
    - **port_koordynowany:** 0
  - **miejsca**
    - **przeszla:** 1
    - **powod:** 32 wolnych miejsc na 1 wlasnych rejsach
    - **wolnych_miejsc:** 32
    - **rejsow:** 1
    - **lista**
      - **LO3994-2026-08-21**
        - **numer:** LO3994
        - **std:** 2026-08-21T14:55:00+00:00
        - **wolnych:** 32
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
