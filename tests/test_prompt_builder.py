"""Skladanie promptu z raportow runu.

Dwa niezmienniki maja tu znaczenie. Pierwszy: pula dozwolonych liczb pochodzi
z kanonicznych plikow `.json`, nie z tekstu promptu -- inaczej straznik
sprawdzalby model wzgledem tego, co model sam widzial, czyli wzgledem niczego.
Drugi: persona dostaje wylacznie raporty, ktore deklaruje, bo to jest granica
uprawnien, a nie optymalizacja kontekstu.
"""

import json
import tempfile
import unittest
from pathlib import Path

from lotis.ai_layer import personas
from lotis.ai_layer.prompt_builder import (
    MAX_USER_CHARS, NodeReport, allowed_numbers, build_prompt, find_runs,
    iter_numbers, latest_run, load_run,
)


def zapisz_run(directory: Path, nodes: list[tuple[str, str, dict]],
               manifest: dict | None = None) -> Path:
    run = directory / "run_test"
    run.mkdir(parents=True, exist_ok=True)
    for node_id, name, payload in nodes:
        full = {"schema": "lotis.report/v1",
                "node": {"id": node_id, "name": name, "title": name.upper()},
                "status": "ok", "numbers": {}, "findings": {},
                "decisions": [], "assumptions": [], "data_gaps": [], "warnings": [],
                **payload}
        (run / f"{node_id}_{name}.json").write_text(
            json.dumps(full, ensure_ascii=False), encoding="utf-8")
        (run / f"{node_id}_{name}.md").write_text(
            f"# [{node_id}] {name.upper()}\n\ntresc raportu {node_id}\n", encoding="utf-8")
    (run / "_manifest.json").write_text(
        json.dumps(manifest or {"run_id": "test", "snapshot": "sha256:abc",
                                "budget": {"level": "FULL"}}, ensure_ascii=False),
        encoding="utf-8")
    return run


class TestIterNumbers(unittest.TestCase):
    def test_liczby_proste(self):
        self.assertEqual(set(iter_numbers(42)), {42.0})
        self.assertEqual(set(iter_numbers(1.5)), {1.5})

    def test_bool_nie_jest_liczba(self):
        """`bool` jest podklasa `int` -- bez odsiania kazde `true` dawaloby jedynke."""
        self.assertEqual(list(iter_numbers(True)), [])
        self.assertEqual(list(iter_numbers(False)), [])

    def test_napis_dajacy_sie_sparsowac(self):
        """Kwoty serializuja sie jako {'major': '1234.56'}."""
        self.assertEqual(set(iter_numbers("1234.56")), {1234.56})

    def test_napis_z_przecinkiem(self):
        self.assertEqual(set(iter_numbers("1234,56")), {1234.56})

    def test_napis_nieliczbowy_jest_pomijany(self):
        self.assertEqual(list(iter_numbers("REBOOK-OAL")), [])

    def test_zagniezdzenie(self):
        payload = {"a": 1, "b": [2, {"c": 3}], "d": {"e": [4]}}
        self.assertEqual(set(iter_numbers(payload)), {1.0, 2.0, 3.0, 4.0})

    def test_none_jest_pomijany(self):
        self.assertEqual(list(iter_numbers(None)), [])

    def test_pula_zbiera_z_wielu_raportow(self):
        reports = (
            NodeReport("01", "a", "A", "ok", "", {"numbers": {"x": {"value": 10}}}),
            NodeReport("02", "b", "B", "ok", "", {"numbers": {"y": {"value": 20}}}),
        )
        self.assertTrue({10.0, 20.0} <= allowed_numbers(reports))


