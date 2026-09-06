# [10] NETWORK IMPACT

**Status:** degraded · **run:** `20260906T191132` · **snapshot:** `sha256:f3c290f4e6930407` · **6.78 ms**

Horyzont propagacji: 0 odcinkow, zatrzymany na `END_OF_DAY`. 120 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 0 | szt |
| `powod_zatrzymania` | END_OF_DAY | - |
| `koniec_doby_operacyjnej` | 2026-08-21T09:00:00+00:00 | - |
| `pasazerow_transferowych` | 120 | osob |
| `zalogi_poza_fdp` | 11 | osob |

## Co ten node ustalil

- horyzont konczy sie na `END_OF_DAY` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont:** -
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 70
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 120
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 120
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **CANCEL**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 120
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0

## Ostrzezenia

- rejs zrodlowy nie ma odcinkow ponizej -- network impact wynosi zero i nie rozroznia opcji

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
