# [15] PRACOWNIK

**Status:** ok · **run:** `20260905T181101` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **0.05 ms**

OCC-DUTY: ACCEPT dla `REBOOK-OWN` (88103.99 PLN). Wymagana rola: Supervisor OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | REBOOK-OWN | - |
| `rekomendacja_silnika` | REBOOK-OWN | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 113800.99 PLN | PLN |
| `rola_autoryzujaca` | Supervisor OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 113800.99 PLN miesci sie w pasmie roli `Supervisor OCC`

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
  - **label:** Przenies na wlasny rejs LO3852 (+190 min)
  - **what_changes**
    - LO3850: rejs odwolany
    - 55 pasazerow na wlasny rejs (LO3852, odlot 08:45 UTC) -- oczekiwanie 190 min
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX003129:** wlasny rejs
    - **PAX003130:** wlasny rejs
    - **PAX003131:** wlasny rejs
    - **PAX003132:** wlasny rejs
    - **PAX003133:** wlasny rejs
    - **PAX003134:** wlasny rejs
    - **PAX003135:** wlasny rejs
    - **PAX003136:** wlasny rejs
    - **PAX003137:** wlasny rejs
    - **PAX003138:** wlasny rejs
    - **PAX003139:** wlasny rejs
    - **PAX003140:** wlasny rejs
    - **PAX003141:** wlasny rejs
    - **PAX003142:** wlasny rejs
    - **PAX003143:** wlasny rejs
    - **PAX003144:** wlasny rejs
    - **PAX003145:** wlasny rejs
    - **PAX003146:** wlasny rejs
    - **PAX003147:** wlasny rejs
    - **PAX003148:** wlasny rejs
  - **crew_actions**
    - bez zmian dla zalogi
  - **valid_until:** 2026-08-25T05:35:00+00:00
  - **cost_low**
    - **minor:** 8 259 749
    - **currency:** PLN
    - **major:** 82597.49
  - **cost_expected**
    - **minor:** 8 810 399
    - **currency:** PLN
    - **major:** 88103.99
  - **cost_high**
    - **minor:** 11 380 099
    - **currency:** PLN
    - **major:** 113800.99
  - **threshold_note:** `REBOOK-OWN` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Supervisor OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
