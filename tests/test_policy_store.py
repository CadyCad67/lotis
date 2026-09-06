"""Polityka i stawki -- jedno zrodlo prawdy z warstwa nadpisan.

Sens tej warstwy: kazde odstepstwo od bazy ma byc widoczne w raporcie. Cicha
podmiana kwoty odszkodowania jest dokladnie tym, za co UOKiK wydal decyzje
zobowiazujaca wobec Enter Air (RBG-1/2026), i pliku `overrides.json` nie
wolno uzywac do jej powtorzenia.
"""

import json
import tempfile
import unittest
from pathlib import Path

from lotis.kernel.policy_store import PolicyStore

from ._helpers import db


class TestWarstwaBazowa(unittest.TestCase):
    def setUp(self):
        self.store = PolicyStore(db=db())

    def test_sekcje_bazy_sa_dostepne(self):
        self.assertTrue(self.store.cost)
        self.assertTrue(self.store.legal)
        self.assertTrue(self.store.ftl)
        self.assertTrue(self.store.config)

    def test_get_wchodzi_w_sciezke_kropkowa(self):
        self.assertEqual(self.store.get("fx.EUR_PLN"), db().eur_pln)

    def test_get_nieistniejacej_sciezki_daje_domyslna(self):
        self.assertEqual(self.store.get("nie.ma.takiej", "domyslna"), "domyslna")
        self.assertIsNone(self.store.get("nie.ma.takiej"))

    def test_require_wybucha_z_nazwa_sciezki(self):
        with self.assertRaises(KeyError) as ctx:
            self.store.require("nie.ma.takiej")
        self.assertIn("nie.ma.takiej", str(ctx.exception))

    def test_przeliczenie_na_zlote(self):
        self.assertAlmostEqual(self.store.pln("nie.ma", 100.0), 100.0 * self.store.eur_pln)

    def test_filtry_twarde_sa_zadeklarowane(self):
        """CF.hard -- filtry, ktorych zaden suwak nie moze wylaczyc."""
        self.assertIsInstance(self.store.hard_filters, list)

    def test_presety_maja_ksztalt_listy(self):
        self.assertIsInstance(self.store.presets, list)


class TestUzupelnieniaSpozaBazy(unittest.TestCase):
    """Trzy pliki, ktorych baza nie pokrywa: luki 4, 5 i 6 tablicy."""

    def setUp(self):
        self.store = PolicyStore(db=db())

    def test_progi_autoryzacji_rosna(self):
        """Luka 4: decyzja za 20 tys. i za 300 tys. nie moze przechodzic identycznie."""
        progi = [b["max_value"] for b in self.store.authorization["bands"]
                 if b["max_value"] is not None]
        self.assertEqual(progi, sorted(progi))

    def test_najwyzszy_prog_jest_otwarty(self):
        self.assertIsNone(self.store.authorization["bands"][-1]["max_value"])

    def test_wysokie_kwoty_wymagaja_drugiego_podpisu(self):
        bands = self.store.authorization["bands"]
        self.assertFalse(bands[0]["second_signature"])
        self.assertTrue(bands[-1]["second_signature"])

    def test_eskalacja_ma_adresata_zastepce_i_termin(self):
        """Luka 5: galaz BRAK DOPUSZCZALNEJ OPCJI nie miala adresata ani terminu."""
        esc = self.store.escalation
        self.assertTrue(esc["addressee"]["role"])
        self.assertTrue(esc["addressee"]["fallback_role"])
        self.assertGreater(esc["sla_minutes"], 0)
        self.assertGreater(esc["addressee"]["fallback_after_minutes"], 0)

    def test_zastepca_wchodzi_przed_uplywem_sla(self):
        esc = self.store.escalation
        self.assertLess(esc["addressee"]["fallback_after_minutes"], esc["sla_minutes"])

    def test_pakiet_eskalacyjny_ma_regule_ktora_zabila_opcje(self):
        """Bez tego pola eskalacja jest zgloszeniem, a nie uzasadnieniem."""
        self.assertIn("rule_that_killed_each", self.store.escalation["packet_fields"])

    def test_kody_odrzucenia_sa_zdefiniowane(self):
        self.assertTrue(self.store.authorization["reject_requires_reason_code"])
        self.assertTrue(self.store.authorization["reason_codes"])


class TestNadpisania(unittest.TestCase):
    def store_z(self, overrides: dict) -> tuple[PolicyStore, tempfile.TemporaryDirectory]:
        tmp = tempfile.TemporaryDirectory()
        directory = Path(tmp.name)
        (directory / "overrides.json").write_text(
            json.dumps(overrides), encoding="utf-8")
        return PolicyStore(directory, db=db()), tmp

    def test_bez_pliku_dziala_sama_baza(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = PolicyStore(tmp, db=db())
            self.assertEqual(store.declared_overrides(), {})
            self.assertEqual(store.provenance("fx.EUR_PLN"), "baza")

    def test_nadpisanie_wygrywa_z_baza(self):
        store, tmp = self.store_z({"fx.EUR_PLN": 4.30})
        try:
            self.assertEqual(store.get("fx.EUR_PLN"), 4.30)
            self.assertEqual(store.eur_pln, 4.30)
        finally:
            tmp.cleanup()

    def test_klucze_z_podkreslnikiem_to_komentarze_a_nie_nadpisania(self):
        """`_opis` i `_przyklad` w pliku nie moga stac sie parametrami silnika."""
        store, tmp = self.store_z({"_opis": "komentarz", "_przyklad": {"fx.EUR_PLN": 9.99}})
        try:
            self.assertEqual(store.declared_overrides(), {})
            self.assertNotEqual(store.eur_pln, 9.99)
        finally:
            tmp.cleanup()

    def test_pochodzenie_wartosci_jest_raportowane(self):
        store, tmp = self.store_z({"fx.EUR_PLN": 4.30})
        try:
            self.assertEqual(store.provenance("fx.EUR_PLN"), "override")
            self.assertEqual(store.provenance("reb.one_way_fare_estimate_eur"), "baza")
        finally:
            tmp.cleanup()

    def test_uzyte_nadpisania_sa_sledzone(self):
        """Node raportuje tylko te odstepstwa, ktore faktycznie wplynely na wynik."""
        store, tmp = self.store_z({"fx.EUR_PLN": 4.30, "care.hotel_night_eur": 120})
        try:
            self.assertEqual(store.applied_overrides(), {})
            store.get("fx.EUR_PLN")
            self.assertEqual(store.applied_overrides(), {"fx.EUR_PLN": 4.30})
        finally:
            tmp.cleanup()

    def test_zadeklarowane_to_wszystkie_a_uzyte_to_podzbior(self):
        store, tmp = self.store_z({"a.b": 1, "c.d": 2})
        try:
            store.get("a.b")
            self.assertEqual(len(store.declared_overrides()), 2)
            self.assertEqual(len(store.applied_overrides()), 1)
        finally:
            tmp.cleanup()

    def test_realny_plik_projektu_nie_nadpisuje_niczego(self):
        """Domyslnie liczymy dokladnie tym, co jest w bazie."""
        self.assertEqual(PolicyStore(db=db()).declared_overrides(), {})


if __name__ == "__main__":
    unittest.main()
