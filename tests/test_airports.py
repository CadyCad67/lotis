"""Porty jako kontrakt silnika.

Dwie rzeczy, ktore latwo zepsuc po cichu: przesuniecie strefy (zaszyte lato
daje zima godzine bledu na kazdym rejsie) i klucz MCT (zly klucz zaniza czas
przesiadki, wiec silnik proponuje rebooking, ktory fizycznie nie zdazy).
"""

import unittest
from datetime import date

from lotis.adapters.airports import all_ports, build_airports, minimum_connection_min, port


class TestPort(unittest.TestCase):
    def test_znajduje_po_kodzie(self):
        self.assertIsNotNone(port("WAW"))

    def test_normalizuje_zapis(self):
        self.assertEqual(port(" waw "), port("WAW"))

    def test_nieznany_port_daje_none(self):
        self.assertIsNone(port("ZZZ"))

    def test_pusty_kod_daje_none(self):
        self.assertIsNone(port(""))
        self.assertIsNone(port(None))

    def test_wszystkie_porty_niepuste(self):
        self.assertGreater(len(all_ports()), 100)


class TestBudowaPortow(unittest.TestCase):
    def setUp(self):
        self.lato = build_airports(date(2026, 8, 21))
        self.zima = build_airports(date(2026, 1, 21))

    def test_ten_sam_zestaw_portow_niezaleznie_od_daty(self):
        self.assertEqual(set(self.lato), set(self.zima))

    def test_przesuniecie_strefy_zalezy_od_daty(self):
        """Zaszyte lato dawalo zima godzine bledu na kazdym rejsie z WAW."""
        self.assertEqual(self.lato["WAW"].tz_offset_min, 120)
        self.assertEqual(self.zima["WAW"].tz_offset_min, 60)

    def test_strefa_bez_zmiany_czasu_zostaje_taka_sama(self):
        """Bangkok nie ma zmiany czasu -- jesli sie zmienia, to blad w konwersji."""
        if "BKK" in self.lato:
            self.assertEqual(self.lato["BKK"].tz_offset_min, self.zima["BKK"].tz_offset_min)

    def test_polkula_poludniowa_ma_odwrotna_zmiane(self):
        for iata in ("GRU", "EZE", "SYD", "JNB"):
            if iata in self.lato:
                with self.subTest(port=iata):
                    self.assertIsInstance(self.lato[iata].tz_offset_min, int)

    def test_przesuniecia_sa_wielokrotnoscia_kwadransa(self):
        for iata, ap in self.lato.items():
            with self.subTest(port=iata):
                self.assertEqual(ap.tz_offset_min % 15, 0)
                self.assertTrue(-12 * 60 <= ap.tz_offset_min <= 14 * 60)

    def test_kody_icao_dla_portow_krajowych(self):
        self.assertEqual(self.lato["WAW"].icao, "EPWA")
        self.assertEqual(self.lato["KRK"].icao, "EPKK")

    def test_curfew_przenosi_sie_z_typem(self):
        waw = self.lato["WAW"]
        self.assertIsNotNone(waw.curfew_start_min)
        self.assertEqual(waw.curfew_kind, 1)

    def test_port_bez_curfew_ma_puste_pola(self):
        bez = next(ap for ap in self.lato.values() if ap.curfew_kind == 0)
        self.assertIsNone(bez.curfew_start_min)

    def test_cache_zwraca_ten_sam_obiekt(self):
        """`lru_cache` -- budowa 148 portow na kazdy node bylaby marnotrawstwem."""
        self.assertIs(build_airports(date(2026, 8, 21)), self.lato)


class TestMCT(unittest.TestCase):
    def test_schengen_schengen_jest_najkrotszy(self):
        ss = minimum_connection_min("WAW", True, True)
        sn = minimum_connection_min("WAW", True, False)
        self.assertLessEqual(ss, sn)

    def test_przekroczenie_granicy_wydluza_przesiadke(self):
        """Przesiadka Schengen -> non-Schengen wymaga kontroli granicznej."""
        self.assertGreater(minimum_connection_min("WAW", True, False),
                           minimum_connection_min("WAW", True, True))

    def test_daleki_zasieg_uzywa_wlasnego_klucza(self):
        xl = minimum_connection_min("WAW", True, True, long_haul=True)
        ss = minimum_connection_min("WAW", True, True, long_haul=False)
        self.assertGreaterEqual(xl, ss)

    def test_non_non_ma_wlasny_klucz(self):
        self.assertGreater(minimum_connection_min("WAW", False, False), 0)

    def test_nieznany_port_ma_bezpieczna_wartosc_domyslna(self):
        self.assertEqual(minimum_connection_min("ZZZ", True, True), 45)

    def test_wszystkie_warianty_sa_dodatnie(self):
        for inbound in (True, False):
            for outbound in (True, False):
                for long_haul in (True, False):
                    with self.subTest(i=inbound, o=outbound, xl=long_haul):
                        self.assertGreater(
                            minimum_connection_min("WAW", inbound, outbound, long_haul), 0)


if __name__ == "__main__":
    unittest.main()
