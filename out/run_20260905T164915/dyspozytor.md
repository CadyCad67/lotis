## 1. SYTUACJA

**Status silnika: DEGRADOWANY** — run `20260905T164915` (snapshot `sha256:f3c290f4e6930407`) zostal przeliczony w trybie FULL, ale z polem `ciaglosc_rotacji` na ESTIMATED, co w raporcie 02 oznacza **czesciowy ranking**. Decyzja podjeta na tych danych wymaga dodatkowej ostroznosci.

- Do operacyjna: **piatek 2026-08-21** (horyzont do **2026-08-22 11:25 UTC**, rozpietosc **35.2 h**)
- **390 rejsow** na **86 rotacjach**, **94 maszyny**, **536 osob** zalogi, **32 911** pasazerow, **148** portow, **11** typow statkow
- Czas do decyzji OCC: brak danych w raporcie (nie wskazano terminu; deterministyczny run trwal **1787.24 ms** + walidacja **11.02 ms**)

Kontekst operacyjny do rozpatrzenia przez czlowieka:
- **6 rotacji** ma blad `ciaglosc_rotacji` (odlot przed przylotem poprzedniego odcinka): ROT-SP-LMD, ROT-SP-LMF, ROT-SP-LNG, ROT-SP-LNK, ROT-SP-LSG + ROT-SP-LSD/LSG — patrz szczegoly w raporcie 02
- **47 operacji** w oknie ciszy nocnej (20 wyswietlonych, **27 pominietych** w raporcie) — istniejace, ale nie wolno na nich planowac nowych
- **2 rejsy** (LOT3AD WAW→BOJ na SP-LVN, LOT7LP WAW→VAR na SP-LYL) — brak numeru handlowego, nie rozstrzygniete: techniczne czy handlowe z utraconym numerem
- **1 maszyna** z przerwanym lancuchem doby (okno eksportu, nie blad)

## 2. REKOMENDACJA

**Brak rekomendacji silnika w otrzymanych raportach.**

W raportach `01_snapshot` i `02_walidacja` **nie ma zadnej opcji decyzyjnej** ani rankingu opcji z kosztem. Silnik wykonal snapshot i walidacje 6 rodzin niezmiennikow — nie przedstawil propozycji dzialania. Jedyne co silnik przekazal to **ostrzezenia do weryfikacji przez czlowieka**:

1. 6 rotacji z naruszona kolejnoscia odlot/przylot — kandydaci do korekty rozkladu lub przebazowania
2. 47 operacji w ciszy nocnej — kandydaci do rozlozenia poza oknem zakazu lub do utrzymania jako wyjatek
3. 2 rejsy bez numeru handlowego — wymagaja potwierdzenia, czy maja podlegac regulom handlowym (Art. 7 EU261 — ekspozycja) czy traktowane jako techniczne (bez ekspozycji)

Koszt kazdej z tych akcji: **brak danych w raporcie** (powinien policzyc node planistyczny/finansowy — brak w runie).

## 3. ALTERNATYWA

Nie ma drugiej opcji w raportach — nie przedstawiono rowniez kosztu zaniechania (status quo vs. korekta). Material nie pozwala porownac wariantow.

## 4. CO MOZE TO WYWROCIC

- **Pole `ciaglosc_rotacji` = ESTIMATED** — node 11 rozszerza widelki, ale ranking jest czesciowy. Jakikolwiek wniosek o zmiane rotacji (np. ROT-SP-LMD, LMF, LNG, LNK, LSG) oparty na tej dobie jest niepewny.
- **`crew` = ESTIMATED** (0.70 z tabel FDP EASA, nie z grafiku operatora) — ogranicza wiarygodnosc wnioskow o obsadzeniu i FDP.
- **`passengers` = ESTIMATED** (0.60) — manifest syntetyczny; **2 rejsy techniczne (LOT3AD, LOT7LP) nie maja pasazerow**, wiec ekspozycja EU261 Art. 7 = 0, ale decyzja czy to faktycznie loty techniczne **nie jest rozstrzygnieta**.
- **`fares` = ESTIMATED** — kazda kalkulacja przychodu/ekspozycji finansowej na tych danych jest szacunkiem.
- **`manifest` syntetyczny** (4 oddzielne zalozenia po 0.60): udzialy klas, ancillary jako ulamek taryfy, moment zakupu skorelowany z elastycznoscia, FDP z tabel — zadna z tych warstw nie jest zrodlem operacyjnym.
- **6 bledow `ciaglosc_rotacji`** — jezeli ktorys z tych przypadkow to nie blad danych lecz faktyczny konflikt slot/operacyjny, skutki (opoznienia, AOG, koniecznosc przebazowania) nie sa w raporcie.
- **1 przerwany lancuch doby** — moze ukrywac kolejny rejs poza oknem eksportu, co znieksztalcilo by statystyki tego lotu.

## 5. CZEGO SYSTEM NIE POLICZYL

- Zadnej rekomendacji decyzyjnej ani rankingu opcji (brak nodu planistycznego/optimizera w runie).
- Kosztu korekty kazdej z 6 rotacji z bledem `ciaglosc_rotacji`.
- Kosztu przesuniecia 47 operacji poza okno ciszy nocnej (albo kosztu ich utrzymania).
- Skutkow finansowych i ekspozycji EU261 Art. 7 dla 32 911 pasazerow na dobe 2026-08-21.
- Obsadzenia konkretnymi ludzmi (brak importu z grafiku operatora — tylko FDP z tabel).
- Tozsamosci 2 rejsow bez numeru handlowego (LOT3AD, LOT7LP) — czy techniczne, czy handlowe.
- Delty wplywu na hub WAW, gdzie skupia sie wiekszosc nocnych przylotow/wylotow (360 operacji w WAW vs. 27 w KRK — patrz raport 01).

**Podsumowanie dla OCC:** run dostarcza stanu i walidacji, ale **nie dostarcza materialu do podjecia decyzji**. Zanim ktokolwiek podpisze zmiane rozkladu/rotacji, potrzebny jest run z nodem planistycznym i/lub importerem grafiku zalogi — w przeciwnym razie decyzja bedzie oparta na czesciowym rankingu (pole `ciaglosc_rotacji` ESTIMATED) i syntetycznym manifescie.

---

## Kontrola straznika liczb

sprawdzono 39 liczb, 1 spoza raportow.

**Liczby, ktorych nie ma w raportach tego runu:**

- `20` -- ...- **47 operacji** w oknie ciszy nocnej ( [20] wyswietlonych, **27 pominietych** w rap...

Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku.

_Zdjete przed skanem jako nieobliczeniowe -- artykul: 3, data ISO: 3, identyfikator node: 1, identyfikator runu: 1, naglowek struktury: 5, numer rejsu: 6, numeracja listy: 3, odcisk snapshotu: 1, rozporzadzenie EU261: 3, znak rejestracyjny: 9._
