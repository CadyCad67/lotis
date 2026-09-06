# 1. SYTUACJA

**Co się stało.** Rejs LO6 (WAW-JFK, B788, maszyna SP-LRG, 241 pasażerów). Zgłoszona usterka techniczna (kod 41, grupa "Techniczne"), szacowane opóźnienie 120 min. Oryginalny STD: 12:10 UTC. Klasa opóźnienia `c`, p(odszkodowania) = 1.00.

**Tryb obliczeń:** FULL, ale z degradacją (szczegóły poniżej). Ranking 5 opcji dopuszczalnych prawnie (REBOOK-OAL odrzucony przez Art. 9 EU261 — oczekiwanie 925 min bez zapewnionego noclegu).

**Okno decyzji:** 45 min od wejścia (decyzja wymaga podpisu do ok. 12:10 UTC w dniu operacji 2026-08-22).

**Degradacja, która wymaga uwagi:**
- Node 01: status `degraded` — 3 maszyny z przerwanym łańcuchem doby (okno eksportu, nie błąd).
- Node 05: 35 operacji w oknie ciszy nocnej typu 1; nie dotyczy LO6.
- Node 06: SLOT@WAW sporny (poziom 3, port koordynowany).
- Node 11/13/14: status `degraded` — silnik zszedł po drabinie degradacji, ranking wstępny częściowy (szczegóły w sekcji 4).
- Node 15b: **wykonanie nie powiodło się** na kroku `nowy_slot` — EUROCONTROL nie potwierdził wystąpienia o nowe okno startowe. To znacza, że **rekomendacja HOLD nie została fizycznie zrealizowana** w tym runie.
- Node 17: wynik rzeczywisty (z innego wykonania) — opóźnienie faktyczne 46 min zamiast 120 min; strata rzeczywista 104238.70 PLN vs prognoza 148598.00 PLN; błąd -29.85% POZA widelkami. Rodzaj: BLAD_WYKONANIA (nie obciąża modelu).

# 2. REKOMENDACJA

**Opcja: HOLD** (Wstrzymaj odlot o 120 min).

- **Strata (oczekiwana):** 148598.00 PLN
- **Widelki:** 138099.23 PLN (min) – 229357.78 PLN (max)
- **Składniki kosztu (z node 09):** opóźnienie w siatce 71934.00 PLN + załoga 4730.00 PLN + propagacja 71934.00 PLN (node 10).
- **Co zmienia w operacji:** LO6 odlatuje 120 min później (z 12:10 UTC). 0 pasażerów zdjętych. Załoga LO6 pozostaje na służbie +120 min — wymaga sprawdzenia FDP przed odlotem.
- **Dlaczego ta:** najniższa strata w całym badanym zakresie do +120 min (node 13). HOLD pozostaje najlepsza opcją; opcja domyślna to też HOLD, więc oszczędność = 0.00 PLN.
- **Wykonanie:** według node 15b krok `nowy_slot` nie został potwierdzony przez Slot Coordination / EUROCONTROL — rekomendacja nie została wykonana w tym runie.
- **Autoryzacja:** Duty Manager OCC, drugi podpis wymagany. Kwota 229357.78 PLN (górna widełka) mieści się w paśmie roli.

# 3. ALTERNATYWA

**Następna opcja w rankingu: SWAP-SP-LSB** (podmiana maszyny na SP-LSB, B789).

- **Strata:** 235689.22 PLN (o 87091.22 PLN więcej niż HOLD).
- **Widelki:** 219037.27 PLN – 363781.18 PLN.
- **Różnica wobec rekomendowanej:** SWAP daje +42 miejsca pojemności, ale:
  - propagacja 136 min (vs 120 min dla HOLD) — opóźnienie przenosi się na rejs LO79,
  - 114 przesiadek utraconych (vs 0 przy HOLD — przy HOLD pasażerowie dojeżdżają na ten sam rejs, przesiadki w horyzoncie propagacji nie są liczone jako utracone, bo rejs LO7-WAW wraca zgodnie z rotacją),
  - bramka załoga/miejsca przy oryginalnym LO6 już odpadły (11 osób przekracza FDP, brak późniejszego własnego rejsu WAW-JFK) — SWAP korzysta z maszyny zapasowej, ale załoga i tak wymaga sprawdzenia FDP,
  - koszt propagacji 81525.20 PLN vs 71934.00 PLN.
