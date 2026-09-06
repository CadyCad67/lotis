"""Typy statkow, koszt minuty opoznienia i czasy postoju.

Dwa miejsca, w ktorych latwo o cichy blad: wspolne uprawnienie zalogi
(pomylka kosztuje SWAP, ktorego nie da sie wykonac) i ksztalt krzywej kosztu
(liniowa stawka zaniza dlugie opoznienia o kilkadziesiat procent).
"""

import unittest

from lotis.adapters.aircraft_perf import (
    build_types, delay_cost_eur_per_min, gauge_delta, get_type, same_crew_rating,
    spec, turnaround_min,
)

from ._helpers import db


class TestSpecyfikacja(unittest.TestCase):
    def test_znajduje_typ(self):
        self.assertIsNotNone(spec("E75S"))

    def test_normalizuje_zapis(self):
        self.assertEqual(spec(" e75s "), spec("E75S"))

    def test_nieznany_typ_daje_none(self):
        self.assertIsNone(spec("XXX"))
        self.assertIsNone(get_type("XXX"))

    def test_pusty_kod_daje_none(self):
        self.assertIsNone(spec(""))
        self.assertIsNone(spec(None))

    def test_konwersja_do_kontraktu_zachowuje_pojemnosc(self):
        s, t = spec("E75S"), get_type("E75S")
        self.assertEqual(t.seats_declared, s.seats)
        self.assertEqual(t.rating, s.rating)

    def test_build_types_zwraca_cala_flote_typow(self):
        types = build_types()
        self.assertEqual(set(types), set(db().types))
        for code, t in types.items():
            with self.subTest(typ=code):
                self.assertGreater(t.seats_total, 0)


class TestUprawnienia(unittest.TestCase):
    def test_ten_sam_typ_zawsze_pasuje(self):
        self.assertTrue(same_crew_rating("E75S", "E75S"))

    def test_737_ng_i_max_dziela_uprawnienie(self):
        """SWAP B738 <-> B38M jest zalogowo darmowy."""
        self.assertTrue(same_crew_rating("B738", "B38M"))

    def test_embraer_i_boeing_nie_dziela_uprawnienia(self):
        self.assertFalse(same_crew_rating("E195", "B738"))

    def test_waskokadlubowiec_i_szerokokadlubowiec_nie_dziela(self):
        self.assertFalse(same_crew_rating("B738", "B789"))

    def test_nieznany_typ_nie_pasuje_do_niczego(self):
        """Brak danych nie moze udawac zgodnosci -- to by wypuscilo zaloge bez uprawnien."""
        self.assertFalse(same_crew_rating("XXX", "E75S"))
        self.assertFalse(same_crew_rating("XXX", "YYY"))

    def test_relacja_jest_symetryczna(self):
        for a in db().types:
            for b in db().types:
                with self.subTest(a=a, b=b):
                    self.assertEqual(same_crew_rating(a, b), same_crew_rating(b, a))


class TestKosztOpoznienia(unittest.TestCase):
    def test_nieznany_typ_daje_zero(self):
        self.assertEqual(delay_cost_eur_per_min("XXX", 30), 0.0)

    def test_stawka_jest_dodatnia(self):
        self.assertGreater(delay_cost_eur_per_min("E75S", 15), 0.0)

    def test_krzywa_jest_wypukla(self):
        """Minuta przy 30 minutach kosztuje wiecej niz przy 5 -- dochodzi propagacja.
        Liniowa stawka, ktorej uzywalem wczesniej, zanizala dlugie opoznienia."""
        self.assertGreater(delay_cost_eur_per_min("E75S", 30),
                           delay_cost_eur_per_min("E75S", 5))

    def test_stawka_jest_niemalejaca(self):
        wartosci = [delay_cost_eur_per_min("E75S", m) for m in range(1, 61, 5)]
        self.assertEqual(wartosci, sorted(wartosci))

    def test_ponizej_pierwszej_kotwicy_stawka_jest_stala(self):
        self.assertEqual(delay_cost_eur_per_min("E75S", 1), delay_cost_eur_per_min("E75S", 5))

    def test_powyzej_ostatniej_kotwicy_stawka_jest_stala(self):
        self.assertEqual(delay_cost_eur_per_min("E75S", 30), delay_cost_eur_per_min("E75S", 300))

    def test_wiekszy_samolot_kosztuje_wiecej(self):
        self.assertGreater(delay_cost_eur_per_min("B789", 30), delay_cost_eur_per_min("E75S", 30))

    def test_787_nie_jest_liczony_przez_747(self):
        """Adnotacja w bazie mowi to wprost -- B744 zawyzylby koszt kilkukrotnie."""
        self.assertNotEqual(spec("B789").cost_proxy, "B744")


class TestPostoje(unittest.TestCase):
    def test_zwraca_pare_rekomendowany_minimum(self):
        rekomendowany, minimum = turnaround_min("E75S", "europe")
        self.assertLessEqual(minimum, rekomendowany)
        self.assertGreater(minimum, 0)

    def test_nieznany_sektor_spada_na_europe(self):
        self.assertEqual(turnaround_min("E75S", "nieistniejacy"), turnaround_min("E75S", "europe"))

    def test_nieznany_typ_ma_wartosc_domyslna(self):
        self.assertEqual(turnaround_min("XXX", "europe"), (45, 35))

    def test_daleki_zasieg_stoi_dluzej(self):
        krotki = turnaround_min("B789", "europe")[0]
        daleki = turnaround_min("B789", "longhaul")[0]
        self.assertGreaterEqual(daleki, krotki)


class TestZmianaPojemnosci(unittest.TestCase):
    def test_upgauge_jest_dodatni(self):
        self.assertGreater(gauge_delta("E75S", "B789"), 0)

    def test_downgauge_jest_ujemny(self):
        self.assertLess(gauge_delta("B789", "E75S"), 0)

    def test_ten_sam_typ_daje_zero(self):
        self.assertEqual(gauge_delta("E75S", "E75S"), 0)

    def test_antysymetria(self):
        self.assertEqual(gauge_delta("E75S", "B738"), -gauge_delta("B738", "E75S"))

    def test_nieznany_typ_wybucha_z_nazwa(self):
        """Cicha zerowka tutaj znaczylaby, ze podmiana nie zmienia pojemnosci."""
        with self.assertRaises(KeyError) as ctx:
            gauge_delta("XXX", "E75S")
        self.assertIn("XXX", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
