# 1. PODSTAWY PRAWNE ZASTOSOWANE W TYM RUNIE

Źródło: raport [12] FILTR PRAWNY (sekcja `podstawy_prawne` i `filtry_twarde`) oraz [02] DATA ENGINE.

**Akty i przepisy uruchomione jako twarde filtry decyzyjne:**

- Rozporządzenie (WE) nr 261/2004 – Art. 4 (wezwanie ochotników przed odmową boarding), Art. 7 (pełna stawka odszkodowania – zakaz ugód poniżej stawki, zobowiązanie UOKiK), Art. 8 ust. 1 lit. a (prawo do zwrotu lub zmiany planu podróży, próg 300 min), Art. 9 (opieka).
- Konwencja montrealska 1999 – Art. 19 i Art. 22 ust. 1 (odszkodowanie za opóźnienie – MC99_DELAY), Art. 17 i Art. 22 ust. 2 (bagaż – MC99_BAGGAGE).
- Rozporządzenie (WE) nr 2027/97 zmienione 889/2002 (REG_2027_97).
- Rozporządzenie (WE) nr 1107/2006, Art. 3, 4, 7, 8 (prawa osób niepełnosprawnych – PRM).
- Rozporządzenie (EWG) nr 95/93, Art. 8, 10 (sloty).
- Rozporządzenie (UE) nr 255/2010 + procedury EUROCONTROL NM (ATFM / CTOT).
- Rozporządzenie (WE) nr 1008/2008, Art. 13 (wet-lease).
- Ustawa z dnia 3.07.2002 – Prawo lotnicze, art. 205a–205c.
- Rozporządzenie (UE) nr 965/2012, CAT.OP.MPA.155 oraz ORO.CC.100 (limity FDP i wypoczynku – EASA_CAT_OP_MPA_155).
- Zasada Lokalna EPWA 1 (zatwierdzona przez Prezes ULC 04.10.2017), obowiązuje od 25.03.2018 (cisza nocna typu ban na lotnisku WAW).
- Ustawa o ochronie konkurencji i konsumentów, art. 24 (UOKiK) – przywołana dwukrotnie, w tym z powołaniem na decyzję zobowiązującą **RBG-1/2026**.

**Klasyfikacja kategorii EU261:** C (z raportu [12]).  
**Próg opieki z Art. 9:** 240 min (z raportu [12]).

**Sygnatura orzeczenia widniejąca w raporcie:** decyzja zobowiązująca UOKiK RBG-1/2026 – przywołana przy zakazie zaniżania odszkodowań z Art. 7 EU261.

# 2. OPCJE ODRZUCONE I REGUŁA, KTÓRA JE ODRZUCIŁA

Źródło: raport [12] FILTR PRAWNY (`werdykty`) oraz [16] LOG (`powod_odrzucenia`). Wpis w logu ma `dopuszczalna = 0`, więc odrzucenie jest twarde i ostateczne.

**Odrzucona przez filtr prawny – HOLD (pozycja końcowa: brak).**  
Reguły, które ją zabiły (oba warunki spełnione jednocześnie):

- **Art. 8 EU261** – 8 pasażerów zdjętych z rejsu bez zapewnienia dalszego przewozu ani zwrotu kosztu biletu.
- **Art. 4 EU261** – 8 pasażerów zdjętych wbrew woli bez uprzedniego wezwania ochotników (denied boarding w rozumieniu przepisu).

Filtr usuwa tę opcję, nigdy jej nie przecenia – gdyby odszkodowanie było pozycją kosztową, zdjęcie pasażerów wbrew woli stałoby się rozwiązaniem optymalnym kosztowo, co byłoby niezgodne z art. 4 i 8 EU261.

**Opcje dopuszczone, lecz odrzucone przez ranking decyzyjny** (nie przez filtr prawny – mają `dopuszczalna = 1`, więc usunięcie ma charakter decyzyjny, nie normatywny; zostają w logu dla celów dowodowych):

- SWAP-SP-LSA, SWAP-SP-LSE, REBOOK-OWN, REBOOK-OAL, OVERNIGHT, CANCEL, SPLIT – wszystkie odrzucone na etapie wyboru (pozycja końcowa 2–8 w logu), ponieważ ich wycena straty przekracza koszt wybranej opcji.

