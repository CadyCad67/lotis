# [12] FILTR PRAWNY

**Status:** degraded · **run:** `20260906T131947` · **snapshot:** `sha256:3b1d18402faf79f0` · **1.32 ms**

Z 7 opcji przez filtr przeszlo 4. Odrzucono: SWAP-SP-LRD, SWAP-SP-LRG, REBOOK-OAL.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_na_wejsciu` | 7 | szt |
| `opcji_dopuszczalnych` | 4 | szt |
| `opcji_odrzuconych` | 3 | szt |
| `kategoria_eu261` | C | - |
| `prog_opieki` | 240 | min |

## Co ten node ustalil

- `SWAP-SP-LRD` odrzucona -- Art. 8 EU261: 29 pasazerow zdjetych bez zapewnienia przewozu ani zwrotu
- `SWAP-SP-LRD` odrzucona -- Art. 4 EU261: 29 pasazerow zdjetych wbrew woli bez uprzedniego wezwania ochotnikow
- `SWAP-SP-LRG` odrzucona -- Art. 8 EU261: 29 pasazerow zdjetych bez zapewnienia przewozu ani zwrotu
- `SWAP-SP-LRG` odrzucona -- Art. 4 EU261: 29 pasazerow zdjetych wbrew woli bez uprzedniego wezwania ochotnikow
- `REBOOK-OAL` odrzucona -- Art. 9 EU261: oczekiwanie 925 min bez zapewnionego noclegu (prog opieki 240 min)
- filtr usuwa opcje, nigdy ich nie przecenia -- odszkodowanie jako pozycja kosztowa uczynilby zdjecie pasazerow wbrew woli optymalnym
- pelna kwota z Art. 7 jest nienaruszalna: zaniżanie odszkodowan bylo przedmiotem decyzji zobowiazujacej UOKiK (RBG-1/2026)

## Szczegoly

- **werdykty**
  - **HOLD**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia:** -
  - **SWAP-SP-LRD**
    - **dopuszczalna:** 0
    - **zlamane_reguly**
      - **podstawa:** Art. 8 EU261
      - **powod:** 29 pasazerow zdjetych bez zapewnienia przewozu ani zwrotu
      - **podstawa:** Art. 4 EU261
      - **powod:** 29 pasazerow zdjetych wbrew woli bez uprzedniego wezwania ochotnikow
    - **ostrzezenia:** -
  - **SWAP-SP-LRG**
    - **dopuszczalna:** 0
    - **zlamane_reguly**
      - **podstawa:** Art. 8 EU261
      - **powod:** 29 pasazerow zdjetych bez zapewnienia przewozu ani zwrotu
      - **podstawa:** Art. 4 EU261
      - **powod:** 29 pasazerow zdjetych wbrew woli bez uprzedniego wezwania ochotnikow
    - **ostrzezenia:** -
  - **SWAP-SP-LSC**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia:** -
  - **REBOOK-OAL**
    - **dopuszczalna:** 0
    - **zlamane_reguly**
      - **podstawa:** Art. 9 EU261
      - **powod:** oczekiwanie 925 min bez zapewnionego noclegu (prog opieki 240 min)
    - **ostrzezenia**
      - opoznienie 925 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
  - **OVERNIGHT**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia**
      - opoznienie 840 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
  - **CANCEL**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia**
      - opoznienie 840 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
- **filtry_twarde**
  - Opieka z Art. 9 EU261
  - Prawo do zmiany planu z Art. 8 EU261
  - Limity FDP i wypoczynku EASA
  - Cisza nocna typu ban
  - Minimum personelu pokladowego
  - Asysta PRM wg 1107/2006
  - Zakaz rozdzielania rodzin, grup i UMNR
  - Pełna kwota odszkodowania z Art. 7 — zakaz ugód poniżej stawki (UOKiK)
- **podstawy_prawne**
  - **MC99_DELAY**
    - **akt:** Konwencja montrealska 1999, Art. 19 i 22 ust. 1
  - **MC99_BAGGAGE**
    - **akt:** Konwencja montrealska 1999, Art. 17 i 22 ust. 2
  - **REG_2027_97**
    - **akt:** Rozporzadzenie (WE) nr 2027/97 zm. 889/2002
  - **REG_1107_2006**
    - **akt:** Rozporzadzenie (WE) nr 1107/2006, Art. 3, 4, 7, 8
  - **REG_95_93_SLOTS**
    - **akt:** Rozporzadzenie (EWG) nr 95/93, Art. 8, 10
  - **ATFM_CTOT**
    - **akt:** Rozporzadzenie (UE) nr 255/2010 (ATFM) + procedury EUROCONTROL NM
  - **REG_1008_2008_WETLEASE**
    - **akt:** Rozporzadzenie (WE) nr 1008/2008, Art. 13
  - **PL_PRAWO_LOTNICZE_205**
    - **akt:** Ustawa Prawo lotnicze z 3.07.2002, art. 205a-205c
  - **EASA_CAT_OP_MPA_155**
    - **akt:** Rozporzadzenie (UE) nr 965/2012, CAT.OP.MPA.155 / ORO.CC.100
  - **NOISE_CURFEW_WAW**
    - **akt:** Zasada Lokalna EPWA 1 (zatw. Prezes ULC 04.10.2017), obowiazuje od 25.03.2018
  - **UOKIK_ZIK**
    - **akt:** Ustawa o ochronie konkurencji i konsumentow, art. 24
  - **UOKIK_ZIK**
    - **akt:** Ustawa o ochronie konkurencji i konsumentow, art. 24

## Ostrzezenia

- `OVERNIGHT`: opoznienie 840 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
- `CANCEL`: opoznienie 840 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
