# 1. SYTUACJA

Zaklocenie pasazerskie na rejsie **LO6 (WAW-JFK, B789, maszyna SP-LSC)**: 272 pasazerow na pokladzie, 30 nadsprzedanych rezerwacji, **8 osob ponad pojemnosc kabiny**. Szacowane opoznienie 0 min. Kod opoznienia 14 (nadsprzedaz). P(odszkodowania Art. 7 EU261) = 1.0.

- Snapshot: `sha256:6c790f69f87c359132b1de878467789b`, doba 2026-08-24 (poniedzialek)
- Termin decyzji: **2026-08-24T12:10:00+00:00** (czas odlotu LO6) - okno 45 min
- Brama samolot, port i miejsca przeszly; **brama zaloga odpadla** (11 osob z SP-LSC poza FDP, najgorszy zapas -485 min)
- Silnik liczyl w trybie FULL, ale **3 node'y weszly w tryb degraded**: 11 (ranking wstepny, ale ranking koncowy w 13 poprawny), 12 (filtr prawny odrzucil HOLD), 14 (kontrola AI wykryla anomalie). Decyzja stoi na kompletnym rankingu - to samo.

# 2. REKOMENDACJA

**REBOOK-SPILL** - przeniesienie 8 nadmiarowych pasazerow na wlasny rejs **LO26 (16:50 UTC, 19 wolnych miejsc)**, oczekiwanie 280 min.

- **Koszt oczekiwany: 38201.20 PLN**, widelki 35502.21 - 58962.72 PLN
- Najwieksze skladniki: odszkodowanie Art. 7 dla 8 pax = 20640.00 PLN; roszczenia MC99 = 8978.40 PLN; rebooking wlasny (spill) = 7826.00 PLN
- 8 pasazerow z przepisaniem na wlasny rejs (identyfikatory w karcie wykonania: PAX010317, 010352, 010363, 010367, 010455, 010460, 010461, 010500). Brak pax offloaded
- Przewaga nad druga opcja (SWAP-SP-LSA): **162913.84 PLN**
- Autoryzacja: Supervisor OCC (kwota w pasmie do 150000.00 PLN)
- Rejs LO6 odlatuje o czasie (12:10 UTC), brak propagacji na LO7 (bufor 0 min, 130 transferowych ale przy propagacji 0 min nie traci przesiadek)

# 3. ALTERNATYWA

**SWAP-SP-LSA** - podmiana maszyny (SP-LSC -> SP-LSA, B789).

- Strata: **201115.04 PLN**, widelki 186905.83 - 310416.69 PLN
- Roznica wobec rekomendacji: **+162913.84 PLN** (gorsza o ok. 5.3x)
- 130 transferowych traci przesiadki; minimalny postoj 139 min
- **Anomalia krytyczna**: oczekiwanie 139 min lezy 41 min ponizej progu 180 min z Art. 7. Przesuniecie o 41 min (np. drobne opoznienie na wylocie) dodaje ok. 292400.00 PLN kosztu - SWAP staje sie wtedy najdrozsza opcja obok rebookingu wlasnego. Pozycja SWAP w rankingu jest stabilna **tylko przy dotrzymaniu minimalnego postoju 139 min**.

# 4. CO MOZE TO WYWROCIC

- **Pewnosc manifestu 0.60** (syntetyczny): koszyki rezerwacyjne, ancillary, moment zakupu i rozklad FDP zalogi - kazde z tych pol wplywa na kwote odszkodowania i rebookingu; rozbieznosc moze przesunac straty w widelkach.
- **Zaloga rezerwowa (0.40)** - oszacowana z obsady bazy, brak rzeczywistego grafiku standby; gdyby zabraklo obsady dla LO26, spill staje sie niewykonalny.
- **Miejsca u partnera (0.40)** - obecnosc B6 w JFK nie jest potwierdzona; istotne przy ewakuacji do OAL.
- **MEL/ETOPS (0.40)** - 5 maszyn kandydatow do SWAP nie ma zweryfikowanego statusu technicznego; SWAP moze odpasc z bramy samolot w pozniejszej iteracji.
- **6 bledow ciaglosci rotacji** (LOWA-Z) + 3 przerwane rotacje - czesc odcinkow wypadla poza okno eksportu; moze znieksztalcic baze maszyn zapasowych i zalogi.
- **43 operacje w ciszy nocnej** - nie wolno na nich planowac; istotne jesli opoznienie LO6 rozleje sie na LO7.
- **Widelki REBOOK-SPILL: 35502.21 - 58962.72 PLN** (rozpietosc 23460.51 PLN). Gorny widelek przekracza 50000.00 PLN (granica roli Dyzurny OCC) - tu juz wymagany Supervisor OCC.
- **Anomalie w SWAP-SP-LSA i SWAP-SP-LSE**: prog 180 min, bufor tylko 41 min. Jakiekolwiek opoznienie rotacji powyzej 41 min od minimalnego postoju uruchamia Art. 7 dla wszystkich 272 pax i wywraca ranking.
- **Ostrzezenie w REBOOK-OAL/OVERNIGHT/SPLIT**: oczekiwanie 625-840 min przekracza prog 300 min - pasazerowie moga zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a); nie dotyczy rekomendacji.

