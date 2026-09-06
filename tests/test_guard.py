"""Straznik liczb.

Wartosc straznika stoi na precyzji. Straznik, ktory podnosi alarm co dziesiata
liczbe, po tygodniu jest ignorowany i przestaje chronic przed czymkolwiek --
dlatego polowa testow nizej to tekst wierny, ktory NIE moze wzbudzic alarmu.

Wzorce zwolnien nie sa teoretyczne. Kazdy przypadek w `TestZwolnienia` pochodzi
z prawdziwej odpowiedzi modelu, ktora straznik oznaczyl blednie.
"""

import unittest

from lotis.ai_layer.guard import (
    EXEMPTIONS, Severity, annotate, check, parse_number, strip_exemptions,
)
from lotis.ai_layer.prompt_builder import NodeReport


def raport(numbers: dict, findings: dict | None = None) -> NodeReport:
    return NodeReport(
        node_id="01", node_name="test", title="TEST", status="ok", markdown="",
        payload={"numbers": {k: {"value": v, "unit": ""} for k, v in numbers.items()},
                 "findings": findings or {}},
    )


PROSTY = (raport({"rejsy": 390, "pasazerowie": 32911, "koszt": 184320.50}),)


class TestParsowanieLiczb(unittest.TestCase):
    def test_liczba_calkowita(self):
        self.assertEqual(parse_number("390"), 390.0)

    def test_przecinek_dziesietny(self):
        self.assertEqual(parse_number("12,43"), 12.43)

    def test_kropka_dziesietna(self):
        self.assertEqual(parse_number("12.43"), 12.43)

    def test_separator_tysiecy_spacja(self):
        self.assertEqual(parse_number("32 911"), 32911.0)

    def test_spacja_nierozdzielajaca(self):
        self.assertEqual(parse_number("32 911"), 32911.0)

    def test_zapis_polski_z_kropka_i_przecinkiem(self):
        self.assertEqual(parse_number("1.234,56"), 1234.56)

    def test_zapis_angielski_z_przecinkiem_i_kropka(self):
        self.assertEqual(parse_number("1,234.56"), 1234.56)

    def test_liczba_ujemna(self):
        self.assertEqual(parse_number("-22"), -22.0)

    def test_smieci_daja_none(self):
        self.assertIsNone(parse_number("abc"))
        self.assertIsNone(parse_number(""))


class TestZwolnienia(unittest.TestCase):
    """Kazdy przypadek pochodzi z realnej odpowiedzi modelu."""

    def zdjete(self, text: str) -> str:
        return strip_exemptions(text)[0]

    def test_odcisk_snapshotu(self):
        self.assertNotIn("f3c2", self.zdjete("sha256:f3c290f4e6930407fb2bcad856fc671f"))

    def test_identyfikator_runu_z_podkreslnikiem(self):
        self.assertNotIn("2026", self.zdjete("katalog run_20260905T164915"))

    def test_identyfikator_runu_bez_podkreslnika(self):
        """Model pisze `Run 20260905T164915` -- bez tego wzorca to sa dwie liczby."""
        self.assertNotIn("2026", self.zdjete("Run 20260905T164915, snapshot"))

    def test_data_iso_z_czasem_i_strefa(self):
        self.assertNotIn("2026", self.zdjete("ostatni przylot 2026-08-22T11:25:00+00:00"))

    def test_sama_data(self):
        self.assertNotIn("2026", self.zdjete("doba 2026-08-21"))

    def test_godzina(self):
        self.assertNotIn("23", self.zdjete("odlot o 23:45"))

    def test_numer_rejsu(self):
        self.assertNotIn("281", self.zdjete("rejs LO281 z Warszawy"))

    def test_znak_wywolawczy_z_dwoma_literami(self):
        """`LOT3AD` -- wczesniejszy wzorzec dopuszczal jedna litere i zostawial cyfre."""
        wynik = self.zdjete("znaki LOT3AD i LOT7LP")
        self.assertNotIn("3", wynik)
        self.assertNotIn("7", wynik)

    def test_znak_z_prefiksem_zrodla(self):
        self.assertNotIn("1155", self.zdjete("rejs znak:LOT1155 bez numeru"))

    def test_rejestracja(self):
        self.assertNotIn("7", self.zdjete("maszyna SP-LRA"))

    def test_rozporzadzenie_eu261(self):
        """`EU261` to nazwa aktu, nie wynik obliczenia."""
        for zapis in ("EU261", "EU 261", "EU261/2004"):
            with self.subTest(zapis=zapis):
                self.assertNotIn("261", self.zdjete(f"ekspozycja z {zapis} wynosi"))

    def test_akt_prawny_ze_slaszem(self):
        self.assertNotIn("2004", self.zdjete("rozporzadzenie 261/2004"))

    def test_artykul(self):
        self.assertNotIn("7", self.zdjete("Art. 7 rozporzadzenia"))
        self.assertNotIn("9", self.zdjete("Artykul 9 ust. 1"))

    def test_sygnatura_tsue(self):
        self.assertNotIn("402", self.zdjete("wyrok C-402/07"))

    def test_identyfikator_node(self):
        self.assertNotIn("09", self.zdjete("node 09 policzyl"))
        self.assertNotIn("12", self.zdjete("raport [12] mowi"))

    def test_wersja(self):
        self.assertNotIn("1", self.zdjete("silnik 1.0.0"))

    def test_numeracja_listy(self):
        self.assertNotIn("1", self.zdjete("1. SYTUACJA"))

    def test_naglowek_z_numerem(self):
        self.assertNotIn("2", self.zdjete("## 2. REKOMENDACJA"))

    def test_identyfikator_rekordu(self):
        self.assertNotIn("000123", self.zdjete("pasazer PAX000123"))

    def test_licznik_zwolnien_jest_raportowany(self):
        _, counts = strip_exemptions("LO281 o 14:30 dnia 2026-08-21")
        self.assertEqual(set(counts), {"numer rejsu", "godzina", "data ISO"})

    def test_kazdy_wzorzec_ma_etykiete(self):
        for label, pattern in EXEMPTIONS:
            with self.subTest(wzorzec=label):
                self.assertTrue(label)
                self.assertTrue(pattern)


