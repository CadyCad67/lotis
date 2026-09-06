"""Pieniadze. Najwazniejszy plik w calym zestawie.

Blad zaokraglenia nie wywraca systemu -- daje liczbe, ktora wyglada dobrze
i jest o grosz obok. Pomnozone przez 32 tysiace pasazerow przestaje byc
o grosz obok.
"""

import unittest
from decimal import Decimal

from lotis.kernel.errors import CurrencyMismatch
from lotis.kernel.money import Money, money_sum


class TestKonstruktory(unittest.TestCase):
    def test_minor_to_glowne(self):
        self.assertEqual(Money(12345).major, Decimal("123.45"))

    def test_from_major_przyjmuje_napis_float_i_decimal(self):
        for value in ("123.45", 123.45, Decimal("123.45")):
            with self.subTest(value=value):
                self.assertEqual(Money.from_major(value).minor, 12345)

    def test_from_major_z_napisu_jest_dokladny(self):
        """0.1 + 0.2 na floatach daje 0.30000000000000004. Tu nie moze."""
        self.assertEqual(
            Money.from_major("0.1") + Money.from_major("0.2"),
            Money.from_major("0.3"),
        )

    def test_zaokraglanie_half_up_w_gore(self):
        self.assertEqual(Money.from_major("0.005").minor, 1)
        self.assertEqual(Money.from_major("1.235").minor, 124)

    def test_zaokraglanie_half_up_takze_dla_ujemnych(self):
        # ROUND_HALF_UP w Decimalu zaokragla od zera, wiec -0.005 -> -0.01.
        self.assertEqual(Money.from_major("-0.005").minor, -1)

    def test_zero(self):
        self.assertEqual(Money.zero("EUR"), Money(0, "EUR"))

    def test_odrzuca_float_jako_minor(self):
        with self.assertRaises(TypeError):
            Money(123.45)

    def test_odrzuca_bool_jako_minor(self):
        """bool jest podklasa int, wiec bez jawnego sprawdzenia przeszedlby."""
        with self.assertRaises(TypeError):
            Money(True)

    def test_odrzuca_zla_walute(self):
        for bad in ("", "PL", "PLNN"):
            with self.subTest(waluta=bad), self.assertRaises(ValueError):
                Money(100, bad)


class TestArytmetyka(unittest.TestCase):
    def test_dodawanie_i_odejmowanie(self):
        self.assertEqual(Money(100) + Money(250), Money(350))
        self.assertEqual(Money(100) - Money(250), Money(-150))

    def test_negacja_i_wartosc_bezwzgledna(self):
        self.assertEqual(-Money(100), Money(-100))
        self.assertEqual(abs(Money(-100)), Money(100))

    def test_mnozenie_zaokragla_half_up(self):
        self.assertEqual((Money(101) * 0.5).minor, 51)     # 50.5 -> 51
        self.assertEqual((Money(100) * Decimal("1.005")).minor, 101)

    def test_mnozenie_jest_przemienne(self):
        self.assertEqual(Money(100) * 3, 3 * Money(100))

    def test_dzielenie(self):
        self.assertEqual((Money(100) / 3).minor, 33)
        self.assertEqual((Money(101) / 2).minor, 51)       # 50.5 -> 51

    def test_dzielenie_przez_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Money(100) / 0

    def test_mnozenie_przez_bool_odrzucone(self):
        with self.assertRaises(TypeError):
            Money(100) * True

    def test_rozne_waluty_nie_sumuja_sie(self):
        with self.assertRaises(CurrencyMismatch):
            Money(100, "PLN") + Money(100, "EUR")

    def test_dodawanie_nie_money_zwraca_typeerror(self):
        with self.assertRaises(TypeError):
            Money(100) + 100


class TestPorownania(unittest.TestCase):
    def test_kolejnosc(self):
        self.assertLess(Money(100), Money(200))
        self.assertLessEqual(Money(100), Money(100))
        self.assertGreater(Money(200), Money(100))
        self.assertGreaterEqual(Money(200), Money(200))

    def test_porownanie_roznych_walut_wybucha(self):
        with self.assertRaises(CurrencyMismatch):
            Money(100, "PLN") < Money(100, "EUR")

    def test_porownanie_z_liczba_wybucha(self):
        """Cicha konwersja tutaj oznaczalaby porownanie groszy z zlotowkami."""
        with self.assertRaises(TypeError):
            Money(100) < 100

    def test_rownosc_rozroznia_walute(self):
        self.assertNotEqual(Money(100, "PLN"), Money(100, "EUR"))


class TestSuma(unittest.TestCase):
    def test_pusta_sekwencja_daje_zero_we_wskazanej_walucie(self):
        self.assertEqual(money_sum([], "EUR"), Money(0, "EUR"))

    def test_suma_tysiaca_kwot_nie_gubi_grosza(self):
        total = money_sum([Money.from_major("0.01")] * 1000)
        self.assertEqual(total, Money.from_major("10.00"))

    def test_suma_mieszanych_walut_wybucha(self):
        with self.assertRaises(CurrencyMismatch):
            money_sum([Money(100, "PLN"), Money(100, "EUR")])


class TestPrezentacja(unittest.TestCase):
    def test_str_i_repr(self):
        self.assertEqual(str(Money(12345)), "123.45 PLN")
        self.assertEqual(repr(Money(12345)), "Money(12345, 'PLN')")

    def test_to_json_niesie_obie_postacie(self):
        self.assertEqual(
            Money(12345).to_json(),
            {"minor": 12345, "currency": "PLN", "major": "123.45"},
        )

    def test_money_jest_hashowalny(self):
        """Mrozony, wiec musi dac sie trzymac w zbiorze -- klucze koszykow."""
        self.assertEqual(len({Money(100), Money(100), Money(200)}), 2)


if __name__ == "__main__":
    unittest.main()
