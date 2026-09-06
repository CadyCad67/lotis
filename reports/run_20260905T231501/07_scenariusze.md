# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260905T231501` · **snapshot:** `sha256:f3c290f4e6930407` · **33.22 ms**

Wygenerowano 6 opcji dla rejsu LO3996 (61 pasazerow, opoznienie 90 min). Odrzucono 1 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 6 | szt |
| `rodzajow_odrzuconych` | 1 | szt |
| `pasazerow_dotknietych` | 61 | osob |
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
      - LO3996-2026-08-21
    - **opoznienia**
      - **LO3996-2026-08-21:** 90
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
  - **REBOOK-OWN**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OWN
    - **rejsy**
      - LO3996-2026-08-21
      - LO3994-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO3996-2026-08-21
    - **uwagi**
      - koszt = utracona sprzedaz miejsca (spill), nie pelna taryfa
      - czekanie 560 min liczy sie do progu opieki z Art. 9
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO3996-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO3996-2026-08-21
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 625 min z CF.onward.next_bank_min (2 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: LO
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO3996-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO3996-2026-08-21
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO3996-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO3996-2026-08-21
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
      - LO3996-2026-08-21
      - LO3994-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO3996-2026-08-21
    - **uwagi**
      - koszt = suma kosztow skladowych
      - ZAKAZ rozdzielania rodzin, grup i maloletnich bez opieki -- sprawdza filtr prawny
- **odrzucone_rodzaje**
  - **SWAP**
    - **powod:** port BZG nie jest baza SWAP (baza dopuszcza WAW)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
