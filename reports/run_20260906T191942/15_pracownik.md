# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **0.06 ms**

OCC-DUTY: ACCEPT dla `OVERNIGHT` (1497475.90 PLN). Wymagana rola: Director Network Operations, drugi podpis.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | OVERNIGHT | - |
| `rekomendacja_silnika` | OVERNIGHT | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 2311321.49 PLN | PLN |
| `rola_autoryzujaca` | Director Network Operations | - |
| `drugi_podpis` | 1 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 2311321.49 PLN miesci sie w pasmie roli `Director Network Operations` i wymaga drugiego podpisu

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
    - LO6: rejs odwolany
    - 242 pasazerow na wlasny rejs -- oczekiwanie 840 min
    - 242 pasazerow z noclegiem na koszt przewoznika (Art. 9)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX009416:** wlasny rejs
    - **PAX009425:** wlasny rejs
    - **PAX009431:** wlasny rejs
    - **PAX009443:** wlasny rejs
    - **PAX009460:** wlasny rejs
    - **PAX009480:** wlasny rejs
    - **PAX009490:** wlasny rejs
    - **PAX009499:** wlasny rejs
    - **PAX009505:** wlasny rejs
    - **PAX009521:** wlasny rejs
    - **PAX009526:** wlasny rejs
    - **PAX009854:** wlasny rejs
    - **PAX009865:** wlasny rejs
    - **PAX009868:** wlasny rejs
    - **PAX009875:** wlasny rejs
    - **PAX009885:** wlasny rejs
    - **PAX009886:** wlasny rejs
    - **PAX009888:** wlasny rejs
    - **PAX009930:** wlasny rejs
    - **PAX009931:** wlasny rejs
  - **crew_actions**
    - nocleg zalogi poza baza
  - **valid_until:** 2026-08-21T12:10:00+00:00
  - **cost_low**
    - **minor:** 139 167 598
    - **currency:** PLN
    - **major:** 1391675.98
  - **cost_expected**
    - **minor:** 149 747 590
    - **currency:** PLN
    - **major:** 1497475.90
  - **cost_high**
    - **minor:** 231 132 149
    - **currency:** PLN
    - **major:** 2311321.49
  - **threshold_note:** `OVERNIGHT` jest najlepsza do okolo +30 min dodatkowego opoznienia; powyzej przejmuje `SWAP-SP-LSC`
  - **authorization_role:** Director Network Operations
  - **second_signature:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
