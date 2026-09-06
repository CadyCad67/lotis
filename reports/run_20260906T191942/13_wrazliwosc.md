# [13] WRAZLIWOSC

**Status:** ok · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **0.82 ms**

Ranking koncowy 4 dopuszczalnych opcji. Rekomendacja: `OVERNIGHT` (1497475.90 PLN), oszczednosc wobec opcji domyslnej `SWAP-SP-LRF`: -1318854.03 PLN.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `rekomendacja` | OVERNIGHT | - |
| `strata_rekomendacji` | 1497475.90 PLN | PLN |
| `widelki_min` | 1391675.98 PLN | PLN |
| `widelki_max` | 2311321.49 PLN | PLN |
| `opcja_domyslna` | SWAP-SP-LRF | - |
| `strata_opcji_domyslnej` | 178621.87 PLN | PLN |
| `oszczednosc` | -1318854.03 PLN | PLN |
| `prog_oplacalnosci` | 30 | min |
| `opcji_w_rankingu` | 4 | szt |

## Co ten node ustalil

- opcja domyslna to `SWAP-SP-LRF` -- oszczednosc liczy sie wzgledem niej, a nie wzgledem nicnierobienia
- `OVERNIGHT` jest najlepsza do okolo +30 min dodatkowego opoznienia; powyzej przejmuje `SWAP-SP-LSC`
- waga polityki firmy przesuwa ranking, ale nie zmienia zadnej kwoty w raporcie

## Szczegoly

- **ranking_koncowy**
  - **OVERNIGHT**
    - **pozycja:** 1
    - **strata**
      - **minor:** 149 747 590
      - **currency:** PLN
      - **major:** 1497475.90
    - **min**
      - **minor:** 139 167 598
      - **currency:** PLN
      - **major:** 1391675.98
    - **max**
      - **minor:** 231 132 149
      - **currency:** PLN
      - **major:** 2311321.49
    - **oszczednosc**
      - **minor:** -131 885 403
      - **currency:** PLN
      - **major:** -1318854.03
    - **wskaznik:** 6 791 092.27
    - **uwaga_polityki:** 99 utraconych przesiadek; szerokie widelki; priorytet 0, indeks pasazerski 18.00
  - **CANCEL**
    - **pozycja:** 2
    - **strata**
      - **minor:** 169 292 421
      - **currency:** PLN
      - **major:** 1692924.21
    - **min**
      - **minor:** 157 331 544
      - **currency:** PLN
      - **major:** 1573315.44
    - **max**
      - **minor:** 261 299 171
      - **currency:** PLN
      - **major:** 2612991.71
    - **oszczednosc**
      - **minor:** -151 430 234
      - **currency:** PLN
      - **major:** -1514302.34
    - **wskaznik:** 7 677 455.45
    - **uwaga_polityki:** 99 utraconych przesiadek; szerokie widelki; priorytet 0, indeks pasazerski 24.00
  - **SWAP-SP-LSC**
    - **pozycja:** 3
    - **strata**
      - **minor:** 16 186 462
      - **currency:** PLN
      - **major:** 161864.62
    - **min**
      - **minor:** 15 042 854
      - **currency:** PLN
      - **major:** 150428.54
    - **max**
      - **minor:** 24 983 452
      - **currency:** PLN
      - **major:** 249834.52
    - **oszczednosc**
      - **minor:** 1 675 725
      - **currency:** PLN
      - **major:** 16757.25
    - **wskaznik:** 13 021 576.75
    - **uwaga_polityki:** propagacja 136 min (waga rotacji 1.0); 99 utraconych przesiadek; szerokie widelki; priorytet 0, indeks pasazerski 2.27
  - **SWAP-SP-LRF**
    - **pozycja:** 4
    - **strata**
      - **minor:** 17 862 187
      - **currency:** PLN
      - **major:** 178621.87
    - **min**
      - **minor:** 16 600 185
      - **currency:** PLN
      - **major:** 166001.85
    - **max**
      - **minor:** 27 569 897
      - **currency:** PLN
      - **major:** 275698.97
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **wskaznik:** 14 369 652.80
    - **uwaga_polityki:** propagacja 136 min (waga rotacji 1.0); 99 utraconych przesiadek; szerokie widelki; priorytet 0, indeks pasazerski 2.27
- **test_wrazliwosci**
  - **krok_min:** 30
  - **lider:** SWAP-SP-LSC
  - **ranking**
    - **SWAP-SP-LSC**
      - **strata**
        - **minor:** 16 222 462
        - **currency:** PLN
        - **major:** 162224.62
    - **SWAP-SP-LRF**
      - **strata**
        - **minor:** 17 898 187
        - **currency:** PLN
        - **major:** 178981.87
    - **OVERNIGHT**
      - **strata**
        - **minor:** 149 747 590
        - **currency:** PLN
        - **major:** 1497475.90
    - **CANCEL**
      - **strata**
        - **minor:** 169 292 421
        - **currency:** PLN
        - **major:** 1692924.21
  - **krok_min:** 60
  - **lider:** SWAP-SP-LSC
  - **ranking**
    - **SWAP-SP-LSC**
      - **strata**
        - **minor:** 16 258 462
        - **currency:** PLN
        - **major:** 162584.62
    - **SWAP-SP-LRF**
      - **strata**
        - **minor:** 17 934 187
        - **currency:** PLN
        - **major:** 179341.87
    - **OVERNIGHT**
      - **strata**
        - **minor:** 149 747 590
        - **currency:** PLN
        - **major:** 1497475.90
    - **CANCEL**
      - **strata**
        - **minor:** 169 292 421
        - **currency:** PLN
        - **major:** 1692924.21
  - **krok_min:** 120
  - **lider:** SWAP-SP-LSC
  - **ranking**
    - **SWAP-SP-LSC**
      - **strata**
        - **minor:** 16 330 462
        - **currency:** PLN
        - **major:** 163304.62
    - **SWAP-SP-LRF**
      - **strata**
        - **minor:** 18 006 187
        - **currency:** PLN
        - **major:** 180061.87
    - **OVERNIGHT**
      - **strata**
        - **minor:** 149 747 590
        - **currency:** PLN
        - **major:** 1497475.90
    - **CANCEL**
      - **strata**
        - **minor:** 169 292 421
        - **currency:** PLN
        - **major:** 1692924.21
- **prog_oplacalnosci**
  - **do_minut:** 30
  - **przejmuje:** SWAP-SP-LSC
  - **opis:** `OVERNIGHT` jest najlepsza do okolo +30 min dodatkowego opoznienia; powyzej przejmuje `SWAP-SP-LSC`
- **wagi_polityki**
  - **rot:** 1.00
  - **trf:** 1.00
  - **vuln:** 1.00
  - **unc:** 1.00
  - **cx:** 1.00
  - **crew:** 1.00
- **opcje_odrzucone_przez_prawo**
  - **HOLD**
    - **reguly**
      - Art. 8 EU261
      - Art. 4 EU261
  - **REBOOK-OAL**
    - **reguly**
      - Art. 9 EU261
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

## Zalozenia

| pole | zrodlo | pewnosc | uwaga |
| --- | --- | --- | --- |
| `prog oplacalnosci` | derived | 0.70 | policzony na siatce +30/+60/+120 min, nie w sposob ciagly |

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
