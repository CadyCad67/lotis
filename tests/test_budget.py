"""Budzet czasu i drabina degradacji.

Sedno: system nigdy nie oddaje niczego. Po przekroczeniu progu schodzi o szczebel
i zwraca wynik oznaczony jako policzony pod presja czasu.
"""

import time
import unittest

from lotis.kernel.budget import Degradation, RunBudget


class TestDrabina(unittest.TestCase):
    def test_kolejnosc_szczebli(self):
        self.assertLess(Degradation.FULL, Degradation.REDUCED_SCENARIOS)
        self.assertLess(Degradation.REDUCED_SCENARIOS, Degradation.CACHED_NETWORK)
        self.assertLess(Degradation.CACHED_NETWORK, Degradation.HARD_STOP)

    def test_kazdy_szczebel_ma_opis(self):
        for level in Degradation:
            with self.subTest(level=level):
                self.assertTrue(level.label)


class TestProgi(unittest.TestCase):
    def poziom_przy(self, zuzycie: float) -> Degradation:
        """Budzet z rozciagnietym `_started`, zeby nie czekac naprawde."""
        budget = RunBudget(total_ms=1000.0)
        budget._started = time.perf_counter() - zuzycie
        return budget.level()

    def test_swiezy_budzet_jest_pelny(self):
        self.assertIs(RunBudget().level(), Degradation.FULL)

    def test_kolejne_progi(self):
        for zuzycie, oczekiwany in (
            (0.30, Degradation.FULL),
            (0.60, Degradation.REDUCED_SCENARIOS),
            (0.85, Degradation.CACHED_NETWORK),
            (0.99, Degradation.HARD_STOP),
            (5.00, Degradation.HARD_STOP),
        ):
            with self.subTest(zuzycie=zuzycie):
                self.assertIs(self.poziom_przy(zuzycie), oczekiwany)

    def test_dokladnie_na_progu_schodzi_nizej(self):
        """Prog jest domkniety od dolu -- 0.55 to juz zawezona siatka."""
        self.assertIs(self.poziom_przy(0.55), Degradation.REDUCED_SCENARIOS)

    def test_zerowy_budzet_to_natychmiast_twardy_stop(self):
        """Dzielenie przez zero nie moze wywalic silnika w polowie runu."""
        self.assertIs(RunBudget(total_ms=0.0).level(), Degradation.HARD_STOP)


class TestPomiar(unittest.TestCase):
    def test_record_sumuje_po_node(self):
        budget = RunBudget()
        budget.record("01", 10.0)
        budget.record("01", 5.0)
        budget.record("02", 3.0)
        self.assertEqual(budget.spent(), {"01": 15.0, "02": 3.0})

    def test_spent_zwraca_kopie(self):
        budget = RunBudget()
        budget.record("01", 10.0)
        budget.spent()["01"] = 999.0
        self.assertEqual(budget.spent()["01"], 10.0)

    def test_reset_czysci_licznik_i_zegar(self):
        budget = RunBudget(total_ms=1000.0)
        budget.record("01", 10.0)
        budget._started = time.perf_counter() - 5.0
        budget.reset()
        self.assertEqual(budget.spent(), {})
        self.assertIs(budget.level(), Degradation.FULL)

    def test_remaining_nie_schodzi_ponizej_zera(self):
        budget = RunBudget(total_ms=1.0)
        budget._started = time.perf_counter() - 10.0
        self.assertEqual(budget.remaining_ms, 0.0)

    def test_snapshot_ma_komplet_pol(self):
        budget = RunBudget()
        budget.record("01", 12.34)
        snap = budget.snapshot()
        self.assertEqual(
            set(snap),
            {"total_ms", "elapsed_ms", "remaining_ms", "level", "level_label", "per_node_ms"},
        )
        self.assertEqual(snap["per_node_ms"]["01"], 12.3)
        self.assertEqual(snap["level"], "FULL")


if __name__ == "__main__":
    unittest.main()
