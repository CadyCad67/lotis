# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **9.75 ms**

Cztery bramki na rejsie LO35 przy opoznieniu 0 min. Odpadly: zaloga, miejsca.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | odpadla | - |
| `dopuszczonych_rodzajow` | 5 | szt |
| `nowy_std` | 2026-08-23T11:00:00+00:00 | - |
| `nowy_sta` | 2026-08-23T23:00:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 11 osob przekracza FDP przy opoznieniu 0 min (najgorszy zapas -710 min) -- opcje od niej zalezne odpadaja
- bramka miejsca: brak pozniejszego wlasnego rejsu WAW-SFO z wolnymi miejscami -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 7 maszyn do podmiany w WAW
    - **kandydaci:** 7
    - **lista**
      - **reg:** SP-LRB
      - **typ:** B788
      - **reg:** SP-LRC
      - **typ:** B788
      - **reg:** SP-LRD
      - **typ:** B788
      - **reg:** SP-LRE
      - **typ:** B788
      - **reg:** SP-LRG
      - **typ:** B788
      - **reg:** SP-LRH
      - **typ:** B788
    - **minimalny_postoj_min:** 139
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 11 osob przekracza FDP przy opoznieniu 0 min (najgorszy zapas -710 min)
    - **przekroczen:** 11
    - **lista**
      - **SP-LSE-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 385
        - **limit_min:** 675
        - **zapas_min:** -710
      - **SP-LSE-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 385
        - **limit_min:** 675
        - **zapas_min:** -710
      - **SP-LSE-FIR2**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 385
        - **limit_min:** 675
        - **zapas_min:** -710
      - **SP-LSE-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 370
        - **limit_min:** 690
        - **zapas_min:** -680
      - **SP-LSE-CAB4**
        - **rola:** CABIN
        - **potrzeba_min:** 1 370
        - **limit_min:** 690
        - **zapas_min:** -680
      - **SP-LSE-CAB5**
        - **rola:** CABIN
        - **potrzeba_min:** 1 370
        - **limit_min:** 690
        - **zapas_min:** -680
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 0
    - **powod:** brak pozniejszego wlasnego rejsu WAW-SFO z wolnymi miejscami
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
