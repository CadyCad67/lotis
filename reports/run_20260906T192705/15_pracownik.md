# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T192705` · **snapshot:** `sha256:f3c290f4e6930407` · **0.06 ms**

OCC-DUTY: ACCEPT dla `SWAP-SP-LIO` (14158.46 PLN). Wymagana rola: Dyzurny OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | SWAP-SP-LIO | - |
| `rekomendacja_silnika` | SWAP-SP-LIO | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 15843.99 PLN | PLN |
| `rola_autoryzujaca` | Dyzurny OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 15843.99 PLN miesci sie w pasmie roli `Dyzurny OCC`

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
  - **opcja:** SWAP-SP-LIO
  - **kod_przyczyny:** 
  - **rola:** Dyzurny OCC
  - **drugi_podpis:** 0
- **karta_wykonania**
  - **option_id:** SWAP-SP-LIO
  - **label:** Podmien maszyne na SP-LIO (E75S)
  - **what_changes**
    - podmiana maszyny miedzy LO3981 i LO265
    - LO265: odlot pozniej o 20 min (z 07:25 UTC)
    - LO3981: odlot pozniej o 36 min (z 07:05 UTC)
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO3981 pozostaje na sluzbie +36 min -- sprawdzic FDP przed odlotem
    - wezwanie zalogi z rezerwy dla rejsu przejmujacego maszyne
  - **valid_until:** 2026-08-21T07:05:00+00:00
  - **cost_low**
    - **minor:** 1 264 149
    - **currency:** PLN
    - **major:** 12641.49
  - **cost_expected**
    - **minor:** 1 415 846
    - **currency:** PLN
    - **major:** 14158.46
  - **cost_high**
    - **minor:** 1 584 399
    - **currency:** PLN
    - **major:** 15843.99
  - **threshold_note:** `SWAP-SP-LIO` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Dyzurny OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
