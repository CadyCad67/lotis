# Analiza kosztowa — rejs LO6 / OVERNIGHT — run 20260906T191942

## 1. STRUKTURA KOSZTU — składniki i ich udział

Silnik wycenił 6 opcji. W tabeli poniżej rozbicie kosztów (bez propagacji sieciowej i revenue_at_risk, które node 11 dolicza osobno). Tryb liczenia różni się — MODIFYING liczy różnicę wobec sytuacji bez zakłócenia, RESTRUCTURING liczy pełny nowy zestaw kosztów. To oznacza, że porównywanie kwot nominalnych HOLD vs SWAP bez trybu jest mylące.

| Opcja | Tryb | Koszt całkowity (PLN) | Główne składniki (kwota / pozycja) |
|---|---|---:|---|
| HOLD | MODIFYING | 27 339.13 | 18 060.00 odmowa_przyjecia_art4; 8 490.80 opoznienie_w_siatce; 788.33 zaloga |
| SWAP-SP-LRF | RESTRUCTURING | 97 096.67 | 90 016.00 opoznienie_w_siatce; 7 080.67 zaloga |
| SWAP-SP-LSC | RESTRUCTURING | 80 339.42 | 91 405.40 opoznienie_w_siatce; 7 080.67 zaloga; −18 146.65 roznica_kosztu_typu |
| OVERNIGHT | RESTRUCTURING | 1 253 880.90 | 624 360.00 odszkodowanie_art7; 269 610.00 pozycjonowanie; 236 736.50 rebooking_wlasny_spill |
| CANCEL | MODIFYING | 1 023 594.40 | 624 360.00 odszkodowanie_art7; 269 610.00 pozycjonowanie; 110 693.22 opieka_art9 |
| REBOOK-OAL | RESTRUCTURING | 1 601 240.88 | 676 390.00 rozliczenie_interline; 624 360.00 odszkodowanie_art7; 269 610.00 pozycjonowanie |

Udział procentowy największego składnika w kazdej opcji (liczony wprost z powyższych wartości):

- HOLD: 66.1% (odmowa_przyjecia_art4)
- SWAP-SP-LRF: 92.7% (opoznienie_w_siatce)
- SWAP-SP-LSC: 113.8% (opoznienie_w_siatce) — sam ten składnik przekracza sumę, co oznacza, że ujemna korekta roznica_kosztu_typu (−18 146.65) kompensuje nadmiar
- OVERNIGHT: 49.8% (odszkodowanie_art7)
- CANCEL: 61.0% (odszkodowanie_art7)
- REBOOK-OAL: 42.2% (rozliczenie_interline)

Parametry wejściowe EU261: kategoria C, odszkodowanie 2 580.00 PLN na pasażera, próg opieki 240 min, próg odszkodowania 180 min, p(odszkodowanie) = 1.0, kurs EUR/PLN = 4.3.

## 2. CO DECYDUJE O WYNIKU

Dwie grupy opcji determinują zupełnie różne składniki:

- **Opcje niskokosztowe (HOLD, SWAP-*)** — o wyniku decyduje opóźnienie w siatce (opoznienie_w_siatce) oraz odmowa przyjęcia art. 4. Żadna z tych opcji nie uruchamia odszkodowania art. 7 (pasazerow_z_odszkodowaniem = 0). Noclegów: 0.
- **Opcje wysokokosztowe (OVERNIGHT, CANCEL, REBOOK-OAL)** — o wyniku decyduje odszkodowanie art. 7 (624 360.00 PLN we wszystkich trzech) plus pozycjonowanie (269 610.00 PLN) i składnik właściwy dla trybu: nocleg i rebooking (OVERNIGHT), opieka art. 9 (CANCEL), rozliczenie interline (REBOOK-OAL). Pasazerow_z_odszkodowaniem = 242, noclegów = 242 w tych trzech.