# 3. EKSPOZYCJA ODSZKODOWAWCZA – KWOTY I PROGI Z RAPORTU

Źródło: raport [12] (kategoria EU261, próg opieki, ostrzeżenia o art. 8 ust. 1 lit. a) oraz [14] i [16] (składniki kosztu wybranej opcji i widelki).

**Próg uprawniający do rezygnacji i żądania zwrotu:** 300 min – art. 8 ust. 1 lit. a EU261. Trzy opcje dopuszczone przez filtr prawny przekraczają ten próg i muszą być prezentowane pasażerowi jako dające prawo do zwrotu:

- REBOOK-OAL – opóźnienie 625 min (przekracza próg 300 min).
- OVERNIGHT – opóźnienie 840 min (przekracza próg 300 min).
- SPLIT – opóźnienie 625 min (przekracza próg 300 min).

**Próg opieki z Art. 9:** 240 min – przyjęty jako punkt odniesienia w raporcie [12].  
**Próg z Art. 7 EU261:** 180 min – przywołany w raporcie [14] przy opisie anomalii SWAP-SP-LSA i SWAP-SP-LSE (anomalia: zakładane oczekiwanie 139 min leży 41 min poniżej tego progu, a przesunięcie o 41 min dodałoby ok. 292 400,00 PLN kosztu).

**Kwoty dla wybranej opcji REBOOK-SPILL (karta wykonania w [16], uzasadnienie w [14]):**

- Strata oczekiwana: 3 820 120 (minor) = 38 201,20 PLN.
- Widelki – min: 3 550 221 = 35 502,21 PLN.
- Widelki – max: 5 896 272 = 58 962,72 PLN.
- Składniki kosztu (z [14]): odszkodowanie_art7 20 640,00 PLN; roszczenia_mc99 8 978,40 PLN; rebooking_wlasny_spill 7 826,00 PLN.

**Różnica wobec alternatywy SWAP-SP-LSA:** 16 291 384 minor = 162 913,84 PLN – jest to przewaga REBOOK-SPILL nad drugą w kolejności (wartość wprost z raportu [14]).

**Pełna kwota odszkodowania z Art. 7 jest nienaruszalna** – zakaz ugód poniżej stawki wynika z decyzji zobowiązującej UOKiK RBG-1/2026.

# 4. OBOWIĄZKI OPIEKI – CO I OD KTÓREJ MINUTY

Źródło: raport [12] FILTR PRAWNY (`filtry_twarde`, `prog_opieki`) oraz [02] DATA ENGINE (`operacje_w_ciszy_nocnej`, `rejsy_bez_numeru_handlowego`).

- **Art. 9 EU261 (opieka)** – aktywowany jako filtr twardy. Próg opieki w raporcie: 240 min. Z treści raportu nie wynika, od której konkretnej minuty lotu obowiązek opieki już zaistniał w tym zakłóceniu; wiadomo jedynie, że próg 240 min jest przyjętym punktem odniesienia dla tego runu. Brak danych w raporcie o godzinie startu opóźnienia, od której należy liczyć bieg opieki – powinien to ustalić node 04 (raport widoczny dla roli analityka zgodności).
- **Cisza nocna – Zasada Lokalna EPWA 1** – 43 operacje lotniskowe w oknie nocnym. Zgodnie z raportem [02] node 05 traktuje je jako istniejące, ale zabrania planowania na nich nowych operacji. Wykaz operacji (z [02]):
  - Wyloty z WAW: LO151 01:00, LO195 01:00, LO3803 01:10, LO3827 00:55, LO3849 00:45, LO3879 00:45.
  - Przyłoty do WAW: LO234 23:55, LO254 23:50, LO268 23:45, LO280 23:45, LO304 23:30, LO320 23:50, LO336 00:05, LO380 23:45, LO3860 00:25, LO3922 00:20, LO3936 00:25, LO3986 00:30.
  - Przyłoty do MUC: LO355 00:20.
  - Przyłoty do HAM: LO397 00:15.
  - Liczba operacji pominiętych w wykazie: 23.