class TestBrakFalszywychAlarmow(unittest.TestCase):
    """Tekst cytujacy wylacznie liczby z raportu nie moze wzbudzic alarmu."""

    def test_liczby_wprost_z_raportu(self):
        result = check("W siatce jest 390 rejsow i 32911 pasazerow.", PROSTY)
        self.assertTrue(result.clean)
        self.assertEqual(result.checked, 2)

    def test_separator_tysiecy_jest_rozpoznawany(self):
        """Model formatuje liczby po polsku -- 32 911 to nadal 32911."""
        self.assertTrue(check("Na pokladach 32 911 pasazerow.", PROSTY).clean)

    def test_kwota_z_przecinkiem_dziesietnym(self):
        self.assertTrue(check("Koszt to 184320,50 PLN.", PROSTY).clean)

    def test_pelna_wierna_odpowiedz(self):
        tekst = """\
1. SYTUACJA
Run 20260905T164915, snapshot sha256:f3c290f4e6930407fb2bcad856fc671f.
Doba 2026-08-21, pierwszy odlot o 04:20. W siatce 390 rejsow i 32 911 pasazerow.
Rejs LO281 wykonuje SP-LRA. Znaki bez numeru: LOT3AD, LOT7LP.
Podstawa: Art. 7 EU261, por. C-402/07. Silnik 1.0.0, node 01.
Koszt 184 320,50 PLN."""
        result = check(tekst, PROSTY)
        self.assertTrue(result.clean, [v.text for v in result.errors])

    def test_liczby_z_findings_tez_sa_dozwolone(self):
        reports = (raport({}, {"opcje": [{"koszt": 12345, "opoznienie": 47}]}),)
        self.assertTrue(check("Koszt 12345, opoznienie 47 minut.", reports).clean)

    def test_kwota_jako_napis_w_raporcie(self):
        """Money serializuje sie jako {'major': '1234.56'} -- napis tez jest liczba."""
        reports = (raport({"kwota": {"minor": 123456, "major": "1234.56"}}),)
        self.assertTrue(check("Kwota 1234.56 PLN.", reports).clean)

    def test_tekst_bez_liczb(self):
        result = check("Brak danych w raporcie.", PROSTY)
        self.assertEqual(result.checked, 0)
        self.assertTrue(result.clean)
        self.assertIn("nie zawiera", result.summary())


