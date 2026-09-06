# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260906T175725` · **snapshot:** `sha256:91cb2a4af61a3714` · **40.38 ms**

Horyzont propagacji: 1 odcinkow, zatrzymany na `BASE_RETURN`. 114 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 1 | szt |
| `powod_zatrzymania` | BASE_RETURN | - |
| `koniec_doby_operacyjnej` | 2026-08-23T02:00:00+00:00 | - |
| `pasazerow_transferowych` | 114 | osob |
| `zalogi_poza_fdp` | 11 | osob |

## Co ten node ustalil

- horyzont konczy sie na `BASE_RETURN` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont**
  - **LO7-2026-08-22**
    - **numer:** LO7
    - **z:** JFK
    - **do:** WAW
    - **std:** 2026-08-22T23:40:00+00:00
    - **bufor_min:** 0
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 30
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 1 798 350
      - **currency:** PLN
      - **major:** 17983.50
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LSB**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 136
    - **przesiadek_utraconych:** 114
    - **koszt_propagacji**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LSG**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 136
    - **przesiadek_utraconych:** 114
    - **koszt_propagacji**
      - **minor:** 8 152 520
      - **currency:** PLN
      - **major:** 81525.20
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 114
    - **koszt_propagacji**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **rejsow_bez_podstawienia:** 1
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 114
    - **koszt_propagacji**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **rejsow_bez_podstawienia:** 1
  - **CANCEL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 114
    - **koszt_propagacji**
      - **minor:** 24 359 500
      - **currency:** PLN
      - **major:** 243595.00
    - **rejsow_bez_podstawienia:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