- **Anomalia (node 14):** opóźnienie 136 min leży 44 min poniżej progu 180 min z Art. 7 — przesunięcie o ten margines dodałoby ~259075.00 PLN kosztu. Węzły SWAP są kruche.

Kolejne pozycje: SWAP-SP-LSG (244517.32 PLN, pozycja 3), OVERNIGHT (1492964.88 PLN, pozycja 4), CANCEL (1785988.59 PLN, pozycja 5).

# 4. CO MOŻE TO WYWRÓCIĆ

**Braki danych / niska pewność:**
- `opoznienie_szacowane` 120 min — pewność 0.50 (wartość ze zgłoszenia, nie zmierzona). Rzeczywista mediana opóźnienia dla tej klasy zakłóceń w node 17 wyniosła 46 min (z 6374 operacji).
- `crew`, `passengers`, `fares` — ESTIMATED (node 01/02). Pole `ciaglosc_rotacji` liczone jako ESTIMATED.
- `zaloga_rezerwowa` 21 osób — derived, pewność 0.40 (brak grafiku standby w źródłach).
- `PARTNER_SEATS@JFK` (B6 JetBlue) — obecność partnera w porcie, nie potwierdzona dostępność miejsc; pewność 0.40.
- `MEL i ETOPS` — brak bieżącego statusu technicznego floty; pewność 0.40.
- Manifest pasażerski: rozkład klas rezerwacyjnych, ancillary, moment zakupu — wszystko synthetic, pewność 0.60.

**Ostrzeżenia i degradacje:**
- Node 02: 5 błędów ciągłości rotacji (ROT-SP-LRC, ROT-SP-LRD, ROT-SP-LSD, ROT-SP-LSF, ROT-SP-LYA) — odlot przed przylotem poprzedniego odcinka. Wśród nich ROT-SP-LYA (LO195/LO190 TAS-NQZ) dotyczy rotacji, w której uczestniczy jedna z operacji ciszy nocnej (LO195 wylot WAW 01:00 czasu lokalnego). To nie jest rejs LO6, ale wpływa na ranking, jeśli model propagacji uwzględnia sąsiednie łańcuchy.
- Node 02: 35 operacji w oknie ciszy nocnej (nie dotyczy LO6 bezpośrednio).
- Node 12: OVERNIGHT i CANCEL mają ostrzeżenie — opóźnienie 840 min przekracza próg 300 min z Art. 8 ust. 1 lit. a (prawo do rezygnacji i żądania zwrotu).
- Node 15b: wykonanie nie powiodło się — `nowy_slot` nie potwierdzony przez EUROCONTROL.
- Node 17: błąd -29.85% w rzeczywistości; klasyfikacja BLAD_WYKONANIA; model nie jest kalibrowany tym przypadkiem; tłumienie 0.20. Widelki prognozy były

---

## Kontrola straznika liczb

sprawdzono 82 liczb, 6 spoza raportow.

**Liczby, ktorych nie ma w raportach tego runu:**

- `925` -- ...K-OAL odrzucony przez   — oczekiwanie [925] min bez zapewnionego noclegu). **Okno...
- `42` -- ...nica wobec rekomendowanej:** SWAP daje + [42] miejsca pojemności, ale:  - propagacja...
- `44` -- ...Anomalia ( ):** opóźnienie 136 min leży [44] min poniżej progu 180 min z  — przesun...
- `259075.00` -- ...— przesunięcie o ten margines dodałoby ~ [259075.00] PLN kosztu. Węzły SWAP są kruche. Kole...
- `6374` -- ...j klasy zakłóceń w  wyniosła 46 min (z [6374] operacji). - `crew`, `passengers`, `far...
- `300` -- ...ie — opóźnienie 840 min przekracza próg [300] min z  lit. a (prawo do rezygnacji i ż...

Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku.

_Zdjete przed skanem jako nieobliczeniowe -- artykul: 3, data ISO: 1, godzina: 4, identyfikator node: 7, naglowek struktury: 4, numer rejsu: 12, rozporzadzenie EU261: 1, typ statku: 2, znak rejestracyjny: 10._
