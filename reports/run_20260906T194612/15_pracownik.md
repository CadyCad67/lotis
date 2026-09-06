# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T194612` · **snapshot:** `sha256:6c790f69f87c3591` · **0.04 ms**

OCC-DUTY: ACCEPT dla `REBOOK-SPILL` (30198.38 PLN). Wymagana rola: Dyzurny OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | REBOOK-SPILL | - |
| `rekomendacja_silnika` | REBOOK-SPILL | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 41522.77 PLN | PLN |
| `rola_autoryzujaca` | Dyzurny OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 41522.77 PLN miesci sie w pasmie roli `Dyzurny OCC`

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
  - **rola:** Dyzurny OCC
  - **drugi_podpis:** 0
- **karta_wykonania**
  - **option_id:** REBOOK-SPILL
  - **label:** Przenies 3 nadmiarowych na LO393 (+480 min)
  - **what_changes**
    - LO395: odlot pozniej o 60 min (z 09:05 UTC)
    - 3 pasazerow na wlasny rejs (LO393, odlot 17:05 UTC) -- oczekiwanie 480 min
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX002023:** wlasny rejs
    - **PAX002029:** wlasny rejs
    - **PAX002036:** wlasny rejs
  - **crew_actions**
    - zaloga rejsu LO395 pozostaje na sluzbie +60 min -- sprawdzic FDP przed odlotem
  - **valid_until:** 2026-08-24T09:05:00+00:00
  - **cost_low**
    - **minor:** 2 705 272
    - **currency:** PLN
    - **major:** 27052.72
  - **cost_expected**
    - **minor:** 3 019 838
    - **currency:** PLN
    - **major:** 30198.38
  - **cost_high**
    - **minor:** 4 152 277
    - **currency:** PLN
    - **major:** 41522.77
  - **threshold_note:** `REBOOK-SPILL` jest najlepsza do okolo +60 min dodatkowego opoznienia; powyzej przejmuje `SWAP-SP-LII`
  - **authorization_role:** Dyzurny OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
