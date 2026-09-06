"""Geometria. Dystans wchodzi do proraty O&D i do progu EU261, wiec blad
tutaj przesuwa kwote odszkodowania o cala kategorie."""

import unittest

from lotis.kernel.geo import haversine_km

WAW = (52.1657, 20.9671)
KRK = (50.0777, 19.7848)
JFK = (40.6413, -73.7781)
NRT = (35.7647, 140.3864)


class TestHaversine(unittest.TestCase):
    def test_ten_sam_punkt_daje_zero(self):
        self.assertEqual(haversine_km(*WAW, *WAW), 0.0)

    def test_symetria(self):
        self.assertAlmostEqual(haversine_km(*WAW, *JFK), haversine_km(*JFK, *WAW), places=9)

    def test_znane_dystanse(self):
        # Wartosci referencyjne z wielkiego kola, tolerancja 1%.
        for a, b, expected in ((WAW, KRK, 246), (WAW, JFK, 6867), (WAW, NRT, 8578)):
            with self.subTest(cel=b):
                self.assertAlmostEqual(haversine_km(*a, *b), expected, delta=expected * 0.01)

    def test_przez_poludnik_180(self):
        """Bez poprawnej roznicy dlugosci wyszlaby droga naokolo swiata."""
        d = haversine_km(0.0, 179.0, 0.0, -179.0)
        self.assertAlmostEqual(d, 222.4, delta=2.0)

    def test_antypody_to_polowa_obwodu(self):
        d = haversine_km(0.0, 0.0, 0.0, 180.0)
        self.assertAlmostEqual(d, 20015.1, delta=1.0)

    def test_bieguny(self):
        d = haversine_km(90.0, 0.0, -90.0, 0.0)
        self.assertAlmostEqual(d, 20015.1, delta=1.0)

    def test_asin_nie_wychodzi_poza_dziedzine(self):
        """Przy antypodach sqrt(a) potrafi wyjsc na 1.0000000000000002."""
        try:
            haversine_km(90.0, 0.0, -90.0, 180.0)
        except ValueError as exc:                       # pragma: no cover
            self.fail(f"math domain error przy antypodach: {exc}")

    def test_progi_eu261_dziela_sie_wlasciwie(self):
        """1500 km i 3500 km to granice kategorii A/B/C -- musza wypadac po wlasciwej stronie."""
        self.assertLess(haversine_km(*WAW, *KRK), 1500)
        self.assertGreater(haversine_km(*WAW, *JFK), 3500)


if __name__ == "__main__":
    unittest.main()
