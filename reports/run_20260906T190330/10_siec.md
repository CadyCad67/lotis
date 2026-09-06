# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260906T190330` · **snapshot:** `sha256:f3c290f4e6930407` · **60.0 ms**

Horyzont propagacji: 1 odcinkow, zatrzymany na `BASE_RETURN`. 0 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 1 | szt |
| `powod_zatrzymania` | BASE_RETURN | - |
| `koniec_doby_operacyjnej` | 2026-08-22T02:00:00+00:00 | - |
| `pasazerow_transferowych` | 0 | osob |
| `zalogi_poza_fdp` | 4 | osob |

## Co ten node ustalil

- horyzont konczy sie na `BASE_RETURN` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont**
  - **LO3982-2026-08-21**
    - **numer:** LO3982
    - **z:** IEG
    - **do:** WAW
    - **std:** 2026-08-21T08:45:00+00:00
    - **bufor_min:** 7
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 173
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 2 608 148
      - **currency:** PLN
      - **major:** 26081.48
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LDH**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 209
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 2 961 730
      - **currency:** PLN
      - **major:** 29617.30
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LIO**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 187
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 2 806 278
      - **currency:** PLN
      - **major:** 28062.78
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LIQ**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 202
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 3 032 418
      - **currency:** PLN
      - **major:** 30324.18
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **rejsow_bez_podstawienia:** 1
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **rejsow_bez_podstawienia:** 1
  - **CANCEL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **rejsow_bez_podstawienia:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
