# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260906T194321` · **snapshot:** `sha256:6c790f69f87c3591` · **29.49 ms**

Horyzont propagacji: 1 odcinkow, zatrzymany na `BASE_RETURN`. 105 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 1 | szt |
| `powod_zatrzymania` | BASE_RETURN | - |
| `koniec_doby_operacyjnej` | 2026-08-24T19:00:00+00:00 | - |
| `pasazerow_transferowych` | 105 | osob |
| `zalogi_poza_fdp` | 11 | osob |

## Co ten node ustalil

- horyzont konczy sie na `BASE_RETURN` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont**
  - **LO4-2026-08-24**
    - **numer:** LO4
    - **z:** ORD
    - **do:** WAW
    - **std:** 2026-08-24T04:50:00+00:00
    - **bufor_min:** 0
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 0
      - **currency:** PLN
      - **major:** 0.00
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 105
    - **koszt_propagacji**
      - **minor:** 25 778 500
      - **currency:** PLN
      - **major:** 257785.00
    - **rejsow_bez_podstawienia:** 1
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 105
    - **koszt_propagacji**
      - **minor:** 25 778 500
      - **currency:** PLN
      - **major:** 257785.00
    - **rejsow_bez_podstawienia:** 1
  - **CANCEL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 105
    - **koszt_propagacji**
      - **minor:** 25 778 500
      - **currency:** PLN
      - **major:** 257785.00
    - **rejsow_bez_podstawienia:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
