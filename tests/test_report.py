"""Koperta raportu -- jedyny styk silnika ze swiatem.

Osiemnascie nodes zapisuje ten sam ksztalt. Gdyby `.json` i `.md` renderowaly
sie osobno, model cytowalby liczby z narracji, a czlowiek z kanonicznego pliku
i po tygodniu nikt nie wiedzialby, ktora wersja jest prawdziwa.
"""

import json
import tempfile
import unittest
from datetime import UTC, datetime
from decimal import Decimal
from pathlib import Path

from lotis.kernel.contracts import Cabin
from lotis.kernel.money import Money
from lotis.kernel.report import Report, ReportWriter, Status, to_jsonable
from lotis.kernel.versions import REPORT_SCHEMA


def raport() -> Report:
    return Report(node_id="09", node_name="koszt", node_title="COST ENGINE")


class TestBudowanie(unittest.TestCase):
    def test_number_zawsze_niesie_jednostke(self):
        r = raport()
        r.number("koszt", 1234, "PLN")
        self.assertEqual(r.numbers["koszt"], {"value": 1234, "unit": "PLN"})

    def test_number_bez_jednostki_zapisuje_pusty_napis(self):
        r = raport()
        r.number("licznik", 7)
        self.assertEqual(r.numbers["licznik"]["unit"], "")

    def test_number_sprowadza_money_do_json(self):
        r = raport()
        r.number("kwota", Money(12345), "PLN")
        self.assertEqual(r.numbers["kwota"]["value"]["minor"], 12345)

    def test_ostrzezenie_degraduje_status(self):
        r = raport()
        self.assertIs(r.status, Status.OK)
        r.warn("cos jest nie tak")
        self.assertIs(r.status, Status.DEGRADED)

    def test_ostrzezenie_nie_podnosi_statusu_z_blocked(self):
        """BLOCKED jest gorszy niz DEGRADED -- ostrzezenie nie moze go poprawic."""
        r = raport()
        r.status = Status.BLOCKED
        r.warn("kolejne ostrzezenie")
        self.assertIs(r.status, Status.BLOCKED)

    def test_zalozenie_ma_zrodlo_i_pewnosc(self):
        r = raport()
        r.assume("kurs", "policy", 0.5, "placeholder w bazie")
        self.assertEqual(r.assumptions[0].source, "policy")
        self.assertEqual(r.assumptions[0].confidence, 0.5)


class TestToJsonable(unittest.TestCase):
    def test_typy_proste_przechodza(self):
        for value in (None, "tekst", 1, 1.5, True):
            with self.subTest(value=value):
                self.assertEqual(to_jsonable(value), value)

    def test_money_enum_data_decimal(self):
        self.assertEqual(to_jsonable(Money(100))["minor"], 100)
        self.assertEqual(to_jsonable(Cabin.BUSINESS), "J")
        self.assertEqual(to_jsonable(datetime(2026, 8, 21, tzinfo=UTC))[:10], "2026-08-21")
        self.assertEqual(to_jsonable(Decimal("1.5")), "1.5")

    def test_zbior_jest_sortowany_dla_powtarzalnosci(self):
        """Bez sortowania ten sam raport dawalby inny odcisk przy kazdym uruchomieniu."""
        self.assertEqual(to_jsonable({"c", "a", "b"}), ["a", "b", "c"])

    def test_krotka_staje_sie_lista(self):
        self.assertEqual(to_jsonable((1, 2)), [1, 2])

    def test_klucze_slownika_staja_sie_napisami(self):
        self.assertEqual(to_jsonable({1: "a"}), {"1": "a"})

    def test_zagniezdzenie(self):
        self.assertEqual(
            to_jsonable({"a": [Money(100), {"b": Cabin.ECONOMY}]}),
            {"a": [{"minor": 100, "currency": "PLN", "major": "1.00"}, {"b": "Y"}]},
        )

    def test_cykl_w_danych_nie_wywala_rekurencji(self):
        """Znalezisko audytu: cykl konczyl sie `RecursionError`, czyli awaria
        calego runu zamiast degradacji jednego node. `to_jsonable` jest jedynym
        wyjsciem raportu na dysk, wiec nie ma prawa sie wywrocic."""
        petla: dict = {"a": 1}
        petla["self"] = petla
        wynik = to_jsonable(petla)
        self.assertEqual(wynik["a"], 1)
        self.assertIn("cykl", str(wynik["self"]))

    def test_cykl_w_liscie(self):
        lista: list = [1, 2]
        lista.append(lista)
        self.assertIn("cykl", str(to_jsonable(lista)[2]))

    def test_ten_sam_obiekt_dwa_razy_obok_siebie_nie_jest_cyklem(self):
        """Wspoldzielony obiekt to nie petla -- oba wystapienia maja byc pelne."""
        wspolny = {"x": 1}
        wynik = to_jsonable({"a": wspolny, "b": wspolny})
        self.assertEqual(wynik["a"], {"x": 1})
        self.assertEqual(wynik["b"], {"x": 1})

    def test_raport_z_cyklem_da_sie_zapisac(self):
        import json as _json
        r = raport()
        petla: dict = {}
        petla["self"] = petla
        r.findings["petla"] = petla
        _json.dumps(r.to_dict())        # nie moze rzucic

    def test_nieznany_obiekt_ladnie_ladnie_do_napisu(self):
        class Cos:
            def __str__(self): return "cos"
        self.assertEqual(to_jsonable(Cos()), "cos")

    def test_caly_raport_jest_serializowalny(self):
        r = raport()
        r.number("kwota", Money(100), "PLN")
        r.findings["zbior"] = {"b", "a"}
        r.findings["data"] = datetime(2026, 8, 21, tzinfo=UTC)
        json.dumps(r.to_dict())          # nie moze rzucic


