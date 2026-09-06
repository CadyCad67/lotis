# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **47.3 ms**

Wygenerowano 4 opcji dla rejsu LO82 (227 pasazerow, opoznienie 0 min). Odrzucono 3 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 4 | szt |
| `rodzajow_odrzuconych` | 3 | szt |
| `pasazerow_dotknietych` | 227 | osob |
| `modyfikujacych` | 2 | szt |
| `restrukturyzujacych` | 2 | szt |

## Co ten node ustalil

- SWAP wchodzi zawsze jako para rejsow -- rejs oddajacy i rejs otrzymujacy maszyne liczy sie razem
- opcje modyfikujace wycenia sie jako roznice wobec sytuacji bez zaklocenia, restrukturyzujace jako pelny nowy zestaw minus stary

## Szczegoly

- **opcje**
  - **HOLD**
    - **tryb:** MODIFYING
    - **generator:** SZ.HOLD
    - **rejsy**
      - LO82-2026-08-24
    - **opoznienia**
      - **LO82-2026-08-24:** 0
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
      - odmowa przyjecia z nadsprzedazy: Art. 4 ust. 3 odsyla do Art. 7
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO82-2026-08-24
    - **opoznienia:** {}
    - **kasowane**
      - LO82-2026-08-24
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 625 min z CF.onward.next_bank_min (2 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: LO
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO82-2026-08-24
    - **opoznienia:** {}
    - **kasowane**
      - LO82-2026-08-24
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO82-2026-08-24
    - **opoznienia:** {}
    - **kasowane**
      - LO82-2026-08-24
    - **uwagi**
      - Art. 5: prawo wyboru zwrotu albo zmiany planu
      - Art. 5 ust. 1 lit. c: odszkodowanie nalezy sie za SAM fakt odwolania, bez progu opoznienia
      - pelna opieka przez czas oczekiwania (Art. 9)
      - pelna utrata przychodu z pasazerow nieprzebukowanych
      - przestawienie rotacji na kolejne odcinki
- **odrzucone_rodzaje**
  - **REBOOK-SPILL**
    - **powod:** brak wlasnego rejsu dla nadmiarowych
  - **SWAP**
    - **powod:** port NRT nie jest baza SWAP (baza dopuszcza WAW)
  - **REBOOK-OWN**
    - **powod:** brak pozniejszego wlasnego rejsu

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
