# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T175204` · **snapshot:** `sha256:91cb2a4af61a3714` · **0.06 ms**

OCC-DUTY: ACCEPT dla `HOLD` (148598.00 PLN). Wymagana rola: Duty Manager OCC, drugi podpis.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | HOLD | - |
| `rekomendacja_silnika` | HOLD | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 229357.78 PLN | PLN |
| `rola_autoryzujaca` | Duty Manager OCC | - |
| `drugi_podpis` | 1 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 229357.78 PLN miesci sie w pasmie roli `Duty Manager OCC` i wymaga drugiego podpisu

## Szczegoly

- **pasma_autoryzacji**
  - **max_value:** 50 000.00
  - **role:** Dyzurny OCC
  - **second_signature:** 0
  - **max_value:** 150 000.00
  - **role:** Supervisor OCC
  - **second_signature:** 0
  - **max_value:** 400 000.00
  - **role:** Duty Manager OCC
  - **second_signature:** 1
  - **max_value:** None
  - **role:** Director Network Operations
  - **second_signature:** 1
- **dopuszczalne_kody_odrzucenia**
  - DANE_NIEAKTUALNE
  - CZYNNIK_NIEUJETY_W_MODELU
  - DECYZJA_HANDLOWA
  - RYZYKO_REPUTACYJNE
  - NIEWYKONALNE_OPERACYJNIE
- **decyzja**
  - **operator:** OCC-DUTY
  - **rodzaj:** ACCEPT
  - **opcja:** HOLD
  - **kod_przyczyny:** 
  - **rola:** Duty Manager OCC
  - **drugi_podpis:** 1
- **karta_wykonania**
  - **option_id:** HOLD
  - **label:** Wstrzymaj odlot o 120 min
  - **what_changes**
    - LO6: odlot pozniej o 120 min (z 12:10 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO6 pozostaje na sluzbie +120 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-22T12:10:00+00:00
  - **cost_low**
    - **minor:** 13 809 923
    - **currency:** PLN
    - **major:** 138099.23
  - **cost_expected**
    - **minor:** 14 859 800
    - **currency:** PLN
    - **major:** 148598.00
  - **cost_high**
    - **minor:** 22 935 778
    - **currency:** PLN
    - **major:** 229357.78
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Duty Manager OCC
  - **second_signature:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
