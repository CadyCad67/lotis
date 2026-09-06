# [15b] WYKONANIE

**Status:** ok · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **0.1 ms**

Wykonano 5 krokow opcji `OVERNIGHT`. 1 krokow nieodwracalnych.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `krokow` | 5 | szt |
| `krokow_nieodwracalnych` | 1 | szt |
| `wykonawcow` | 4 | szt |
| `opcja` | OVERNIGHT | - |

## Co ten node ustalil

- wykonanie jest osobnym etapem miedzy decyzja a logiem -- bez niego node 17 nie odroznilby bledu modelu od nieudanej realizacji
- krok `kasacja_w_systemie` jest nieodwracalny -- po nim przeliczenie nie przywroci stanu wyjsciowego

## Szczegoly

- **kroki**
  - **kasacja_w_systemie**
    - **wykonawca:** System rezerwacyjny
    - **opis:** odwolanie rejsu i zwolnienie miejsc
    - **odwracalny:** 0
    - **krytyczny:** 1
    - **status:** wykonany
  - **przepisanie_wlasne**
    - **wykonawca:** System rezerwacyjny
    - **opis:** przepisanie pasazerow na wlasny rejs
    - **odwracalny:** 1
    - **krytyczny:** 0
    - **status:** wykonany
  - **rezerwacja_hotelu**
    - **wykonawca:** Pax Care
    - **opis:** rezerwacja hoteli i transportu
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
- **punkt_bez_powrotu**
  - **krok:** kasacja_w_systemie
  - **opis:** odwolanie rejsu i zwolnienie miejsc
- **sciezka_porazki**
  - **wyzwalacz:** EXECUTION_FAILED
  - **wraca_do:** node 04 ZAKLOCENIE
  - **po_co:** blad wykonania nie moze byc liczony jako blad modelu (luka 3)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
