# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T191017` · **snapshot:** `sha256:f3c290f4e6930407` · **0.06 ms**

OCC-DUTY: ACCEPT dla `HOLD` (805722.60 PLN). Wymagana rola: Director Network Operations, drugi podpis.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | HOLD | - |
| `rekomendacja_silnika` | HOLD | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 1402554.15 PLN | PLN |
| `rola_autoryzujaca` | Director Network Operations | - |
| `drugi_podpis` | 1 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 1402554.15 PLN miesci sie w pasmie roli `Director Network Operations` i wymaga drugiego podpisu

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
  - **rola:** Director Network Operations
  - **drugi_podpis:** 1
- **karta_wykonania**
  - **option_id:** HOLD
  - **label:** Wstrzymaj odlot o 180 min
  - **what_changes**
    - LO2098: odlot pozniej o 180 min (z 00:10 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO2098 pozostaje na sluzbie +180 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-21T00:10:00+00:00
  - **cost_low**
    - **minor:** 73 484 886
    - **currency:** PLN
    - **major:** 734848.86
  - **cost_expected**
    - **minor:** 80 572 260
    - **currency:** PLN
    - **major:** 805722.60
  - **cost_high**
    - **minor:** 140 255 415
    - **currency:** PLN
    - **major:** 1402554.15
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Director Network Operations
  - **second_signature:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
