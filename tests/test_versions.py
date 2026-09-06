"""Wersje silnika i danych.

Kazdy raport je niesie. Bez nich nie da sie odtworzyc, czym byl policzony run
sprzed miesiaca -- a to jest cala wartosc logu z node 16.
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from lotis.kernel import versions


class TestBlokWersji(unittest.TestCase):
    def test_ma_komplet_pol(self):
        block = versions.version_block()
        for key in ("engine", "data", "data_generated", "authorization",
                    "escalation", "sop", "overrides"):
            with self.subTest(pole=key):
                self.assertIn(key, block)

    def test_wersja_silnika_jest_semver(self):
        czesci = versions.ENGINE_VERSION.split(".")
        self.assertEqual(len(czesci), 3)
        self.assertTrue(all(c.isdigit() for c in czesci))

    def test_wersja_danych_pochodzi_z_bazy(self):
        from lotis.adapters.lot_db import load_lot_db
        self.assertEqual(versions.version_block()["data"], load_lot_db().version)

    def test_schema_raportu_jest_wersjonowany(self):
        self.assertTrue(versions.REPORT_SCHEMA.endswith("/v1"))

    def test_niedostepna_baza_nie_wywraca_bloku(self):
        """Raport ma sie zapisac takze wtedy, gdy zrodlo danych padlo."""
        with mock.patch("lotis.adapters.lot_db.load_lot_db",
                        side_effect=FileNotFoundError("brak pliku")):
            block = versions.version_block()
        self.assertEqual(block["data"], "unavailable")


class TestOdciskNadpisan(unittest.TestCase):
    def odcisk_dla(self, payload: dict | None, nazwa: str = "overrides.json") -> str:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            if payload is not None:
                (directory / nazwa).write_text(json.dumps(payload), encoding="utf-8")
            with mock.patch.object(versions, "POLICY_DIR", directory):
                return versions.overrides_fingerprint()

    def test_brak_pliku_daje_brak(self):
        self.assertEqual(self.odcisk_dla(None), "brak")

    def test_sam_komentarz_to_nadal_brak(self):
        self.assertEqual(self.odcisk_dla({"_opis": "komentarz"}), "brak")

    def test_pusty_obiekt_to_brak(self):
        self.assertEqual(self.odcisk_dla({}), "brak")

    def test_wpis_zmienia_odcisk(self):
        odcisk = self.odcisk_dla({"fx.EUR_PLN": 4.30})
        self.assertNotEqual(odcisk, "brak")
        self.assertTrue(odcisk.startswith("1@"))

    def test_liczba_wpisow_jest_widoczna_w_odcisku(self):
        self.assertTrue(self.odcisk_dla({"a": 1, "b": 2}).startswith("2@"))

    def test_inna_wartosc_daje_inny_odcisk(self):
        self.assertNotEqual(self.odcisk_dla({"fx.EUR_PLN": 4.30}),
                            self.odcisk_dla({"fx.EUR_PLN": 4.40}))

    def test_kolejnosc_kluczy_nie_wplywa_na_odcisk(self):
        self.assertEqual(self.odcisk_dla({"a": 1, "b": 2}), self.odcisk_dla({"b": 2, "a": 1}))

    def test_nieczytelny_plik_jest_oznaczony(self):
        """Cichy powrot do 'brak' udawalby, ze nadpisan nie ma."""
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "overrides.json").write_text("{to nie jest json", encoding="utf-8")
            with mock.patch.object(versions, "POLICY_DIR", Path(tmp)):
                self.assertEqual(versions.overrides_fingerprint(), "nieczytelny")


class TestWersjeLokalne(unittest.TestCase):
    def test_pliki_polityki_maja_wersje(self):
        block = versions.version_block()
        for key in ("authorization", "escalation", "sop"):
            with self.subTest(plik=key):
                self.assertNotEqual(block[key], "brak")

    def test_brakujacy_plik_daje_brak(self):
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(versions, "POLICY_DIR", Path(tmp)):
                self.assertEqual(versions._local_version("nie-ma.json"), "brak")


if __name__ == "__main__":
    unittest.main()
