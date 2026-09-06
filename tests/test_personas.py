"""Persony -- cztery role czytajace te same raporty.

Najwazniejszy test w tym pliku dotyczy GRANICY UPRAWNIEN, a nie tresci promptu:
persona `komunikacja` nie moze widziec raportu z silnika kosztowego. Nie
dlatego, ze to niegrzeczne, tylko dlatego, ze pasazer nie ma prawa dowiedziec
sie z komunikatu, ze byl tanszym wariantem. Filtrowanie na poziomie doboru
raportow jest jedynym sposobem, ktory tego nie zalezy od dobrej woli modelu.
"""

import unittest

from lotis.ai_layer import personas
from lotis.ai_layer.personas import COMMON_RULES, Persona


class TestKatalog(unittest.TestCase):
    def test_sa_cztery_persony(self):
        self.assertEqual(len(personas.ALL), 4)

    def test_nazwy_sa_posortowane(self):
        self.assertEqual(personas.names(), sorted(personas.ALL))

    def test_domyslna_istnieje(self):
        self.assertIn(personas.DEFAULT, personas.ALL)

    def test_pobranie_po_nazwie(self):
        self.assertIs(personas.get("dyspozytor"), personas.DYSPOZYTOR)

    def test_pobranie_znosi_wielkosc_liter_i_spacje(self):
        self.assertIs(personas.get("  DYSPOZYTOR "), personas.DYSPOZYTOR)

    def test_nieznana_persona_wybucha_z_lista(self):
        with self.assertRaises(KeyError) as ctx:
            personas.get("nie-ma-takiej")
        self.assertIn("dyspozytor", str(ctx.exception))

    def test_pusta_nazwa_wybucha(self):
        with self.assertRaises(KeyError):
            personas.get("")

    def test_identyfikator_zgadza_sie_z_kluczem(self):
        for key, persona in personas.ALL.items():
            with self.subTest(persona=key):
                self.assertEqual(persona.id, key)


class TestKsztaltPersony(unittest.TestCase):
    def test_kazda_ma_komplet_pol(self):
        for persona in personas.ALL.values():
            with self.subTest(persona=persona.id):
                self.assertTrue(persona.name)
                self.assertTrue(persona.audience)
                self.assertTrue(persona.reads)
                self.assertTrue(persona.instruction.strip())
                self.assertTrue(persona.structure)

    def test_parametry_generowania_sa_sensowne(self):
        for persona in personas.ALL.values():
            with self.subTest(persona=persona.id):
                self.assertGreater(persona.max_tokens, 500)
                self.assertTrue(0.0 <= persona.temperature <= 1.0)

    def test_niska_temperatura_bo_to_raport_a_nie_esej(self):
        for persona in personas.ALL.values():
            with self.subTest(persona=persona.id):
                self.assertLessEqual(persona.temperature, 0.4)

    def test_persona_jest_mrozona(self):
        with self.assertRaises((AttributeError, TypeError)):
            personas.DYSPOZYTOR.name = "inna"


class TestPromptSystemowy(unittest.TestCase):
    def test_niesie_wspolne_reguly(self):
        for persona in personas.ALL.values():
            with self.subTest(persona=persona.id):
                self.assertIn(COMMON_RULES.strip()[:40], persona.system_prompt())

    def test_zakazuje_liczenia(self):
        """Zasada nadrzedna: silnik liczy, AI wyjasnia."""
        self.assertIn("NIE LICZYSZ", personas.DYSPOZYTOR.system_prompt())

    def test_nakazuje_przyznanie_sie_do_braku_danych(self):
        self.assertIn("brak danych w raporcie", personas.DYSPOZYTOR.system_prompt())

    def test_odbiera_prawo_do_decyzji(self):
        self.assertIn("Nie podejmujesz decyzji", personas.DYSPOZYTOR.system_prompt())

    def test_niesie_role_i_odbiorce(self):
        for persona in personas.ALL.values():
            prompt = persona.system_prompt()
            with self.subTest(persona=persona.id):
                self.assertIn(persona.name, prompt)
                self.assertIn(persona.audience, prompt)

    def test_niesie_narzucona_strukture_w_kolejnosci(self):
        prompt = personas.PRAWNIK.system_prompt()
        pozycje = [prompt.index(h) for h in personas.PRAWNIK.structure]
        self.assertEqual(pozycje, sorted(pozycje))

    def test_struktura_jest_numerowana(self):
        prompt = personas.ANALITYK.system_prompt()
        self.assertIn("1. " + personas.ANALITYK.structure[0], prompt)