Tryb liczenia silnie zaburza porównywalność: SWAP-SP-LRF (RESTRUCTURING, 97 096.67) i CANCEL (MODIFYING, 1 023 594.40) nie mogą być porównywane nominalnie — różnica ok. 10× wynika głównie z konwencji liczenia, nie z natury zakłócenia. Ranking straty z node 11 (HOLD = 38 377.09 vs REBOOK-OAL = 1 844 835.88) wprowadza dodatkowo revenue_at_risk i propagację, więc pozycje w nim są inne niż w surowym koszcie.

## 3. NIEPEWNOŚĆ — widelki i ich źródło

Źródło widelek: kwantyle p25/mediana/p90 z 57 obserwacji na poziomie rejsu; p25 = 33.00, mediana = 46.00, p90 = 121.00, punktualność15 = 0.00. Pewność widelek: 0.80 (real).

Widelki straty z node 11 (PLN):

| Opcja | strata | widelki_min | widelki_max | rozpiętość |
|---|---:|---:|---:|---:|
| HOLD | 38 377.09 | 35 665.67 | 59 234.20 | 23 568.53 |
| SWAP-SP-LSC | 161 864.62 | 150 428.54 | 249 834.52 | 99 405.98 |
| SWAP-SP-LRF | 178 621.87 | 166 001.85 | 275 698.97 | 109 697.12 |
| OVERNIGHT | 1 497 475.90 | 1 391 675.98 | 2 311 321.49 | 919 645.51 |
| CANCEL | 1 692 924.21 | 1 573 315.44 | 2 612 991.71 | 1 039 676.27 |

Obserwacje:

- Widelki SWAP-SP-LSC i SWAP-SP-LRF zachodzą na siebie (obie strony mają widełki w okolicach 150–280 tys. PLN). Różnica między nimi (16 757.25 PLN w korzyść SWAP-SP-LSC) jest mniejsza niż rozpiętość każdej z widełek z osobna — różnica nie jest istotna statystycznie przy tych widełkach.
- Widelki OVERNIGHT i CANCEL również zachodzą na siebie (1 391 675.98–2 311 321.49 vs 1 573 315.44–2 612 991.71). Różnica między nimi (195 448.31 PLN w korzyść OVERNIGHT) jest wielokrotnie mniejsza niż rozpiętości widełek — rozróżnienie tych dwóch opcji przy tych widełkach nie jest istotne.
- HOLD jest jedyną opcją z wąskimi widełkami (rozpiętość 23 568.53 PLN) i jest rzędu wielkości niżej niż wszystkie pozostałe — ta przewaga jest istotna.
- Współczynnik dolny 0.93 i górny 1.54 z node 11 opisują skalę rozstrzału względem wartości centralnej; 1.54 oznacza, że górne widelki niektórych opcji są o ponad 50% powyżej mediany.

Dodatkowo, rzeczywisty koszt operacji nie jest dostępny w żadnym źródle (node 17 sygnalizuje brak — porównanie opiera się na opóźnieniu, nie na fakturach). Stawki K.care/K.reb/K.crew/K.grd/K.cxl/K.div/K.mc99 mają pewność 0.60 (policy, estimate); kurs EUR/PLN ma pewność 0.50 (placeholder). To poszerza rzeczywisty rozstrzał ponad to, co pokazują widelki.

## 4. WPŁYW NA SIATKĘ — propagacja poza rejs źródłowy

Horyzont propagacji: 1 odcinek, zatrzymany na BASE_RETURN (koniec doby operacyjnej 2026-08-22T02:00:00+00:00). Jeden rejs poniżej progu: LO7 JFK→WAW, STD 2026-08-21T23:40:00+00:00, bufor 0 min. Pasażerów transferowych na rejsie źródłowym: 99. Zalogi poza FDP: 11.

Propagacja wg opcji (koszt_propagacji, przesiadki utracone, suma_propagacji_min):

