# [16] LOG

**Status:** ok · **run:** `20260905T173539` · **snapshot:** `sha256:f3c290f4e6930407` · **3.85 ms**

Zapisano 6 rozwazonych opcji, w tym 0 odrzuconych przez filtr prawny wraz z podstawa kazdego odrzucenia.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_w_logu` | 6 | szt |
| `opcji_odrzuconych` | 0 | szt |
| `odcisk_wpisu` | sha256:c0766b4ba029fdaf5a0a9548 | - |
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
  - **run_id:** 20260905T173539
  - **snapshot:** sha256:f3c290f4e6930407fb2bcad856fc671f
  - **czas_runu:** 2026-09-05T17:35:39.613020+00:00
  - **zaklocenie**
    - **id:** DSR-LO3996-2026-08-21-0
    - **rejs:** LO3996-2026-08-21
    - **typ:** TECHNICAL
    - **opoznienie_min:** 90
    - **termin_decyzji:** 2026-08-21T05:35:00+00:00
    - **iteracja:** 0
    - **wyzwalacz:** INITIAL
  - **opcje_rozwazone**
    - **HOLD**
      - **tryb:** MODIFYING
      - **generator:** SZ.HOLD
      - **strata**
        - **minor:** 3 375 366
        - **currency:** PLN
        - **major:** 33753.66
      - **widelki**
        - **min**
          - **minor:** 3 058 925
          - **currency:** PLN
          - **major:** 30589.25
        - **max**
          - **minor:** 4 078 567
          - **currency:** PLN
          - **major:** 40785.67
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 1
    - **REBOOK-OWN**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.REBOOK-OWN
      - **strata**
        - **minor:** 8 771 613
        - **currency:** PLN
        - **major:** 87716.13
      - **widelki**
        - **min**
          - **minor:** 7 949 274
          - **currency:** PLN
          - **major:** 79492.74
        - **max**
          - **minor:** 10 599 032
          - **currency:** PLN
          - **major:** 105990.32
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 2
    - **REBOOK-OAL**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.REBOOK-OAL
      - **strata**
        - **minor:** 10 306 068
        - **currency:** PLN
        - **major:** 103060.68
      - **widelki**
        - **min**
          - **minor:** 9 339 874
          - **currency:** PLN
          - **major:** 93398.74
        - **max**
          - **minor:** 12 453 165
          - **currency:** PLN
          - **major:** 124531.65
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 5
    - **OVERNIGHT**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.OVERNIGHT
      - **strata**
        - **minor:** 11 394 106
        - **currency:** PLN
        - **major:** 113941.06
      - **widelki**
        - **min**
          - **minor:** 10 325 909
          - **currency:** PLN
          - **major:** 103259.09
        - **max**
          - **minor:** 13 767 878
          - **currency:** PLN
          - **major:** 137678.78
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 6
    - **CANCEL**
      - **tryb:** MODIFYING
      - **generator:** SZ.CANCEL
      - **strata**
        - **minor:** 9 241 722
        - **currency:** PLN
        - **major:** 92417.22
      - **widelki**
        - **min**
          - **minor:** 8 375 311
          - **currency:** PLN
          - **major:** 83753.11
        - **max**
          - **minor:** 11 167 081
          - **currency:** PLN
          - **major:** 111670.81
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 3
    - **SPLIT**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.SPLIT
      - **strata**
        - **minor:** 9 551 418
        - **currency:** PLN
        - **major:** 95514.18
      - **widelki**
        - **min**
          - **minor:** 8 655 973
          - **currency:** PLN
          - **major:** 86559.73
        - **max**
          - **minor:** 11 541 297
          - **currency:** PLN
          - **major:** 115412.97
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 4
  - **rekomendacja**
    - **id:** HOLD
    - **strata**
      - **minor:** 3 375 366
      - **currency:** PLN
      - **major:** 33753.66
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
  - **decyzja_czlowieka**
    - **rodzaj:** ACCEPT
    - **opcja:** HOLD
    - **operator:** OCC-DUTY
    - **kod_przyczyny:** 
    - **rola:** Dyzurny OCC
    - **drugi_podpis:** 0
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
    - **label:** Wstrzymaj odlot o 90 min
    - **what_changes**
      - LO3996: odlot pozniej o 90 min (z 05:35 UTC)
    - **pax_offloaded:** 0
    - **pax_order:** -
    - **rebooked_to:** {}
    - **crew_actions**
      - zaloga rejsu LO3996 pozostaje na sluzbie +90 min -- sprawdzic FDP przed odlotem
    - **valid_until:** 2026-08-21T05:35:00+00:00
    - **cost_low**
      - **minor:** 3 058 925
      - **currency:** PLN
      - **major:** 30589.25
    - **cost_expected**
      - **minor:** 3 375 366
      - **currency:** PLN
      - **major:** 33753.66
    - **cost_high**
      - **minor:** 4 078 567
      - **currency:** PLN
      - **major:** 40785.67
    - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
    - **authorization_role:** Dyzurny OCC
    - **second_signature:** 0
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
    - **elapsed_ms:** 2 496.70
    - **remaining_ms:** 17 503.30
    - **level:** FULL
    - **level_label:** pelny
    - **per_node_ms**
      - **01:** 1 738.10
      - **02:** 12.10
      - **03:** 533.00
      - **04:** 15.80
      - **05:** 10.10
      - **06:** 0.10
      - **07:** 36.80
      - **08:** 2.90
      - **09:** 4.80
      - **10:** 69.50
      - **11:** 0.30
      - **12:** 0.30
      - **13:** 0.30
      - **14:** 31.40
      - **15:** 0.10
      - **15b:** 0.10
  - **degradacja:** FULL
  - **odcisk:** sha256:c0766b4ba029fdaf5a0a9548

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
