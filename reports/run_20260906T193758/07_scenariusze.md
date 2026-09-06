# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260906T193758` · **snapshot:** `sha256:6c790f69f87c3591` · **39.53 ms**

Wygenerowano 8 opcji dla rejsu LO6 (272 pasazerow, opoznienie 30 min). Odrzucono 0 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 8 | szt |
| `rodzajow_odrzuconych` | 0 | szt |
| `pasazerow_dotknietych` | 272 | osob |
| `modyfikujacych` | 2 | szt |
| `restrukturyzujacych` | 6 | szt |

## Co ten node ustalil

- SWAP wchodzi zawsze jako para rejsow -- rejs oddajacy i rejs otrzymujacy maszyne liczy sie razem
- opcje modyfikujace wycenia sie jako roznice wobec sytuacji bez zaklocenia, restrukturyzujace jako pelny nowy zestaw minus stary

## Szczegoly

- **opcje**
  - **HOLD**
    - **tryb:** MODIFYING
    - **generator:** SZ.HOLD
    - **rejsy**
      - LO6-2026-08-24
    - **opoznienia**
      - **LO6-2026-08-24:** 30
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
  - **SWAP-SP-LSA**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO6-2026-08-24
      - LO79-2026-08-24
    - **opoznienia**
      - **LO6-2026-08-24:** 139
      - **LO79-2026-08-24:** 30
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +0 miejsc
      - rejs LO79 przejmuje opoznienie 30 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **SWAP-SP-LSE**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO6-2026-08-24
      - LO99-2026-08-24
    - **opoznienia**
      - **LO6-2026-08-24:** 139
      - **LO99-2026-08-24:** 30
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +0 miejsc
      - rejs LO99 przejmuje opoznienie 30 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OWN
    - **rejsy**
      - LO6-2026-08-24
      - LO26-2026-08-24
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-24
    - **uwagi**
      - koszt = utracona sprzedaz miejsca (spill), nie pelna taryfa
      - czekanie 280 min liczy sie do progu opieki z Art. 9
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO6-2026-08-24
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-24
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 625 min z CF.onward.next_bank_min (2 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: B6
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO6-2026-08-24
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-24
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO6-2026-08-24
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-24
    - **uwagi**
      - Art. 5: prawo wyboru zwrotu albo zmiany planu
      - Art. 5 ust. 1 lit. c: odszkodowanie nalezy sie za SAM fakt odwolania, bez progu opoznienia
      - pelna opieka przez czas oczekiwania (Art. 9)
      - pelna utrata przychodu z pasazerow nieprzebukowanych
      - przestawienie rotacji na kolejne odcinki
  - **SPLIT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SPLIT
    - **rejsy**
      - LO6-2026-08-24
      - LO26-2026-08-24
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-24
    - **uwagi**
      - koszt = suma kosztow skladowych
      - ZAKAZ rozdzielania rodzin, grup i maloletnich bez opieki -- sprawdza filtr prawny
- **odrzucone_rodzaje:** -

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
