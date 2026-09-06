# [06] REZERWACJA ZASOBU

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **0.09 ms**

W NRT do dyspozycji 2 rodzajow zasobu. Sporne: SLOT.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rodzajow_zasobu` | 2 | szt |
| `zasobow_spornych` | 1 | szt |
| `zapasowych_maszyn` | 0 | szt |
| `zalogi_rezerwowej` | 0 | osob |
| `partnerow_w_porcie_docelowym` | 1 | szt |

## Co ten node ustalil

- SLOT w NRT jest sporny (1 szt) -- dwie opcje nie moga po niego siegnac naraz
- brak zapasowej maszyny w NRT -- SWAP odpada
- NRT jest portem koordynowanym (poziom 3) -- kazda zmiana godziny wymaga nowego slotu

## Szczegoly

- **zasoby**
  - **PARTNER_SEATS@WAW**
    - **ilosc:** 1
    - **sporny:** 0
  - **SLOT@NRT**
    - **ilosc:** 1
    - **sporny:** 1
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
