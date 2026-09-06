# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260906T130705` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **31.65 ms**

Wygenerowano 9 opcji dla rejsu LO417 (52 pasazerow, opoznienie 180 min). Odrzucono 0 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 9 | szt |
| `rodzajow_odrzuconych` | 0 | szt |
| `pasazerow_dotknietych` | 52 | osob |
| `modyfikujacych` | 2 | szt |
| `restrukturyzujacych` | 7 | szt |

## Co ten node ustalil

- SWAP wchodzi zawsze jako para rejsow -- rejs oddajacy i rejs otrzymujacy maszyne liczy sie razem
- opcje modyfikujace wycenia sie jako roznice wobec sytuacji bez zaklocenia, restrukturyzujace jako pelny nowy zestaw minus stary

## Szczegoly

- **opcje**
  - **HOLD**
    - **tryb:** MODIFYING
    - **generator:** SZ.HOLD
    - **rejsy**
      - LO417-2026-08-25
    - **opoznienia**
      - **LO417-2026-08-25:** 180
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
  - **SWAP-SP-LDH**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO417-2026-08-25
      - LO509-2026-08-25
    - **opoznienia**
      - **LO417-2026-08-25:** 36
      - **LO509-2026-08-25:** 180
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci -6 miejsc
      - rejs LO509 przejmuje opoznienie 180 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **SWAP-SP-LIK**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO417-2026-08-25
      - LO3905-2026-08-25
    - **opoznienia**
      - **LO417-2026-08-25:** 36
      - **LO3905-2026-08-25:** 180
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +0 miejsc
      - rejs LO3905 przejmuje opoznienie 180 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **SWAP-SP-LIL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO417-2026-08-25
      - LO527-2026-08-25
    - **opoznienia**
      - **LO417-2026-08-25:** 36
      - **LO527-2026-08-25:** 180
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +0 miejsc
      - rejs LO527 przejmuje opoznienie 180 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OWN
    - **rejsy**
      - LO417-2026-08-25
      - LO415-2026-08-25
    - **opoznienia:** {}
    - **kasowane**
      - LO417-2026-08-25
    - **uwagi**
      - koszt = utracona sprzedaz miejsca (spill), nie pelna taryfa
      - czekanie 550 min liczy sie do progu opieki z Art. 9
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO417-2026-08-25
    - **opoznienia:** {}
    - **kasowane**
      - LO417-2026-08-25
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 625 min z CF.onward.next_bank_min (2 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: LX
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO417-2026-08-25
    - **opoznienia:** {}
    - **kasowane**
      - LO417-2026-08-25
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO417-2026-08-25
    - **opoznienia:** {}
    - **kasowane**
      - LO417-2026-08-25
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
      - LO417-2026-08-25
      - LO415-2026-08-25
    - **opoznienia:** {}
    - **kasowane**
      - LO417-2026-08-25
    - **uwagi**
      - koszt = suma kosztow skladowych
      - ZAKAZ rozdzielania rodzin, grup i maloletnich bez opieki -- sprawdza filtr prawny
- **odrzucone_rodzaje:** -

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
