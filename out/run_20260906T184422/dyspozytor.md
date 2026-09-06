# 1. SYTUACJA

**Co się stało:** Usterka techniczna (kod 41, grupa Techniczne) na rejsie LO35 WAW-SFO (B789, SP-LSE), 256 pasażerów, szacowane opóźnienie **0 min** w momencie zgłoszenia. Klasa kodu `c`, p(odszkodowania) = **1.0**.

**Snapshot:** sha256:d7806668b46167a39f400ef7880d14c4 (zamrożona niedziela 2026-08-23: 371 rejsów, 87 rotacji, 31 966 pasażerów).

**Czas do decyzji:** termin **2026-08-23T11:00:00+00:00** — okno **45 min**.

**Tryb obliczeń:** FULL — ale raporty [01], [10], [12], [14] weszły w status **degraded**. **Silnik zszedł po drabinie degradacji** (manifest/crew/passengers/fares oznaczone ESTIMATED, bramka załogi i miejsc odpadły). Decyzja wymaga dodatkowej ostrożności.

**Ostrzeżenie po wykonaniu:** [17] pokazuje, że rejs faktycznie poleciał z opóźnieniem **53 min** (mediana z 6374 operacji). To jest **powyżej progu opieki 240 min? Nie — 53 min poniżej**, ale powyżej progu odszkodowania 180 min. Dane o kosztach rzeczywistych nie istnieją w źródłach — brak danych w raporcie (node 17 sygnalizuje ten brak).

# 2. REKOMENDACJA

**Opcja: HOLD** — wstrzymaj odlot o **0 min** (bez zmian operacyjnych).

**Koszt / strata (z [11] i [13]):** **0.00 PLN**
- revenue at risk: **0.00 PLN**
- koszty bezpośrednie: **0.00 PLN**
- propagacja sieciowa: **0.00 PLN**
- widelki: min **0.00 PLN** / max **0.00 PLN**

**Dlaczego ta:**
- W bramce feasibility [05] odpadły SWAP/REBOOK-OWN — brak zgodnej załogi (11 osób przekracza FDP, najgorszy zapas **-710 min**) i brak wolnych miejsc na WAW-SFO.
- Filtr prawny [12] odrzucił wszystkie 3 SWAP (Art. 8 + Art. 4: 4 pasażerów zdejmowanych wbrew woli) oraz REBOOK-OAL (Art. 9: oczekiwanie **925 min** bez noclegu, przekracza próg **240 min**).
- Ranking końcowy [13] ma tylko 3 dopuszczalne opcje: HOLD, OVERNIGHT, CANCEL. HOLD wygrywa.
- **OVERNIGHT i CANCEL niosą ostrzeżenie** — opóźnienie docelowe 840 min przekracza próg 300 min z Art. 8 ust. 1 lit. a (pasażer może zrezygnować i żądać zwrotu).

**Autoryzacja [15]:** OCC-DUTY ACCEPT, rola **Dyzurny OCC**, drugi podpis **nie**, kwota **0.00 PLN** — mieści się w paśmie do 50 000.00 PLN.

# 3. ALTERNATYWA

**Następna opcja: OVERNIGHT** (pozycja 2 w [13]).

**Różnica wobec rekomendowanej:**
- Strata: **1 373 062.46 PLN** (vs 0.00 PLN dla HOLD).
- Widelki: min **1 308 295.37 PLN** / max **2 132 996.40 PLN** — szerokie widelki (ostrzeżenie polityki).
- Powód wzrostu kosztu: nocleg + posiłki + transport dla 256 pasażerów, pełna ekspozycja EU261 przy klasie kodu przewoźnika.

**Inne dopuszczalne (pozycja 3):** CANCEL — strata **1 784 680.71 PLN**, widelki min/max **1 700 497.66 / 2 772 428.52 PLN**.

# 4. CO MOŻE TO WYWRÓCIĆ

