# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T193758` · **snapshot:** `sha256:6c790f69f87c3591` · **0.07 ms**

OCC-DUTY: ACCEPT dla `HOLD` (43034.90 PLN). Wymagana rola: Supervisor OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | HOLD | - |
| `rekomendacja_silnika` | HOLD | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 66423.43 PLN | PLN |
| `rola_autoryzujaca` | Supervisor OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 66423.43 PLN miesci sie w pasmie roli `Supervisor OCC`

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
  - **rola:** Supervisor OCC
  - **drugi_podpis:** 0
- **karta_wykonania**
  - **option_id:** HOLD
  - **label:** Wstrzymaj odlot o 30 min
  - **what_changes**
    - LO6: odlot pozniej o 30 min (z 12:10 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO6 pozostaje na sluzbie +30 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-24T12:10:00+00:00
  - **cost_low**
    - **minor:** 3 999 440
    - **currency:** PLN
    - **major:** 39994.40
  - **cost_expected**
    - **minor:** 4 303 490
    - **currency:** PLN
    - **major:** 43034.90
  - **cost_high**
    - **minor:** 6 642 343
    - **currency:** PLN
    - **major:** 66423.43
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Supervisor OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
