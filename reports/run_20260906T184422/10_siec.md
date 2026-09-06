# [10] NETWORK IMPACT

**Status:** degraded · **run:** `20260906T184422` · **snapshot:** `sha256:d7806668b46167a3` · **11.5 ms**

Horyzont propagacji: 0 odcinkow, zatrzymany na `ROTATION_END`. 0 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 0 | szt |
| `powod_zatrzymania` | ROTATION_END | - |
| `koniec_doby_operacyjnej` | 2026-08-24T02:00:00+00:00 | - |
| `pasazerow_transferowych` | 0 | osob |
| `zalogi_poza_fdp` | 11 | osob |

## Co ten node ustalil

- horyzont konczy sie na `ROTATION_END` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont:** -
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LRC**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LRD**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LRH**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **CANCEL**
    - **odcinkow_ponizej:** 0
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0

## Ostrzezenia

- rejs zrodlowy nie ma odcinkow ponizej -- network impact wynosi zero i nie rozroznia opcji

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
