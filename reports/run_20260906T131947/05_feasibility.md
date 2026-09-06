# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **10.0 ms**

Cztery bramki na rejsie LO21 przy opoznieniu 30 min. Odpadly: zaloga, miejsca.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | odpadla | - |
| `dopuszczonych_rodzajow` | 5 | szt |
| `nowy_std` | 2026-08-26T11:50:00+00:00 | - |
| `nowy_sta` | 2026-08-27T00:05:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 11 osob przekracza FDP przy opoznieniu 30 min (najgorszy zapas -750 min) -- opcje od niej zalezne odpadaja
- bramka miejsca: brak pozniejszego wlasnego rejsu WAW-LAX z wolnymi miejscami -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 7 maszyn do podmiany w WAW
    - **kandydaci:** 7
    - **lista**
      - **reg:** SP-LRC
      - **typ:** B788
      - **reg:** SP-LRD
      - **typ:** B788
      - **reg:** SP-LRG
      - **typ:** B788
      - **reg:** SP-LSC
      - **typ:** B789
      - **reg:** SP-LSD
      - **typ:** B789
      - **reg:** SP-LSF
      - **typ:** B789
    - **minimalny_postoj_min:** 139
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 11 osob przekracza FDP przy opoznieniu 30 min (najgorszy zapas -750 min)
    - **przekroczen:** 11
    - **lista**
      - **SP-LSA-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 410
        - **limit_min:** 660
        - **zapas_min:** -750
      - **SP-LSA-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 410
        - **limit_min:** 660
        - **zapas_min:** -750
      - **SP-LSA-FIR2**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 410
        - **limit_min:** 660
        - **zapas_min:** -750
      - **SP-LSA-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 410
        - **limit_min:** 720
        - **zapas_min:** -690
      - **SP-LSA-CAB4**
        - **rola:** CABIN
        - **potrzeba_min:** 1 410
        - **limit_min:** 720
        - **zapas_min:** -690
      - **SP-LSA-CAB5**
        - **rola:** CABIN
        - **potrzeba_min:** 1 410
        - **limit_min:** 720
        - **zapas_min:** -690
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 3
    - **port_koordynowany:** 1
  - **miejsca**
    - **przeszla:** 0
    - **powod:** brak pozniejszego wlasnego rejsu WAW-LAX z wolnymi miejscami
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
