# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260906T192747` · **snapshot:** `sha256:f3c290f4e6930407` · **80.71 ms**

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
  - **LO3932-2026-08-21**
    - **numer:** LO3932
    - **z:** SZZ
    - **do:** WAW
    - **std:** 2026-08-21T08:50:00+00:00
    - **bufor_min:** 7
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 13
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 99 463
      - **currency:** PLN
      - **major:** 994.63
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-SPILL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 13
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 99 463
      - **currency:** PLN
      - **major:** 994.63
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LDH**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 49
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 622 830
      - **currency:** PLN
      - **major:** 6228.30
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LIC**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 47
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 599 338
      - **currency:** PLN
      - **major:** 5993.38
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LIO**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 29
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 424 270
      - **currency:** PLN
      - **major:** 4242.70
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OWN**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 782 600
      - **currency:** PLN
      - **major:** 7826.00
    - **rejsow_bez_podstawienia:** 1
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 782 600
      - **currency:** PLN
      - **major:** 7826.00
    - **rejsow_bez_podstawienia:** 1
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 782 600
      - **currency:** PLN
      - **major:** 7826.00
    - **rejsow_bez_podstawienia:** 1
  - **CANCEL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 782 600
      - **currency:** PLN
      - **major:** 7826.00
    - **rejsow_bez_podstawienia:** 1
  - **SPLIT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 782 600
      - **currency:** PLN
      - **major:** 7826.00
    - **rejsow_bez_podstawienia:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