| Opcja | odcinki poniżej | suma_prop. min | przesiadki utracone | koszt_propagacji (PLN) | rejsów bez podstawienia |
|---|---:|---:|---:|---:|---:|
| HOLD | 1 | 20 | 0 | 8 490.80 | 0 |
| SWAP-SP-LRF | 1 | 136 | 99 | 81 525.20 | 0 |
| SWAP-SP-LSC | 1 | 136 | 99 | 81 525.20 | 0 |
| REBOOK-OAL | 1 | 0 | 99 | 243 595.00 | 1 |
| OVERNIGHT | 1 | 0 | 99 | 243 595.00 | 1 |
| CANCEL | 1 | 0 | 99 | 243 595.00 | 1 |

Uwagi:

- Propagacja mierzona poza rejsem źródłowym zamyka się na LO7 i na 99 pasażerach transferowych — to

---

## Kontrola straznika liczb

sprawdzono 141 liczb, 15 spoza raportow, 2 zaokraglonych.

**Liczby, ktorych nie ma w raportach tego runu:**

- `18 146.65` -- ...opoznienie_w_siatce; 7 080.67 zaloga; − [18 146.65] roznica_kosztu_typu | | OVERNIGHT | RES...
- `7` -- ...53 880.90 | 624 360.00 odszkodowanie_art [7] ; 269 610.00 pozycjonowanie; 236 736.50...
- `66.1` -- ...wprost z powyższych wartości): - HOLD: [66.1] % (odmowa_przyjecia_art4) - SWAP- : 92.7...
- `92.7` -- ...66.1% (odmowa_przyjecia_art4) - SWAP- : [92.7] % (opoznienie_w_siatce) - SWAP- : 113.8%...
- `113.8` -- ...: 92.7% (opoznienie_w_siatce) - SWAP- : [113.8] % (opoznienie_w_siatce) — sam ten składn...
- `49.8` -- ...146.65) kompensuje nadmiar - OVERNIGHT: [49.8] % (odszkodowanie_art7) - CANCEL: 61.0% (...
- `61.0` -- ...T: 49.8% (odszkodowanie_art7) - CANCEL: [61.0] % (odszkodowanie_art7) - REBOOK-OAL: 42....
- `42.2` -- ...1.0% (odszkodowanie_art7) - REBOOK-OAL: [42.2] % (rozliczenie_interline) Parametry wej...
- `25` -- ...i ich źródło Źródło widelek: kwantyle p [25] /mediana/p90 z 57 obserwacji na poziomie...
- `90` -- ...Źródło widelek: kwantyle p25/mediana/p [90] z 57 obserwacji na poziomie rejsu; p25...
- `15` -- ...iana = 46.00, p90 = 121.00, punktualność [15] = 0.00. Pewność widelek: 0.80 (real)....
- `150` -- ...e (obie strony mają widełki w okolicach [150] –280 tys. PLN). Różnica między nimi (16...
- `280` -- ...bie strony mają widełki w okolicach 150– [280] tys. PLN). Różnica między nimi (16 757....
- `195 448.31` -- ....44–2 612 991.71). Różnica między nimi ( [195 448.31] PLN w korzyść OVERNIGHT) jest wielokrot...
- `50` -- ...rne widelki niektórych opcji są o ponad [50] % powyżej mediany. Dodatkowo, rzeczywis...

Tych wartosci nie wolno cytowac dalej bez sprawdzenia w silniku.

**Zaokraglone wzgledem raportu (dopuszczalne, warto sprawdzic):**

- `0.93` -- ...waga jest istotna. - Współczynnik dolny [0.93] i górny 1.54 z  opisują skalę rozstrza...
- `1.54` -- ...otna. - Współczynnik dolny 0.93 i górny [1.54] z  opisują skalę rozstrzału względem w...

_Zdjete przed skanem jako nieobliczeniowe -- data ISO: 2, identyfikator node: 5, identyfikator runu: 1, naglowek struktury: 4, numer rejsu: 3, rozporzadzenie EU261: 1, znak rejestracyjny: 12._
