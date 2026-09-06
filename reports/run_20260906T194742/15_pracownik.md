# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T194742` · **snapshot:** `sha256:6c790f69f87c3591` · **0.05 ms**

OCC-DUTY: ACCEPT dla `REBOOK-OWN` (135169.21 PLN). Wymagana rola: Duty Manager OCC, drugi podpis.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | REBOOK-OWN | - |
| `rekomendacja_silnika` | REBOOK-OWN | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 185857.66 PLN | PLN |
| `rola_autoryzujaca` | Duty Manager OCC | - |
| `drugi_podpis` | 1 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 185857.66 PLN miesci sie w pasmie roli `Duty Manager OCC` i wymaga drugiego podpisu

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
  - **rola:** Duty Manager OCC
  - **drugi_podpis:** 1
- **karta_wykonania**
  - **option_id:** REBOOK-OWN
  - **label:** Przenies na wlasny rejs LO393 (+480 min)
  - **what_changes**
    - LO395: rejs odwolany
    - 79 pasazerow na wlasny rejs (LO393, odlot 17:05 UTC) -- oczekiwanie 480 min
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX002023:** wlasny rejs
    - **PAX002029:** wlasny rejs
    - **PAX002036:** wlasny rejs
    - **PAX002058:** wlasny rejs
    - **PAX002089:** wlasny rejs
    - **PAX002101:** wlasny rejs
    - **PAX002113:** wlasny rejs
    - **PAX004499:** wlasny rejs
    - **PAX004540:** wlasny rejs
    - **PAX005143:** wlasny rejs
    - **PAX005145:** wlasny rejs
    - **PAX005166:** wlasny rejs
    - **PAX005173:** wlasny rejs
    - **PAX005568:** wlasny rejs
    - **PAX005579:** wlasny rejs
    - **PAX005582:** wlasny rejs
    - **PAX005588:** wlasny rejs
    - **PAX005590:** wlasny rejs
    - **PAX005609:** wlasny rejs
    - **PAX005617:** wlasny rejs
  - **crew_actions**
    - bez zmian dla zalogi
  - **valid_until:** 2026-08-24T09:05:00+00:00
  - **cost_low**
    - **minor:** 12 108 909
    - **currency:** PLN
    - **major:** 121089.09
  - **cost_expected**
    - **minor:** 13 516 921
    - **currency:** PLN
    - **major:** 135169.21
  - **cost_high**
    - **minor:** 18 585 766
    - **currency:** PLN
    - **major:** 185857.66
  - **threshold_note:** `REBOOK-OWN` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Duty Manager OCC
  - **second_signature:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
