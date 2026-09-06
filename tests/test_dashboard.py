"""Dashboard.

Testy chodza na prawdziwym serwerze podniesionym na porcie efemerycznym --
atrapa HTTP sprawdzalaby atrape, a nie routing.

Osobno sprawdzana jest sciezka, ktora latwo przeoczyc: identyfikator runu idzie
wprost z zapytania i sklada sie ze sciezka pliku. Bez kontroli `..` w tym polu
byloby czytaniem dowolnego katalogu na dysku.
"""

import json
import threading
import unittest
import urllib.error
import urllib.request

from lotis.dashboard.server import (
    INDEX, ApiError, DashboardServer, _int, _str, api_board, api_personas,
)


class TestPomocnicze(unittest.TestCase):
    def test_int_z_domyslna(self):
        self.assertEqual(_int({}, "day", 4, 0, 6), 4)

    def test_int_parsuje(self):
        self.assertEqual(_int({"day": ["2"]}, "day", 4, 0, 6), 2)

    def test_int_odrzuca_smieci(self):
        with self.assertRaises(ApiError):
            _int({"day": ["poniedzialek"]}, "day", 4, 0, 6)

    def test_int_pilnuje_zakresu(self):
        for wartosc in ("-1", "7"):
            with self.subTest(v=wartosc), self.assertRaises(ApiError):
                _int({"day": [wartosc]}, "day", 4, 0, 6)

    def test_str_wymaga_wartosci(self):
        self.assertEqual(_str({"id": ["abc"]}, "id"), "abc")
        for query in ({}, {"id": [""]}, {"id": ["   "]}):
            with self.subTest(q=query), self.assertRaises(ApiError):
                _str(query, "id")

    def test_apierror_niesie_kod(self):
        self.assertEqual(ApiError("x", 404).status, 404)
        self.assertEqual(ApiError("x").status, 400)


class TestEndpointyBezSerwera(unittest.TestCase):
    def test_mapa_ma_osiemnascie_etapow(self):
        d = api_board({})
        self.assertEqual(len(d["nodes"]), 18)
        for node in d["nodes"]:
            with self.subTest(node=node["id"]):
                self.assertTrue(node["tytul"])
                self.assertIsInstance(node["konsumuje"], list)

    def test_mapa_zawiera_node_z_luki(self):
        self.assertIn("15b", [n["id"] for n in api_board({})["nodes"]])

    def test_persony_maja_granice_uprawnien(self):
        d = api_personas({})
        komunikacja = next(p for p in d["personas"] if p["id"] == "komunikacja")
        self.assertNotIn("09", komunikacja["czyta"])


class TestWidok(unittest.TestCase):
    def test_plik_istnieje(self):
        self.assertTrue(INDEX.exists())

    def test_ma_tytul_i_skrypt(self):
        tresc = INDEX.read_text(encoding="utf-8")
        self.assertIn("<title>", tresc)
        self.assertIn("LOTIS", tresc)
        self.assertIn("</script>", tresc)

    def test_nie_ma_zewnetrznych_zaleznosci(self):
        """Dashboard ma dzialac bez internetu -- zadnych CDN-ow."""
        tresc = INDEX.read_text(encoding="utf-8")
        for wzorzec in ("src=\"http", "href=\"http", "cdn."):
            with self.subTest(wzorzec=wzorzec):
                self.assertNotIn(wzorzec, tresc)

    def test_modify_nie_podstawia_opcji_na_sztywno(self):
        """Znalezisko audytu: przy 'Modify' widok wysylal zawsze `CANCEL`,
        niezaleznie od tego, co czlowiek wskazal. System wykonywalby co innego,
        niz zostalo wybrane -- i zapisywal to w logu jako decyzje operatora."""
        tresc = INDEX.read_text(encoding="utf-8")
        self.assertNotIn('"MODIFY" ? "CANCEL"', tresc)
        self.assertIn('s-option', tresc)

    def test_krzywe_cudzyslowy_nie_trafily_do_atrybutow(self):
        """Krzywy cudzyslow w atrybucie po cichu psuje styl i nie daje bledu.

        Wzorzec musi uzywac kodow `\\u201c` i `\\u201d`, a nie samych znakow --
        wpisane doslownie zostaja znormalizowane do prostych cudzyslowow przy
        pierwszej edycji pliku i test przestaje sprawdzac cokolwiek.
        Wymagamy `\\w+=` przed cudzyslowem, zeby polska proza w tekscie
        strony mogla go uzywac swobodnie.
        """
        import re
        tresc = INDEX.read_text(encoding="utf-8")
        znalezione = re.findall(r"\w+=[“”‘’]", tresc)
        self.assertEqual(znalezione, [])


