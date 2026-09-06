# [12] FILTR PRAWNY

**Status:** degraded · **run:** `20260905T231259` · **snapshot:** `sha256:f3c290f4e6930407` · **0.27 ms**

Z 6 opcji przez filtr przeszlo 6. Zadna nie odpadla.

## Liczby

| pole | wartosc | jednostka |
| --- | --- | --- |
| `opcji_na_wejsciu` | 6 | szt |
| `opcji_dopuszczalnych` | 6 | szt |
| `opcji_odrzuconych` | 0 | szt |
| `kategoria_eu261` | A | - |
| `prog_opieki` | 120 | min |

## Co ten node ustalil

- filtr usuwa opcje, nigdy ich nie przecenia -- odszkodowanie jako pozycja kosztowa uczynilby zdjecie pasazerow wbrew woli optymalnym
- pelna kwota z Art. 7 jest nienaruszalna: zaniżanie odszkodowan bylo przedmiotem decyzji zobowiazujacej UOKiK (RBG-1/2026)

## Szczegoly

- **werdykty**
  - **HOLD**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia:** -
  - **REBOOK-OWN**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia**
      - opoznienie 560 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
  - **REBOOK-OAL**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia**
      - opoznienie 625 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
  - **OVERNIGHT**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia**
      - opoznienie 840 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
  - **CANCEL**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia**
      - opoznienie 560 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
  - **SPLIT**
    - **dopuszczalna:** 1
    - **zlamane_reguly:** -
    - **ostrzezenia**
      - opoznienie 560 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
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

- `REBOOK-OWN`: opoznienie 560 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
- `REBOOK-OAL`: opoznienie 625 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
- `OVERNIGHT`: opoznienie 840 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
- `CANCEL`: opoznienie 560 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)
- `SPLIT`: opoznienie 560 min przekracza prog 300 min -- pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)

_silnik 1.0.0 · baza danych 5.0 (2026-08-28)_
