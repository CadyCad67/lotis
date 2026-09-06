# [16] LOG

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **3.86 ms**

Zapisano 4 rozwazonych opcji, w tym 1 odrzuconych przez filtr prawny wraz z podstawa kazdego odrzucenia.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_w_logu` | 4 | szt |
| `opcji_odrzuconych` | 1 | szt |
| `odcisk_wpisu` | sha256:d415f7e0ef00ebfb701aae9c | - |
| `wersja_silnika` | 1.0.0 | - |
| `wersja_bazy` | 5.0 | - |
| `nadpisania` | brak | - |
| `decyzja` | ACCEPT | - |
| `wybrana_opcja` | OVERNIGHT | - |

## Co ten node ustalil

- log zapisuje podstawe odrzucenia kazdej opcji -- w sporze liczy sie to, czego nie wybrano i dlaczego
- wersja bazy `5.0` jest jednoczesnie wersja modelu kosztowego i prawa -- oba pochodza z tego samego pliku

## Szczegoly

- **wpis**
  - **schema:** lotis.audit/v1
  - **run_id:** 20260906T194321
  - **snapshot:** sha256:6c790f69f87c359132b1de878467789b
  - **czas_runu:** 2026-09-06T19:43:21.711570+00:00
  - **zaklocenie**
    - **id:** DSR-LO82-2026-08-24-0
    - **rejs:** LO82-2026-08-24
    - **typ:** PAX
    - **opoznienie_min:** 0
    - **termin_decyzji:** 2026-08-24T01:15:00+00:00
    - **iteracja:** 0
    - **wyzwalacz:** INITIAL
  - **opcje_rozwazone**
    - **HOLD**
      - **tryb:** MODIFYING
      - **generator:** SZ.HOLD
      - **strata**
        - **minor:** 3 397 527
        - **currency:** PLN
        - **major:** 33975.27
      - **widelki**
        - **min**
          - **minor:** 3 191 617
          - **currency:** PLN
          - **major:** 31916.17
        - **max**
          - **minor:** 6 863 690
          - **currency:** PLN
          - **major:** 68636.90
      - **dopuszczalna:** 0
      - **powod_odrzucenia**
        - **podstawa:** Art. 8 EU261
        - **powod:** 8 pasazerow zdjetych bez zapewnienia przewozu ani zwrotu
        - **podstawa:** Art. 4 EU261
        - **powod:** 8 pasazerow zdjetych wbrew woli bez uprzedniego wezwania ochotnikow
      - **pozycja_koncowa:** None
    - **REBOOK-OAL**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.REBOOK-OAL
      - **strata**
        - **minor:** 150 588 580
        - **currency:** PLN
        - **major:** 1505885.80
      - **widelki**
        - **min**
          - **minor:** 141 462 000
          - **currency:** PLN
          - **major:** 1414620.00
        - **max**
          - **minor:** 304 219 353
          - **currency:** PLN
          - **major:** 3042193.53
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 2
    - **OVERNIGHT**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.OVERNIGHT
      - **strata**
        - **minor:** 121 389 006
        - **currency:** PLN
        - **major:** 1213890.06
      - **widelki**
        - **min**
          - **minor:** 114 032 097
          - **currency:** PLN
          - **major:** 1140320.97
        - **max**
          - **minor:** 245 230 315
          - **currency:** PLN
          - **major:** 2452303.15
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 1
    - **CANCEL**
      - **tryb:** MODIFYING
      - **generator:** SZ.CANCEL
      - **strata**
        - **minor:** 169 173 593
        - **currency:** PLN
        - **major:** 1691735.93
      - **widelki**
        - **min**
          - **minor:** 158 920 648
          - **currency:** PLN
          - **major:** 1589206.48
        - **max**
          - **minor:** 341 764 834
          - **currency:** PLN
          - **major:** 3417648.34
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 3
  - **rekomendacja**
    - **id:** OVERNIGHT
    - **strata**
      - **minor:** 121 389 006
      - **currency:** PLN
      - **major:** 1213890.06
    - **oszczednosc**
      - **minor:** 29 199 574
      - **currency:** PLN
      - **major:** 291995.74
  - **decyzja_czlowieka**
    - **rodzaj:** ACCEPT
    - **opcja:** OVERNIGHT
    - **operator:** OCC-DUTY
    - **kod_przyczyny:** 
    - **rola:** Director Network Operations
    - **drugi_podpis:** 1
    - **odstepstwo:** 0
  - **wykonanie**
    - **opcja:** OVERNIGHT
    - **kroki**
      - **kasacja_w_systemie**
        - **wykonawca:** System rezerwacyjny
        - **opis:** odwolanie rejsu i zwolnienie miejsc
        - **odwracalny:** 0
        - **krytyczny:** 1
        - **status:** wykonany
      - **przepisanie_wlasne**
        - **wykonawca:** System rezerwacyjny
        - **opis:** przepisanie pasazerow na wlasny rejs
        - **odwracalny:** 1
        - **krytyczny:** 0
        - **status:** wykonany
      - **rezerwacja_hotelu**
        - **wykonawca:** Pax Care
        - **opis:** rezerwacja hoteli i transportu
        - **odwracalny:** 1
        - **krytyczny:** 0
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
    - **option_id:** OVERNIGHT
    - **label:** Nocleg i rejs nastepnego dnia
    - **what_changes**
      - LO82: rejs odwolany
      - 227 pasazerow na wlasny rejs -- oczekiwanie 840 min
      - 227 pasazerow z noclegiem na koszt przewoznika (Art. 9)
    - **pax_offloaded:** 0
    - **pax_order:** -
    - **rebooked_to**
      - **PAX000236:** wlasny rejs
      - **PAX000237:** wlasny rejs
      - **PAX000238:** wlasny rejs
      - **PAX000239:** wlasny rejs
      - **PAX000240:** wlasny rejs
      - **PAX000241:** wlasny rejs
      - **PAX000242:** wlasny rejs
      - **PAX000243:** wlasny rejs
      - **PAX000244:** wlasny rejs
      - **PAX000245:** wlasny rejs
      - **PAX000246:** wlasny rejs
      - **PAX000247:** wlasny rejs
      - **PAX000248:** wlasny rejs
      - **PAX000249:** wlasny rejs
      - **PAX000250:** wlasny rejs
      - **PAX000251:** wlasny rejs
      - **PAX000252:** wlasny rejs
      - **PAX000253:** wlasny rejs
      - **PAX000254:** wlasny rejs
      - **PAX000255:** wlasny rejs
    - **crew_actions**
      - nocleg zalogi poza baza
    - **valid_until:** 2026-08-24T01:15:00+00:00
    - **cost_low**
      - **minor:** 114 032 097
      - **currency:** PLN
      - **major:** 1140320.97
    - **cost_expected**
      - **minor:** 121 389 006
      - **currency:** PLN
      - **major:** 1213890.06
    - **cost_high**
      - **minor:** 245 230 315
      - **currency:** PLN
      - **major:** 2452303.15
    - **threshold_note:** `OVERNIGHT` pozostaje najlepsza w calym badanym zakresie do +120 min
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
    - **elapsed_ms:** 2 565.50
    - **remaining_ms:** 17 434.50
    - **level:** FULL
    - **level_label:** pelny
    - **per_node_ms**
      - **01:** 1 793.10
      - **02:** 12.20
      - **03:** 574.10
      - **04:** 12.70
      - **05:** 10.50
      - **06:** 0.10
      - **07:** 47.30
      - **08:** 3.50
      - **09:** 15.10
      - **10:** 29.50
      - **11:** 0.40
      - **12:** 0.70
      - **13:** 0.40
      - **14:** 22.70
      - **15:** 0.00
      - **15b:** 0.10
  - **degradacja:** FULL
  - **odcisk:** sha256:d415f7e0ef00ebfb701aae9c

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