class TestSerwer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = DashboardServer("127.0.0.1", 0, quiet=True)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def get(self, path: str, timeout: float = 120.0):
        with urllib.request.urlopen(
                f"http://127.0.0.1:{self.port}{path}", timeout=timeout) as r:
            return r.status, r.read()

    def post(self, path: str, payload: dict, timeout: float = 300.0):
        request = urllib.request.Request(
            f"http://127.0.0.1:{self.port}{path}",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(request, timeout=timeout) as r:
            return r.status, json.loads(r.read())

    def blad(self, path: str, metoda: str = "GET", payload: dict | None = None):
        try:
            if metoda == "GET":
                self.get(path)
            else:
                self.post(path, payload or {})
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read())
        self.fail(f"{path} nie zwrocilo bledu")

    # ---- podstawy ----

    def test_strona_glowna(self):
        status, body = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn(b"LOTIS", body)

    def test_adres_serwera(self):
        self.assertTrue(self.server.url.startswith("http://127.0.0.1:"))

    def test_nieznana_sciezka_daje_404(self):
        code, payload = self.blad("/api/nie-ma")
        self.assertEqual(code, 404)
        self.assertIn("blad", payload)

    def test_nieznany_post_daje_404(self):
        self.assertEqual(self.blad("/api/nie-ma", "POST")[0], 404)

    # ---- endpointy ----

    def test_health(self):
        status, body = self.get("/api/health")
        d = json.loads(body)
        self.assertEqual(status, 200)
        self.assertTrue(d["gotowy"])
        self.assertIn("baza_parametryczna", d["zrodla"])
        self.assertIn("baza_operacyjna", d["zrodla"])

    def test_board(self):
        d = json.loads(self.get("/api/board")[1])
        self.assertEqual(len(d["nodes"]), 18)

    def test_personas(self):
        d = json.loads(self.get("/api/personas")[1])
        self.assertEqual(len(d["personas"]), 4)
        self.assertTrue(d["domyslna"])

    def test_stats(self):
        d = json.loads(self.get("/api/stats")[1])
        self.assertIn("odlot", d["globalna"])
        self.assertTrue(d["najgorsze_porty"])

    def test_flights(self):
        d = json.loads(self.get("/api/flights?day=4")[1])
        self.assertGreater(len(d["rejsy"]), 0)
        for rejs in d["rejsy"][:5]:
            with self.subTest(rejs=rejs["nr"]):
                self.assertIn("pasazerow", rejs)
                self.assertIn("ponizej", rejs)

    def test_flights_pilnuje_zakresu_dnia(self):
        self.assertEqual(self.blad("/api/flights?day=9")[0], 400)

    def test_snapshot(self):
        d = json.loads(self.get("/api/snapshot?day=4")[1])
        self.assertTrue(d["odcisk"].startswith("sha256:"))
        self.assertGreater(d["liczby"]["rejsy"], 0)

    def test_runs(self):
        d = json.loads(self.get("/api/runs")[1])
        self.assertIn("runs", d)

    # ---- bezpieczenstwo sciezek ----

    def test_wyjscie_poza_katalog_runow_jest_odrzucone(self):
        for zly in ("../../etc", "..%2F..%2Fetc", "run_../..", "a/b"):
            with self.subTest(id=zly):
                code, _ = self.blad(f"/api/run?id={zly}")
                self.assertIn(code, (400, 404))

    def test_nieistniejacy_run_daje_404(self):
        self.assertEqual(self.blad("/api/run?id=nie-ma-takiego")[0], 404)

    def test_nazwa_persony_nie_sklada_sciezki(self):
        """Znalezisko audytu: `persona` szla wprost z zapytania do sciezki pliku.

        `?persona=../../../../Windows/win.ini` dawalo sciezke poza katalogiem
        `out/`. Nie konczylo sie odczytem tylko dlatego, ze plik musialby miec
        koncowke `.json` -- czyli o bezpieczenstwie decydowal przypadek.
        """
        _, run = self.post("/api/run", {"day": 4, "delay": 90})
        for zla in ("../../../../Windows/win.ini", "..%2F..%2Fsecret",
                    "a/b", "nie-ma-takiej"):
            with self.subTest(persona=zla):
                code, payload = self.blad(
                    f"/api/ai?id={run['id']}&persona={zla}")
                self.assertEqual(code, 400)
                self.assertIn("persona", payload["blad"])

    def test_poprawna_persona_przechodzi(self):
        _, run = self.post("/api/run", {"day": 4, "delay": 90})
        self.post("/api/ai", {"run": run["id"], "dry_run": True,
                              "personas": ["dyspozytor"]})
        status, body = self.get(f"/api/ai?id={run['id']}&persona=dyspozytor")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["persona"], "dyspozytor")

    def test_brak_parametru_daje_400(self):
        self.assertEqual(self.blad("/api/run")[0], 400)

    # ---- cialo zadania ----

    def test_niepoprawny_json_daje_400(self):
        request = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/api/run", data=b"{to nie json",
            headers={"Content-Type": "application/json"}, method="POST")
        try:
            urllib.request.urlopen(request, timeout=30)
        except urllib.error.HTTPError as exc:
            self.assertEqual(exc.code, 400)
        else:
            self.fail("brak bledu")

    def test_cialo_niebedace_obiektem_daje_400(self):
        request = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/api/run", data=b"[1,2,3]",
            headers={"Content-Type": "application/json"}, method="POST")
        try:
            urllib.request.urlopen(request, timeout=30)
        except urllib.error.HTTPError as exc:
            self.assertEqual(exc.code, 400)
        else:
            self.fail("brak bledu")

    def test_zly_dzien_w_body_daje_400(self):
        self.assertEqual(self.blad("/api/run", "POST", {"day": 99})[0], 400)

    def test_zle_opoznienie_daje_400(self):
        self.assertEqual(self.blad("/api/run", "POST", {"delay": -5})[0], 400)

    def test_nieznana_decyzja_daje_400(self):
        self.assertEqual(self.blad("/api/run", "POST", {"decision": "MOZE"})[0], 400)

    # ---- pelny przebieg ----

    def test_uruchomienie_przeplywu(self):
        status, d = self.post("/api/run", {"day": 4, "delay": 180})
        self.assertEqual(status, 200)
        self.assertEqual(len(d["nodes"]), 18)
        self.assertTrue(d["ranking"])
        self.assertIsNotNone(d["karta"])
        self.assertTrue(d["snapshot"].startswith("sha256:"))

    def test_kwoty_wychodza_jako_obiekty_a_nie_napisy(self):
        """`json.dumps(default=str)` zamienial `Money` w napis "1234.56 PLN".

        Tekst wyswietlal sie poprawnie, wiec blad byl niewidoczny -- ale
        przegladarka liczyla szerokosc slupka z `Number("1234.56 PLN")`,
        czyli z NaN, i caly ranking mial slupki o zerowej szerokosci.
        """
        _, d = self.post("/api/run", {"day": 4, "delay": 180})
        for row in d["ranking"]:
            for pole in ("strata", "min", "max", "oszczednosc"):
                with self.subTest(opcja=row["opcja"], pole=pole):
                    self.assertIsInstance(row[pole], dict)
                    self.assertIn("minor", row[pole])
                    self.assertIsInstance(float(row[pole]["major"]), float)

    def test_karta_wychodzi_jako_obiekt_z_polami(self):
        _, d = self.post("/api/run", {"day": 4, "delay": 180})
        karta = d["karta"]
        self.assertIsInstance(karta, dict)
        self.assertTrue(karta["label"])
        self.assertIsInstance(karta["what_changes"], list)
        self.assertTrue(karta["authorization_role"])
        for pole in ("cost_low", "cost_expected", "cost_high"):
            with self.subTest(pole=pole):
                self.assertIsInstance(karta[pole], dict)

    def test_snapshot_zwraca_liczby_a_nie_napisy(self):
        d = json.loads(self.get("/api/snapshot?day=4")[1])
        for klucz, wartosc in d["liczby"].items():
            with self.subTest(pole=klucz):
                self.assertIsInstance(wartosc, (int, float))

    def test_run_jest_potem_widoczny_i_czytelny(self):
        _, run = self.post("/api/run", {"day": 4, "delay": 90})
        d = json.loads(self.get(f"/api/run?id={run['id']}")[1])
        self.assertEqual(len(d["raporty"]), 18)
        self.assertTrue(all(r["markdown"] for r in d["raporty"]))

    def test_ai_na_sucho_bez_klucza(self):
        _, run = self.post("/api/run", {"day": 4, "delay": 90})
        _, d = self.post("/api/ai", {"run": run["id"], "dry_run": True,
                                     "personas": ["dyspozytor"]})
        self.assertTrue(d["dry_run"])
        self.assertTrue(d["wyniki"][0]["prompt_chars"] > 100)

    def test_ai_bez_identyfikatora_runu_daje_400(self):
        self.assertEqual(self.blad("/api/ai", "POST", {"dry_run": True})[0], 400)


if __name__ == "__main__":
    unittest.main()
