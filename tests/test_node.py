"""Kontrakt node i przeplyw.

Klasa bazowa ma jedna twarda obietnice: `execute` nigdy nie propaguje wyjatku.
Node, ktory wybucha, zatrzymalby caly run i zostawil dyzurnego z tracebackiem
zamiast z raportem.
"""

import json
import tempfile
import unittest
from pathlib import Path

from lotis.kernel.budget import Degradation, RunBudget
from lotis.kernel.errors import DataGap, ExecutionFailure, NoLawfulOption
from lotis.kernel.node import Node, NodeOutput, Pipeline, RunContext
from lotis.kernel.report import Status


class Sprawny(Node):
    id, name, title = "01", "sprawny", "SPRAWNY"
    produces = "wynik"

    def run(self, ctx):
        report = self.new_report()
        report.number("licznik", 1, "szt")
        return NodeOutput(report, {"wynik": 42})


class Zalezny(Node):
    id, name, title = "02", "zalezny", "ZALEZNY"
    consumes = ("wynik",)

    def run(self, ctx):
        report = self.new_report()
        report.number("odczyt", ctx.require("wynik"), "szt")
        return NodeOutput(report)


class BezOpcji(Node):
    id, name, title = "03", "bezopcji", "BEZ OPCJI"

    def run(self, ctx):
        raise NoLawfulOption({"addressee": {"role": "Duty Manager OCC"}, "options": []})


class Niewykonalny(Node):
    id, name, title = "04", "niewykonalny", "NIEWYKONALNY"

    def run(self, ctx):
        raise ExecutionFailure("rezerwacja slotu", "port odmowil", recoverable=True)


class BrakDanych(Node):
    id, name, title = "05", "brakdanych", "BRAK DANYCH"

    def run(self, ctx):
        raise DataGap("kurs_walutowy", "brak notowania na dobe")


class Wybuchowy(Node):
    id, name, title = "06", "wybuchowy", "WYBUCHOWY"

    def run(self, ctx):
        raise ZeroDivisionError("dzielenie przez zero w node")


