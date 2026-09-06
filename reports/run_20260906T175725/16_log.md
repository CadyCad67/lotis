# [16] LOG

**Status:** ok · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **3.89 ms**

Zapisano 6 rozwazonych opcji, w tym 1 odrzuconych przez filtr prawny wraz z podstawa kazdego odrzucenia.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_w_logu` | 6 | szt |
| `opcji_odrzuconych` | 1 | szt |
| `odcisk_wpisu` | sha256:1a3bc8165e1e8e30220ffcab | - |
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
  - **run_id:** 20260906T175725
  - **snapshot:** sha256:91cb2a4af61a3714f4c72ed8bbad9666
  - **czas_runu:** 2026-09-06T17:57:25.779922+00:00
  - **zaklocenie**
    - **id:** DSR-LO6-2026-08-22-0
    - **rejs:** LO6-2026-08-22
    - **typ:** TECHNICAL
    - **opoznienie_min:** 30
    - **termin_decyzji:** 2026-08-22T12:10:00+00:00
    - **iteracja:** 0
    - **wyzwalacz:** INITIAL
  - **opcje_rozwazone**
    - **HOLD**
      - **tryb:** MODIFYING
      - **generator:** SZ.HOLD
      - **strata**
        - **minor:** 3 714 950
        - **currency:** PLN
        - **major:** 37149.50
      - **widelki**
        - **min**
          - **minor:** 3 452 481
          - **currency:** PLN
          - **major:** 34524.81
        - **max**
          - **minor:** 5 733 944
          - **currency:** PLN
          - **major:** 57339.44
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 1
    - **SWAP-SP-LSB**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.SWAP
      - **strata**
        - **minor:** 17 291 062
        - **currency:** PLN
        - **major:** 172910.62
      - **widelki**
        - **min**
          - **minor:** 16 069 411
          - **currency:** PLN
          - **major:** 160694.11
        - **max**
          - **minor:** 26 688 378
          - **currency:** PLN
          - **major:** 266883.78
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 2
    - **SWAP-SP-LSG**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.SWAP
      - **strata**
        - **minor:** 18 173 872
        - **currency:** PLN
        - **major:** 181738.72
      - **widelki**
        - **min**
          - **minor:** 16 889 849
          - **currency:** PLN
          - **major:** 168898.49
        - **max**
          - **minor:** 28 050 976
          - **currency:** PLN
          - **major:** 280509.76
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 3
    - **REBOOK-OAL**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.REBOOK-OAL
      - **strata**
        - **minor:** 152 798 092
        - **currency:** PLN
        - **major:** 1527980.92
      - **widelki**
        - **min**
          - **minor:** 142 002 575
          - **currency:** PLN
          - **major:** 1420025.75
        - **max**
          - **minor:** 235 840 533
          - **currency:** PLN
          - **major:** 2358405.33
      - **dopuszczalna:** 0
      - **powod_odrzucenia**
        - **podstawa:** Art. 9 EU261
        - **powod:** oczekiwanie 925 min bez zapewnionego noclegu (prog opieki 240 min)
      - **pozycja_koncowa:** None
    - **OVERNIGHT**
      - **tryb:** RESTRUCTURING
      - **generator:** SZ.OVERNIGHT
      - **strata**
        - **minor:** 118 207 488
        - **currency:** PLN
        - **major:** 1182074.88
      - **widelki**
        - **min**
          - **minor:** 109 855 873
          - **currency:** PLN
          - **major:** 1098558.73
        - **max**
          - **minor:** 182 450 688
          - **currency:** PLN
          - **major:** 1824506.88
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 4
    - **CANCEL**
      - **tryb:** MODIFYING
      - **generator:** SZ.CANCEL
      - **strata**
        - **minor:** 147 509 859
        - **currency:** PLN
        - **major:** 1475098.59
      - **widelki**
        - **min**
          - **minor:** 137 087 967
          - **currency:** PLN
          - **major:** 1370879.67
        - **max**
          - **minor:** 227 678 260
          - **currency:** PLN
          - **major:** 2276782.60
      - **dopuszczalna:** 1
      - **powod_odrzucenia:** -
      - **pozycja_koncowa:** 5
  - **rekomendacja**
    - **id:** HOLD
    - **strata**
      - **minor:** 3 714 950
      - **currency:** PLN
      - **major:** 37149.50
    - **oszczednosc**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
  - **decyzja_czlowieka**
    - **rodzaj:** ACCEPT
    - **opcja:** HOLD
    - **operator:** OCC-DUTY
    - **kod_przyczyny:** 
    - **rola:** Supervisor OCC
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
    - **label:** Wstrzymaj odlot o 30 min
    - **what_changes**
      - LO6: odlot pozniej o 30 min (z 12:10 UTC)
    - **pax_offloaded:** 0
    - **pax_order:** -
    - **rebooked_to:** {}
    - **crew_actions**
      - zaloga rejsu LO6 pozostaje na sluzbie +30 min -- sprawdzic FDP przed odlotem
    - **valid_until:** 2026-08-22T12:10:00+00:00
    - **cost_low**
      - **minor:** 3 452 481
      - **currency:** PLN
      - **major:** 34524.81
    - **cost_expected**
      - **minor:** 3 714 950
      - **currency:** PLN
      - **major:** 37149.50
    - **cost_high**
      - **minor:** 5 733 944
      - **currency:** PLN
      - **major:** 57339.44
    - **threshold_note:** `HOLD` pozostaje najlepsza w calym badanym zakresie do +120 min
    - **authorization_role:** Supervisor OCC
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
    - **elapsed_ms:** 2 477.00
    - **remaining_ms:** 17 523.00
    - **level:** FULL
    - **level_label:** pelny
    - **per_node_ms**
      - **01:** 1 741.60
      - **02:** 12.10
      - **03:** 548.20
      - **04:** 6.00
      - **05:** 10.00
      - **06:** 0.10
      - **07:** 17.30
      - **08:** 3.90
      - **09:** 17.30
      - **10:** 40.40
      - **11:** 0.20
      - **12:** 0.90
      - **13:** 0.60
      - **14:** 34.80
      - **15:** 0.10
      - **15b:** 0.10
  - **degradacja:** FULL
  - **odcisk:** sha256:1a3bc8165e1e8e30220ffcab

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