class TestGraniceUprawnien(unittest.TestCase):
    def test_dyspozytor_widzi_wszystko(self):
        self.assertEqual(personas.DYSPOZYTOR.reads, ("*",))
        for node in ("01", "09", "12", "17"):
            with self.subTest(node=node):
                self.assertTrue(personas.DYSPOZYTOR.wants(node))

    def test_komunikacja_nie_widzi_silnika_kosztowego(self):
        """Pasazer nie ma prawa dowiedziec sie, ze byl tanszym wariantem."""
        for node in ("08", "09", "10", "11", "13"):
            with self.subTest(node=node):
                self.assertFalse(personas.KOMUNIKACJA.wants(node))

    def test_komunikacja_widzi_prawo_i_stan(self):
        self.assertTrue(personas.KOMUNIKACJA.wants("01"))
        self.assertTrue(personas.KOMUNIKACJA.wants("12"))

    def test_prawnik_widzi_filtr_prawny_i_log(self):
        self.assertTrue(personas.PRAWNIK.wants("12"))
        self.assertTrue(personas.PRAWNIK.wants("16"))

    def test_prawnik_nie_widzi_generatora_scenariuszy(self):
        self.assertFalse(personas.PRAWNIK.wants("07"))

    def test_analityk_widzi_koszt_i_kalibracje(self):
        for node in ("09", "10", "11", "17"):
            with self.subTest(node=node):
                self.assertTrue(personas.ANALITYK.wants(node))

    def test_zadna_persona_nie_odrzuca_wszystkiego(self):
        for persona in personas.ALL.values():
            widziane = [n for n in ("01", "02", "09", "12", "16", "17") if persona.wants(n)]
            with self.subTest(persona=persona.id):
                self.assertTrue(widziane)


class TestInstrukcje(unittest.TestCase):
    def test_komunikacja_zakazuje_ujawniania_kosztu(self):
        self.assertIn("kosztu wewnetrznego", personas.KOMUNIKACJA.instruction)

    def test_prawnik_wymaga_podstawy_przy_kazdej_kwocie(self):
        self.assertIn("podstawe prawna", personas.PRAWNIK.instruction)

    def test_prawnik_nie_proponuje_obejsc(self):
        self.assertIn("Nie proponujesz obejsc", personas.PRAWNIK.instruction)

    def test_analityk_rozroznia_tryby_liczenia(self):
        self.assertIn("MODIFYING", personas.ANALITYK.instruction)
        self.assertIn("RESTRUCTURING", personas.ANALITYK.instruction)

    def test_dyspozytor_zaczyna_od_degradacji(self):
        self.assertIn("degradacji", personas.DYSPOZYTOR.instruction)


class TestBudowaWlasnej(unittest.TestCase):
    def test_persona_bez_struktury_daje_krotszy_prompt(self):
        prosta = Persona(id="x", name="Test", audience="test", reads=("01",),
                         instruction="Zrob cos.")
        self.assertNotIn("Struktura odpowiedzi", prosta.system_prompt())

    def test_gwiazdka_oznacza_wszystkie_nodes(self):
        wszystko = Persona(id="x", name="T", audience="t", reads=("*",), instruction="i")
        self.assertTrue(wszystko.wants("99"))

    def test_lista_ogranicza_do_wymienionych(self):
        waska = Persona(id="x", name="T", audience="t", reads=("01",), instruction="i")
        self.assertTrue(waska.wants("01"))
        self.assertFalse(waska.wants("02"))


if __name__ == "__main__":
    unittest.main()