class Baza(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.ctx = RunContext("t", reports_root=Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()


class TestKontekst(Baza):
    def test_put_get_require(self):
        self.ctx.put("a", 1)
        self.assertEqual(self.ctx.get("a"), 1)
        self.assertEqual(self.ctx.require("a"), 1)

    def test_get_nieistniejacego_daje_domyslna(self):
        self.assertIsNone(self.ctx.get("nie-ma"))
        self.assertEqual(self.ctx.get("nie-ma", "domyslna"), "domyslna")

    def test_require_nieistniejacego_wybucha_z_nazwa_klucza(self):
        with self.assertRaises(KeyError) as e:
            self.ctx.require("kurs")
        self.assertIn("kurs", str(e.exception))

    def test_has_sprawdza_komplet(self):
        self.ctx.put("a", 1)
        self.assertTrue(self.ctx.has("a"))
        self.assertFalse(self.ctx.has("a", "b"))

    def test_halt_ustawia_powod_i_pakiet(self):
        self.ctx.halt("brak opcji", {"role": "OCC"})
        self.assertTrue(self.ctx.halted)
        self.assertEqual(self.ctx.escalation, {"role": "OCC"})

    def test_request_recalc(self):
        self.ctx.request_recalc("ETA_CHANGE")
        self.assertEqual(self.ctx.recalc_trigger, "ETA_CHANGE")


class TestWykonanie(Baza):
    def test_sprawny_node_zapisuje_stan_i_raport(self):
        report = Sprawny().execute(self.ctx)
        self.assertIs(report.status, Status.OK)
        self.assertEqual(self.ctx.get("wynik"), 42)
        self.assertTrue((self.ctx.writer.dir / "01_sprawny.json").exists())

    def test_mierzy_czas(self):
        self.assertGreater(Sprawny().execute(self.ctx).duration_ms, 0.0)

    def test_brak_wejscia_daje_blocked_zamiast_wyjatku(self):
        report = Zalezny().execute(self.ctx)
        self.assertIs(report.status, Status.BLOCKED)
        self.assertIn("wynik", report.summary)
        self.assertTrue(report.data_gaps)

    def test_kolejnosc_naprawia_brak_wejscia(self):
        Sprawny().execute(self.ctx)
        self.assertIs(Zalezny().execute(self.ctx).status, Status.OK)

    def test_po_zatrzymaniu_nastepne_nodes_nie_licza(self):
        self.ctx.halt("test")
        report = Sprawny().execute(self.ctx)
        self.assertIs(report.status, Status.BLOCKED)
        self.assertIsNone(self.ctx.get("wynik"))

    def test_brak_dopuszczalnej_opcji_zatrzymuje_i_niesie_pakiet(self):
        report = BezOpcji().execute(self.ctx)
        self.assertIs(report.status, Status.BLOCKED)
        self.assertTrue(self.ctx.halted)
        self.assertEqual(self.ctx.escalation["addressee"]["role"], "Duty Manager OCC")
        self.assertIn("escalation", report.findings)

    def test_niewykonalnosc_prosi_o_przeliczenie_ale_nie_zatrzymuje(self):
        """Node 15b: wykonanie nie powiodlo sie, ale run ma isc dalej."""
        report = Niewykonalny().execute(self.ctx)
        self.assertIs(report.status, Status.DEGRADED)
        self.assertFalse(self.ctx.halted)
        self.assertEqual(self.ctx.recalc_trigger, "EXECUTION_FAILED")
        self.assertEqual(self.ctx.get("execution_failure")["step"], "rezerwacja slotu")

    def test_brak_danych_blokuje_node(self):
        report = BrakDanych().execute(self.ctx)
        self.assertIs(report.status, Status.BLOCKED)
        self.assertIn("kurs_walutowy", report.data_gaps[0])
        self.assertFalse(self.ctx.halted)

    def test_wyjatek_spoza_rodziny_lotis_propaguje(self):
        """Blad programisty ma byc glosny, a nie zamieciony pod raport."""
        with self.assertRaises(ZeroDivisionError):
            Wybuchowy().execute(self.ctx)

    def test_budzet_degraduje_status(self):
        import time
        budget = RunBudget(total_ms=1000.0)
        budget._started = time.perf_counter() - 0.9
        ctx = RunContext("t", budget=budget, reports_root=Path(self.tmp.name))
        report = Sprawny().execute(ctx)
        self.assertIs(report.status, Status.DEGRADED)
        self.assertIs(ctx.degradation, Degradation.CACHED_NETWORK)
        self.assertTrue(report.warnings)

    def test_budzet_zapisuje_czas_per_node(self):
        Sprawny().execute(self.ctx)
        self.assertIn("01", self.ctx.budget.spent())


class TestPipeline(Baza):
    def test_uruchamia_po_kolei_i_pisze_manifest(self):
        reports = Pipeline([Sprawny(), Zalezny()]).run(self.ctx)
        self.assertEqual([r.node_id for r in reports], ["01", "02"])
        manifest = json.loads(
            (self.ctx.writer.dir / "_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["statuses"], {"01": "ok", "02": "ok"})
        self.assertIn("budget", manifest)

    def test_zatrzymanie_w_srodku_blokuje_reszte(self):
        reports = Pipeline([Sprawny(), BezOpcji(), Zalezny()]).run(self.ctx)
        self.assertEqual([r.status.value for r in reports], ["ok", "blocked", "blocked"])
        manifest = json.loads(
            (self.ctx.writer.dir / "_manifest.json").read_text(encoding="utf-8"))
        self.assertTrue(manifest["halted"])
        self.assertIsNotNone(manifest["escalation"])

    def test_pusty_przeplyw_nie_wybucha(self):
        self.assertEqual(Pipeline([]).run(self.ctx), [])
        self.assertTrue((self.ctx.writer.dir / "_manifest.json").exists())

    def test_manifest_niesie_odcisk_snapshotu(self):
        self.ctx.snapshot_digest = "sha256:abc"
        Pipeline([Sprawny()]).run(self.ctx)
        manifest = json.loads(
            (self.ctx.writer.dir / "_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["snapshot"], "sha256:abc")


if __name__ == "__main__":
    unittest.main()
