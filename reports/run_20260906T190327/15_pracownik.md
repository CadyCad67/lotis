# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T190327` · **snapshot:** `sha256:f3c290f4e6930407` · **0.06 ms**

OCC-DUTY: ACCEPT dla `OVERNIGHT` (157321.96 PLN). Wymagana rola: Duty Manager OCC, drugi podpis.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | OVERNIGHT | - |
| `rekomendacja_silnika` | OVERNIGHT | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 176050.76 PLN | PLN |
| `rola_autoryzujaca` | Duty Manager OCC | - |
| `drugi_podpis` | 1 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 176050.76 PLN miesci sie w pasmie roli `Duty Manager OCC` i wymaga drugiego podpisu

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
  - **rola:** Duty Manager OCC
  - **drugi_podpis:** 1
- **karta_wykonania**
  - **option_id:** OVERNIGHT
  - **label:** Nocleg i rejs nastepnego dnia
  - **what_changes**
    - LO3981: rejs odwolany
    - 82 pasazerow na wlasny rejs -- oczekiwanie 840 min
    - 82 pasazerow z noclegiem na koszt przewoznika (Art. 9)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to**
    - **PAX001266:** wlasny rejs
    - **PAX001293:** wlasny rejs
    - **PAX001320:** wlasny rejs
    - **PAX001328:** wlasny rejs
    - **PAX001373:** wlasny rejs
    - **PAX001379:** wlasny rejs
    - **PAX001387:** wlasny rejs
    - **PAX002053:** wlasny rejs
    - **PAX002084:** wlasny rejs
    - **PAX002086:** wlasny rejs
    - **PAX002089:** wlasny rejs
    - **PAX002097:** wlasny rejs
    - **PAX002105:** wlasny rejs
    - **PAX002130:** wlasny rejs
    - **PAX002136:** wlasny rejs
    - **PAX002137:** wlasny rejs
    - **PAX002156:** wlasny rejs
    - **PAX002163:** wlasny rejs
    - **PAX002169:** wlasny rejs
    - **PAX002171:** wlasny rejs
  - **crew_actions**
    - nocleg zalogi poza baza
  - **valid_until:** 2026-08-21T07:05:00+00:00
  - **cost_low**
    - **minor:** 14 046 604
    - **currency:** PLN
    - **major:** 140466.04
  - **cost_expected**
    - **minor:** 15 732 196
    - **currency:** PLN
    - **major:** 157321.96
  - **cost_high**
    - **minor:** 17 605 076
    - **currency:** PLN
    - **major:** 176050.76
  - **threshold_note:** `OVERNIGHT` jest najlepsza do okolo +30 min dodatkowego opoznienia; powyzej przejmuje `SWAP-SP-LIO`
  - **authorization_role:** Duty Manager OCC
  - **second_signature:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