class TestSerializacja(unittest.TestCase):
    def test_dict_ma_komplet_pol(self):
        d = raport().to_dict()
        for key in ("schema", "run_id", "node", "versions", "snapshot", "status",
                    "degradation", "summary", "numbers", "findings", "decisions",
                    "assumptions", "data_gaps", "warnings", "duration_ms"):
            self.assertIn(key, d)
        self.assertEqual(d["schema"], REPORT_SCHEMA)

    def test_markdown_zawiera_wszystkie_liczby(self):
        r = raport()
        r.number("koszt", 184320, "PLN")
        r.number("opoznienie", 137, "min")
        md = r.to_markdown()
        self.assertIn("koszt", md)
        self.assertIn("184 320", md)     # separator tysiecy z `_fmt`
        self.assertIn("137", md)

    def test_markdown_ma_wszystkie_sekcje(self):
        r = raport()
        r.summary = "podsumowanie"
        r.number("x", 1, "szt")
        r.decide("ustalenie")
        r.findings["szczegol"] = {"klucz": "wartosc"}
        r.assume("pole", "real")
        r.data_gaps.append("brak")
        r.warn("ostrzezenie")
        md = r.to_markdown()
        for naglowek in ("# [09] COST ENGINE", "## Liczby", "## Co ten node ustalil",
                         "## Szczegoly", "## Zalozenia", "## Braki danych",
                         "## Ostrzezenia"):
            self.assertIn(naglowek, md)

    def test_markdown_bez_tresci_nie_ma_pustych_sekcji(self):
        md = raport().to_markdown()
        self.assertNotIn("## Liczby", md)
        self.assertNotIn("## Ostrzezenia", md)

    def test_markdown_oznacza_tryb_degradacji(self):
        r = raport()
        r.degradation = "HARD_STOP"
        self.assertIn("HARD_STOP", r.to_markdown())

    def test_findings_z_lista_slownikow_ma_naglowki(self):
        r = raport()
        r.findings["opcje"] = [{"id": "OPT1", "koszt": 100}]
        md = r.to_markdown()
        self.assertIn("OPT1", md)
        self.assertIn("koszt", md)


class TestWriter(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.writer = ReportWriter("test123", Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def test_zapisuje_obie_formy(self):
        path = self.writer.write(raport())
        self.assertTrue(path.exists())
        self.assertTrue(path.with_suffix(".md").exists())
        self.assertEqual(path.name, "09_koszt.json")

    def test_katalog_niesie_identyfikator_runu(self):
        self.assertEqual(self.writer.dir.name, "run_test123")

    def test_wstrzykuje_run_id_snapshot_i_tryb(self):
        r = raport()
        self.writer.write(r, snapshot="sha256:abc", degradation="HARD_STOP")
        self.assertEqual(r.run_id, "test123")
        self.assertEqual(r.snapshot, "sha256:abc")
        self.assertEqual(r.degradation, "HARD_STOP")

    def test_obie_formy_maja_te_same_liczby(self):
        """Jedyna gwarancja, ze narracja nie rozjedzie sie z kanonem."""
        r = raport()
        r.number("koszt", 184320, "PLN")
        path = self.writer.write(r)
        payload = json.loads(path.read_text(encoding="utf-8"))
        md = path.with_suffix(".md").read_text(encoding="utf-8")
        self.assertEqual(payload["numbers"]["koszt"]["value"], 184320)
        self.assertIn("184 320", md)

    def test_manifest_zbiera_wszystkie_wpisy(self):
        self.writer.write(raport())
        second = Report("10", "siec", "NETWORK IMPACT")
        second.warn("uwaga")
        self.writer.write(second)
        manifest = json.loads(self.writer.write_manifest().read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["nodes"]), 2)
        self.assertEqual(manifest["run_id"], "test123")
        self.assertEqual(manifest["nodes"][1]["warnings"], 1)

    def test_manifest_przyjmuje_dodatkowe_pola(self):
        self.writer.write(raport())
        manifest = json.loads(
            self.writer.write_manifest({"halted": True}).read_text(encoding="utf-8"))
        self.assertTrue(manifest["halted"])

    def test_odcisk_wpisu_zmienia_sie_z_trescia(self):
        first = self.writer.write(raport())
        digest_a = self.writer.entries[0]["digest"]
        other = raport()
        other.number("cos", 1, "szt")
        self.writer.write(other)
        self.assertNotEqual(digest_a, self.writer.entries[1]["digest"])
        self.assertTrue(first.exists())

    def test_paths_wypisuje_zapisane_pliki(self):
        self.writer.write(raport())
        self.writer.write_manifest()
        self.assertEqual(
            {p.name for p in self.writer.paths()}, {"09_koszt.json", "_manifest.json"})

    def test_utf8_w_polskich_znakach(self):
        r = raport()
        r.summary = "Zamrożony stan piątek — łańcuch rotacji"
        path = self.writer.write(r)
        self.assertIn("łańcuch", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
