"""Baza operacyjna z `lot-siatka.json`.

Siedem rzeczywistych dob i statystyka wykonanych operacji. Ta druga sekcja
jest w projekcie najcenniejsza -- daje node 11 widelki z pomiaru zamiast
z zalozenia.

Zasada rozdzialu przyjeta w zrodle: rozklad (STD, STA, blok) to dane twarde,
wartosci rzeczywiste (ATD, ATA) siedza wylacznie w statystyce. Testy nizej
pilnuja, zeby te dwie warstwy sie nie zmieszaly.
"""

import unittest

from lotis.adapters.siatka import DelayStats, _hm

from ._helpers import siatka


class TestStatystykaOpoznien(unittest.TestCase):
    def wiersz(self, **kw):
        base = {"n": 100, "mediana": 10.0, "srednia": 15.0, "p25": 0.0,
                "p75": 25.0, "p90": 45.0, "max": 300.0, "punktualnosc15": 70.0}
        base.update(kw)
        return DelayStats.parse(base)

    def test_parsowanie(self):
        s = self.wiersz()
        self.assertEqual(s.n, 100)
        self.assertEqual(s.median, 10.0)

    def test_rozstep_miedzykwartylowy(self):
        self.assertEqual(self.wiersz(p25=5.0, p75=25.0).iqr, 20.0)

    def test_widelki_to_p25_mediana_p90(self):
        self.assertEqual(self.wiersz().band(), (0.0, 10.0, 45.0))

    def test_widelki_sa_niemalejace(self):
        low, mid, high = self.wiersz().band()
        self.assertLessEqual(low, mid)
        self.assertLessEqual(mid, high)


