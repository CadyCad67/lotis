# [06] REZERWACJA ZASOBU

**Status:** ok · **run:** `20260906T130726` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **0.11 ms**

W WAW do dyspozycji 4 rodzajow zasobu. Sporne: SLOT.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rodzajow_zasobu` | 4 | szt |
| `zasobow_spornych` | 1 | szt |
| `zapasowych_maszyn` | 19 | szt |
| `zalogi_rezerwowej` | 19 | osob |
| `partnerow_w_porcie_docelowym` | 1 | szt |

## Co ten node ustalil

- SLOT w WAW jest sporny (1 szt) -- dwie opcje nie moga po niego siegnac naraz
- WAW jest portem koordynowanym (poziom 3) -- kazda zmiana godziny wymaga nowego slotu

## Szczegoly

- **zasoby**
  - **SPARE_AIRCRAFT@WAW**
    - **ilosc:** 19
    - **sporny:** 0
  - **RESERVE_CREW@WAW**
    - **ilosc:** 19
    - **sporny:** 0
  - **PARTNER_SEATS@GVA**
    - **ilosc:** 1
    - **sporny:** 0
  - **SLOT@WAW**
    - **ilosc:** 1
    - **sporny:** 1
- **partnerzy**
  - **LX**
    - **nazwa:** SWISS
    - **poziom:** 1
    - **rodzaj:** codeshare
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
