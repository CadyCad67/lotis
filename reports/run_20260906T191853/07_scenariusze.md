# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260906T191853` · **snapshot:** `sha256:f3c290f4e6930407` · **18.23 ms**

Wygenerowano 6 opcji dla rejsu LO6 (242 pasazerow, opoznienie 20 min). Odrzucono 2 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 6 | szt |
| `rodzajow_odrzuconych` | 2 | szt |
| `pasazerow_dotknietych` | 242 | osob |
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
      - LO6-2026-08-21
    - **opoznienia**
      - **LO6-2026-08-21:** 20
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
      - odmowa przyjecia z nadsprzedazy: Art. 4 ust. 3 odsyla do Art. 7
  - **SWAP-SP-LRF**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO6-2026-08-21
      - LO71-2026-08-21
    - **opoznienia**
      - **LO6-2026-08-21:** 136
      - **LO71-2026-08-21:** 20
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +0 miejsc
      - rejs LO71 przejmuje opoznienie 20 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **SWAP-SP-LSC**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO6-2026-08-21
      - LO79-2026-08-21
    - **opoznienia**
      - **LO6-2026-08-21:** 136
      - **LO79-2026-08-21:** 20
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +42 miejsc
      - rejs LO79 przejmuje opoznienie 20 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO6-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-21
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 925 min z CF.onward.next_bank_min (1 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: B6
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO6-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-21
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO6-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO6-2026-08-21
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
