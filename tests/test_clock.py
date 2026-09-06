"""Zegar runu i doba operacyjna.

Doba operacyjna zaczyna sie o 04:00, a nie o polnocy. Rejs o 01:15 nalezy do
poprzedniego dnia pracy -- gdyby liczyc kalendarzowo, horyzont propagacji
urwalby sie w srodku nocnej fali.
"""

import unittest
from datetime import UTC, datetime, timedelta

from lotis.kernel.clock import RunClock, operational_day_bounds


class TestRunClock(unittest.TestCase):
    def test_zamrozony_czas_nie_plynie(self):
        clock = RunClock()
        self.assertEqual(clock.now(), clock.now())

    def test_wymaga_strefy(self):
        with self.assertRaises(ValueError):
            RunClock(datetime(2026, 8, 21, 12, 0))

    def test_normalizuje_do_utc(self):
        from zoneinfo import ZoneInfo
        warsaw = datetime(2026, 8, 21, 14, 0, tzinfo=ZoneInfo("Europe/Warsaw"))
        self.assertEqual(RunClock(warsaw).now().hour, 12)   # lato: UTC+2

    def test_minutes_until_dodatnie_i_ujemne(self):
        now = datetime(2026, 8, 21, 12, 0, tzinfo=UTC)
        clock = RunClock(now)
        self.assertAlmostEqual(clock.minutes_until(now + timedelta(minutes=90)), 90.0)
        self.assertAlmostEqual(clock.minutes_until(now - timedelta(minutes=30)), -30.0)

    def test_minutes_until_odrzuca_czas_bez_strefy(self):
        with self.assertRaises(ValueError):
            RunClock().minutes_until(datetime(2026, 8, 21, 12, 0))

    def test_repr_niesie_czas(self):
        self.assertIn("2026-08-21", repr(RunClock(datetime(2026, 8, 21, 12, 0, tzinfo=UTC))))


class TestDobaOperacyjna(unittest.TestCase):
    def test_wymaga_strefy(self):
        with self.assertRaises(ValueError):
            operational_day_bounds(datetime(2026, 8, 21, 12, 0))

    def test_doba_trwa_dokladnie_24h(self):
        start, end = operational_day_bounds(datetime(2026, 8, 21, 12, 0, tzinfo=UTC))
        self.assertEqual(end - start, timedelta(days=1))

    def test_moment_lezy_w_swojej_dobie(self):
        moment = datetime(2026, 8, 21, 12, 0, tzinfo=UTC)
        start, end = operational_day_bounds(moment)
        self.assertLessEqual(start, moment)
        self.assertLess(moment, end)

    def test_przed_czwarta_nalezy_do_poprzedniej_doby(self):
        """03:59 to jeszcze wczoraj, 04:00 to juz dzis. Tu jest cala roznica."""
        wczoraj = operational_day_bounds(datetime(2026, 8, 21, 3, 59, tzinfo=UTC))
        dzis = operational_day_bounds(datetime(2026, 8, 21, 4, 0, tzinfo=UTC))
        self.assertEqual(wczoraj[0].date(), datetime(2026, 8, 20).date())
        self.assertEqual(dzis[0].date(), datetime(2026, 8, 21).date())
        self.assertEqual(wczoraj[1], dzis[0])

    def test_przesuniecie_strefy_przesuwa_granice(self):
        moment = datetime(2026, 8, 21, 12, 0, tzinfo=UTC)
        utc_start, _ = operational_day_bounds(moment, 0)
        waw_start, _ = operational_day_bounds(moment, 120)
        self.assertEqual(utc_start - waw_start, timedelta(minutes=120))

    def test_rejs_o_pierwszej_w_nocy_nalezy_do_wczorajszej_doby(self):
        nocny = datetime(2026, 8, 22, 1, 15, tzinfo=UTC)
        wieczorny = datetime(2026, 8, 21, 22, 0, tzinfo=UTC)
        self.assertEqual(operational_day_bounds(nocny), operational_day_bounds(wieczorny))

    def test_ujemne_przesuniecie(self):
        """Strefy zachodnie: -300 min to Nowy Jork zima."""
        start, end = operational_day_bounds(datetime(2026, 1, 21, 12, 0, tzinfo=UTC), -300)
        self.assertEqual(end - start, timedelta(days=1))
        self.assertEqual(start.hour, 9)                # 04:00 lokalnie = 09:00 UTC


if __name__ == "__main__":
    unittest.main()