class TestTydzien(unittest.TestCase):
    def setUp(self):
        self.sn = siatka()

    def test_jest_siedem_dob(self):
        self.assertEqual(sorted(self.sn.week), list(range(7)))

    def test_kazda_doba_ma_rejsy_i_date(self):
        for day, entry in self.sn.week.items():
            with self.subTest(dzien=day):
                self.assertGreater(len(entry.flights), 0)
                self.assertEqual(entry.weekday, day)
                self.assertEqual(entry.day.weekday(), day)   # 0 = poniedzialek

    def test_doby_pokrywaja_jeden_tydzien_bez_powtorzen(self):
        """Okno zrodla to 21-27 sierpnia 2026, a 21 sierpnia jest piatkiem.

        Uporzadkowane po indeksie dnia tygodnia daty NIE sa wiec rosnace --
        poniedzialek wypada 24 sierpnia, a piatek 21. Test pilnuje tego, co
        naprawde ma znaczenie: kazdy dzien tygodnia raz i wszystko w jednym
        oknie siedmiu dni.
        """
        dni = sorted(self.sn.week[i].day for i in range(7))
        self.assertEqual(len(set(dni)), 7)
        self.assertEqual((dni[-1] - dni[0]).days, 6)

    def test_wszystkie_rejsy_maja_dodatni_blok(self):
        for day, entry in self.sn.week.items():
            for f in entry.flights:
                with self.subTest(dzien=day, rejs=f.number):
                    self.assertGreater(f.block_min, 0)

    def test_minuta_odlotu_miesci_sie_w_dobie(self):
        for entry in self.sn.week.values():
            for f in entry.flights:
                with self.subTest(rejs=f.number):
                    self.assertTrue(0 <= f.std_utc_min < 1440)

    def test_przeliczenie_na_utc_zachowuje_blok(self):
        entry = self.sn.day_for(4)
        f = entry.flights[0]
        self.assertEqual(int((f.sta_utc(entry.day) - f.std_utc(entry.day)).total_seconds() // 60),
                         f.block_min)

    def test_grupowanie_po_rejestracji_sortuje_chronologicznie(self):
        for reg, legs in self.sn.day_for(4).by_registration().items():
            with self.subTest(reg=reg):
                self.assertEqual([f.std_utc_min for f in legs],
                                 sorted(f.std_utc_min for f in legs))

    def test_ciaglosc_lancuchow_jest_wysoka(self):
        """Zrodlo deklaruje 92-98%. Nagly spadek znaczylby zly klucz grupowania."""
        entry = self.sn.day_for(4)
        przejsc = sum(max(0, len(legs) - 1) for legs in entry.by_registration().values())
        przerw = len(entry.continuity_breaks())
        self.assertGreater(1 - przerw / max(1, przejsc), 0.90)

    def test_najbardziej_obciazona_doba(self):
        busiest = self.sn.busiest_day()
        self.assertEqual(len(busiest.flights),
                         max(len(d.flights) for d in self.sn.week.values()))

    def test_wszystkie_rejsy_naleza_do_lot(self):
        """System jest zawezony do jednej linii -- to sprawdza, ze zrodlo tez.

        Czesc rekordow nie ma numeru handlowego i wystepuje jako `znak:LOT1NZ`.
        To nadal LOT: prefiks `LOT` w znaku wywolawczym nalezy do przewoznika.
        Node 02 raportuje te rejsy osobno, bo brak numeru znaczy, ze nie wiadomo,
        czy sa na nich pasazerowie.
        """
        obce = {f.number for e in self.sn.week.values() for f in e.flights
                if not f.number.upper().startswith(("LO", "ZNAK:LOT"))}
        self.assertEqual(obce, set())

    def test_rejsy_bez_numeru_handlowego_sa_marginesem(self):
        wszystkie = [f for e in self.sn.week.values() for f in e.flights]
        bez_numeru = [f for f in wszystkie if f.number.lower().startswith("znak:")]
        self.assertLess(len(bez_numeru) / len(wszystkie), 0.05)


class TestStatystyka(unittest.TestCase):
    def setUp(self):
        self.sn = siatka()

    def test_statystyka_globalna_ma_odlot_i_przylot(self):
        self.assertEqual(set(self.sn.global_stats), {"odlot", "przylot"})

    def test_opoznienia_sa_odrabiane_w_locie(self):
        """Mediana odlotu dodatnia, przylotu ujemna -- dlatego node 10 liczy
        propagacje na przylotach, a nie na odlotach."""
        g = self.sn.global_stats
        self.assertGreater(g["odlot"].median, 0)
        self.assertLess(g["przylot"].median, g["odlot"].median)

    def test_kwantyle_sa_uporzadkowane(self):
        for nazwa, s in self.sn.global_stats.items():
            with self.subTest(rodzaj=nazwa):
                self.assertLessEqual(s.p25, s.median)
                self.assertLessEqual(s.median, s.p75)
                self.assertLessEqual(s.p75, s.p90)
                self.assertLessEqual(s.p90, s.max)

    def test_punktualnosc_w_zakresie_procentowym(self):
        for s in self.sn.global_stats.values():
            self.assertTrue(0 <= s.on_time_15_pct <= 100)

    def test_statystyka_per_rejs_i_per_trasa_nie_jest_pusta(self):
        self.assertGreater(len(self.sn.by_flight), 0)
        self.assertGreater(len(self.sn.by_route), 0)
        self.assertGreater(len(self.sn.by_departure_port), 0)


class TestKaskadaWidelek(unittest.TestCase):
    """Kaskada ma znaczenie: rozklad dla LO521 jest inny niz sredni dla siatki,
    a udawanie, ze nie jest, zawyza pewnosc."""

    def setUp(self):
        self.sn = siatka()

    def test_nieznany_rejs_spada_do_globalnej(self):
        self.assertEqual(self.sn.departure_band("LO99999"),
                         self.sn.global_stats["odlot"].band())

    def test_znany_rejs_ma_wlasne_widelki(self):
        number = next(nr for nr, row in self.sn.by_flight.items()
                      if "odlot" in row and row["odlot"].n >= 5)
        self.assertEqual(self.sn.departure_band(number),
                         self.sn.by_flight[number]["odlot"].band())

    def test_rzadki_rejs_spada_do_trasy(self):
        """Ponizej pieciu obserwacji wlasny rozklad nie jest rozkladem."""
        kandydat = next(
            (nr for nr, row in self.sn.by_flight.items()
             if "odlot" in row and row["odlot"].n < 5), None)
        if kandydat is None:
            self.skipTest("brak rejsu z mniej niz pieciu obserwacjami")
        self.assertNotEqual(self.sn.departure_band(kandydat),
                            self.sn.by_flight[kandydat]["odlot"].band())

    def test_widelki_zawsze_maja_trzy_wartosci(self):
        for number in list(self.sn.by_flight)[:50]:
            with self.subTest(rejs=number):
                self.assertEqual(len(self.sn.departure_band(number)), 3)


class TestPomocnicze(unittest.TestCase):
    def test_konwersja_godziny(self):
        self.assertEqual(_hm("14:35"), 875)

    def test_summary_ma_niezerowe_liczniki(self):
        s = siatka().summary()
        for key in ("porty", "trasy", "numery_rejsow", "doby_tygodnia",
                    "rejsow_w_tygodniu"):
            with self.subTest(pole=key):
                self.assertGreater(s[key], 0)


if __name__ == "__main__":
    unittest.main()
