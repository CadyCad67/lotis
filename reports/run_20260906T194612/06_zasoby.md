# [06] REZERWACJA ZASOBU

**Status:** ok · **run:** `20260906T194612` · **snapshot:** `sha256:6c790f69f87c3591` · **0.11 ms**

W WAW do dyspozycji 3 rodzajow zasobu. Sporne: SLOT.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rodzajow_zasobu` | 3 | szt |
| `zasobow_spornych` | 1 | szt |
| `zapasowych_maszyn` | 15 | szt |
| `zalogi_rezerwowej` | 20 | osob |
| `partnerow_w_porcie_docelowym` | 0 | szt |

## Co ten node ustalil

- SLOT w WAW jest sporny (1 szt) -- dwie opcje nie moga po niego siegnac naraz
- WAW jest portem koordynowanym (poziom 3) -- kazda zmiana godziny wymaga nowego slotu

## Szczegoly

- **zasoby**
  - **SPARE_AIRCRAFT@WAW**
    - **ilosc:** 15
    - **sporny:** 0
  - **RESERVE_CREW@WAW**
    - **ilosc:** 20
    - **sporny:** 0
  - **SLOT@WAW**
    - **ilosc:** 1
    - **sporny:** 1
- **partnerzy:** -
- **bazy_maszyn_zapasowych**
  - WAW
  - KRK

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `zaloga rezerwowa` | derived | 0.40 | oszacowana z obsady bazy; zrodla nie podaja grafiku standby |
| `miejsca u partnera` | derived | 0.40 | obecnosc partnera w porcie, nie potwierdzona dostepnosc miejsc |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