class TestWykrywanie(unittest.TestCase):
    def test_zmyslona_kwota(self):
        result = check("Koszt SWAP to 184 320 PLN.", (raport({"rejsy": 390}),))
        self.assertFalse(result.clean)
        self.assertEqual(result.errors[0].value, 184320.0)

    def test_wiele_zmyslonych_liczb(self):
        tekst = "SWAP 184320 PLN, rebooking 212480 PLN, roznica 28160 PLN, opoznienie 137 min."
        result = check(tekst, (raport({"rejsy": 390}),))
        self.assertEqual(len(result.errors), 4)

    def test_zepsuta_data_jest_wykrywana(self):
        """Model napisal `2026-22` zamiast `2026-08-22`. Wzorzec ISO nie zlapal,
        wiec fragmenty przeszly do skanu -- i tak ma byc."""
        result = check("ostatni przylot 2026-22T11:25", (raport({"rejsy": 390}),))
        self.assertFalse(result.clean)

    def test_zaokraglenie_to_ostrzezenie_a_nie_blad(self):
        result = check("Udzial 12,43%.", (raport({"udzial": 12.4321}),))
        self.assertTrue(result.clean)
        self.assertEqual(len(result.warnings), 1)
        self.assertIs(result.warnings[0].severity, Severity.WARN)

    def test_zaokraglenie_w_zla_strone_to_blad(self):
        """12.5 to inna liczba niz 12.43 -- czytelnik dostaje co innego."""
        result = check("Udzial 12,5%.", (raport({"udzial": 12.4321}),))
        self.assertFalse(result.clean)

    def test_bool_nie_staje_sie_dozwolona_jedynka(self):
        """`bool` jest podklasa `int` -- bez odsiania kazde `true` dawaloby 1."""
        result = check("Policzono 1 opcje.", (raport({"gotowe": True}),))
        self.assertFalse(result.clean)

    def test_ta_sama_liczba_zglaszana_raz(self):
        result = check("184320 tu i 184320 tam.", (raport({"rejsy": 390}),))
        self.assertEqual(len(result.errors), 1)

    def test_kontekst_wskazuje_miejsce(self):
        result = check("Rekomendujemy SWAP za 184320 PLN dzisiaj.", (raport({"x": 1}),))
        self.assertIn("SWAP", result.errors[0].context)

    def test_dodatkowa_pula_dozwolonych(self):
        result = check("Wartosc 999.", (raport({"x": 1}),), extra_allowed={999.0})
        self.assertTrue(result.clean)

    def test_pusta_pula_wszystko_zglasza(self):
        result = check("Wartosc 42.", (raport({}),))
        self.assertEqual(len(result.errors), 1)


class TestWynik(unittest.TestCase):
    def test_podsumowanie_czystego_wyniku(self):
        self.assertIn("Wszystkie", check("390 rejsow.", PROSTY).summary())

    def test_podsumowanie_z_naruszeniami(self):
        summary = check("999 rejsow.", PROSTY).summary()
        self.assertIn("spoza raportow", summary)

    def test_serializacja_ma_komplet_pol(self):
        d = check("999 rejsow.", PROSTY).as_dict()
        for key in ("clean", "checked", "allowed_pool", "exempted",
                    "errors", "warnings", "summary"):
            self.assertIn(key, d)

    def test_bledy_i_ostrzezenia_sa_rozdzielone(self):
        result = check("999 i 12,43", (raport({"udzial": 12.4321}),))
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(len(result.warnings), 1)


class TestAdnotacja(unittest.TestCase):
    def test_zachowuje_tresc_odpowiedzi(self):
        tekst = "Oryginalna tresc modelu."
        self.assertIn(tekst, annotate(tekst, check(tekst, PROSTY)))

    def test_dopisuje_sekcje_straznika(self):
        self.assertIn("Kontrola straznika", annotate("390 rejsow.", check("390 rejsow.", PROSTY)))

    def test_wypisuje_naruszenia_zamiast_je_kasowac(self):
        """Ciche skasowanie odebraloby czlowiekowi informacje, co model napisal."""
        tekst = "Koszt 999999 PLN."
        out = annotate(tekst, check(tekst, PROSTY))
        self.assertIn("999999", out)
        self.assertIn("nie ma w raportach", out)

    def test_wypisuje_zdjete_wzorce(self):
        tekst = "Rejs LO281 o 14:30."
        self.assertIn("numer rejsu", annotate(tekst, check(tekst, PROSTY)))


if __name__ == "__main__":
    unittest.main()
