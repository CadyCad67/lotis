# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260906T192705` · **snapshot:** `sha256:f3c290f4e6930407` · **25.7 ms**

Wygenerowano 7 opcji dla rejsu LO3981 (82 pasazerow, opoznienie 20 min). Odrzucono 3 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 7 | szt |
| `rodzajow_odrzuconych` | 3 | szt |
| `pasazerow_dotknietych` | 82 | osob |
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
      - LO3981-2026-08-21
    - **opoznienia**
      - **LO3981-2026-08-21:** 20
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
      - odmowa przyjecia z nadsprzedazy: Art. 4 ust. 3 odsyla do Art. 7
  - **SWAP-SP-LDH**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO3981-2026-08-21
      - LO3965-2026-08-21
    - **opoznienia**
      - **LO3981-2026-08-21:** 36
      - **LO3965-2026-08-21:** 20
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci -6 miejsc
      - rejs LO3965 przejmuje opoznienie 20 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
      - downgauge: 6 pasazerow schodzi
  - **SWAP-SP-LIO**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO3981-2026-08-21
      - LO265-2026-08-21
    - **opoznienia**
      - **LO3981-2026-08-21:** 36
      - **LO265-2026-08-21:** 20
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +0 miejsc
      - rejs LO265 przejmuje opoznienie 20 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **SWAP-SP-LIQ**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.SWAP
    - **rejsy**
      - LO3981-2026-08-21
      - LO655-2026-08-21
    - **opoznienia**
      - **LO3981-2026-08-21:** 36
      - **LO655-2026-08-21:** 20
    - **kasowane:** -
    - **uwagi**
      - zmiana pojemnosci +0 miejsc
      - rejs LO655 przejmuje opoznienie 20 min
      - rejs otrzymujacy maszyne nie zarabia -- unika straty
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO3981-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO3981-2026-08-21
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 625 min z CF.onward.next_bank_min (2 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: brak
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO3981-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO3981-2026-08-21
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO3981-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO3981-2026-08-21
    - **uwagi**
      - Art. 5: prawo wyboru zwrotu albo zmiany planu
      - Art. 5 ust. 1 lit. c: odszkodowanie nalezy sie za SAM fakt odwolania, bez progu opoznienia
      - pelna opieka przez czas oczekiwania (Art. 9)
      - pelna utrata przychodu z pasazerow nieprzebukowanych
      - przestawienie rotacji na kolejne odcinki
- **odrzucone_rodzaje**
  - **REBOOK-SPILL**
    - **powod:** brak wlasnego rejsu dla nadmiarowych
  - **REBOOK-OWN**
    - **powod:** brak pozniejszego wlasnego rejsu WAW-IEG z wolnymi miejscami
  - **SPLIT**
    - **powod:** wylaczone przelacznikiem albo brak miejsc

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
