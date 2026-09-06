# [15] PRACOWNIK

**Status:** ok · **run:** `20260906T130726` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **0.06 ms**

OCC-DUTY: ACCEPT dla `SWAP-SP-LDH` (60783.55 PLN). Wymagana rola: Supervisor OCC.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | SWAP-SP-LDH | - |
| `rekomendacja_silnika` | SWAP-SP-LDH | - |
| `odstepstwo_od_rekomendacji` | 0 | - |
| `kwota_do_autoryzacji` | 78005.55 PLN | PLN |
| `rola_autoryzujaca` | Supervisor OCC | - |
| `drugi_podpis` | 0 | - |
| `kod_przyczyny` | - | - |

## Co ten node ustalil

- kwota 78005.55 PLN miesci sie w pasmie roli `Supervisor OCC`

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
  - **opcja:** SWAP-SP-LDH
  - **kod_przyczyny:** 
  - **rola:** Supervisor OCC
  - **drugi_podpis:** 0
- **karta_wykonania**
  - **option_id:** SWAP-SP-LDH
  - **label:** Podmien maszyne na SP-LDH (E170)
  - **what_changes**
    - podmiana maszyny miedzy LO417 i LO509
    - LO417: odlot pozniej o 36 min (z 07:20 UTC)
    - LO509: odlot pozniej o 180 min (z 11:05 UTC)
    - LO417: typ E75S -> E170
    - LO509: typ E170 -> E75S
  - **pax_offloaded:** 0
  - **pax_order:** -
  - **rebooked_to:** {}
  - **crew_actions**
    - zaloga rejsu LO417 pozostaje na sluzbie +36 min -- sprawdzic FDP przed odlotem
    - wezwanie zalogi z rezerwy dla rejsu przejmujacego maszyne
  - **valid_until:** 2026-08-25T07:20:00+00:00
  - **cost_low**
    - **minor:** 5 698 458
    - **currency:** PLN
    - **major:** 56984.58
  - **cost_expected**
    - **minor:** 6 078 355
    - **currency:** PLN
    - **major:** 60783.55
  - **cost_high**
    - **minor:** 7 800 555
    - **currency:** PLN
    - **major:** 78005.55
  - **threshold_note:** `SWAP-SP-LDH` pozostaje najlepsza w calym badanym zakresie do +120 min
  - **authorization_role:** Supervisor OCC
  - **second_signature:** 0

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