class TestWczytywanie(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_wczytuje_raporty_i_manifest(self):
        run = zapisz_run(self.dir, [("01", "snapshot", {}), ("02", "walidacja", {})])
        bundle = load_run(run)
        self.assertEqual(len(bundle.reports), 2)
        self.assertEqual(bundle.snapshot, "sha256:abc")
        self.assertEqual(bundle.degradation, "FULL")

    def test_manifest_nie_jest_obowiazkowy(self):
        run = zapisz_run(self.dir, [("01", "snapshot", {})])
        (run / "_manifest.json").unlink()
        bundle = load_run(run)
        self.assertEqual(len(bundle.reports), 1)
        self.assertEqual(bundle.run_id, "test")

    def test_raporty_sa_posortowane_po_identyfikatorze(self):
        run = zapisz_run(self.dir, [("09", "koszt", {}), ("01", "snapshot", {})])
        self.assertEqual([r.node_id for r in load_run(run).reports], ["01", "09"])

    def test_markdown_jest_wczytywany(self):
        run = zapisz_run(self.dir, [("01", "snapshot", {})])
        self.assertIn("tresc raportu 01", load_run(run).reports[0].markdown)

    def test_brak_markdownu_nie_wywala(self):
        run = zapisz_run(self.dir, [("01", "snapshot", {})])
        (run / "01_snapshot.md").unlink()
        self.assertEqual(load_run(run).reports[0].markdown, "")

    def test_nieistniejacy_katalog_wybucha(self):
        with self.assertRaises(FileNotFoundError):
            load_run(self.dir / "nie-ma")

    def test_katalog_bez_raportow_wybucha(self):
        pusty = self.dir / "run_pusty"
        pusty.mkdir()
        with self.assertRaises(FileNotFoundError):
            load_run(pusty)

    def test_stem_laczy_id_i_nazwe(self):
        run = zapisz_run(self.dir, [("01", "snapshot", {})])
        self.assertEqual(load_run(run).reports[0].stem, "01_snapshot")

    def test_find_runs_pomija_pliki_i_obce_katalogi(self):
        zapisz_run(self.dir, [("01", "a", {})])
        (self.dir / "inny_katalog").mkdir()
        (self.dir / "plik.txt").write_text("x", encoding="utf-8")
        self.assertEqual([p.name for p in find_runs(self.dir)], ["run_test"])

    def test_find_runs_na_pustym_katalogu(self):
        self.assertEqual(find_runs(self.dir / "nie-ma"), [])

    def test_latest_run_zwraca_none_gdy_pusto(self):
        self.assertIsNone(latest_run(self.dir))


class TestBudowaPromptu(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.run = zapisz_run(self.dir, [
            ("01", "snapshot", {"numbers": {"rejsy": {"value": 390, "unit": "szt"}}}),
            ("09", "koszt", {"numbers": {"koszt": {"value": 184320, "unit": "PLN"}}}),
            ("12", "filtr_prawny", {"numbers": {"odrzucone": {"value": 2, "unit": "szt"}}}),
        ])
        self.bundle = load_run(self.run)

    def tearDown(self):
        self.tmp.cleanup()

    def test_zwraca_pare_system_user(self):
        system, user = build_prompt(self.bundle, personas.DYSPOZYTOR)
        self.assertTrue(system)
        self.assertTrue(user)

    def test_naglowek_niesie_run_i_snapshot(self):
        _, user = build_prompt(self.bundle, personas.DYSPOZYTOR)
        self.assertIn("RUN test", user)
        self.assertIn("sha256:abc", user)

    def test_dyspozytor_dostaje_wszystkie_raporty(self):
        _, user = build_prompt(self.bundle, personas.DYSPOZYTOR)
        for node in ("01", "09", "12"):
            with self.subTest(node=node):
                self.assertIn(f"tresc raportu {node}", user)

    def test_komunikacja_nie_dostaje_raportu_kosztowego(self):
        """Granica uprawnien: model fizycznie nie ma z czego wypisac kosztu."""
        _, user = build_prompt(self.bundle, personas.KOMUNIKACJA)
        self.assertNotIn("tresc raportu 09", user)
        self.assertIn("tresc raportu 01", user)

    def test_pula_liczb_wyklucza_niewidoczne_raporty(self):
        """Straznik dla komunikacji nie moze dopuszczac kwoty z node 09."""
        widoczne = self.bundle.for_persona(personas.KOMUNIKACJA)
        self.assertNotIn(184320.0, allowed_numbers(widoczne))
        self.assertIn(390.0, allowed_numbers(widoczne))

    def test_prompt_niesie_liste_dozwolonych_liczb(self):
        _, user = build_prompt(self.bundle, personas.DYSPOZYTOR)
        self.assertIn("LICZBY, KTORE WOLNO CI ZACYTOWAC", user)
        self.assertIn("184320", user)

    def test_pytanie_dodatkowe_trafia_na_koniec(self):
        _, user = build_prompt(self.bundle, personas.DYSPOZYTOR, "Co z transferowymi?")
        self.assertTrue(user.rstrip().endswith("Co z transferowymi?"))

    def test_bez_pytania_jest_polecenie_domyslne(self):
        _, user = build_prompt(self.bundle, personas.DYSPOZYTOR)
        self.assertIn("zgodnie ze swoja rola", user)

    def test_persona_bez_zadnego_raportu_wybucha_z_lista(self):
        waski = zapisz_run(Path(self.tmp.name) / "b", [("09", "koszt", {})])
        bundle = load_run(waski)
        with self.assertRaises(ValueError) as ctx:
            build_prompt(bundle, personas.KOMUNIKACJA)
        self.assertIn("09", str(ctx.exception))

    def test_zatrzymany_przeplyw_jest_zapowiedziany(self):
        run = zapisz_run(Path(self.tmp.name) / "c", [("01", "a", {})],
                         manifest={"run_id": "c", "halted": True,
                                   "halt_reason": "brak dopuszczalnej opcji"})
        _, user = build_prompt(load_run(run), personas.DYSPOZYTOR)
        self.assertIn("przeplyw zatrzymany", user)

    def test_degradacja_jest_zapowiedziana(self):
        run = zapisz_run(Path(self.tmp.name) / "d", [("01", "a", {})],
                         manifest={"run_id": "d", "budget": {"level": "HARD_STOP"}})
        _, user = build_prompt(load_run(run), personas.DYSPOZYTOR)
        self.assertIn("nie zdazyl policzyc", user)

    def test_dlugi_prompt_miesci_sie_w_budzecie(self):
        wielki = zapisz_run(Path(self.tmp.name) / "e", [("01", "a", {})])
        (wielki / "01_a.md").write_text("x" * (MAX_USER_CHARS + 5000), encoding="utf-8")
        _, user = build_prompt(load_run(wielki), personas.DYSPOZYTOR)
        self.assertLessEqual(len(user), MAX_USER_CHARS)
        self.assertIn("raport skrocony", user)

    def test_skracanie_nie_gubi_ostatnich_raportow(self):
        """Wczesniej prompt ucinalo sie jednym cieciem na koncu -- dyspozytor
        tracil dokladnie LOG i WYNIK RZECZYWISTY, czyli dwa ostatnie etapy."""
        duzy = zapisz_run(Path(self.tmp.name) / "g",
                          [(f"{i:02d}", f"n{i}", {}) for i in range(1, 19)])
        for i in range(1, 19):
            (duzy / f"{i:02d}_n{i}.md").write_text(
                f"# raport {i:02d}\n" + "x" * 8000, encoding="utf-8")
        _, user = build_prompt(load_run(duzy), personas.DYSPOZYTOR)
        self.assertLessEqual(len(user), MAX_USER_CHARS)
        for i in (1, 9, 17, 18):
            with self.subTest(node=i):
                self.assertIn(f"# raport {i:02d}", user)

    def test_skracanie_zachowuje_poczatek_raportu(self):
        """Poczatek niesie status, podsumowanie i sekcje Liczby -- czyli
        wszystko, co model ma prawo zacytowac."""
        duzy = zapisz_run(Path(self.tmp.name) / "h",
                          [(f"{i:02d}", f"n{i}", {}) for i in range(1, 19)])
        for i in range(1, 19):
            (duzy / f"{i:02d}_n{i}.md").write_text(
                f"# raport {i:02d}\n\n## Liczby\n\nWAZNE-{i:02d}\n" + "x" * 8000,
                encoding="utf-8")
        _, user = build_prompt(load_run(duzy), personas.DYSPOZYTOR)
        for i in (1, 12, 18):
            with self.subTest(node=i):
                self.assertIn(f"WAZNE-{i:02d}", user)

    def test_krotkie_raporty_nie_sa_ruszane(self):
        _, user = build_prompt(self.bundle, personas.DYSPOZYTOR)
        self.assertNotIn("raport skrocony", user)

    def test_brak_markdownu_zastepuje_sie_json_em(self):
        run = zapisz_run(Path(self.tmp.name) / "f",
                         [("01", "a", {"numbers": {"x": {"value": 7, "unit": "szt"}}})])
        (run / "01_a.md").unlink()
        _, user = build_prompt(load_run(run), personas.DYSPOZYTOR)
        self.assertIn("`x`: 7", user)


if __name__ == "__main__":
    unittest.main()