- **Drabina degradacji aktywna.** Pola `crew`, `passengers`, `fares`, `ciaglosc_rotacji` oznaczone **ESTIMATED** (pewność **0.60** dla manifestu, **0.40** dla załogi rezerwowej i MEL/ETOPS). Załoga w [05] to synteza z tabel FDP EASA, nie z grafiku operatora.
- **Brak biezacego statusu technicznego floty** — założenie `MEL i ETOPS` ma pewność **0.40**. Jeśli SP-LSE ma aktywne MEL ograniczające ETOPS, opóźnienie 0 min może być nierealistyczne.
- **Szacowane opóźnienie 0 min przy pewności 0.50** — wartość podana przy zgłoszeniu, niezmierzona. Rzeczywiste opóźnienie wyniosło **53 min** ([17], pewność 0.90). Przy +41 min względem progu 180 min, SWAP-y z odcinkiem 139 min zbliżyłyby się do progu odszkodowania Art. 7 — anomalie [14] sygnalizują, że przesunięcie o 41 min dodałoby ok. **275 200.00 PLN** kosztu (nie wchodzi do widelek rekomendacji).
- **7 operacji w oknie ciszy nocnej typu ban** z rotacji, której dotyczy zakłócenie — rejs z nią powiązany (LO36, LO24) ma ten sam problem ciągłości co LO35. Brak własnego rejsu WAW-SFO z wolnymi miejscami [05] — nie ma planu B w sieci.
- **SLOT@WAW sporny** (1 szt, port koordynowany poziom 3) — jeśli równolegle inna operacja potrzebuje tego samego slotu, wykonanie HOLD może być zablokowane.
- **Symulacja nadsprzedaży: +63 rezerwacji ponad manifest snapshotu** — poza modelem; wpływa na realną liczbę dotkniętych pasażerów i ekspozycję EU261.
- **Filtr prawny nie dopuszcza kompensacji pieniężnej zamiast opieki** — zaniżanie odszkodowań było przedmiotem decyzji zobowiązującej UOKiK RBG-1/2026. Nie wolno „optymalizować" przez obniżkę Art. 7.
- **Anomalie [14]:** strata HOLD bliska zeru mimo 256 dotkniętych pasażerów — opcja dotyka pasażerów, a nie ma żadnego składnika kosztu. To efekt bramki załogi (odpadła) i miejsc (odpadła) — nie pozostały żadne pozycje kosztowe do naliczenia, co jest zgodne z modelem, ale może budzić wątpliwości przy podpisie.

# 5. CZEGO SYSTEM NIE POLICZYŁ

- **Rzeczywisty koszt operacji dla porównania z prognozą** — [17] sygnalizuje brak danych; opiera się tylko na opóźnieniu, nie na fakturach. Węzeł, który powinien to policzyć: brak — po stronie integracji z systemem finansowym.
- **Grafik standby załogi rezerwowej** (założenie derived, pewność **0.40**) — nie ma źródła; węzeł odpowiedzialny: brak po stronie systemu, wymaga potwierdzenia przez Crew Control.
- **Potwierdzona dostępność miejsc u partnerów OAL w SFO** (założenie derived, pewn

---

## Kontrola straznika liczb

sprawdzono 62 liczb, 7 spoza raportow, 1 zaokraglonych.

**Liczby, ktorych nie ma w raportach tego runu:**

- `6374` -- ...iał z opóźnieniem **53 min** (mediana z [6374] operacji). To jest **powyżej progu opie...
- `925` -- ...woli) oraz REBOOK-OAL ( : oczekiwanie ** [925] min** bez noclegu, przekracza próg **24...
- `840` -- ...osą ostrzeżenie** — opóźnienie docelowe [840] min przekracza próg 300 min z  lit. a...
- `300` -- ...nienie docelowe 840 min przekracza próg [300] min z  lit. a (pasażer może zrezygnowa...
- `275 200.00` -- ...że przesunięcie o 41 min dodałoby ok. ** [275 200.00] PLN** kosztu (nie wchodzi do widelek re...
- `63` -- ...blokowane. - **Symulacja nadsprzedaży: + [63] rezerwacji ponad manifest snapshotu** —...
- `-1` -- ...dmiotem decyzji zobowiązującej UOKiK RBG [-1] /2026. Nie wolno „optymalizować" przez o...

Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku.

**Zaokraglone wzgledem raportu (dopuszczalne, warto sprawdzic):**

- `2026` -- ...otem decyzji zobowiązującej UOKiK RBG-1/ [2026] . Nie wolno „optymalizować" przez obniżk...

_Zdjete przed skanem jako nieobliczeniowe -- artykul: 6, data ISO: 2, identyfikator node: 19, naglowek struktury: 5, numer rejsu: 4, odcisk snapshotu: 1, rozporzadzenie EU261: 2, typ statku: 1, znak rejestracyjny: 2._
