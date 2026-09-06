"""Prorata wartosci podrozy -- wspolna regula node 03 i node 08.

Ten modul powstal po audycie. Wczesniej kazdy z tych nodes mial wlasny podzial:
03 dzielil po dystansie, 08 po LICZBIE odcinkow. Node 11 odejmowal jedna miare
od drugiej i na siedmiu dobach dawalo to 30 przypadkow ujemnego przychodu,
a na pojedynczym pasazerze rozjazd siegal trzykrotnosci.

Testy nizej pilnuja trzech rzeczy: suma czesci rowna sie calosci co do grosza,
podzial idzie po dystansie, i obie strony silnika uzywaja tej samej funkcji.
"""

import unittest

from lotis.kernel.money import Money, money_sum
from lotis.kernel.prorate import distance_shares, split_value, value_on

from ._helpers import flight, itinerary, tiny_snapshot


class TestUdzialyDystansu(unittest.TestCase):
    def test_sumuja_sie_do_jedynki(self):
        snap = tiny_snapshot()
        self.assertAlmostEqual(sum(distance_shares(snap, ("F1", "F2"))), 1.0, places=9)

    def test_pojedynczy_odcinek_dostaje_calosc(self):
        self.assertEqual(distance_shares(tiny_snapshot(), ("F1",)), [1.0])

    def test_dluzszy_odcinek_dostaje_wiekszy_udzial(self):
        """WAW-FRA-JFK to nie sa dwa rowne kawalki -- dowoz do huba jest tanszy."""
        legs = [
            flight("KROTKI", "WAW", "KRK", 0, 60, seq=0),
            flight("DLUGI", "KRK", "JFK", 120, 600, seq=1),
        ]
        snap = tiny_snapshot(legs, airports={
            "WAW": _port("WAW", 52.17, 20.97),
            "KRK": _port("KRK", 50.08, 19.78),
            "JFK": _port("JFK", 40.64, -73.78),
        })
        krotki, dlugi = distance_shares(snap, ("KROTKI", "DLUGI"))
        self.assertLess(krotki, 0.05)
        self.assertGreater(dlugi, 0.95)

    def test_nieznany_odcinek_nie_wywala(self):
        udzialy = distance_shares(tiny_snapshot(), ("NIE-MA", "TEZ-NIE"))
        self.assertAlmostEqual(sum(udzialy), 1.0, places=9)

    def test_pusta_podroz_nie_dzieli_przez_zero(self):
        self.assertEqual(distance_shares(tiny_snapshot(), ()), [])


class TestPodzialWartosci(unittest.TestCase):
    def test_suma_czesci_rowna_sie_calosci(self):
        snap = tiny_snapshot()
        czesci = split_value(snap, itinerary("OD1", ("F1", "F2")), Money(100_00))
        self.assertEqual(money_sum(czesci.values()), Money(100_00))

    def test_domyka_sie_co_do_grosza_na_nierownym_podziale(self):
        """Kwota niepodzielna przez liczbe odcinkow nie moze gubic groszy."""
        snap = tiny_snapshot()
        for kwota in (1, 7, 33, 101, 999, 100_01):
            with self.subTest(kwota=kwota):
                czesci = split_value(snap, itinerary("OD1", ("F1", "F2")), Money(kwota))
                self.assertEqual(money_sum(czesci.values()), Money(kwota))

    def test_zachowuje_walute(self):
        snap = tiny_snapshot()
        czesci = split_value(snap, itinerary("OD1", ("F1",)), Money(100, "EUR"))
        self.assertEqual(czesci["F1"].currency, "EUR")

    def test_powtorzony_odcinek_nie_gubi_wartosci(self):
        snap = tiny_snapshot()
        czesci = split_value(snap, itinerary("OD1", ("F1", "F1")), Money(100_00))
        self.assertEqual(money_sum(czesci.values()), Money(100_00))


class TestWartoscNaOdcinkach(unittest.TestCase):
    def test_caly_zbior_daje_pelna_wartosc(self):
        snap = tiny_snapshot()
        itin = itinerary("OD1", ("F1", "F2"))
        self.assertEqual(value_on(snap, itin, Money(100_00), ("F1", "F2")), Money(100_00))

    def test_pusty_zbior_daje_zero(self):
        snap = tiny_snapshot()
        self.assertEqual(
            value_on(snap, itinerary("OD1", ("F1", "F2")), Money(100_00), ()),
            Money.zero())

    def test_odcinek_spoza_podrozy_nie_wnosi_nic(self):
        snap = tiny_snapshot()
        self.assertEqual(
            value_on(snap, itinerary("OD1", ("F1",)), Money(100_00), ("F2",)),
            Money.zero())

    def test_czesci_dopelniaja_sie_do_calosci(self):
        snap = tiny_snapshot()
        itin = itinerary("OD1", ("F1", "F2"))
        a = value_on(snap, itin, Money(100_00), ("F1",))
        b = value_on(snap, itin, Money(100_00), ("F2",))
        self.assertEqual(a + b, Money(100_00))


class TestSpojnoscSilnika(unittest.TestCase):
    """Oba nodes musza liczyc tym samym. To jest test, ktorego brakowalo."""

    def test_node_03_i_node_08_uzywaja_tej_samej_funkcji(self):
        import inspect

        from lotis.nodes import n03_baseline, n08_revenue
        self.assertIn("split_value", inspect.getsource(n03_baseline))
        self.assertIn("value_on", inspect.getsource(n08_revenue))

    def test_baseline_rejsu_rowna_sie_sumie_udzialow_pasazerow(self):
        """Najmocniejszy test spojnosci: agregat z node 03 musi sie zgadzac
        z suma indywidualnych udzialow liczonych funkcja z node 08."""
        import tempfile
        from pathlib import Path

        from lotis.kernel.node import Pipeline, RunContext
        from lotis.nodes import build_pipeline

        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            Pipeline(build_pipeline(weekday=4)).run(ctx)
            snap = ctx.require("snapshot")
            baseline = ctx.require("baseline")

        badane = sorted(baseline.per_flight, key=lambda k: -baseline.per_flight[k].minor)[:15]
        for flight_id in badane:
            suma = Money.zero()
            for pax in snap.passengers.values():
                itin = snap.itineraries.get(pax.itinerary_id)
                if itin and flight_id in itin.segments:
                    suma = suma + value_on(snap, itin, pax.value, (flight_id,))
            with self.subTest(rejs=flight_id):
                self.assertEqual(suma, baseline.of(flight_id))


def _port(iata, lat, lon):
    from lotis.kernel.contracts import Airport
    return Airport(iata=iata, icao="", tz_offset_min=0, lat=lat, lon=lon)


if __name__ == "__main__":
    unittest.main()