- **Limity FDP i wypoczynku – CAT.OP.MPA.155 / ORO.CC.100 (Rozporządzenie 965/2012).** Status `zapas_fdp_bledow = 0` w raporcie [02], co oznacza, że w danych nie znaleziono naruszeń; pole `crew` ma jednak status ESTIMATED – skład

---

## Kontrola straznika liczb

sprawdzono 74 liczb, 21 spoza raportow, 2 zaokraglonych.

**Liczby, ktorych nie ma w raportach tego runu:**

- `300` -- ...o zwrotu lub zmiany planu podróży, próg [300] min),  (opieka). - Konwencja montreals...
- `1999` -- ...n),  (opieka). - Konwencja montrealska [1999] –  i  (odszkodowanie za opóźnienie –...
- `99` -- ...i  (odszkodowanie za opóźnienie – MC [99] _DELAY),  i  (bagaż – MC99_BAGGAGE). -...
- `2027` -- ...MC99_BAGGAGE). - Rozporządzenie (WE) nr [2027] /97 zmienione  (REG_2027_97). - Rozporz...
- `97` -- ...BAGGAGE). - Rozporządzenie (WE) nr 2027/ [97] zmienione  (REG_2027_97). - Rozporządz...
- `95` -- ...wnych – PRM). - Rozporządzenie (EWG) nr [95] /93, , 10 (sloty). - Rozporządzenie (UE...
- `93` -- ...ch – PRM). - Rozporządzenie (EWG) nr 95/ [93] , , 10 (sloty). - Rozporządzenie (UE) n...
- `205` -- ...Ustawa z dnia  – Prawo lotnicze, art. [205] a–205c. - Rozporządzenie (UE) nr , CAT....
- `155` -- ...- Rozporządzenie (UE) nr , CAT.OP.MPA. [155] oraz ORO.CC.100 (limity FDP i wypoczynk...
- `100` -- ...e (UE) nr , CAT.OP.MPA.155 oraz ORO.CC. [100] (limity FDP i wypoczynku – EASA_CAT_OP_...
- `24` -- ...chronie konkurencji i konsumentów, art. [24] (UOKiK) – przywołana dwukrotnie, w tym...
- `-1` -- ...owołaniem na decyzję zobowiązującą **RBG [-1] /2026**. **Klasyfikacja kategorii :**...
- `625` -- ...o do zwrotu: - REBOOK-OAL – opóźnienie [625] min (przekracza próg 300 min). - OVERNI...
- `840` -- ...próg 300 min). - OVERNIGHT – opóźnienie [840] min (przekracza próg 300 min). - SPLIT...
- `180` -- ...esienia w raporcie .  **Próg z  :** [180] min – przywołany w raporcie  przy opis...
- `139` -- ...SWAP- (anomalia: zakładane oczekiwanie [139] min leży 41 min poniżej tego progu, a p...
- `41` -- ...lia: zakładane oczekiwanie 139 min leży [41] min poniżej tego progu, a przesunięcie...
- `292 400,00` -- ...u, a przesunięcie o 41 min dodałoby ok. [292 400,00] PLN kosztu). **Kwoty dla wybranej opcj...
- `20 640,00` -- ...adniki kosztu (z ): odszkodowanie_art7 [20 640,00] PLN; roszczenia_mc99 8 978,40 PLN; rebo...
- `8 978,40` -- ...nie_art7 20 640,00 PLN; roszczenia_mc99 [8 978,40] PLN; rebooking_wlasny_spill 7 826,00 PL...
- `7 826,00` -- ...99 8 978,40 PLN; rebooking_wlasny_spill [7 826,00] PLN. **Różnica wobec alternatywy SWAP-...

Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku.

**Zaokraglone wzgledem raportu (dopuszczalne, warto sprawdzic):**

- `10` -- ...M). - Rozporządzenie (EWG) nr 95/93, , [10] (sloty). - Rozporządzenie (UE) nr  + p...
- `2026` -- ...łaniem na decyzję zobowiązującą **RBG-1/ [2026] **. **Klasyfikacja kategorii :** C (z...

_Zdjete przed skanem jako nieobliczeniowe -- akt prawny: 7, artykul: 19, godzina: 20, identyfikator node: 22, naglowek struktury: 4, numer rejsu: 20, rozporzadzenie EU261: 9, wersja: 3, znak rejestracyjny: 5._
