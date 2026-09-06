# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **0.05 ms**

OCC-DUTY: ACCEPT dla `HOLD` (22108.70 PLN). Wymagana rola: Dyzurny OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | HOLD | - |
| `rekomendacja_silnika` | HOLD | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 29127.33 PLN | PLN |
| `rola_autoryzujaca` | Dyzurny OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 29127.33 PLN miesci sie w pasmie roli `Dyzurny OCC`

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
  - **rola:** Dyzurny OCC
  - **drugi_podpis:** 0
- **karta_wykonania**
  - **option_id:** HOLD
  - **label:** Wstrzymaj odlot o 30 min
  - **what_changes**
    - LO21: odlot pozniej o 30 min (z 11:20 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO21 pozostaje na sluzbie +30 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-26T11:20:00+00:00
  - **cost_low**
    - **minor:** 2 092 431
    - **currency:** PLN
    - **major:** 20924.31
  - **cost_expected**
    - **minor:** 2 210 870
    - **currency:** PLN
    - **major:** 22108.70
  - **cost_high**
    - **minor:** 2 912 733
    - **currency:** PLN
    - **major:** 29127.33
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Dyzurny OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
