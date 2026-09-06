"""Wczytywanie `.env`.

Parser jest celowo scisly. Cicho przepuszczona linia w konfiguracji znaczy,
ze silnik liczy innym kluczem niz ten, ktory wpisano do pliku -- i nikt sie
o tym nie dowie.
"""

import os
import tempfile
import unittest
from pathlib import Path

from lotis.kernel import env


class TestParser(unittest.TestCase):
    def test_podstawowa_para(self):
        self.assertEqual(env.parse_env("KLUCZ=wartosc"), {"KLUCZ": "wartosc"})

    def test_puste_linie_i_komentarze_sa_pomijane(self):
        text = "\n# komentarz\n\nA=1\n   # wciety komentarz\nB=2\n"
        self.assertEqual(env.parse_env(text), {"A": "1", "B": "2"})

    def test_prefiks_export_jest_zdejmowany(self):
        self.assertEqual(env.parse_env("export A=1"), {"A": "1"})

    def test_cudzyslowy_zdejmowane_tylko_gdy_otaczaja_calosc(self):
        self.assertEqual(env.parse_env('A="ma spacje"')["A"], "ma spacje")
        self.assertEqual(env.parse_env("A='pojedyncze'")["A"], "pojedyncze")
        self.assertEqual(env.parse_env('A=cudzyslow" w srodku')["A"], 'cudzyslow" w srodku')

    def test_komentarz_na_koncu_linii(self):
        self.assertEqual(env.parse_env("A=1 # to komentarz")["A"], "1")

    def test_hash_w_cudzyslowie_nie_jest_komentarzem(self):
        """Klucze API bywaja z krzyzykiem. Ucinanie go po cichu psuje autoryzacje."""
        self.assertEqual(env.parse_env('A="sk-or-v1#abc"')["A"], "sk-or-v1#abc")

    def test_hash_bez_spacji_zostaje(self):
        self.assertEqual(env.parse_env("A=abc#def")["A"], "abc#def")

    def test_wartosc_ze_znakiem_rownosci(self):
        self.assertEqual(env.parse_env("A=klucz=wartosc")["A"], "klucz=wartosc")

    def test_pusta_wartosc_jest_dozwolona(self):
        self.assertEqual(env.parse_env("A=")["A"], "")

    def test_brak_znaku_rownosci_to_blad_z_numerem_linii(self):
        with self.assertRaises(ValueError) as ctx:
            env.parse_env("A=1\nSMIECI\n")
        self.assertIn("linia 2", str(ctx.exception))

    def test_pusty_klucz_to_blad(self):
        with self.assertRaises(ValueError):
            env.parse_env("=wartosc")

    def test_klucz_jest_przycinany(self):
        self.assertEqual(env.parse_env("  A  = 1 ")["A"], "1")


class TestLadowanie(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / ".env"
        self.zachowane = {k: os.environ.get(k)
                          for k in ("LOTIS_TEST_A", "LOTIS_TEST_B", "LOTIS_TEST_PUSTY")}
        for key in self.zachowane:
            os.environ.pop(key, None)

    def tearDown(self):
        for key, value in self.zachowane.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        self.tmp.cleanup()

    def test_ustawia_zmienne(self):
        self.path.write_text("LOTIS_TEST_A=jeden\n", encoding="utf-8")
        env.load_env(self.path)
        self.assertEqual(os.environ["LOTIS_TEST_A"], "jeden")

    def test_zmienna_ze_srodowiska_wygrywa_z_plikiem(self):
        """`set KLUCZ=...` w terminalu ma nadpisywac .env bez edycji pliku."""
        os.environ["LOTIS_TEST_A"] = "z terminala"
        self.path.write_text("LOTIS_TEST_A=z pliku\n", encoding="utf-8")
        applied = env.load_env(self.path)
        self.assertEqual(os.environ["LOTIS_TEST_A"], "z terminala")
        self.assertNotIn("LOTIS_TEST_A", applied)

    def test_override_odwraca_pierwszenstwo(self):
        os.environ["LOTIS_TEST_A"] = "z terminala"
        self.path.write_text("LOTIS_TEST_A=z pliku\n", encoding="utf-8")
        env.load_env(self.path, override=True)
        self.assertEqual(os.environ["LOTIS_TEST_A"], "z pliku")

    def test_pusty_wpis_nie_ustawia_zmiennej(self):
        """`OPENROUTER_API_KEY=` znaczy 'nie ustawiaj', a nie 'ustaw na pusto'."""
        self.path.write_text("LOTIS_TEST_PUSTY=\n", encoding="utf-8")
        env.load_env(self.path)
        self.assertNotIn("LOTIS_TEST_PUSTY", os.environ)

    def test_brak_pliku_nie_wybucha(self):
        self.assertEqual(env.load_env(Path(self.tmp.name) / "nie-ma"), {})


class TestDostep(unittest.TestCase):
    def test_get_zwraca_domyslna_gdy_pusto(self):
        os.environ.pop("LOTIS_TEST_NIEMA", None)
        self.assertEqual(env.get("LOTIS_TEST_NIEMA", "domyslna"), "domyslna")

    def test_get_int_parsuje(self):
        os.environ["LOTIS_TEST_INT"] = "42"
        try:
            self.assertEqual(env.get_int("LOTIS_TEST_INT", 0), 42)
        finally:
            os.environ.pop("LOTIS_TEST_INT")

    def test_get_int_odrzuca_smieci_z_nazwa_zmiennej(self):
        os.environ["LOTIS_TEST_INT"] = "dwadziescia"
        try:
            with self.assertRaises(ValueError) as ctx:
                env.get_int("LOTIS_TEST_INT", 0)
            self.assertIn("LOTIS_TEST_INT", str(ctx.exception))
        finally:
            os.environ.pop("LOTIS_TEST_INT")

    def test_get_int_bez_zmiennej_daje_domyslna(self):
        os.environ.pop("LOTIS_TEST_INT", None)
        self.assertEqual(env.get_int("LOTIS_TEST_INT", 7), 7)

    def test_require_mowi_czego_brakuje_i_gdzie_to_ustawic(self):
        os.environ.pop("LOTIS_TEST_WYMAGANY", None)
        with self.assertRaises(RuntimeError) as ctx:
            env.require("LOTIS_TEST_WYMAGANY", "Podpowiedz.")
        message = str(ctx.exception)
        self.assertIn("LOTIS_TEST_WYMAGANY", message)
        self.assertIn("Podpowiedz.", message)
        self.assertIn(".env", message)


if __name__ == "__main__":
    unittest.main()
