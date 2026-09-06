# Baza siatki połączeń PLL LOT

Zbudowana z dziewięciu eksportów historii lotów Flightradar24 (po jednym na typ floty).
Dwa pliki: `lot-siatka.json` (baza) i `lot-siatka.xlsx` (to samo do przeglądania, 9 arkuszy).

**Zasada:** dane twarde to rozkład — STD, STA i blok. Wartości rzeczywiste (ATD, ATA)
są wydzielone do osobnej sekcji `statystyka` i nigdzie nie mieszają się z rozkładem.

## Zawartość

| Sekcja | Ile | Co |
|---|---|---|
| `flota` | 91 maszyn | znak, typ, kod ICAO, MSN, Mode S, operator, liczba operacji, zakres dat |
| `porty` | 124 | IATA, nazwa, strefa czasowa, ruch, lista kierunków |
| `trasy` | 312 | blok rozkładowy, czas w powietrzu, kołowanie, typy, numery, częstotliwość |
| `rejsy` | 716 numerów | rozkład dzień po dniu tygodnia: STD, STA, blok, liczba obserwacji |
| `tydzienOperacyjny` | 2602 rejsy | siedem dób z rotacjami maszyn |
| `statystyka` | 6236 operacji | punktualność globalna, per rejs, per trasa, per port |

## Trzy problemy w danych, które trzeba było rozwiązać

**Kolumna DATE raz na pozycji 0, raz na 1.** To był ten rozjazd, o którym mówiłeś.
Parser kotwiczy się teraz na wzorcu daty, a nie na stałym indeksie — odzyskane 82 wiersze,
w tym rejsy z samym znakiem wywoławczym zamiast numeru (LOT1NZ, LOT4EC).

**Brak stref czasowych.** STD jest lokalne w porcie wylotu, STA w porcie przylotu, więc
ich różnica zawiera przesunięcie stref — dla SFO–WAW wychodziło 600 minut „kołowania".
Wyliczyłem strefy z samych danych: różnicę (STA−STD) porównałem z czasem w powietrzu na obu
kierunkach każdej trasy. Weryfikacja na 17 portach o znanej strefie: **16 trafień co do minuty**.
SFO wyszło o 30 minut obok (za mało obserwacji) i poprawiłem je ręcznie — jest to odnotowane.
Po korekcie mediana kołowania wynosi 24 minuty, a nierealnych bloków jest 0,5%.

**47 zduplikowanych rekordów** w obrębie tych samych plików, głównie SP-LYG (33). Odsiane.

## Tydzień operacyjny

Zamiast składać tydzień z uśrednionych rozkładów, wziąłem **siedem rzeczywistych dób** —
dla każdego dnia tygodnia tę najlepiej pokrytą w danych. Wyszedł z tego ciągły tydzień
**21–27 sierpnia 2026**.

| Dzień | Doba | Rejsów | Maszyn | Rotacje ciągłe |
|---|---|---|---|---|
| poniedziałek | 2026-08-24 | 378 | 86 | 81/86 |
| wtorek | 2026-08-25 | 350 | 81 | 78/81 |
| środa | 2026-08-26 | 382 | 83 | 80/83 |
| czwartek | 2026-08-27 | 382 | 84 | 79/84 |
| piątek | 2026-08-21 | 390 | 86 | 85/86 |
| sobota | 2026-08-22 | 348 | 87 | 84/87 |
| niedziela | 2026-08-23 | 371 | 87 | 83/87 |

„Rotacja ciągła" znaczy, że każdy kolejny odcinek startuje z portu, w którym skończył się
poprzedni. 92–98% się domyka; reszta to maszyny, których część doby wypadła poza okno eksportu.

Kontrola spójności: 0 rejsów z portem albo trasą spoza bazy, 0 bez bloku, 0 z blokiem
nierealnym, 0 z maszyną spoza floty.

## Statystyka — to, co wydarzyło się naprawdę

|  | mediana | średnia | P90 | punktualność ≤15 min |
|---|---|---|---|---|
| odlot | +22 min | +30,7 | +61 | **32,4%** |
| przylot | −4 min | +1,8 | +27 | **83,3%** |

To najciekawsza rzecz w tych danych. LOT wylatuje spóźniony w dwóch trzecich przypadków,
ale przylatuje na czas w czterech piątych. Bloki rozkładowe mają zapas, który załoga odrabia
w powietrzu. Każda analiza punktualności oparta wyłącznie na odlotach da fałszywy obraz.

Statystyka jest rozpisana na 452 numery rejsu, 212 tras i 68 portów wylotu.
