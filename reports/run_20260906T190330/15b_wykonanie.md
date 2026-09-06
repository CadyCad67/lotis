# [15b] WYKONANIE

**Status:** ok · **run:** `20260906T190330` · **snapshot:** `sha256:f3c290f4e6930407` · **0.06 ms**

Wykonano 5 krokow opcji `SWAP-SP-LIO`. 1 krokow nieodwracalnych.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `krokow` | 5 | szt |
| `krokow_nieodwracalnych` | 1 | szt |
| `wykonawcow` | 5 | szt |
| `opcja` | SWAP-SP-LIO | - |

## Co ten node ustalil

- wykonanie jest osobnym etapem miedzy decyzja a logiem -- bez niego node 17 nie odroznilby bledu modelu od nieudanej realizacji
- krok `nowy_slot` jest nieodwracalny -- po nim przeliczenie nie przywroci stanu wyjsciowego

## Szczegoly

- **kroki**
  - **przydzial_maszyny**
    - **wykonawca:** OCC / Maintenance Control
    - **opis:** przepiecie rejsow miedzy maszynami
    - **odwracalny:** 1
    - **krytyczny:** 0
    - **status:** wykonany
  - **obsluga_naziemna**
    - **wykonawca:** Handling
    - **opis:** przestawienie sprzetu i bagazu
    - **odwracalny:** 1
    - **krytyczny:** 0
    - **status:** wykonany
  - **nowy_slot**
    - **wykonawca:** Slot Coordination / EUROCONTROL
    - **opis:** wystapienie o nowe okno startowe
    - **odwracalny:** 0
    - **krytyczny:** 1
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
  - **krok:** nowy_slot
  - **opis:** wystapienie o nowe okno startowe
- **sciezka_porazki**
  - **wyzwalacz:** EXECUTION_FAILED
  - **wraca_do:** node 04 ZAKLOCENIE
  - **po_co:** blad wykonania nie moze byc liczony jako blad modelu (luka 3)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
