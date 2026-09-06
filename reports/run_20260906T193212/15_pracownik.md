# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T193212` · **snapshot:** `sha256:6c790f69f87c3591` · **0.06 ms**

OCC-DUTY: ACCEPT dla `REBOOK-SPILL` (38201.20 PLN). Wymagana rola: Supervisor OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | REBOOK-SPILL | - |
| `rekomendacja_silnika` | REBOOK-SPILL | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 58962.72 PLN | PLN |
| `rola_autoryzujaca` | Supervisor OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 58962.72 PLN miesci sie w pasmie roli `Supervisor OCC`

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
  - **opcja:** REBOOK-SPILL
  - **kod_przyczyny:** 
  - **rola:** Supervisor OCC
  - **drugi_podpis:** 0
- **karta_wykonania**
  - **option_id:** REBOOK-SPILL
  - **label:** Przenies 8 nadmiarowych na LO26 (+280 min)
  - **what_changes**
    - 8 pasazerow na wlasny rejs (LO26, odlot 16:50 UTC) -- oczekiwanie 280 min
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX010317:** wlasny rejs
    - **PAX010352:** wlasny rejs
    - **PAX010363:** wlasny rejs
    - **PAX010367:** wlasny rejs
    - **PAX010455:** wlasny rejs
    - **PAX010460:** wlasny rejs
    - **PAX010461:** wlasny rejs
    - **PAX010500:** wlasny rejs
  - **crew_actions**
    - bez zmian dla zalogi
  - **valid_until:** 2026-08-24T12:10:00+00:00
  - **cost_low**
    - **minor:** 3 550 221
    - **currency:** PLN
    - **major:** 35502.21
  - **cost_expected**
    - **minor:** 3 820 120
    - **currency:** PLN
    - **major:** 38201.20
  - **cost_high**
    - **minor:** 5 896 272
    - **currency:** PLN
    - **major:** 58962.72
  - **threshold_note:** `REBOOK-SPILL` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Supervisor OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
