# [06] REZERWACJA ZASOBU

**Status:** ok · **run:** `20260905T181228` · **snapshot:** `sha256:f3c290f4e6930407` · **0.08 ms**

W BZG do dyspozycji 1 rodzajow zasobu. Zaden nie jest sporny.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rodzajow_zasobu` | 1 | szt |
| `zasobow_spornych` | 0 | szt |
| `zapasowych_maszyn` | 0 | szt |
| `zalogi_rezerwowej` | 0 | osob |
| `partnerow_w_porcie_docelowym` | 1 | szt |

## Co ten node ustalil

- brak zapasowej maszyny w BZG -- SWAP odpada

## Szczegoly

- **zasoby**
  - **PARTNER_SEATS@WAW**
    - **ilosc:** 1
    - **sporny:** 0
- **partnerzy**
  - **LO**
    - **nazwa:** LOT Polish Airlines
    - **poziom:** 0
    - **rodzaj:** own
    - **mnoznik_kosztu:** 1.00
- **bazy_maszyn_zapasowych**
  - WAW
  - KRK

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `zaloga rezerwowa` | derived | 0.40 | oszacowana z obsady bazy; zrodla nie podaja grafiku standby |
| `miejsca u partnera` | derived | 0.40 | obecnosc partnera w porcie, nie potwierdzona dostepnosc miejsc |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
