# [10] NETWORK IMPACT

**Status:** ok · **run:** `20260905T181301` · **snapshot:** `sha256:44a9b3ee12dd2f25` · **61.22 ms**

Horyzont propagacji: 2 odcinkow, zatrzymany na `BASE_RETURN`. 22 pasazerow transferowych na rejsie zrodlowym.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `odcinkow_w_horyzoncie` | 2 | szt |
| `powod_zatrzymania` | BASE_RETURN | - |
| `koniec_doby_operacyjnej` | 2026-08-26T02:00:00+00:00 | - |
| `pasazerow_transferowych` | 22 | osob |
| `zalogi_poza_fdp` | 4 | osob |

## Co ten node ustalil

- horyzont konczy sie na `BASE_RETURN` -- dalej opcje przestaja sie roznic i liczenie nie zmienia rankingu
- opoznienie propaguje sie pomniejszone o bufor postoju; bufor wieszy od opoznienia wchlania je w calosci

## Szczegoly

- **horyzont**
  - **LO417-2026-08-25**
    - **numer:** LO417
    - **z:** WAW
    - **do:** GVA
    - **std:** 2026-08-25T07:20:00+00:00
    - **bufor_min:** 17
  - **LO418-2026-08-25**
    - **numer:** LO418
    - **z:** GVA
    - **do:** WAW
    - **std:** 2026-08-25T10:25:00+00:00
    - **bufor_min:** 12
- **propagacja_wg_opcji**
  - **HOLD**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 434
    - **przesiadek_utraconych:** 22
    - **koszt_propagacji**
      - **minor:** 6 542 984
      - **currency:** PLN
      - **major:** 65429.84
    - **rejsow_bez_podstawienia:** 0
  - **REBOOK-OWN**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 22
    - **koszt_propagacji**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **rejsow_bez_podstawienia:** 2
  - **REBOOK-OAL**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 22
    - **koszt_propagacji**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **rejsow_bez_podstawienia:** 2
  - **OVERNIGHT**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 22
    - **koszt_propagacji**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **rejsow_bez_podstawienia:** 2
  - **CANCEL**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 22
    - **koszt_propagacji**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **rejsow_bez_podstawienia:** 2
  - **SPLIT**
    - **odcinkow_ponizej:** 2
    - **suma_propagacji_min:** 0
    - **przesiadek_utraconych:** 22
    - **koszt_propagacji**
      - **minor:** 1 685 600
      - **currency:** PLN
      - **major:** 16856.00
    - **rejsow_bez_podstawienia:** 2

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