# 5. CZEGO SYSTEM NIE POLICZYL

- **Rzeczywisty koszt operacji** (brak danych w raporcie - node 17 potwierdza). Porownanie prognozy z rzeczywistoscia opiera sie na opoznieniu (mediana 46 min z 6374 operacji), nie na fakturach. W tym incydencie odnotowano opoznienie rzeczywiste 46 min przy prognozie 0 min - model zakwalifikowal blad jako 0% (w szumie 5%), ale nie zweryfikowal, czy faktyczna ekspozycja Art. 7 zostala wyplacona.
- **Dostepnosci ochotnikow do rebookingu** (node 05/07 nie raportuje). System zaklada, ze 8 pax zostanie przepisanych na LO26, ale nie sprawdza preferencji pasazerow (polaczenia, klasy, status UMNR).
- **Rzeczywistego statusu technicznego 5 maszyn zapasowych** (MEL/ETOPS, pewnosc 0.40) - brak danych w raporcie, powinien liczyc node 05.
- **Grafiku standby zalogi** (pewnosc 0.40) - liczone z tabel FDP EASA, nie z grafiku operatora.
- **Potwierdzonej dostepnosci miejsc u B6 w JFK** (pewnosc 0.40) - obecnosc partnera tak, miejsca nie.
- **Ewentualnych oplat za zmiane slotu w WAW** (poziom 3, port koordynowany) - node 06 wskazuje SLOT jako sporny (1 szt), ale brak danych o koszcie jego przesuniecia w raporcie.
- **Strat wlasnych LO26** jesli 8 pax z LO6 zabierze miejsce pasazerom LO26 oczekujacym na ten rejs - node 10 pokazuje 19 wolnych miejsc, ale nie sprawdza, kto juz tam jest i czy nie powstana wtornie nadsprzedane.
- **Kosztu briefu zalogi i czasu pracy Crew Control** przy zmianach

---

## Kontrola straznika liczb

sprawdzono 88 liczb, 16 spoza raportow.

**Liczby, ktorych nie ma w raportach tego runu:**

- `280` -- ...UTC, 19 wolnych miejsc)**, oczekiwanie [280] min. - **Koszt oczekiwany: 38201.20 PL...
- `99` -- ...dla 8 pax = 20640.00 PLN; roszczenia MC [99] = 8978.40 PLN; rebooking wlasny (spill)...
- `010352` -- ...(identyfikatory w karcie wykonania: , [010352] , 010363, 010367, 010455, 010460, 010461...
- `010363` -- ...fikatory w karcie wykonania: , 010352, [010363] , 010367, 010455, 010460, 010461, 010500...
- `010367` -- ...w karcie wykonania: , 010352, 010363, [010367] , 010455, 010460, 010461, 010500). Brak...
- `010455` -- ...e wykonania: , 010352, 010363, 010367, [010455] , 010460, 010461, 010500). Brak pax offl...
- `010460` -- ...nia: , 010352, 010363, 010367, 010455, [010460] , 010461, 010500). Brak pax offloaded -...
- `010461` -- ...010352, 010363, 010367, 010455, 010460, [010461] , 010500). Brak pax offloaded - Przewaga...
- `010500` -- ...010363, 010367, 010455, 010460, 010461, [010500] ). Brak pax offloaded - Przewaga nad dru...
- `5.3` -- ...dacji: **+162913.84 PLN** (gorsza o ok. [5.3] x) - 130 transferowych traci przesiadki;...
- `41` -- ...a krytyczna**: oczekiwanie 139 min lezy [41] min ponizej progu 180 min z . Przesuni...
- `292400.00` -- ...robne opoznienie na wylocie) dodaje ok. [292400.00] PLN kosztu - SWAP staje sie wtedy najdr...
- `625` -- ...BOOK-OAL/OVERNIGHT/SPLIT**: oczekiwanie [625] -840 min przekracza prog 300 min - pasaz...
- `-840` -- ...K-OAL/OVERNIGHT/SPLIT**: oczekiwanie 625 [-840] min przekracza prog 300 min - pasazerow...
- `300` -- ...oczekiwanie 625-840 min przekracza prog [300] min - pasazerowie moga zrezygnowac i za...
- `6374` -- ...era sie na opoznieniu (mediana 46 min z [6374] operacji), nie na fakturach. W tym incy...

Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku.

_Zdjete przed skanem jako nieobliczeniowe -- artykul: 6, data ISO: 2, godzina: 2, identyfikator node: 5, identyfikator rekordu: 1, naglowek struktury: 5, numer rejsu: 12, odcisk snapshotu: 1, rozporzadzenie EU261: 1, typ statku: 2, znak rejestracyjny: 8._
