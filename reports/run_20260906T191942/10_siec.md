# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260906T191942` · **snapshot:** `sha256:f3c290f4e6930407` · **41.82 ms**

Horyzont propagacji: 1 odcinkow, zatrzymany na `BASE_RETURN`. 99 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 1 | szt |
| `powod_zatrzymania` | BASE_RETURN | - |
| `koniec_doby_operacyjnej` | 2026-08-22T02:00:00+00:00 | - |
| `pasazerow_transferowych` | 99 | osob |
| `zalogi_poza_fdp` | 11 | osob |

## Co ten node ustalil

- horyzont konczy sie na `BASE_RETURN` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont**
  - **LO7-2026-08-21**
    - **numer:** LO7
    - **z:** JFK
    - **do:** WAW
    - **std:** 2026-08-21T23:40:00+00:00
    - **bufor_min:** 0
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 20
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 849 080
      - **currency:** PLN
      - **major:** 8490.80
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LRF**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 136
    - **przesiadek_utraconych:** 99
    - **koszt_propagacji**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LSC**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 136
    - **przesiadek_utraconych:** 99
    - **koszt_propagacji**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 99
    - **koszt_propagacji**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **rejsow_bez_podstawienia:** 1
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 99
    - **koszt_propagacji**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **rejsow_bez_podstawienia:** 1
  - **CANCEL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 99
    - **koszt_propagacji**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **rejsow_bez_podstawienia:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
