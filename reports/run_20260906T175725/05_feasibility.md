# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **10.02 ms**

Cztery bramki na rejsie LO6 przy opoznieniu 30 min. Odpadly: zaloga, miejsca.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | przeszla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | odpadla | - |
| `dopuszczonych_rodzajow` | 5 | szt |
| `nowy_std` | 2026-08-22T12:40:00+00:00 | - |
| `nowy_sta` | 2026-08-22T22:10:00+00:00 | - |

## Co ten node ustalil

- bramka zaloga: 11 osob przekracza FDP przy opoznieniu 30 min (najgorszy zapas -515 min) -- opcje od niej zalezne odpadaja
- bramka miejsca: brak pozniejszego wlasnego rejsu WAW-JFK z wolnymi miejscami -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 1
    - **powod:** 3 maszyn do podmiany w WAW
    - **kandydaci:** 3
    - **lista**
      - **reg:** SP-LRE
      - **typ:** B788
      - **reg:** SP-LSB
      - **typ:** B789
      - **reg:** SP-LSG
      - **typ:** B789
    - **minimalny_postoj_min:** 136
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 11 osob przekracza FDP przy opoznieniu 30 min (najgorszy zapas -515 min)
    - **przekroczen:** 11
    - **lista**
      - **SP-LRG-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 295
        - **limit_min:** 780
        - **zapas_min:** -515
      - **SP-LRG-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 295
        - **limit_min:** 780
        - **zapas_min:** -515
      - **SP-LRG-FIR2**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 295
        - **limit_min:** 780
        - **zapas_min:** -515
      - **SP-LRG-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 295
        - **limit_min:** 840
        - **zapas_min:** -455
      - **SP-LRG-CAB4**
        - **rola:** CABIN
        - **potrzeba_min:** 1 295
        - **limit_min:** 840
        - **zapas_min:** -455
      - **SP-LRG-CAB5**
        - **rola:** CABIN
        - **potrzeba_min:** 1 295
        - **limit_min:** 840
        - **zapas_min:** -455
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
