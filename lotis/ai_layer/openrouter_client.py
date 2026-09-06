"""Klient OpenRouter -- OUTPUT 2.

Zwykly HTTP na `urllib` ze stdlib. OpenRouter wystawia API zgodne z OpenAI,
wiec cale wywolanie to jeden POST z lista wiadomosci.

Model NIE jest zaszyty w kodzie. Siedzi w `LOTIS_AI_MODEL` w pliku `.env`,
zeby dalo sie wkleic dowolny slug z openrouter.ai/models bez dotykania
zrodel. `cli.py models` pobiera zywa liste, wiec nie trzeba zgadywac nazw.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any

from . import env

API_ROOT = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "minimax/minimax-m3:free"
DEFAULT_TIMEOUT = 120.0

#: Kody, przy ktorych ma sens ponowic. 402 i 401 nie -- to nie mija samo.
RETRY_STATUS = frozenset({408, 409, 429, 500, 502, 503, 504})


class OpenRouterError(RuntimeError):
    """Blad wywolania. Niesie kod HTTP, jesli byl."""

    def __init__(self, message: str, status: int | None = None,
                 body: str = "", retryable: bool = False) -> None:
        self.status = status
        self.body = body
        self.retryable = retryable
        super().__init__(message)


@dataclass(slots=True)
class Completion:
    """Odpowiedz modelu plus to, czego potrzebuje raport: koszt i model."""

    text: str
    model: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    finish_reason: str = ""
    raw: dict[str, Any] = field(default_factory=dict)

    @property
    def total_tokens(self) -> int:
        return self.prompt_tokens + self.completion_tokens


class OpenRouterClient:
    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        *,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = 3,
        referer: str | None = None,
        title: str | None = None,
    ) -> None:
        self._api_key = api_key
        self.model = model or env.get("LOTIS_AI_MODEL", DEFAULT_MODEL)
        self.timeout = timeout
        self.max_retries = max_retries
        self.referer = referer or env.get("LOTIS_AI_REFERER", "https://localhost/lotis")
        self.title = title or env.get("LOTIS_AI_TITLE", "LOTIS V1")

    @property
    def api_key(self) -> str:
        if self._api_key:
            return self._api_key
        return env.require(
            "OPENROUTER_API_KEY",
            "Klucz zalozysz na openrouter.ai/keys.",
        )

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self.referer,
            "X-Title": self.title,
        }

    def _post(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        last: OpenRouterError | None = None
        for attempt in range(self.max_retries):
            request = urllib.request.Request(
                f"{API_ROOT}{path}", data=body, headers=self._headers(), method="POST"
            )
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    return json.loads(response.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                detail = exc.read().decode("utf-8", errors="replace")[:500]
                retryable = exc.code in RETRY_STATUS
                last = OpenRouterError(
                    f"OpenRouter HTTP {exc.code}: {detail}",
                    status=exc.code, body=detail, retryable=retryable,
                )
                if not retryable:
                    raise last from exc
            except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
                last = OpenRouterError(f"OpenRouter: {exc}", retryable=True)
            if attempt < self.max_retries - 1:
                time.sleep(1.5 * (2 ** attempt))
        raise last or OpenRouterError("OpenRouter: brak odpowiedzi")

    # ---- API ----

    def complete(
        self,
        system: str,
        user: str,
        *,
        temperature: float = 0.2,
        max_tokens: int = 4096,
    ) -> Completion:
        """Jedno wywolanie. Niska temperatura, bo to ma byc raport, nie esej."""
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        data = self._post("/chat/completions", payload)
        choices = data.get("choices") or []
        if not choices:
            raise OpenRouterError(
                f"OpenRouter zwrocil odpowiedz bez tresci: {json.dumps(data)[:300]}"
            )
        message = choices[0].get("message") or {}
        usage = data.get("usage") or {}
        return Completion(
            text=(message.get("content") or "").strip(),
            model=data.get("model", self.model),
            prompt_tokens=int(usage.get("prompt_tokens", 0) or 0),
            completion_tokens=int(usage.get("completion_tokens", 0) or 0),
            finish_reason=choices[0].get("finish_reason", "") or "",
            raw=data,
        )

    def list_models(self, free_only: bool = False) -> list[dict[str, Any]]:
        """Zywa lista modeli. Zamiast zgadywac slug, bierze sie go stad."""
        request = urllib.request.Request(
            f"{API_ROOT}/models", headers={"Accept": "application/json"}
        )
        try:
            with urllib.request.urlopen(request, timeout=30.0) as response:
                data = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
            raise OpenRouterError(f"OpenRouter /models: {exc}", retryable=True) from exc
        models = data.get("data", [])
        if free_only:
            models = [m for m in models if str(m.get("id", "")).endswith(":free")]
        return sorted(models, key=lambda m: str(m.get("id", "")))
