# [16] LOG

**Status:** ok · **run:** `20260906T191132` · **snapshot:** `sha256:f3c290f4e6930407` · **3.81 ms**

Zapisano 4 rozwazonych opcji, w tym 1 odrzuconych przez filtr prawny wraz z podstawa kazdego odrzucenia.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_w_logu` | 4 | szt |
| `opcji_odrzuconych` | 1 | szt |
| `odcisk_wpisu` | sha256:e917873461642bfa4262c95e | - |
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
  - **run_id:** 20260906T191132
  - **snapshot:** sha256:f3c290f4e6930407fb2bcad856fc671f
  - **czas_runu:** 2026-09-06T19:11:32.027914+00:00
  - **zaklocenie**
    - **id:** DSR-LO2098-2026-08-21-0
    - **rejs:** LO2098-2026-08-21
    - **typ:** TECHNICAL
    - **opoznienie_min:** 180
    - **termin_decyzji:** 2026-08-21T00:10:00+00:00
    - **iteracja:** 0
    - **wyzwalacz:** INITIAL
  - **opcje_rozwazone**
    - **HOLD**
      - **tryb:** MODIFYING
      - **generator:** SZ.HOLD
      - **strata**
        - **minor:** 80 572 260
        - **currency:** PLN
        - **major:** 805722.60
      - **widelki**
        - **min**
          - **minor:** 73 484 886
          - **currency:** PLN
          - **major:** 734848.86
        - **max**
          - **minor:** 140 255 415
          - **currency:** PLN
          - **major:** 1402554.15
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 1
    - **REBOOK-OAL**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.REBOOK-OAL
      - **strata**
        - **minor:** 168 346 720
        - **currency:** PLN
        - **major:** 1683467.20
      - **widelki**
        - **min**
          - **minor:** 153 538 444
          - **currency:** PLN
          - **major:** 1535384.44
        - **max**
          - **minor:** 293 047 994
          - **currency:** PLN
          - **major:** 2930479.94
      - **dopuszczalna:** 0
      - **powod_odrzucenia**
        - **podstawa:** Art. 9 EU261
        - **powod:** oczekiwanie 925 min bez zapewnionego noclegu (prog opieki 240 min)
      - **pozycja_koncowa:** None
    - **OVERNIGHT**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.OVERNIGHT
      - **strata**
        - **minor:** 135 098 174
        - **currency:** PLN
        - **major:** 1350981.74
      - **widelki**
        - **min**
          - **minor:** 123 214 539
          - **currency:** PLN
          - **major:** 1232145.39
        - **max**
          - **minor:** 235 170 895
          - **currency:** PLN
          - **major:** 2351708.95
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 2
    - **CANCEL**
      - **tryb:** MODIFYING
      - **generator:** SZ.CANCEL
      - **strata**
        - **minor:** 171 911 211
        - **currency:** PLN
        - **major:** 1719112.11
      - **widelki**
        - **min**
          - **minor:** 156 789 392
          - **currency:** PLN
          - **major:** 1567893.92
        - **max**
          - **minor:** 299 252 848
          - **currency:** PLN
          - **major:** 2992528.48
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 3
  - **rekomendacja**
    - **id:** HOLD
    - **strata**
      - **minor:** 80 572 260
      - **currency:** PLN
      - **major:** 805722.60
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
  - **decyzja_czlowieka**
    - **rodzaj:** ACCEPT
    - **opcja:** HOLD
    - **operator:** OCC-DUTY
    - **kod_przyczyny:** 
    - **rola:** Director Network Operations
    - **drugi_podpis:** 1
    - **odstepstwo:** 0
  - **wykonanie**
    - **opcja:** HOLD
    - **kroki**
      - **nowy_slot**
        - **wykonawca:** Slot Coordination / EUROCONTROL
        - **opis:** wystapienie o nowe okno startowe
        - **odwracalny:** 0
        - **krytyczny:** 1
        - **status:** wykonany
      - **powiadomienie_pax**
        - **wykonawca:** Komunikacja
        - **opis:** wyslanie SMS i e-mail do pasazerow
        - **odwracalny:** 1
        - **krytyczny:** 0
        - **status:** wykonany
      - **brief_zalogi**
        - **wykonawca:** Crew Control
        - **opis:** poinformowanie zalogi o zmianie
        - **odwracalny:** 1
        - **krytyczny:** 0
        - **status:** wykonany
    - **udane:** 1
  - **karta_wykonania**
    - **option_id:** HOLD
    - **label:** Wstrzymaj odlot o 180 min
    - **what_changes**
      - LO2098: odlot pozniej o 180 min (z 00:10 UTC)
    - **pax_offloaded:** 0
    - **pax_order:** -
    - **rebooked_to:** {}
    - **crew_actions**
      - zaloga rejsu LO2098 pozostaje na sluzbie +180 min -- sprawdzic FDP przed odlotem
    - **valid_until:** 2026-08-21T00:10:00+00:00
    - **cost_low**
      - **minor:** 73 484 886
      - **currency:** PLN
      - **major:** 734848.86
    - **cost_expected**
      - **minor:** 80 572 260
      - **currency:** PLN
      - **major:** 805722.60
    - **cost_high**
      - **minor:** 140 255 415
      - **currency:** PLN
      - **major:** 1402554.15
    - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
    - **authorization_role:** Director Network Operations
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
    - **elapsed_ms:** 2 697.30
    - **remaining_ms:** 17 302.70
    - **level:** FULL
    - **level_label:** pelny
    - **per_node_ms**
      - **01:** 1 948.60
      - **02:** 12.20
      - **03:** 596.40
      - **04:** 12.10
      - **05:** 13.50
      - **06:** 0.10
      - **07:** 17.10
      - **08:** 4.50
      - **09:** 17.00
      - **10:** 6.80
      - **11:** 0.50
      - **12:** 0.60
      - **13:** 0.40
      - **14:** 24.70
      - **15:** 0.00
      - **15b:** 0.10
  - **degradacja:** FULL
  - **odcisk:** sha256:e917873461642bfa4262c95e

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
