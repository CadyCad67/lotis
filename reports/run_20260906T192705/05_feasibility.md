# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T192705` · **snapshot:** `sha256:f3c290f4e6930407` · **9.9 ms**

Cztery bramki na rejsie LO3981 przy opoznieniu 20 min. Odpadly: zaloga, miejsca.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | odpadla | - |
| `dopuszczonych_rodzajow` | 5 | szt |
| `nowy_std` | 2026-08-21T07:25:00+00:00 | - |
| `nowy_sta` | 2026-08-21T08:25:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 4 osob przekracza FDP przy opoznieniu 20 min (najgorszy zapas -385 min) -- opcje od niej zalezne odpadaja
- bramka miejsca: brak pozniejszego wlasnego rejsu WAW-IEG z wolnymi miejscami -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 12 maszyn do podmiany w WAW
    - **kandydaci:** 12
    - **lista**
      - **reg:** SP-LDH
      - **typ:** E170
      - **reg:** SP-LID
      - **typ:** E75S
      - **reg:** SP-LIO
      - **typ:** E75S
      - **reg:** SP-LIQ
      - **typ:** E75S
      - **reg:** SP-LMC
      - **typ:** E190
      - **reg:** SP-LMF
      - **typ:** E190
    - **minimalny_postoj_min:** 36
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 4 osob przekracza FDP przy opoznieniu 20 min (najgorszy zapas -385 min)
    - **przekroczen:** 4
    - **lista**
      - **SP-LIC-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 015
        - **limit_min:** 630
        - **zapas_min:** -385
      - **SP-LIC-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 015
        - **limit_min:** 630
        - **zapas_min:** -385
      - **SP-LIC-CAB2**
        - **rola:** CABIN
        - **potrzeba_min:** 1 000
        - **limit_min:** 645
        - **zapas_min:** -355
      - **SP-LIC-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 000
        - **limit_min:** 645
        - **zapas_min:** -355
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 0
    - **powod:** brak pozniejszego wlasnego rejsu WAW-IEG z wolnymi miejscami
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
