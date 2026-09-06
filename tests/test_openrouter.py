"""Klient OpenRouter.

Wszystkie testy chodza na podstawionym `urlopen` -- zestaw nie ma prawa
dzwonic do zadnego API. Test, ktory wychodzi do sieci, przestaje byc testem
kodu i staje sie testem laczy.

Najwazniejsze jest tu rozroznienie bledow: 429 mija samo i ma sens ponowic,
401 nie mija i ponawianie go tylko marnuje czas oraz limit.
"""

import io
import json
import unittest
import urllib.error
from unittest import mock

from lotis.ai_layer.openrouter_client import (
    API_ROOT, DEFAULT_MODEL, RETRY_STATUS, Completion, OpenRouterClient, OpenRouterError,
)


def odpowiedz(payload: dict):
    """Atrapa obiektu zwracanego przez `urlopen`."""
    body = json.dumps(payload).encode("utf-8")
    fake = mock.MagicMock()
    fake.read.return_value = body
    fake.__enter__.return_value = fake
    fake.__exit__.return_value = False
    return fake


def blad_http(code: int, tresc: str = "blad"):
    return urllib.error.HTTPError(
        url="x", code=code, msg="err", hdrs=None, fp=io.BytesIO(tresc.encode()))


PELNA = {
    "model": "minimax/minimax-m3:free",
    "choices": [{"message": {"content": "  odpowiedz modelu  "},
                 "finish_reason": "stop"}],
    "usage": {"prompt_tokens": 120, "completion_tokens": 45},
}


class TestKonfiguracja(unittest.TestCase):
    def test_domyslny_model_jest_ustawiony(self):
        self.assertTrue(DEFAULT_MODEL)

    def test_model_da_sie_podac_wprost(self):
        self.assertEqual(OpenRouterClient(model="x/y").model, "x/y")

    def test_klucz_podany_wprost_wygrywa(self):
        self.assertEqual(OpenRouterClient(api_key="sk-test").api_key, "sk-test")

    def test_brak_klucza_mowi_gdzie_go_zalozyc(self):
        """`load_env` jest wyciszone celowo.

        Bez tego test zalezalby od tego, czy plik `.env` zostal juz wczytany
        w tym procesie: przy pierwszym wywolaniu `require` doczytalby go
        z dysku i przywrocil prawdziwy klucz uzytkownika, a test przechodzilby
        albo nie w zaleznosci od kolejnosci calego zestawu.
        """
        import os
        zachowany = os.environ.pop("OPENROUTER_API_KEY", None)
        try:
            with mock.patch("lotis.kernel.env.load_env", return_value={}):
                with self.assertRaises(RuntimeError) as ctx:
                    _ = OpenRouterClient().api_key
            self.assertIn("openrouter.ai/keys", str(ctx.exception))
        finally:
            if zachowany is not None:
                os.environ["OPENROUTER_API_KEY"] = zachowany

    def test_naglowki_niosa_autoryzacje_i_tytul(self):
        headers = OpenRouterClient(api_key="sk-test", title="LOTIS V1")._headers()
        self.assertEqual(headers["Authorization"], "Bearer sk-test")
        self.assertEqual(headers["X-Title"], "LOTIS V1")
        self.assertIn("json", headers["Content-Type"])


class TestWywolanie(unittest.TestCase):
    def setUp(self):
        self.client = OpenRouterClient(api_key="sk-test", model="test/model", max_retries=3)

    def test_poprawna_odpowiedz(self):
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(PELNA)):
            wynik = self.client.complete("system", "user")
        self.assertIsInstance(wynik, Completion)
        self.assertEqual(wynik.text, "odpowiedz modelu")      # przyciete spacje
        self.assertEqual(wynik.prompt_tokens, 120)
        self.assertEqual(wynik.completion_tokens, 45)
        self.assertEqual(wynik.total_tokens, 165)
        self.assertEqual(wynik.finish_reason, "stop")

    def test_wysyla_model_temperature_i_wiadomosci(self):
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(PELNA)) as up:
            self.client.complete("SYS", "USER", temperature=0.15, max_tokens=800)
        payload = json.loads(up.call_args[0][0].data.decode("utf-8"))
        self.assertEqual(payload["model"], "test/model")
        self.assertEqual(payload["temperature"], 0.15)
        self.assertEqual(payload["max_tokens"], 800)
        self.assertEqual([m["role"] for m in payload["messages"]], ["system", "user"])
        self.assertEqual(payload["messages"][1]["content"], "USER")

    def test_trafia_pod_wlasciwy_adres(self):
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(PELNA)) as up:
            self.client.complete("s", "u")
        self.assertEqual(up.call_args[0][0].full_url, f"{API_ROOT}/chat/completions")

    def test_odpowiedz_bez_wyboru_wybucha(self):
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz({"choices": []})):
            with self.assertRaises(OpenRouterError):
                self.client.complete("s", "u")

    def test_brakujace_zuzycie_daje_zera(self):
        payload = {"choices": [{"message": {"content": "x"}}]}
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(payload)):
            wynik = self.client.complete("s", "u")
        self.assertEqual(wynik.total_tokens, 0)

    def test_pusta_tresc_nie_wywala(self):
        payload = {"choices": [{"message": {"content": None}}]}
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(payload)):
            self.assertEqual(self.client.complete("s", "u").text, "")

    def test_polskie_znaki_przechodza(self):
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(PELNA)) as up:
            self.client.complete("s", "łańcuch rotacji, piątek")
        payload = json.loads(up.call_args[0][0].data.decode("utf-8"))
        self.assertIn("łańcuch", payload["messages"][1]["content"])


