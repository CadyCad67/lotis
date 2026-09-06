# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **0.05 ms**

OCC-DUTY: ACCEPT dla `OVERNIGHT` (1213890.06 PLN). Wymagana rola: Director Network Operations, drugi podpis.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | OVERNIGHT | - |
| `rekomendacja_silnika` | OVERNIGHT | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 2452303.15 PLN | PLN |
| `rola_autoryzujaca` | Director Network Operations | - |
| `drugi_podpis` | 1 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 2452303.15 PLN miesci sie w pasmie roli `Director Network Operations` i wymaga drugiego podpisu

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
  - **opcja:** OVERNIGHT
  - **kod_przyczyny:** 
  - **rola:** Director Network Operations
  - **drugi_podpis:** 1
- **karta_wykonania**
  - **option_id:** OVERNIGHT
  - **label:** Nocleg i rejs nastepnego dnia
  - **what_changes**
    - LO82: rejs odwolany
    - 227 pasazerow na wlasny rejs -- oczekiwanie 840 min
    - 227 pasazerow z noclegiem na koszt przewoznika (Art. 9)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX000236:** wlasny rejs
    - **PAX000237:** wlasny rejs
    - **PAX000238:** wlasny rejs
    - **PAX000239:** wlasny rejs
    - **PAX000240:** wlasny rejs
    - **PAX000241:** wlasny rejs
    - **PAX000242:** wlasny rejs
    - **PAX000243:** wlasny rejs
    - **PAX000244:** wlasny rejs
    - **PAX000245:** wlasny rejs
    - **PAX000246:** wlasny rejs
    - **PAX000247:** wlasny rejs
    - **PAX000248:** wlasny rejs
    - **PAX000249:** wlasny rejs
    - **PAX000250:** wlasny rejs
    - **PAX000251:** wlasny rejs
    - **PAX000252:** wlasny rejs
    - **PAX000253:** wlasny rejs
    - **PAX000254:** wlasny rejs
    - **PAX000255:** wlasny rejs
  - **crew_actions**
    - nocleg zalogi poza baza
  - **valid_until:** 2026-08-24T01:15:00+00:00
  - **cost_low**
    - **minor:** 114 032 097
    - **currency:** PLN
    - **major:** 1140320.97
  - **cost_expected**
    - **minor:** 121 389 006
    - **currency:** PLN
    - **major:** 1213890.06
  - **cost_high**
    - **minor:** 245 230 315
    - **currency:** PLN
    - **major:** 2452303.15
  - **threshold_note:** `OVERNIGHT` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Director Network Operations
  - **second_signature:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
