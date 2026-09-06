# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **10.46 ms**

Cztery bramki na rejsie LO82 przy opoznieniu 0 min. Odpadly: samolot, zaloga.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | odpadla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | przeszla | - |
| `dopuszczonych_rodzajow` | 6 | szt |
| `nowy_std` | 2026-08-24T01:15:00+00:00 | - |
| `nowy_sta` | 2026-08-24T15:30:00+00:00 | - |

## Co ten node ustalil

- bramka samolot: port NRT nie jest baza SWAP (baza dopuszcza WAW) -- opcje od niej zalezne odpadaja
- bramka zaloga: 11 osob przekracza FDP przy opoznieniu 0 min (najgorszy zapas -845 min) -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 0
    - **powod:** port NRT nie jest baza SWAP (baza dopuszcza WAW)
    - **kandydaci:** 0
    - **bazy_swap**
      - WAW
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 11 osob przekracza FDP przy opoznieniu 0 min (najgorszy zapas -845 min)
    - **przekroczen:** 11
    - **lista**
      - **SP-LRE-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 595
        - **limit_min:** 750
        - **zapas_min:** -845
      - **SP-LRE-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 595
        - **limit_min:** 750
        - **zapas_min:** -845
      - **SP-LRE-FIR2**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 595
        - **limit_min:** 750
        - **zapas_min:** -845
      - **SP-LRE-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 580
        - **limit_min:** 765
        - **zapas_min:** -815
      - **SP-LRE-CAB4**
        - **rola:** CABIN
        - **potrzeba_min:** 1 580
        - **limit_min:** 765
        - **zapas_min:** -815
      - **SP-LRE-CAB5**
        - **rola:** CABIN
        - **potrzeba_min:** 1 580
        - **limit_min:** 765
        - **zapas_min:** -815
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 1
    - **powod:** 29 wolnych miejsc na 1 wlasnych rejsach
    - **wolnych_miejsc:** 29
    - **rejsow:** 1
    - **lista**
      - **LO80-2026-08-24**
        - **numer:** LO80
        - **std:** 2026-08-24T15:50:00+00:00
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
