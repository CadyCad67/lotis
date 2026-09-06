# [15b] WYKONANIE

**Status:** ok · **run:** `20260906T193212` · **snapshot:** `sha256:6c790f69f87c3591` · **0.12 ms**

Wykonano 3 krokow opcji `REBOOK-SPILL`. Wszystkie kroki odwracalne.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `krokow` | 3 | szt |
| `krokow_nieodwracalnych` | 0 | szt |
| `wykonawcow` | 3 | szt |
| `opcja` | REBOOK-SPILL | - |

## Co ten node ustalil

- wykonanie jest osobnym etapem miedzy decyzja a logiem -- bez niego node 17 nie odroznilby bledu modelu od nieudanej realizacji

## Szczegoly

- **kroki**
  - **przepisanie_wlasne**
    - **wykonawca:** System rezerwacyjny
    - **opis:** przepisanie pasazerow na wlasny rejs
    - **odwracalny:** 1
    - **krytyczny:** 0
    - **status:** wykonany
  - **powiadomienie_pax**
    - **wykonawca:** Komunikacja
    - **opis:** wyslanie SMS i e-mail do pasazerow
    - **odwracalny:** 1
    - **krytyczny:** 0
    - **status:** wykonany
  - **brief_zalogi**
    - **wykonawca:** Crew Control
    - **opis:** poinformowanie zalogi o zmianie
    - **odwracalny:** 1
    - **krytyczny:** 0
    - **status:** wykonany
- **punkt_bez_powrotu:** None
- **sciezka_porazki**
  - **wyzwalacz:** EXECUTION_FAILED
  - **wraca_do:** node 04 ZAKLOCENIE
  - **po_co:** blad wykonania nie moze byc liczony jako blad modelu (luka 3)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
