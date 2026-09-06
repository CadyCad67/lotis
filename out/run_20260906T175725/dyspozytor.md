# 1. SYTUACJA

Pytanie dotyczy overbookingu w klasie ekonomicznej na rejsie LO6 (WAW-JFK, sobota 2026-08-22). Jednak w raportach tego runu (`20260906T175725`) **brak jakichkolwiek danych o overbookingu, klasie rezerwacyjnej ani oblozeniu poszczegolnych kabin na LO6**. Raport 01 podaje jedynie ogolna liczbe pasazerow na rejsie (241) – bez rozbicia na klasy i bez informacji o sprzedanych biletach ponad pojemność. Raport 04 w ogole nie wspomina o overbookingu – wchodzi do silnika jako usterka techniczna z szacowanym opoznieniem 30 min.

Termin decyzji dla zaklocenia LO6: 2026-08-22 12:10:00 UTC (pozostalo w chwili wejscia do runu okolo 45 min wg raportu 04).

# 2. REKOMENDACJA

**Nie moge wydac rekomendacji**, bo zadna z 6 wycenionych opcji (HOLD, SWAP-SP-LSB, SWAP-SP-LSG, REBOOK-OAL, OVERNIGHT, CANCEL) nie odpowiada na overbooking. Silnik generowal opcje dla zaklocenia technicznego, nie dla nadprzedažy w kabinie. Raport 07 wprost wymienia odrzucone rodzaje: REBOOK-OWN (brak pozniejszego wlasnego rejsu WAW-JFK z wolnymi miejscami) i SPLIT (wylaczone przelacznikiem albo brak miejsc) – oba powiazane z brakiem miejsc, ale nie z overbookingiem jako zrodlem.

Raport 17 pokazuje, ze wybrano `HOLD` ze strata prognozowana 37149.50 PLN i rzeczywista 46740.70 PLN – ale to dotyczy obslugi opoznienia, nie overbookingu.

# 3. ALTERNATYWA

Brak w raporcie wariantu „dzialaj przy +20 pax w kabinie ekonomicznej”. Wowczas trzeba by uruchomic inny scenariusz niz ten, ktory silnik przeliczyl. Raporty nie zawieraja danych do wyceny takiej opcji – nie ma pojemnosci kabiny LO6 w zadnym raporcie, brak rozkladu klas rezerwacyjnych (manifest oznaczony jako synthetic, pewnosc 0.60).

# 4. CO MOZE TO WYWROCIC

- **Raporty nie obejmuja overbookingu** – pytanie wykracza poza zakres tego runu; node 04 (zaklocenie) wchodzi tylko z typem `TECHNICAL`, a nie `OVERSALE`.
- Manifest pasazerski w raporcie 01 ma pewnosc **0.60** (syntetyczny) – cokolwiek oparte na liczbie 20 pax to **zalozenie, nie fakt z raportu**.
- Pojemnosc kabiny B788 dla LO6 **brak w raportach** – nie wiem, czy 241 pax to overbooking (bo nie znam limitu miejsc), czy normlany load factor.
- Raport 05 (feasibility) wskazuje, ze SWAP na SP-LSB lub SP-LSG daje zmiane pojemnosci **+42 miejsca** – ale to informacja o wariancie na wypadek opoznienia, nie gotowa procedura na overbooking.
- Filtr prawny (12) wyrzucil REBOOK-OAL ze wzgledu na Art. 9 EU261 (oczekiwanie 925 min bez noclegu) – przy overbookingu moglby zadzialac ten sam filtr, jesli OAL wymusza dlugie oczekiwanie.

# 5. CZEGO SYSTEM NIE POLICZYL

- **Liczby pax w poszczegolnych klasach** na LO6 (Y, J itd.) – brak w raportach.
- **Pojemnosc kabiny LO6** (miejsca Y / J) dla B788 SP-LRG – brak w raportach.
- **Potwierdzenia faktycznego overbookingu +20** – zrodlem ma byc list pasazerski (PBP), ktorego system nie ma w tym runie.
- **Opcji typu „involuntary denied boarding”** (IDOB) wg regulaminu i Rozporzadzenia (WE) 261/2004 Art. 4 – generator scenariuszy w raporcie 07 nie wymienia takiej opcji.
- **Kosztow dobrowolnego zrzeczenia sie biletu (VDB)** – brak stawek w raportach.
- **Dostepnosci rezerwy kadrowej i maszynowej specjalnie pod overbooking** – raport 06 podaje tylko „wolne miejsca w WAW” bez wzgledu na konkretny rejs.

Decyzja o overbookingu wymaga ponownego uruchomienia silnika z wejsciem typu `OVERSALE` (lub weryfikacji licznika rezerwacji w PBP) – obecny run tego nie obsluzyl.

---

## Kontrola straznika liczb

sprawdzono 24 liczb, 3 spoza raportow.

**Liczby, ktorych nie ma w raportach tego runu:**

- `20` -- ...Brak w raporcie wariantu „dzialaj przy + [20] pax w kabinie ekonomicznej”. Wowczas tr...
- `42` -- ...AP na  lub  daje zmiane pojemnosci **+ [42] miejsca** – ale to informacja o warianc...
- `925` -- ...BOOK-OAL ze wzgledu na   (oczekiwanie [925] min bez noclegu) – przy overbookingu mo...

Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku.

_Zdjete przed skanem jako nieobliczeniowe -- akt prawny: 1, artykul: 2, data ISO: 2, identyfikator node: 1, identyfikator runu: 1, naglowek struktury: 5, numer rejsu: 7, rozporzadzenie EU261: 1, typ statku: 2, znak rejestracyjny: 5._
