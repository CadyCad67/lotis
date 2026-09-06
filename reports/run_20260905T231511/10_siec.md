# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260905T231511` · **snapshot:** `sha256:f3c290f4e6930407` · **66.54 ms**

Horyzont propagacji: 2 odcinkow, zatrzymany na `BASE_RETURN`. 24 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 2 | szt |
| `powod_zatrzymania` | BASE_RETURN | - |
| `koniec_doby_operacyjnej` | 2026-08-22T02:00:00+00:00 | - |
| `pasazerow_transferowych` | 24 | osob |
| `zalogi_poza_fdp` | 4 | osob |

## Co ten node ustalil

- horyzont konczy sie na `BASE_RETURN` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont**
  - **LO3805-2026-08-21**
    - **numer:** LO3805
    - **z:** WAW
    - **do:** RZE
    - **std:** 2026-08-21T07:20:00+00:00
    - **bufor_min:** 19
  - **LO3806-2026-08-21**
    - **numer:** LO3806
    - **z:** RZE
    - **do:** WAW
    - **std:** 2026-08-21T08:55:00+00:00
    - **bufor_min:** 4
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 138
    - **przesiadek_utraconych:** 24
    - **koszt_propagacji**
      - **minor:** 1 945 386
      - **currency:** PLN
      - **major:** 19453.86
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OWN**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 24
    - **koszt_propagacji**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **rejsow_bez_podstawienia:** 2
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 24
    - **koszt_propagacji**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **rejsow_bez_podstawienia:** 2
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 24
    - **koszt_propagacji**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **rejsow_bez_podstawienia:** 2
  - **CANCEL**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 24
    - **koszt_propagacji**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **rejsow_bez_podstawienia:** 2
  - **SPLIT**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 24
    - **koszt_propagacji**
      - **minor:** 662 200
      - **currency:** PLN
      - **major:** 6622.00
    - **rejsow_bez_podstawienia:** 2

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
