"""OUTPUT 2 -- spiecie warstwy AI.

Zestaw nie dzwoni nigdzie: albo idzie trybem na sucho, albo podstawia klienta.
Sprawdzane sa trzy rzeczy, ktore decyduja o tym, czy ta warstwa jest bezpieczna:
prompt powstaje bez klucza API, straznik dziala na kazdej odpowiedzi, a blad
jednej persony nie zatrzymuje pozostalych.
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from lotis.ai_layer.openrouter_client import Completion, OpenRouterError
from lotis.ai_layer.prompt_builder import load_run
from lotis.ai_layer.run_ai import AiOutput, run_all, run_directory, run_persona

from .test_prompt_builder import zapisz_run


class FakeClient:
    """Klient, ktory nie wychodzi poza proces."""

    def __init__(self, text: str = "Rejsow bylo 390.", model: str = "fake/model",
                 error: Exception | None = None) -> None:
        self.model = model
        self.text = text
        self.error = error
        self.calls: list[tuple[str, str]] = []

    def complete(self, system, user, **kw):
        self.calls.append((system, user))
        if self.error:
            raise self.error
        return Completion(text=self.text, model=self.model,
                          prompt_tokens=100, completion_tokens=20,
                          finish_reason="stop")


class Baza(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.run = zapisz_run(self.dir, [
            ("01", "snapshot", {"numbers": {"rejsy": {"value": 390, "unit": "szt"}}}),
            ("09", "koszt", {"numbers": {"koszt": {"value": 184320, "unit": "PLN"}}}),
            ("12", "filtr_prawny", {"numbers": {"odrzucone": {"value": 2, "unit": "szt"}}}),
        ])
        self.bundle = load_run(self.run)
        self.out = self.dir / "out"

    def tearDown(self):
        self.tmp.cleanup()


class TestTrybNaSucho(Baza):
    def test_dziala_bez_klucza_api(self):
        """Prompt ma sie skladac bez zadnej konfiguracji zewnetrznej."""
        wynik = run_persona(self.bundle, "dyspozytor", dry_run=True,
                            client=FakeClient(), out_root=self.out)
        self.assertTrue(wynik.ok)
        self.assertTrue(wynik.user)
        self.assertEqual(wynik.text, "")

    def test_nie_wola_modelu(self):
        klient = FakeClient()
        run_persona(self.bundle, "dyspozytor", dry_run=True,
                    client=klient, out_root=self.out)
        self.assertEqual(klient.calls, [])

    def test_zapisuje_prompt_do_pliku(self):
        wynik = run_persona(self.bundle, "dyspozytor", dry_run=True,
                            client=FakeClient(), out_root=self.out)
        sciezka = self.out / "run_test" / "dyspozytor.prompt.txt"
        self.assertTrue(sciezka.exists())
        tresc = sciezka.read_text(encoding="utf-8")
        self.assertIn("===== SYSTEM =====", tresc)
        self.assertIn("===== USER =====", tresc)
        self.assertIn("dyspozytor.prompt.txt", wynik.files)

    def test_nie_zapisuje_markdownu_bez_odpowiedzi(self):
        run_persona(self.bundle, "dyspozytor", dry_run=True,
                    client=FakeClient(), out_root=self.out)
        self.assertFalse((self.out / "run_test" / "dyspozytor.md").exists())

    def test_straznik_nie_uruchamia_sie_na_sucho(self):
        wynik = run_persona(self.bundle, "dyspozytor", dry_run=True,
                            client=FakeClient(), out_root=self.out)
        self.assertIsNone(wynik.guard)


class TestWywolanieModelu(Baza):
    def test_zapisuje_odpowiedz_i_metadane(self):
        wynik = run_persona(self.bundle, "dyspozytor",
                            client=FakeClient(), out_root=self.out)
        self.assertTrue(wynik.ok)
        self.assertEqual(wynik.text, "Rejsow bylo 390.")
        self.assertEqual(wynik.model, "fake/model")
        self.assertEqual(wynik.completion_tokens, 20)
        self.assertGreater(wynik.duration_ms, 0)

    def test_straznik_przepuszcza_liczbe_z_raportu(self):
        wynik = run_persona(self.bundle, "dyspozytor",
                            client=FakeClient("Rejsow bylo 390."), out_root=self.out)
        self.assertTrue(wynik.guard.clean)

    def test_straznik_lapie_liczbe_zmyslona(self):
        wynik = run_persona(self.bundle, "dyspozytor",
                            client=FakeClient("Koszt to 999999 PLN."), out_root=self.out)
        self.assertFalse(wynik.guard.clean)
        self.assertEqual(wynik.guard.errors[0].value, 999999.0)

    def test_straznik_pracuje_na_puli_widocznej_dla_persony(self):
        """Komunikacja nie widzi node 09, wiec 184320 jest dla niej liczba spoza raportow."""
        wynik = run_persona(self.bundle, "komunikacja",
                            client=FakeClient("Koszt 184320 PLN."), out_root=self.out)
        self.assertFalse(wynik.guard.clean)

    def test_zapisuje_markdown_z_adnotacja_straznika(self):
        run_persona(self.bundle, "dyspozytor",
                    client=FakeClient("Koszt to 999999 PLN."), out_root=self.out)
        tresc = (self.out / "run_test" / "dyspozytor.md").read_text(encoding="utf-8")
        self.assertIn("999999", tresc)
        self.assertIn("Kontrola straznika", tresc)

    def test_zapisuje_json_z_kompletem_pol(self):
        run_persona(self.bundle, "dyspozytor", client=FakeClient(), out_root=self.out)
        payload = json.loads(
            (self.out / "run_test" / "dyspozytor.json").read_text(encoding="utf-8"))
        for key in ("schema", "run_id", "persona", "model", "dry_run", "ok",
                    "guard", "text", "files"):
            with self.subTest(pole=key):
                self.assertIn(key, payload)

    def test_blad_modelu_jest_zapisany_a_nie_rzucony(self):
        wynik = run_persona(self.bundle, "dyspozytor",
                            client=FakeClient(error=OpenRouterError("limit")),
                            out_root=self.out)
        self.assertFalse(wynik.ok)
        self.assertIn("limit", wynik.error)
        self.assertEqual(wynik.text, "")

    def test_prompt_zapisuje_sie_takze_przy_bledzie(self):
        run_persona(self.bundle, "dyspozytor",
                    client=FakeClient(error=OpenRouterError("limit")), out_root=self.out)
        self.assertTrue((self.out / "run_test" / "dyspozytor.prompt.txt").exists())


class TestWszystkiePersony(Baza):
    def test_uruchamia_wszystkie(self):
        wyniki = run_all(self.bundle, dry_run=True,
                         client=FakeClient(), out_root=self.out)
        self.assertEqual(len(wyniki), 4)
        self.assertEqual({w.persona for w in wyniki},
                         {"analityk", "dyspozytor", "komunikacja", "prawnik"})

    def test_wybrane_persony(self):
        wyniki = run_all(self.bundle, ["prawnik"], dry_run=True,
                         client=FakeClient(), out_root=self.out)
        self.assertEqual([w.persona for w in wyniki], ["prawnik"])

    def test_nieznana_persona_nie_zatrzymuje_reszty(self):
        wyniki = run_all(self.bundle, ["nie-ma", "dyspozytor"], dry_run=True,
                         client=FakeClient(), out_root=self.out)
        self.assertEqual(len(wyniki), 2)
        self.assertFalse(wyniki[0].ok)
        self.assertTrue(wyniki[1].ok)

    def test_indeks_wypisuje_wszystkie_persony(self):
        run_all(self.bundle, dry_run=True, client=FakeClient(), out_root=self.out)
        index = json.loads(
            (self.out / "run_test" / "_index.json").read_text(encoding="utf-8"))
        self.assertEqual(index["run_id"], "test")
        self.assertEqual(len(index["personas"]), 4)
        self.assertEqual(index["snapshot"], "sha256:abc")

    def test_indeks_niesie_wynik_straznika(self):
        run_all(self.bundle, ["dyspozytor"],
                client=FakeClient("Koszt 999999."), out_root=self.out)
        index = json.loads(
            (self.out / "run_test" / "_index.json").read_text(encoding="utf-8"))
        self.assertFalse(index["personas"][0]["guard_clean"])

    def test_run_directory_przyjmuje_sciezke(self):
        wyniki = run_directory(self.run, ["dyspozytor"], dry_run=True,
                               client=FakeClient(), out_root=self.out)
        self.assertEqual(len(wyniki), 1)


class TestKsztaltWyniku(unittest.TestCase):
    def test_serializacja_nie_gubi_pol(self):
        wynik = AiOutput(run_id="r", persona="p", model="m", dry_run=True,
                         system="s", user="u")
        d = wynik.as_dict()
        self.assertEqual(d["schema"], "lotis.ai/v1")
        self.assertEqual(d["prompt_chars"], 1)
        self.assertIsNone(d["guard"])

    def test_na_sucho_bez_tresci_jest_poprawny(self):
        self.assertTrue(AiOutput("r", "p", "m", True, "s", "u").ok)

    def test_na_zywo_bez_tresci_nie_jest_poprawny(self):
        self.assertFalse(AiOutput("r", "p", "m", False, "s", "u").ok)

    def test_blad_unieważnia_wynik(self):
        self.assertFalse(AiOutput("r", "p", "m", True, "s", "u", error="cos").ok)


class TestObecnoscKlucza(unittest.TestCase):
    def test_wykrywa_brak_klucza(self):
        from lotis.ai_layer.run_ai import api_key_present
        with mock.patch("lotis.kernel.env.get", return_value=""):
            self.assertFalse(api_key_present())

    def test_wykrywa_obecnosc_klucza(self):
        from lotis.ai_layer.run_ai import api_key_present
        with mock.patch("lotis.kernel.env.get", return_value="sk-or-v1-abc"):
            self.assertTrue(api_key_present())


if __name__ == "__main__":
    unittest.main()
