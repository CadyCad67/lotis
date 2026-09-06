# [15] PRACOWNIK

**Status:** ok · **run:** `20260905T214214` · **snapshot:** `sha256:f3c290f4e6930407` · **0.05 ms**

OCC-DUTY: ACCEPT dla `REBOOK-OWN` (87716.13 PLN). Wymagana rola: Supervisor OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | REBOOK-OWN | - |
| `rekomendacja_silnika` | REBOOK-OWN | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 105990.32 PLN | PLN |
| `rola_autoryzujaca` | Supervisor OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 105990.32 PLN miesci sie w pasmie roli `Supervisor OCC`

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
  - **opcja:** REBOOK-OWN
  - **kod_przyczyny:** 
  - **rola:** Supervisor OCC
  - **drugi_podpis:** 0
- **karta_wykonania**
  - **option_id:** REBOOK-OWN
  - **label:** Przenies na wlasny rejs LO3994 (+560 min)
  - **what_changes**
    - LO3996: rejs odwolany
    - 61 pasazerow na wlasny rejs (LO3994, odlot 14:55 UTC) -- oczekiwanie 560 min
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX003776:** wlasny rejs
    - **PAX003777:** wlasny rejs
    - **PAX003778:** wlasny rejs
    - **PAX003779:** wlasny rejs
    - **PAX003780:** wlasny rejs
    - **PAX003781:** wlasny rejs
    - **PAX003782:** wlasny rejs
    - **PAX003783:** wlasny rejs
    - **PAX003784:** wlasny rejs
    - **PAX003785:** wlasny rejs
    - **PAX003786:** wlasny rejs
    - **PAX003787:** wlasny rejs
    - **PAX003788:** wlasny rejs
    - **PAX003789:** wlasny rejs
    - **PAX003790:** wlasny rejs
    - **PAX003791:** wlasny rejs
    - **PAX003792:** wlasny rejs
    - **PAX003793:** wlasny rejs
    - **PAX003794:** wlasny rejs
    - **PAX003795:** wlasny rejs
  - **crew_actions**
    - bez zmian dla zalogi
  - **valid_until:** 2026-08-21T05:35:00+00:00
  - **cost_low**
    - **minor:** 7 949 274
    - **currency:** PLN
    - **major:** 79492.74
  - **cost_expected**
    - **minor:** 8 771 613
    - **currency:** PLN
    - **major:** 87716.13
  - **cost_high**
    - **minor:** 10 599 032
    - **currency:** PLN
    - **major:** 105990.32
  - **threshold_note:** `REBOOK-OWN` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Supervisor OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
