# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260906T175204` · **snapshot:** `sha256:91cb2a4af61a3714` · **16.74 ms**

Wygenerowano 6 opcji dla rejsu LO6 (241 pasazerow, opoznienie 120 min). Odrzucono 2 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 6 | szt |
| `rodzajow_odrzuconych` | 2 | szt |
| `pasazerow_dotknietych` | 241 | osob |
| `modyfikujacych` | 2 | szt |
| `restrukturyzujacych` | 4 | szt |

## Co ten node ustalil

- SWAP wchodzi zawsze jako para rejsow -- rejs oddajacy i rejs otrzymujacy maszyne liczy sie razem
- opcje modyfikujace wycenia sie jako roznice wobec sytuacji bez zaklocenia, restrukturyzujace jako pelny nowy zestaw minus stary

## Szczegoly

- **opcje**
  - **HOLD**
    - **tryb:** MODIFYING
    - **generator:** SZ.HOLD
    - **rejsy**
      - LO6-2026-08-22
    - **opoznienia**
      - **LO6-2026-08-22:** 120
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
  - **SWAP-SP-LSB**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO6-2026-08-22
      - LO79-2026-08-22
    - **opoznienia**
      - **LO6-2026-08-22:** 136
      - **LO79-2026-08-22:** 120
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +42 miejsc
      - rejs LO79 przejmuje opoznienie 120 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **SWAP-SP-LSG**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO6-2026-08-22
      - LO99-2026-08-22
    - **opoznienia**
      - **LO6-2026-08-22:** 136
      - **LO99-2026-08-22:** 120
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +42 miejsc
      - rejs LO99 przejmuje opoznienie 120 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO6-2026-08-22
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-22
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 925 min z CF.onward.next_bank_min (1 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: B6
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO6-2026-08-22
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-22
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO6-2026-08-22
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-22
    - **uwagi**
      - Art. 5: prawo wyboru zwrotu albo zmiany planu
      - Art. 5 ust. 1 lit. c: odszkodowanie nalezy sie za SAM fakt odwolania, bez progu opoznienia
      - pelna opieka przez czas oczekiwania (Art. 9)
      - pelna utrata przychodu z pasazerow nieprzebukowanych
      - przestawienie rotacji na kolejne odcinki
- **odrzucone_rodzaje**
  - **REBOOK-OWN**
    - **powod:** brak pozniejszego wlasnego rejsu WAW-JFK z wolnymi miejscami
  - **SPLIT**
    - **powod:** wylaczone przelacznikiem albo brak miejsc

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
