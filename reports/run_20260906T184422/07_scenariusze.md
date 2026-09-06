# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **16.81 ms**

Wygenerowano 7 opcji dla rejsu LO35 (256 pasazerow, opoznienie 0 min). Odrzucono 2 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 7 | szt |
| `rodzajow_odrzuconych` | 2 | szt |
| `pasazerow_dotknietych` | 256 | osob |
| `modyfikujacych` | 2 | szt |
| `restrukturyzujacych` | 5 | szt |

## Co ten node ustalil

- SWAP wchodzi zawsze jako para rejsow -- rejs oddajacy i rejs otrzymujacy maszyne liczy sie razem
- opcje modyfikujace wycenia sie jako roznice wobec sytuacji bez zaklocenia, restrukturyzujace jako pelny nowy zestaw minus stary

## Szczegoly

- **opcje**
  - **HOLD**
    - **tryb:** MODIFYING
    - **generator:** SZ.HOLD
    - **rejsy**
      - LO35-2026-08-23
    - **opoznienia**
      - **LO35-2026-08-23:** 0
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
  - **SWAP-SP-LRC**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO35-2026-08-23
      - LO71-2026-08-23
    - **opoznienia**
      - **LO35-2026-08-23:** 139
      - **LO71-2026-08-23:** 0
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci -42 miejsc
      - rejs LO71 przejmuje opoznienie 0 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
      - downgauge: 4 pasazerow schodzi
  - **SWAP-SP-LRD**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO35-2026-08-23
      - LO79-2026-08-23
    - **opoznienia**
      - **LO35-2026-08-23:** 139
      - **LO79-2026-08-23:** 0
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci -42 miejsc
      - rejs LO79 przejmuje opoznienie 0 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
      - downgauge: 4 pasazerow schodzi
  - **SWAP-SP-LRH**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO35-2026-08-23
      - LO6-2026-08-23
    - **opoznienia**
      - **LO35-2026-08-23:** 139
      - **LO6-2026-08-23:** 0
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci -42 miejsc
      - rejs LO6 przejmuje opoznienie 0 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
      - downgauge: 4 pasazerow schodzi
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO35-2026-08-23
    - **opoznienia:** {}
    - **kasowane**
      - LO35-2026-08-23
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 925 min z CF.onward.next_bank_min (1 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: brak
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO35-2026-08-23
    - **opoznienia:** {}
    - **kasowane**
      - LO35-2026-08-23
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO35-2026-08-23
    - **opoznienia:** {}
    - **kasowane**
      - LO35-2026-08-23
    - **uwagi**
      - Art. 5: prawo wyboru zwrotu albo zmiany planu
      - Art. 5 ust. 1 lit. c: odszkodowanie nalezy sie za SAM fakt odwolania, bez progu opoznienia
      - pelna opieka przez czas oczekiwania (Art. 9)
      - pelna utrata przychodu z pasazerow nieprzebukowanych
      - przestawienie rotacji na kolejne odcinki
- **odrzucone_rodzaje**
  - **REBOOK-OWN**
    - **powod:** brak pozniejszego wlasnego rejsu WAW-SFO z wolnymi miejscami
  - **SPLIT**
    - **powod:** wylaczone przelacznikiem albo brak miejsc

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
