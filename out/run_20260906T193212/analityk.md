# Analiza kosztowa — LO6, 2026-08-24

## 1. STRUKTURA KOSZTU — składniki i ich udział

Wykonana opcja: **REBOOK-SPILL** (tryb MODIFYING). Koszt oczekiwany: **38 201,20 PLN**. Trzy pozycje składowe:

| Pozycja | Kwota (PLN) | Udział w koszcie | Tryb |
| --- | --- | --- | --- |
| odszkodowanie_art7 | 20 640,00 | 54,0% | MODIFYING |
| roszczenia_mc99 | 8 978,40 | 23,5% | MODIFYING |
| rebooking_wlasny_spill | 7 826,00 | 20,5% | MODIFYING |

Koszt w całości liczony jako różnica wobec sytuacji bez zakłócenia — nie ma tu przebudowy siatki, więc nie wchodzą pozycje typu `pozycjonowanie` (269 610,00 PLN), `rozliczenie_interline` (380 120,00–760 240,00 PLN) czy `opóźnienie_w_siatce` (96 958,06 PLN), które dominują w opcjach RESTRUCTURING.

Dla porządku — pozycje, których tu nie ma, ale decydują o wyniku w opcjach droższych:
- `odszkodowanie_art7` rośnie z 20 640,00 PLN (8 pax z odszkodowaniem w REBOOK-SPILL) do 701 760,00 PLN (272 pax w opcjach RESTRUCTURING) — 34-krotność.
- `pozycjonowanie` (269 610,00 PLN) i `rozliczenie_interline` (do 760 240,00 PLN w REBOOK-OAL) są widoczne tylko w trybie RESTRUCTURING, bo w MODIFYING są częścią baseline.

## 2. CO DECYDUJE O WYNIKU

O wyniku REBOOK-SPILL decyduje liczba pasazerów z odszkodowaniem Art. 7: **8**. To 8 osób z opóźnieniem ≥180 min (próg odszkodowania), które kwalifikują się do rekompensaty 2 580,00 PLN/os. Wszystkie pozostałe pozycje (`mc99`, `rebooking_wlasny_spill`) są z tej samej grupy 8 pax.

Porównanie z opcjami gorszymi:
- CANCEL, OVERNIGHT, SPLIT, REBOOK-OWN, REBOOK-OAL mają **272** pax z odszkodowaniem (pełny rejs), co winduje `odszkodowanie_art7` do 701 760,00 PLN.
- SWAP-SP-LSA / SWAP-SP-LSE nie generują odszkodowania (0 pax), ale ładują 96 958,06 PLN propagacji na LO7 (JFK→WAW) — 130 utraconych przesiadek, 139 min opóźnienia wtórnego.
- HOLD jest najtańsza (20 640,00 PLN), ale node 12 usuwa ją jako niedopuszczalną (Art. 8 i Art. 4 EU261).

Decydujący łańcuch: **próg 180 min → 8 vs 272 pax → 20 640,00 vs 701 760,00 PLN odszkodowania**. To jedna liczba (8 vs 272) różnicuje opcję rekomendowaną od najdroższej o czynnik ~46×.

## 3. NIEPEWNOŚĆ — widelki i ich źródło

Widelki REBOOK-SPILL pochodzą z rozkładu empirycznego 57 obserwacji na poziomie rejsu:
- min: **35 502,21 PLN**
- oczekiwany: **38 201,20 PLN**
- max: **58 962,72 PLN**
- rozpiętość: **23 460,51 PLN**

Źródło: kwantyle p25 = 33,00 min, mediana = 46,00 min, p90 = 121,00 min z rzeczywistych operacji tej siatki. Pewność widelek: 0,80 (real). Kurs EUR/PLN 4,3 — placeholder, pewność 0,50.

**Zachodzenie widelek (istotne dla ranking):**
- HOLD: 26 774,81–44 468,10 PLN
- REBOOK-SPILL: 35 502,21–58 962,72 PLN

Widelki HOLD i REBOOK-SPILL zachodzą się w przedziale 35 502,21–44 468,10 PLN. **Różnica między nimi nie jest istotna statystycznie** (ostrzeżenie node 11). Mimo to ranking daje REBOOK-SPILL pierwszeństwo, bo HOLD jest wykluczona prawnie (Art. 4/8 EU261) — o wyborze decyduje filtr prawny, nie koszt.

W pozostałych parach widelki nie zachodzą — SWAP-y (186 906–310 417 PLN), REBOOK-OWN (1 408 667–2 339 540 PLN) i dalej są wyraźnie droższe bez nakładania się.

Test wrażliwości: przy +30, +60 i +120 min lider pozostaje REBOOK-SPILL. Ranking jest stabilny w zadanym zakresie.

## 4. WPŁYW NA SIATKĘ — propagacja poza rejs źródłowy

Horyzont zatrzymany na `BASE_RETURN` — 1 odcinek poniżej, **LO7** (JFK→WAW, STD 23:40 UTC, bufor 0 min).

| Opcja | Suma propagacji (min) | Utracone przesiadki | Rejsów bez podstawienia | Koszt propagacji |
| --- | --- | --- | --- | --- |
| HOLD | 0 | 0 | 0 | 0,00 PLN |
| REBOOK-SPILL | 0 | 0 | 0 | 0,00 PLN |
| SWAP-SP-LSA | 139 | 130 | 0 | 96 958,06 PLN |
| SWAP-SP-LSE | 139 | 130 | 0 | 96 958,06 PLN |
| REBOOK-OWN | 0 | 130 | 1 | 243 595,00 PLN |
| OVERNIGHT | 0 | 130 | 1 | 243 595,00 PLN |
| CANCEL | 0 | 130 | 1 | 243 595,00 PLN |
| SPLIT | 0 | 130 | 1 | 243 595,00 PLN |
| REBOOK-OAL | 0 | 130 | 1 | 243 595,00 PLN |

