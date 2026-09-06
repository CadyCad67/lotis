"""Tozsamosc przewoznika.

Caly system jest zawezony do LOT-u. Zbyt luzny filtr wpuscilby ruch obcych
przewoznikow do snapshotu, a zbyt ciasny wycialby wlasne rejsy -- oba bledy
koncza sie licznikiem, ktory nie opisuje niczego.
"""

import unittest

from lotis.adapters import airline

from ._helpers import db


class TestCallsign(unittest.TestCase):
    def test_przyjmuje_wlasne_callsigny(self):
        for cs in ("LOT282", "LOT3A", "LOT12345"):
            with self.subTest(callsign=cs):
                self.assertTrue(airline.is_lot_callsign(cs))

    def test_znosi_dopelnienie_spacjami(self):
        """OpenSky zwraca callsigny dopelnione do osmiu znakow."""
        self.assertTrue(airline.is_lot_callsign("LOT282  "))

    def test_znosi_male_litery(self):
        self.assertTrue(airline.is_lot_callsign("lot282"))

    def test_odrzuca_obcych_przewoznikow(self):
        for cs in ("LH1234", "BAW456", "RYR9876", "SAS100", "DLH400"):
            with self.subTest(callsign=cs):
                self.assertFalse(airline.is_lot_callsign(cs))

    def test_odrzuca_prefiks_bez_numeru(self):
        self.assertFalse(airline.is_lot_callsign("LOT"))

    def test_odrzuca_zbyt_dlugi(self):
        self.assertFalse(airline.is_lot_callsign("LOT123456"))

    def test_odrzuca_puste(self):
        self.assertFalse(airline.is_lot_callsign(""))
        self.assertFalse(airline.is_lot_callsign(None))


class TestRejestracja(unittest.TestCase):
    def test_przyjmuje_blok_lot(self):
        for reg in ("SP-LRA", "SP-LIA", "SP-LND"):
            with self.subTest(reg=reg):
                self.assertTrue(airline.is_lot_registration(reg))

    def test_odrzuca_inne_polskie_bloki(self):
        self.assertFalse(airline.is_lot_registration("SP-ABC"))

    def test_odrzuca_obce_rejestracje(self):
        for reg in ("D-AIBC", "G-EUUU", "N123AB"):
            with self.subTest(reg=reg):
                self.assertFalse(airline.is_lot_registration(reg))

    def test_znosi_male_litery_i_spacje(self):
        self.assertTrue(airline.is_lot_registration("  sp-lra "))

    def test_odrzuca_puste(self):
        self.assertFalse(airline.is_lot_registration(""))
        self.assertFalse(airline.is_lot_registration(None))

    def test_flota_wlasna_przechodzi_filtr(self):
        """Test lapie rozjazd miedzy regexem a rzeczywista flota w bazie."""
        wlasne = [reg for reg, ac in db().fleet.items() if not ac.wet_lease]
        odrzucone = [r for r in wlasne if not airline.is_lot_registration(r)]
        self.assertEqual(odrzucone, [])


class TestNumerRejsu(unittest.TestCase):
    def test_konwersja_z_callsignu(self):
        self.assertEqual(airline.flight_number_from_callsign("LOT282  "), "LO282")

    def test_zachowuje_sufiks_alfanumeryczny(self):
        self.assertEqual(airline.flight_number_from_callsign("LOT3A"), "LO3A")

    def test_male_litery(self):
        self.assertEqual(airline.flight_number_from_callsign("lot282"), "LO282")


class TestRodzinyTypow(unittest.TestCase):
    """Rodzina uprawnien pochodzi teraz z bazy (`TY[4]`), a nie z recznej tabeli.

    Poprzednia wersja miala wlasny slownik z kodami `E70`/`E75`/`E95`, ktorych
    w bazie nie ma -- zwracala `None` dla kazdego realnego typu, czyli po cichu
    twierdzila, ze zadna zaloga nie ma uprawnien na nic.
    """

    def test_embraery_klasyczne_sa_jedna_rodzina(self):
        self.assertEqual(airline.family_of("E170"), airline.family_of("E195"))
        self.assertEqual(airline.family_of("E75S"), airline.family_of("E190"))

    def test_e2_ma_osobne_uprawnienie(self):
        """E195-E2 wymaga szkolenia roznicowego, wiec SWAP E195 -> E295 nie jest darmowy."""
        self.assertNotEqual(airline.family_of("E195"), airline.family_of("E295"))

    def test_737_ng_i_max_sa_jedna_rodzina(self):
        self.assertEqual(airline.family_of("B738"), airline.family_of("B38M"))

    def test_787_8_i_9_sa_jedna_rodzina(self):
        self.assertEqual(airline.family_of("B788"), airline.family_of("B789"))

    def test_rodziny_sa_rozlaczne(self):
        self.assertNotEqual(airline.family_of("E195"), airline.family_of("B738"))
        self.assertNotEqual(airline.family_of("B789"), airline.family_of("B772"))

    def test_nieznany_typ_daje_none(self):
        self.assertIsNone(airline.family_of("XXX"))
        self.assertIsNone(airline.family_of(""))
        self.assertIsNone(airline.family_of(None))

    def test_normalizuje_zapis(self):
        self.assertEqual(airline.family_of(" b738 "), airline.family_of("B738"))

    def test_kazdy_typ_z_bazy_ma_rodzine(self):
        for code in db().types:
            with self.subTest(typ=code):
                self.assertIsNotNone(airline.family_of(code))


class TestKwalifikacje(unittest.TestCase):
    def test_zaloga_z_uprawnieniem_moze_leciec(self):
        self.assertTrue(airline.qualified({"EJET"}, "E195"))

    def test_uprawnienie_dziala_na_cala_rodzine(self):
        """SWAP E175 -> E195 nie wymaga zmiany zalogi."""
        for code in ("E170", "E75S", "E190", "E195"):
            with self.subTest(typ=code):
                self.assertTrue(airline.qualified({"EJET"}, code))

    def test_bez_uprawnienia_nie_moze(self):
        self.assertFalse(airline.qualified({"EJET"}, "B738"))
        self.assertFalse(airline.qualified({"EJET"}, "E295"))

    def test_nieznany_typ_nie_przechodzi(self):
        """Brak danych o typie nie moze udawac uprawnienia."""
        self.assertFalse(airline.qualified({"EJET", "B737", "B787"}, "XXX"))

    def test_pusty_zbior_uprawnien(self):
        self.assertFalse(airline.qualified(frozenset(), "E195"))

    def test_zaloga_z_kilkoma_uprawnieniami(self):
        wielo = {"EJET", "B737"}
        self.assertTrue(airline.qualified(wielo, "E195"))
        self.assertTrue(airline.qualified(wielo, "B38M"))
        self.assertFalse(airline.qualified(wielo, "B789"))


class TestStale(unittest.TestCase):
    def test_baza_macierzysta_jest_wsrod_baz_zalogi(self):
        self.assertIn(airline.HOME_BASE, airline.CREW_BASES)

    def test_kody_przewoznika(self):
        self.assertEqual(airline.ICAO, "LOT")
        self.assertEqual(airline.IATA, "LO")

    def test_bazy_zalogi_istnieja_w_bazie_portow(self):
        for base in airline.CREW_BASES:
            with self.subTest(baza=base):
                self.assertIn(base, db().ports)


if __name__ == "__main__":
    unittest.main()
