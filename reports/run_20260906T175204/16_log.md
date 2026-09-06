# [16] LOG

**Status:** ok · **run:** `20260906T175204` · **snapshot:** `sha256:91cb2a4af61a3714` · **4.34 ms**

Zapisano 6 rozwazonych opcji, w tym 1 odrzuconych przez filtr prawny wraz z podstawa kazdego odrzucenia.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_w_logu` | 6 | szt |
| `opcji_odrzuconych` | 1 | szt |
| `odcisk_wpisu` | sha256:754645bbe82937d410c0d54f | - |
| `wersja_silnika` | 1.0.0 | - |
| `wersja_bazy` | 5.0 | - |
| `nadpisania` | brak | - |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | HOLD | - |

## Co ten node ustalil

- log zapisuje podstawe odrzucenia kazdej opcji -- w sporze liczy sie to, czego nie wybrano i dlaczego
- wersja bazy `5.0` jest jednoczesnie wersja modelu kosztowego i prawa -- oba pochodza z tego samego pliku

## Szczegoly

- **wpis**
  - **schema:** lotis.audit/v1
  - **run_id:** 20260906T175204
  - **snapshot:** sha256:91cb2a4af61a3714f4c72ed8bbad9666
  - **czas_runu:** 2026-09-06T17:52:04.144906+00:00
  - **zaklocenie**
    - **id:** DSR-LO6-2026-08-22-0
    - **rejs:** LO6-2026-08-22
    - **typ:** TECHNICAL
    - **opoznienie_min:** 120
    - **termin_decyzji:** 2026-08-22T12:10:00+00:00
    - **iteracja:** 0
    - **wyzwalacz:** INITIAL
  - **opcje_rozwazone**
    - **HOLD**
      - **tryb:** MODIFYING
      - **generator:** SZ.HOLD
      - **strata**
        - **minor:** 14 859 800
        - **currency:** PLN
        - **major:** 148598.00
      - **widelki**
        - **min**
          - **minor:** 13 809 923
          - **currency:** PLN
          - **major:** 138099.23
        - **max**
          - **minor:** 22 935 778
          - **currency:** PLN
          - **major:** 229357.78
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 1
    - **SWAP-SP-LSB**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.SWAP
      - **strata**
        - **minor:** 23 568 922
        - **currency:** PLN
        - **major:** 235689.22
      - **widelki**
        - **min**
          - **minor:** 21 903 727
          - **currency:** PLN
          - **major:** 219037.27
        - **max**
          - **minor:** 36 378 118
          - **currency:** PLN
          - **major:** 363781.18
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 2
    - **SWAP-SP-LSG**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.SWAP
      - **strata**
        - **minor:** 24 451 732
        - **currency:** PLN
        - **major:** 244517.32
      - **widelki**
        - **min**
          - **minor:** 22 724 164
          - **currency:** PLN
          - **major:** 227241.64
        - **max**
          - **minor:** 37 740 716
          - **currency:** PLN
          - **major:** 377407.16
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 3
    - **REBOOK-OAL**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.REBOOK-OAL
      - **strata**
        - **minor:** 183 887 092
        - **currency:** PLN
        - **major:** 1838870.92
      - **widelki**
        - **min**
          - **minor:** 170 895 070
          - **currency:** PLN
          - **major:** 1708950.70
        - **max**
          - **minor:** 283 825 728
          - **currency:** PLN
          - **major:** 2838257.28
      - **dopuszczalna:** 0
      - **powod_odrzucenia**
        - **podstawa:** Art. 9 EU261
        - **powod:** oczekiwanie 925 min bez zapewnionego noclegu (prog opieki 240 min)
      - **pozycja_koncowa:** None
    - **OVERNIGHT**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.OVERNIGHT
      - **strata**
        - **minor:** 149 296 488
        - **currency:** PLN
        - **major:** 1492964.88
      - **widelki**
        - **min**
          - **minor:** 138 748 367
          - **currency:** PLN
          - **major:** 1387483.67
        - **max**
          - **minor:** 230 435 883
          - **currency:** PLN
          - **major:** 2304358.83
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 4
    - **CANCEL**
      - **tryb:** MODIFYING
      - **generator:** SZ.CANCEL
      - **strata**
        - **minor:** 178 598 859
        - **currency:** PLN
        - **major:** 1785988.59
      - **widelki**
        - **min**
          - **minor:** 165 980 462
          - **currency:** PLN
          - **major:** 1659804.62
        - **max**
          - **minor:** 275 663 456
          - **currency:** PLN
          - **major:** 2756634.56
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 5
  - **rekomendacja**
    - **id:** HOLD
    - **strata**
      - **minor:** 14 859 800
      - **currency:** PLN
      - **major:** 148598.00
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
  - **decyzja_czlowieka**
    - **rodzaj:** ACCEPT
    - **opcja:** HOLD
    - **operator:** OCC-DUTY
    - **kod_przyczyny:** 
    - **rola:** Duty Manager OCC
    - **drugi_podpis:** 1
    - **odstepstwo:** 0
  - **wykonanie:** None
  - **karta_wykonania**
    - **option_id:** HOLD
    - **label:** Wstrzymaj odlot o 120 min
    - **what_changes**
      - LO6: odlot pozniej o 120 min (z 12:10 UTC)
    - **pax_offloaded:** 0
    - **pax_order:** -
    - **rebooked_to:** {}
    - **crew_actions**
      - zaloga rejsu LO6 pozostaje na sluzbie +120 min -- sprawdzic FDP przed odlotem
    - **valid_until:** 2026-08-22T12:10:00+00:00
    - **cost_low**
      - **minor:** 13 809 923
      - **currency:** PLN
      - **major:** 138099.23
    - **cost_expected**
      - **minor:** 14 859 800
      - **currency:** PLN
      - **major:** 148598.00
    - **cost_high**
      - **minor:** 22 935 778
      - **currency:** PLN
      - **major:** 229357.78
    - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
    - **authorization_role:** Duty Manager OCC
    - **second_signature:** 1
  - **wersje**
    - **engine:** 1.0.0
    - **data:** 5.0
    - **data_generated:** 2026-08-28
    - **authorization:** 2026.07
    - **escalation:** 2026.07
    - **sop:** 2026.03
    - **overrides:** brak
  - **nadpisania_uzyte:** {}
  - **budzet**
    - **total_ms:** 20 000.00
    - **elapsed_ms:** 2 476.10
    - **remaining_ms:** 17 523.90
    - **level:** FULL
    - **level_label:** pelny
    - **per_node_ms**
      - **01:** 1 738.30
      - **02:** 12.10
      - **03:** 552.20
      - **04:** 6.30
      - **05:** 10.20
      - **06:** 0.10
      - **07:** 16.70
      - **08:** 4.00
      - **09:** 17.20
      - **10:** 40.80
      - **11:** 0.30
      - **12:** 0.90
      - **13:** 0.60
      - **14:** 32.50
      - **15:** 0.10
      - **15b:** 0.10
  - **degradacja:** FULL
  - **odcisk:** sha256:754645bbe82937d410c0d54f

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
