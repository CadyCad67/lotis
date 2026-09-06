# [15] PRACOWNIK

**Status:** ok · **run:** `20260905T175614` · **snapshot:** `sha256:f3c290f4e6930407` · **0.06 ms**

OCC-DUTY: ACCEPT dla `HOLD` (33753.66 PLN). Wymagana rola: Dyzurny OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | HOLD | - |
| `rekomendacja_silnika` | HOLD | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 40785.67 PLN | PLN |
| `rola_autoryzujaca` | Dyzurny OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 40785.67 PLN miesci sie w pasmie roli `Dyzurny OCC`

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
  - **label:** Wstrzymaj odlot o 90 min
  - **what_changes**
    - LO3996: odlot pozniej o 90 min (z 05:35 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO3996 pozostaje na sluzbie +90 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-21T05:35:00+00:00
  - **cost_low**
    - **minor:** 3 058 925
    - **currency:** PLN
    - **major:** 30589.25
  - **cost_expected**
    - **minor:** 3 375 366
    - **currency:** PLN
    - **major:** 33753.66
  - **cost_high**
    - **minor:** 4 078 567
    - **currency:** PLN
    - **major:** 40785.67
  - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Dyzurny OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
