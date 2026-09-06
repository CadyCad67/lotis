# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260906T194742` · **snapshot:** `sha256:6c790f69f87c3591` · **82.72 ms**

Horyzont propagacji: 1 odcinkow, zatrzymany na `BASE_RETURN`. 23 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 1 | szt |
| `powod_zatrzymania` | BASE_RETURN | - |
| `koniec_doby_operacyjnej` | 2026-08-25T02:00:00+00:00 | - |
| `pasazerow_transferowych` | 23 | osob |
| `zalogi_poza_fdp` | 5 | osob |

## Co ten node ustalil

- horyzont konczy sie na `BASE_RETURN` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont**
  - **LO396-2026-08-24**
    - **numer:** LO396
    - **z:** HAM
    - **do:** WAW
    - **std:** 2026-08-24T11:25:00+00:00
    - **bufor_min:** 7
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 713
    - **przesiadek_utraconych:** 23
    - **koszt_propagacji**
      - **minor:** 13 959 827
      - **currency:** PLN
      - **major:** 139598.27
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LIC**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 742
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 11 339 494
      - **currency:** PLN
      - **major:** 113394.94
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LID**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 747
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 11 414 874
      - **currency:** PLN
      - **major:** 114148.74
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LII**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 747
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 11 414 874
      - **currency:** PLN
      - **major:** 114148.74
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OWN**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 23
    - **koszt_propagacji**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **rejsow_bez_podstawienia:** 1
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 23
    - **koszt_propagacji**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **rejsow_bez_podstawienia:** 1
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 23
    - **koszt_propagacji**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **rejsow_bez_podstawienia:** 1
  - **CANCEL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 23
    - **koszt_propagacji**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **rejsow_bez_podstawienia:** 1
  - **SPLIT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 23
    - **koszt_propagacji**
      - **minor:** 1 083 600
      - **currency:** PLN
      - **major:** 10836.00
    - **rejsow_bez_podstawienia:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
