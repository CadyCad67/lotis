# [07] SCENARIO ENGINE

**Status:** ok · **run:** `20260906T174137` · **snapshot:** `sha256:f3c290f4e6930407` · **16.76 ms**

Wygenerowano 4 opcji dla rejsu LO2098 (258 pasazerow, opoznienie 180 min). Odrzucono 3 rodzajow przed wycena.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji` | 4 | szt |
| `rodzajow_odrzuconych` | 3 | szt |
| `pasazerow_dotknietych` | 258 | osob |
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
      - LO2098-2026-08-21
    - **opoznienia**
      - **LO2098-2026-08-21:** 180
    - **kasowane:** -
    - **uwagi**
      - koszt = minuty x stawka krancowa typu + propagacja
      - ekspozycja EU261 rosnie po przekroczeniu 3 h na przylocie
  - **REBOOK-OAL**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.REBOOK-OAL
    - **rejsy**
      - LO2098-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO2098-2026-08-21
    - **uwagi**
      - doplata wg poziomu partnera i dystansu -- bez niej OAL wychodzi za tanio
      - mozliwa redukcja odszkodowania o 50% (Art. 7 ust. 2)
      - oczekiwanie 925 min z CF.onward.next_bank_min (1 rejsow dziennie na tej relacji) + MCT partnera
      - partnerzy w porcie docelowym: LO
  - **OVERNIGHT**
    - **tryb:** RESTRUCTURING
    - **generator:** SZ.OVERNIGHT
    - **rejsy**
      - LO2098-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO2098-2026-08-21
    - **uwagi**
      - pelna opieka: hotel, posilki, transport
      - pelna ekspozycja EU261 przy klasie kodu przewoznika
      - nocleg zalogi dochodzi osobno
  - **CANCEL**
    - **tryb:** MODIFYING
    - **generator:** SZ.CANCEL
    - **rejsy**
      - LO2098-2026-08-21
    - **opoznienia:** {}
    - **kasowane**
      - LO2098-2026-08-21
    - **uwagi**
      - Art. 5: prawo wyboru zwrotu albo zmiany planu
      - Art. 5 ust. 1 lit. c: odszkodowanie nalezy sie za SAM fakt odwolania, bez progu opoznienia
      - pelna opieka przez czas oczekiwania (Art. 9)
      - pelna utrata przychodu z pasazerow nieprzebukowanych
      - przestawienie rotacji na kolejne odcinki
- **odrzucone_rodzaje**
  - **SWAP**
    - **powod:** port ORD nie jest baza SWAP (baza dopuszcza WAW)
  - **REBOOK-OWN**
    - **powod:** brak pozniejszego wlasnego rejsu ORD-KRK z wolnymi miejscami
  - **SPLIT**
    - **powod:** wylaczone przelacznikiem albo brak miejsc

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