Kluczowe: REBOOK-SPILL nie obciąża siatki — 0 min propagacji, 0 utraconych przesiadek. SWAP-y przesuwają rotację o 139 min i tracą 130 połączeń transferowych. Opcje RESTRUCTURING z przekładaniem/cancelowaniem mają 1 rejs bez podstawienia (LO7).

Poza LO7 horyzont się nie rozciąga — dalej opcje przestają się różnić.

## 5. ZAŁOŻENIA, KTÓRE TRZEBA ZWERYFIKOWAĆ

Poniższe pozycje oznaczyłam jako oparte na założeniach, nie na danych pewnych:

- **Kurs EUR/PLN = 4,3** (pewność 0,50) — placeholder, wymaga ustawienia w Konfiguracji. Wpływa na wartość odszkodowania 2 580,00 PLN/os (kategoria C EU261).
- **Stawki kosztowe K.care, K.reb, K.crew, K.grd, K.cxl, K.div, K.mc99** (pewność 0,60 każda) — policy estimates, nie zmierzone.
- **Manifest** (pewność 0,60): rozkład klas rezerwacyjnych, ancillary, moment zakupu — syntetyczny.
- **Załoga** (pewność 0,70): wyliczona z tabel EASA FDP, nie z grafiku operatora.
- **`ciaglosc_rotacji`, `fares`, `passengers`** oznaczone jako ESTIMATED — widelki rozszerzone w node 11.

Braki danych z raportów:
- 4 rejsy mają tylko znak wywoławczy (LOT2HP, LOT3AT, LOT7NB, LOT7PA) — node 02 nie rozstrzyga, czy to loty techniczne. Ekspozycja Art. 7 EU261 zależy od tego, czy niosą pasażerów (node 02 wskazuje: lot techniczny = 0 pasażerów = brak ekspozycji). Przy 4 takich rejsach w dobie, wpływ na ranking może być materialny, jeśli któryś jest handlowy — **brak danych w raporcie**, powinien rozstrzygnąć node źródłowy rozkładu.
- Odsetek ochotników przy odmowie przyjęcia (PoC) nie jest w bazie — opcje z offloadem liczone są ścieżką "wbrew woli", najdroższą. Raport tego nie waliduje.
- Rzeczywisty koszt operacji REBOOK-SPILL nie jest w żadnym źródle — node 17 porównuje prognozę z rzeczywistością tylko po opóźnieniu (46 min vs 0 min prognoza → klasyfikacja ZGODNY, błąd 0,0%). Faktury nie istnieją w tym przebiegu.

---

**Karta wykonania (z node 13):** REBOOK-SPILL — 8 pasażerów (PAX010317, PAX010352, PAX010363, PAX010367, PAX010455, PAX010460, PAX010461, PAX010500) przeniesionych na LO26 (odlot 16:50 UTC, oczekiwanie 280 min). Ważność karty: 2026-08-24T12:10:00+00:00. Rola autoryzująca: Supervisor OCC. Drugi podpis: nie wymagany.

---

## Kontrola straznika liczb

sprawdzono 128 liczb, 8 spoza raportow, 4 zaokraglonych.

**Liczby, ktorych nie ma w raportach tego runu:**

- `54,0` -- ...-- | | odszkodowanie_art7 | 20 640,00 | [54,0] % | MODIFYING | | roszczenia_mc99 | 8 97...
- `99` -- ...00 | 54,0% | MODIFYING | | roszczenia_mc [99] | 8 978,40 | 23,5% | MODIFYING | | rebo...
- `23,5` -- ...IFYING | | roszczenia_mc99 | 8 978,40 | [23,5] % | MODIFYING | | rebooking_wlasny_spill...
- `20,5` -- ...| | rebooking_wlasny_spill | 7 826,00 | [20,5] % | MODIFYING | Koszt w całości liczony...
- `34` -- ...PLN (272 pax w opcjach RESTRUCTURING) — [34] -krotność. - `pozycjonowanie` (269 610,0...
- `25` -- ...ć: **23 460,51 PLN** Źródło: kwantyle p [25] = 33,00 min, mediana = 46,00 min, p90 =...
- `90` -- ...p25 = 33,00 min, mediana = 46,00 min, p [90] = 121,00 min z rzeczywistych operacji t...
- `280` -- ...esionych na  (odlot  UTC, oczekiwanie [280] min). Ważność karty: . Rola autoryzują...

Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku.

**Zaokraglone wzgledem raportu (dopuszczalne, warto sprawdzic):**

- `186 906` -- ...h parach widelki nie zachodzą — SWAP-y ( [186 906] –310 417 PLN), REBOOK-OWN (1 408 667–2 3...
- `310 417` -- ...widelki nie zachodzą — SWAP-y (186 906– [310 417] PLN), REBOOK-OWN (1 408 667–2 339 540 P...
- `1 408 667` -- ...AP-y (186 906–310 417 PLN), REBOOK-OWN ( [1 408 667] –2 339 540 PLN) i dalej są wyraźnie droż...
- `2 339 540` -- ...906–310 417 PLN), REBOOK-OWN (1 408 667– [2 339 540] PLN) i dalej są wyraźnie droższe bez na...

_Zdjete przed skanem jako nieobliczeniowe -- artykul: 5, data ISO: 2, godzina: 2, identyfikator node: 7, identyfikator rekordu: 8, naglowek struktury: 5, numer rejsu: 10, rozporzadzenie EU261: 4, znak rejestracyjny: 4._
