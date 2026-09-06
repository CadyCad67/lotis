# [05] FEASIBILITY

**Status:** ok · **run:** `20260906T174137` · **snapshot:** `sha256:f3c290f4e6930407` · **10.2 ms**

Cztery bramki na rejsie LO2098 przy opoznieniu 180 min. Odpadly: samolot, zaloga, miejsca.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `bramka_samolot` | odpadla | - |
| `bramka_zaloga` | odpadla | - |
| `bramka_port` | przeszla | - |
| `bramka_miejsca` | odpadla | - |
| `dopuszczonych_rodzajow` | 4 | szt |
| `nowy_std` | 2026-08-21T03:10:00+00:00 | - |
| `nowy_sta` | 2026-08-21T12:30:00+00:00 | - |

## Co ten node ustalil

- bramka samolot: port ORD nie jest baza SWAP (baza dopuszcza WAW) -- opcje od niej zalezne odpadaja
- bramka zaloga: 11 osob przekracza FDP przy opoznieniu 180 min (najgorszy zapas -900 min) -- opcje od niej zalezne odpadaja
- bramka miejsca: brak pozniejszego wlasnego rejsu ORD-KRK z wolnymi miejscami -- opcje od niej zalezne odpadaja
- dyskrecja dowodcy (+2 h wg ORO.FTL.205 lit. f) NIE jest wliczana w wykonalnosc -- to decyzja dowodcy, nie planisty

## Szczegoly

- **bramki**
  - **samolot**
    - **przeszla:** 0
    - **powod:** port ORD nie jest baza SWAP (baza dopuszcza WAW)
    - **kandydaci:** 0
    - **bazy_swap**
      - WAW
  - **zaloga**
    - **przeszla:** 0
    - **powod:** 11 osob przekracza FDP przy opoznieniu 180 min (najgorszy zapas -900 min)
    - **przekroczen:** 11
    - **lista**
      - **SP-LSF-CAP0**
        - **rola:** CAPTAIN
        - **potrzeba_min:** 1 560
        - **limit_min:** 660
        - **zapas_min:** -900
      - **SP-LSF-FIR1**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 560
        - **limit_min:** 660
        - **zapas_min:** -900
      - **SP-LSF-FIR2**
        - **rola:** FIRST_OFFICER
        - **potrzeba_min:** 1 560
        - **limit_min:** 660
        - **zapas_min:** -900
      - **SP-LSF-CAB3**
        - **rola:** CABIN
        - **potrzeba_min:** 1 560
        - **limit_min:** 720
        - **zapas_min:** -840
      - **SP-LSF-CAB4**
        - **rola:** CABIN
        - **potrzeba_min:** 1 560
        - **limit_min:** 720
        - **zapas_min:** -840
      - **SP-LSF-CAB5**
        - **rola:** CABIN
        - **potrzeba_min:** 1 560
        - **limit_min:** 720
        - **zapas_min:** -840
  - **port**
    - **przeszla:** 1
    - **powod:** nowe godziny poza oknem zakazu planowania
    - **poziom_slotow_wylotu:** 2
    - **port_koordynowany:** 0
  - **miejsca**
    - **przeszla:** 0
    - **powod:** brak pozniejszego wlasnego rejsu ORD-KRK z wolnymi miejscami
    - **wolnych_miejsc:** 0
    - **rejsow:** 0
- **dopuszczone_rodzaje_opcji**
  - **HOLD:** 0
  - **DEPART:** 1
  - **SWAP:** 0
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
