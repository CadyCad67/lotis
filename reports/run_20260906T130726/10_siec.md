# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260906T130726` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **70.2 ms**

Horyzont propagacji: 1 odcinkow, zatrzymany na `BASE_RETURN`. 16 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 1 | szt |
| `powod_zatrzymania` | BASE_RETURN | - |
| `koniec_doby_operacyjnej` | 2026-08-26T02:00:00+00:00 | - |
| `pasazerow_transferowych` | 16 | osob |
| `zalogi_poza_fdp` | 4 | osob |

## Co ten node ustalil

- horyzont konczy sie na `BASE_RETURN` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont**
  - **LO418-2026-08-25**
    - **numer:** LO418
    - **z:** GVA
    - **do:** WAW
    - **std:** 2026-08-25T10:25:00+00:00
    - **bufor_min:** 12
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 168
    - **przesiadek_utraconych:** 16
    - **koszt_propagacji**
      - **minor:** 2 532 768
      - **currency:** PLN
      - **major:** 25327.68
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LDH**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 204
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 2 835 084
      - **currency:** PLN
      - **major:** 28350.84
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LIK**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 197
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 2 905 772
      - **currency:** PLN
      - **major:** 29057.72
    - **rejsow_bez_podstawienia:** 0
  - **SWAP-SP-LIL**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 197
    - **przesiadek_utraconych:** 0
    - **koszt_propagacji**
      - **minor:** 2 905 772
      - **currency:** PLN
      - **major:** 29057.72
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OWN**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 16
    - **koszt_propagacji**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **rejsow_bez_podstawienia:** 1
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 16
    - **koszt_propagacji**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **rejsow_bez_podstawienia:** 1
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 16
    - **koszt_propagacji**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **rejsow_bez_podstawienia:** 1
  - **CANCEL**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 16
    - **koszt_propagacji**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **rejsow_bez_podstawienia:** 1
  - **SPLIT**
    - **odcinkow_ponizej:** 1
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 16
    - **koszt_propagacji**
      - **minor:** 1 565 200
      - **currency:** PLN
      - **major:** 15652.00
    - **rejsow_bez_podstawienia:** 1

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
