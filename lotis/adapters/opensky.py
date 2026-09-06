"""Klient OpenSky Network -- realny ruch LOT-u z ostatnich dni.

Zwraca wylacznie rejsy LOT-u: OpenSky oddaje ruch calego portu, wiec
filtrujemy po prefiksie callsignu (`LOT...`) zanim cokolwiek wejdzie do
systemu.

Uwierzytelnianie: OpenSky wymaga poswiadczen OAuth2 client credentials.
Ustaw `OPENSKY_CLIENT_ID` i `OPENSKY_CLIENT_SECRET` w srodowisku. Bez nich
klient probuje dostepu anonimowego, ktory jest mocno limitowany i czesto
odmawia -- wtedy node 01 schodzi na rozklad zapasowy i wprost to raportuje.

Odpowiedzi sa cache'owane na dysku, wiec kolejne uruchomienia tego samego
zakresu nie dotykaja sieci i sa w pelni powtarzalne.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from . import airline

API_ROOT = "https://opensky-network.org/api"
TOKEN_URL = (
    "https://auth.opensky-network.org/auth/realms/opensky-network"
    "/protocol/openid-connect/token"
)
MAX_INTERVAL_DAYS = 7
CACHE_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "cache" / "opensky"


class AdapterUnavailable(RuntimeError):
    """Zrodlo zewnetrzne nie odpowiedzialo. Nie jest bledem krytycznym."""


@dataclass(frozen=True, slots=True)
class OpenSkyLeg:
    """Jeden przelot zwrocony przez OpenSky, juz odsiany do LOT-u."""

    icao24: str
    callsign: str
    flight_number: str
    dep_icao: str | None
    arr_icao: str | None
    first_seen: datetime
    last_seen: datetime

    @property
    def block_min(self) -> int:
        return max(1, int((self.last_seen - self.first_seen).total_seconds() // 60))


class OpenSkyClient:
    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        *,
        cache_dir: Path | str | None = None,
        timeout: float = 20.0,
        use_cache: bool = True,
    ) -> None:
        self.client_id = client_id or os.environ.get("OPENSKY_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("OPENSKY_CLIENT_SECRET")
        self.cache_dir = Path(cache_dir) if cache_dir else CACHE_DIR
        self.timeout = timeout
        self.use_cache = use_cache
        self._token: str | None = None
        self._token_expires: float = 0.0

    # ---- uwierzytelnianie ----

    @property
    def authenticated(self) -> bool:
        return bool(self.client_id and self.client_secret)

    def _access_token(self) -> str | None:
        if not self.authenticated:
            return None
        if self._token and time.time() < self._token_expires - 30:
            return self._token
        body = urllib.parse.urlencode({
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }).encode("utf-8")
        req = urllib.request.Request(
            TOKEN_URL,
            data=body,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
            raise AdapterUnavailable(f"OpenSky: nie udalo sie pobrac tokenu ({exc})") from exc
        self._token = payload.get("access_token")
        self._token_expires = time.time() + float(payload.get("expires_in", 1800))
        if not self._token:
            raise AdapterUnavailable("OpenSky: odpowiedz tokenowa bez access_token")
        return self._token

    # ---- warstwa HTTP ----

    def _cache_path(self, kind: str, icao: str, begin: int, end: int) -> Path:
        return self.cache_dir / f"{kind}_{icao}_{begin}_{end}.json"

    def _fetch(self, kind: str, icao: str, begin: int, end: int) -> list[dict[str, Any]]:
        cache = self._cache_path(kind, icao, begin, end)
        if self.use_cache and cache.exists():
            try:
                return json.loads(cache.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass  # uszkodzony cache: pobieramy ponownie

        query = urllib.parse.urlencode({"airport": icao, "begin": begin, "end": end})
        url = f"{API_ROOT}/flights/{kind}?{query}"
        headers = {"Accept": "application/json", "User-Agent": "LOTIS/1.0"}
        token = self._access_token()
        if token:
            headers["Authorization"] = f"Bearer {token}"

        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                rows = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                rows = []          # brak ruchu w tym oknie to poprawna odpowiedz
            else:
                raise AdapterUnavailable(
                    f"OpenSky {kind} {icao}: HTTP {exc.code} {exc.reason}"
                ) from exc
        except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
            raise AdapterUnavailable(f"OpenSky {kind} {icao}: {exc}") from exc

        if self.use_cache:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(rows), encoding="utf-8")
        return rows

    # ---- API ----

    def departures(self, icao: str, begin: datetime, end: datetime) -> list[OpenSkyLeg]:
        """Odloty LOT-u z portu `icao` w podanym oknie."""
        return self._legs("departure", icao, begin, end)

    def arrivals(self, icao: str, begin: datetime, end: datetime) -> list[OpenSkyLeg]:
        return self._legs("arrival", icao, begin, end)

    def _legs(self, kind: str, icao: str, begin: datetime, end: datetime) -> list[OpenSkyLeg]:
        if end <= begin:
            raise ValueError("okno czasowe musi byc dodatnie")
        if end - begin > timedelta(days=MAX_INTERVAL_DAYS):
            raise ValueError(
                f"OpenSky przyjmuje maksymalnie {MAX_INTERVAL_DAYS} dni na zapytanie"
            )
        rows = self._fetch(kind, icao.upper(), int(begin.timestamp()), int(end.timestamp()))
        legs: list[OpenSkyLeg] = []
        for row in rows:
            callsign = (row.get("callsign") or "").strip()
            if not airline.is_lot_callsign(callsign):
                continue          # tu odpada ruch wszystkich innych przewoznikow
            try:
                first = datetime.fromtimestamp(int(row["firstSeen"]), UTC)
                last = datetime.fromtimestamp(int(row["lastSeen"]), UTC)
            except (KeyError, TypeError, ValueError, OSError):
                continue
            if last <= first:
                continue
            legs.append(OpenSkyLeg(
                icao24=str(row.get("icao24", "")).strip(),
                callsign=callsign,
                flight_number=airline.flight_number_from_callsign(callsign),
                dep_icao=(row.get("estDepartureAirport") or None),
                arr_icao=(row.get("estArrivalAirport") or None),
                first_seen=first,
                last_seen=last,
            ))
        legs.sort(key=lambda leg: leg.first_seen)
        return legs

    def network_days(self, days: int = 3, until: datetime | None = None) -> list[OpenSkyLeg]:
        """Odloty LOT-u ze wszystkich baz krajowych za ostatnie `days` dni."""
        end = (until or datetime.now(UTC)).replace(microsecond=0)
        begin = end - timedelta(days=days)
        collected: list[OpenSkyLeg] = []
        errors: list[str] = []
        for icao in airline.SOURCE_AIRPORTS:
            try:
                collected.extend(self.departures(icao, begin, end))
            except AdapterUnavailable as exc:
                errors.append(str(exc))
        if not collected and errors:
            raise AdapterUnavailable("; ".join(errors))
        seen: set[tuple[str, int]] = set()
        unique: list[OpenSkyLeg] = []
        for leg in sorted(collected, key=lambda x: x.first_seen):
            key = (leg.icao24, int(leg.first_seen.timestamp()))
            if key in seen:
                continue
            seen.add(key)
            unique.append(leg)
        return unique