class TestPonawianie(unittest.TestCase):
    def setUp(self):
        self.client = OpenRouterClient(api_key="sk-test", max_retries=3)

    def test_lista_kodow_do_ponowienia(self):
        self.assertIn(429, RETRY_STATUS)
        self.assertIn(503, RETRY_STATUS)
        self.assertNotIn(401, RETRY_STATUS)
        self.assertNotIn(402, RETRY_STATUS)

    def test_429_jest_ponawiany_i_konczy_sie_sukcesem(self):
        proby = [blad_http(429), odpowiedz(PELNA)]
        def kolejno(*a, **k):
            wynik = proby.pop(0)
            if isinstance(wynik, Exception):
                raise wynik
            return wynik
        with mock.patch("urllib.request.urlopen", side_effect=kolejno), \
             mock.patch("time.sleep"):
            self.assertEqual(self.client.complete("s", "u").text, "odpowiedz modelu")

    def test_401_nie_jest_ponawiany(self):
        """Zly klucz nie mija sam -- ponawianie tylko marnuje limit."""
        with mock.patch("urllib.request.urlopen", side_effect=blad_http(401)) as up, \
             mock.patch("time.sleep"):
            with self.assertRaises(OpenRouterError) as ctx:
                self.client.complete("s", "u")
        self.assertEqual(up.call_count, 1)
        self.assertFalse(ctx.exception.retryable)
        self.assertEqual(ctx.exception.status, 401)

    def test_wyczerpanie_prob_wybucha(self):
        with mock.patch("urllib.request.urlopen", side_effect=blad_http(503)) as up, \
             mock.patch("time.sleep"):
            with self.assertRaises(OpenRouterError):
                self.client.complete("s", "u")
        self.assertEqual(up.call_count, 3)

    def test_blad_sieci_jest_ponawiany(self):
        with mock.patch("urllib.request.urlopen",
                        side_effect=urllib.error.URLError("brak sieci")) as up, \
             mock.patch("time.sleep"):
            with self.assertRaises(OpenRouterError):
                self.client.complete("s", "u")
        self.assertEqual(up.call_count, 3)

    def test_odstepy_rosna_wykladniczo(self):
        with mock.patch("urllib.request.urlopen", side_effect=blad_http(503)), \
             mock.patch("time.sleep") as sleep:
            with self.assertRaises(OpenRouterError):
                self.client.complete("s", "u")
        odstepy = [c[0][0] for c in sleep.call_args_list]
        self.assertEqual(odstepy, sorted(odstepy))
        self.assertGreater(odstepy[-1], odstepy[0])

    def test_tresc_bledu_trafia_do_wyjatku(self):
        with mock.patch("urllib.request.urlopen",
                        side_effect=blad_http(400, "zly model")):
            with self.assertRaises(OpenRouterError) as ctx:
                self.client.complete("s", "u")
        self.assertIn("zly model", str(ctx.exception))


class TestListaModeli(unittest.TestCase):
    KATALOG = {"data": [
        {"id": "z/model", "context_length": 8000},
        {"id": "a/model:free", "context_length": 32000},
        {"id": "b/model", "context_length": 16000},
    ]}

    def test_lista_jest_posortowana(self):
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(self.KATALOG)):
            ids = [m["id"] for m in OpenRouterClient(api_key="x").list_models()]
        self.assertEqual(ids, sorted(ids))

    def test_filtr_darmowych(self):
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(self.KATALOG)):
            ids = [m["id"] for m in OpenRouterClient(api_key="x").list_models(free_only=True)]
        self.assertEqual(ids, ["a/model:free"])

    def test_katalog_nie_wymaga_klucza(self):
        """Lista modeli jest publiczna -- `lotis models` ma dzialac bez konfiguracji."""
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz(self.KATALOG)) as up:
            OpenRouterClient(api_key=None, model="x/y").list_models()
        self.assertNotIn("Authorization", up.call_args[0][0].headers)

    def test_blad_sieci_daje_czytelny_komunikat(self):
        with mock.patch("urllib.request.urlopen",
                        side_effect=urllib.error.URLError("brak sieci")):
            with self.assertRaises(OpenRouterError) as ctx:
                OpenRouterClient(api_key="x").list_models()
        self.assertIn("/models", str(ctx.exception))

    def test_pusta_odpowiedz_daje_pusta_liste(self):
        with mock.patch("urllib.request.urlopen", return_value=odpowiedz({})):
            self.assertEqual(OpenRouterClient(api_key="x").list_models(), [])


if __name__ == "__main__":
    unittest.main()
