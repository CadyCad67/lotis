"""Serwer dashboardu -- routing i API.

Kazdy endpoint oddaje to samo, co odpowiadajaca mu komenda CLI. Dashboard nie
ma wlasnej logiki dziedzinowej: gdyby ja mial, zaczalby pokazywac liczby inne
niz raporty, a wtedy przestalby byc widokiem na system i stalby sie drugim
systemem.
"""

from __future__ import annotations

import json
import threading
import traceback
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from collections.abc import Callable
from urllib.parse import parse_qs, urlparse

from ..kernel.report import to_jsonable

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
INDEX = Path(__file__).resolve().parent / "index.html"
REPORTS_ROOT = PROJECT_ROOT / "reports"
OUT_ROOT = PROJECT_ROOT / "out"

#: Budowa snapshotu trwa kilka sekund i trzyma cache'e modulowe. Dwa rownolegle
#: przebiegi nie zepsuja danych, ale zdublowalyby prace, wiec ida szeregowo.
_ENGINE_LOCK = threading.Lock()


class ApiError(Exception):
    def __init__(self, message: str, status: int = 400) -> None:
        self.status = status
        super().__init__(message)


# ---------------------------------------------------------------- endpointy


def api_health(_: dict[str, list[str]]) -> dict[str, Any]:
    from ..kernel.env import get
    from ..ai_layer.run_ai import api_key_present

    out: dict[str, Any] = {
        "czas": datetime.now(UTC).isoformat(timespec="seconds"),
        "model": get("LOTIS_AI_MODEL", "(nie ustawiony)"),
        "klucz_api": api_key_present(),
        "zrodla": {},
        "problemy": [],
    }
    try:
        from ..adapters.lot_db import load_lot_db
        db = load_lot_db()
        out["zrodla"]["baza_parametryczna"] = {
            "plik": db.source.name if db.source else "?",
            "wersja": db.version, "wygenerowano": db.generated,
            **db.summary(),
        }
    except Exception as exc:
        out["problemy"].append(f"loops.jsx: {exc}")
    try:
        from ..adapters.siatka import load_siatka
        sn = load_siatka()
        out["zrodla"]["baza_operacyjna"] = {
            "plik": sn.source.name if sn.source else "?", **sn.summary(),
        }
    except Exception as exc:
        out["problemy"].append(f"lot-siatka.json: {exc}")
    out["gotowy"] = not out["problemy"]
    return out


def api_stats(_: dict[str, list[str]]) -> dict[str, Any]:
    """Statystyka opoznien z 6236 rzeczywistych operacji."""
    from ..adapters.siatka import load_siatka
    sn = load_siatka()

    def row(stats) -> dict[str, Any]:
        return {"n": stats.n, "mediana": stats.median, "srednia": stats.mean,
                "p25": stats.p25, "p75": stats.p75, "p90": stats.p90,
                "max": stats.max, "punktualnosc15": stats.on_time_15_pct}

    ports = sorted(sn.by_departure_port.items(),
                   key=lambda kv: -kv[1].median)[:12]
    routes = sorted(
        ((k, v["odlot"]) for k, v in sn.by_route.items() if "odlot" in v),
        key=lambda kv: -kv[1].median,
    )[:12]
    return {
        "globalna": {k: row(v) for k, v in sn.global_stats.items()},
        "stany_rejsow": sn.flight_states,
        "najgorsze_porty": [{"port": k, **row(v)} for k, v in ports],
        "najgorsze_trasy": [{"trasa": k, **row(v)} for k, v in routes],
        "zrodlo": sn.provenance,
    }


def api_snapshot(query: dict[str, list[str]]) -> dict[str, Any]:
    from ..adapters.network import build_snapshot
    from ..adapters.siatka import WEEKDAYS_PL

    day = _int(query, "day", 4, 0, 6)
    seed = _int(query, "seed", 2026, 0, 10**9)
    with _ENGINE_LOCK:
        snap, rep = build_snapshot(weekday=day, seed=seed)

    flights = sorted(snap.flights.values(), key=lambda f: f.std)[:200]
    return {
        "dzien": day,
        "nazwa_dnia": WEEKDAYS_PL[day],
        "doba": rep.day,
        "odcisk": snap.digest,
        "liczby": {
            "rejsy": rep.flights, "rotacje": rep.rotations,
            "rotacje_przerwane": rep.broken_rotations, "maszyny": rep.aircraft,
            "zaloga": rep.crew, "pasazerowie": rep.passengers,
            "podroze": rep.itineraries,
            "udzial_transferowych": round(rep.connecting_share * 100, 1),
            "porty": len(snap.airports), "typy": len(snap.aircraft_types),
        },
        "zalozenia": list(rep.assumptions),
        "braki": list(rep.gaps),
        "rejsy": [
            {"id": f.id, "nr": f.number, "z": f.dep, "do": f.arr,
             "std": f.std.isoformat(timespec="minutes"),
             "sta": f.sta.isoformat(timespec="minutes"),
             "blok": f.block_min, "typ": f.type_code, "reg": f.aircraft_reg}
            for f in flights
        ],
        "rejsow_pokazano": len(flights),
    }


def api_runs(_: dict[str, list[str]]) -> dict[str, Any]:
    from ..ai_layer.prompt_builder import MANIFEST, find_runs

    runs = []
    for path in find_runs(REPORTS_ROOT):
        entry: dict[str, Any] = {
            "id": path.name.removeprefix("run_"),
            "katalog": path.name,
            "zmieniony": datetime.fromtimestamp(path.stat().st_mtime, UTC)
            .isoformat(timespec="seconds"),
            "raportow": len(list(path.glob("*.json"))) - (1 if (path / MANIFEST).exists() else 0),
        }
        manifest_path = path / MANIFEST
        if manifest_path.exists():
            try:
                m = json.loads(manifest_path.read_text(encoding="utf-8"))
                entry["statusy"] = m.get("statuses", {})
                entry["snapshot"] = m.get("snapshot", "")
                entry["zatrzymany"] = bool(m.get("halted"))
                entry["tryb"] = (m.get("budget") or {}).get("level", "FULL")
            except json.JSONDecodeError:
                entry["statusy"] = {}
        ai_dir = OUT_ROOT / path.name
        entry["ai"] = sorted(p.stem for p in ai_dir.glob("*.md")) if ai_dir.is_dir() else []
        runs.append(entry)
    return {"runs": runs, "katalog": str(REPORTS_ROOT)}


def api_run(query: dict[str, list[str]]) -> dict[str, Any]:
    from ..ai_layer.prompt_builder import load_run

    run_id = _str(query, "id")
    bundle = load_run(_run_dir(run_id))
    return {
        "id": bundle.run_id,
        "snapshot": bundle.snapshot,
        "tryb": bundle.degradation,
        "manifest": bundle.manifest,
        "raporty": [
            {"node": r.node_id, "nazwa": r.node_name, "tytul": r.title,
             "status": r.status, "markdown": r.markdown, "json": r.payload}
            for r in bundle.reports
        ],
    }


def api_personas(_: dict[str, list[str]]) -> dict[str, Any]:
    from ..ai_layer import personas

    return {"personas": [
        {"id": p.id, "nazwa": p.name, "odbiorca": p.audience,
         "czyta": list(p.reads), "struktura": list(p.structure)}
        for p in (personas.get(k) for k in personas.names())
    ], "domyslna": personas.DEFAULT}


def api_ai_output(query: dict[str, list[str]]) -> dict[str, Any]:
    """Zapisany wynik persony dla runu.

    Oba parametry skladaja sie w sciezke pliku, wiec oba musza byc sprawdzone.
    `persona` szla wczesniej wprost z zapytania: `?persona=../../../../Windows/win.ini`
    dawalo sciezke poza katalogiem `out/`. Nie konczylo sie odczytem tylko dlatego,
    ze plik musialby miec koncowke `.json` -- czyli o bezpieczenstwie decydowal
    przypadek, a nie kontrola.

    Nazwa persony pochodzi ze skonczonego katalogu, wiec sprawdzamy ja przez
    przynaleznosc do niego, a nie przez filtrowanie znakow.
    """
    from ..ai_layer import personas

    run_dir = _run_dir(_str(query, "id"))
    persona = _str(query, "persona")
    if persona not in personas.ALL:
        raise ApiError(
            f"nieznana persona: {persona!r}. Dostepne: {', '.join(personas.names())}")

    path = OUT_ROOT / run_dir.name / f"{persona}.json"
    if not path.exists():
        raise ApiError(f"brak wyniku AI: {persona} dla runu {run_dir.name}", 404)
    return json.loads(path.read_text(encoding="utf-8"))


# ---- POST ----


def post_run(body: dict[str, Any]) -> dict[str, Any]:
    """Uruchom pelny przeplyw 18 nodes na wskazanej dobie."""
    from ..kernel.budget import RunBudget
    from ..kernel.env import get_int
    from ..kernel.node import Pipeline, RunContext
    from ..nodes import Decision, build_pipeline

    day = int(body.get("day", 4))
    seed = int(body.get("seed", 2026))
    delay = int(body.get("delay", 180))
    if not 0 <= day <= 6:
        raise ApiError(f"dzien tygodnia poza zakresem 0-6: {day}")
    if not 0 <= delay <= 24 * 60:
        raise ApiError(f"opoznienie poza zakresem 0-1440 min: {delay}")
    try:
        decision = Decision(str(body.get("decision", "ACCEPT")).upper())
    except ValueError as exc:
        raise ApiError(f"nieznana decyzja: {body.get('decision')}") from exc

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%S")
    ctx = RunContext(
        run_id,
        budget=RunBudget(total_ms=float(get_int("LOTIS_BUDGET_MS", 20_000))),
        reports_root=REPORTS_ROOT,
        seed=seed,
    )
    nodes = build_pipeline(
        weekday=day, seed=seed,
        flight_id=(body.get("flight") or None),
        delay_min=delay,
        delay_code=str(body.get("code") or "41"),
        decision=decision,
        chosen_option=(body.get("option") or None),
        reason_code=str(body.get("reason") or ""),
        fail_step=(body.get("fail_step") or None),
        actual_delay_min=(int(body["actual"]) if body.get("actual") else None),
    )
    with _ENGINE_LOCK:
        reports = Pipeline(nodes).run(ctx)

    ranking = ctx.get("ranking") or []
    card = ctx.get("karta")
    return {
        "id": run_id,
        "snapshot": ctx.snapshot_digest,
        "zatrzymany": ctx.halted,
        "powod": ctx.halt_reason,
        "budzet": ctx.budget.snapshot(),
        "eskalacja": ctx.escalation,
        "ranking": [
            {"pozycja": r.rank, "opcja": r.option_id, "strata": r.loss,
             "min": r.band.low, "max": r.band.high,
             "oszczednosc": r.saving_vs_default, "uwaga": r.policy_note}
            for r in ranking
        ],
        "karta": card,
        "nodes": [
            {"node": r.node_id, "tytul": r.node_title, "status": r.status.value,
             "ms": round(r.duration_ms, 1), "ostrzezen": len(r.warnings),
             "braki": len(r.data_gaps), "podsumowanie": r.summary,
             "warnings": list(r.warnings), "data_gaps": list(r.data_gaps)}
            for r in reports
        ],
    }


def api_flights(query: dict[str, list[str]]) -> dict[str, Any]:
    """Rejsy doby jako kandydaci do zaklocenia -- z liczba pasazerow i odcinkow ponizej."""
    from ..adapters.network import build_snapshot

    day = _int(query, "day", 4, 0, 6)
    with _ENGINE_LOCK:
        snap, _ = build_snapshot(weekday=day, seed=_int(query, "seed", 2026, 0, 10**9))

    seated: dict[str, int] = {}
    for pax in snap.passengers.values():
        itin = snap.itineraries.get(pax.itinerary_id)
        for segment in (itin.segments if itin else ()):
            seated[segment] = seated.get(segment, 0) + 1

    rows = []
    for rotation in snap.rotations.values():
        legs = sorted((snap.flights[f] for f in rotation.flight_ids), key=lambda f: f.seq)
        for index, flight in enumerate(legs):
            rows.append({
                "id": flight.id, "nr": flight.number, "z": flight.dep, "do": flight.arr,
                "std": flight.std.isoformat(timespec="minutes"),
                "typ": flight.type_code, "reg": flight.aircraft_reg,
                "pasazerow": seated.get(flight.id, 0),
                "ponizej": len(legs) - index - 1,
            })
    rows.sort(key=lambda r: (-r["ponizej"], -r["pasazerow"]))
    return {"dzien": day, "rejsy": rows[:300], "wszystkich": len(rows)}


def api_board(_: dict[str, list[str]]) -> dict[str, Any]:
    """Mapa systemu: 18 nodes z tym, co konsumuja i produkuja."""
    from ..nodes import NODE_CLASSES

    return {"nodes": [
        {"id": cls.id, "nazwa": cls.name, "tytul": cls.title,
         "konsumuje": list(cls.consumes), "produkuje": cls.produces,
         "opis": (cls.__doc__ or "").strip().split("\n\n")[1].strip()
                 if len((cls.__doc__ or "").split("\n\n")) > 1 else ""}
        for cls in NODE_CLASSES
    ]}


def post_ai(body: dict[str, Any]) -> dict[str, Any]:
    """Uruchom persony na raportach runu. Domyslnie na sucho."""
    from ..ai_layer.prompt_builder import load_run
    from ..ai_layer.run_ai import api_key_present, run_all

    run_id = str(body.get("run") or "").strip()
    if not run_id:
        raise ApiError("brak identyfikatora runu")
    dry_run = bool(body.get("dry_run", True))
    which = body.get("personas") or None
    question = str(body.get("question") or "")

    if not dry_run and not api_key_present():
        raise ApiError(
            "brak OPENROUTER_API_KEY w .env -- dostepny tylko tryb na sucho", 409
        )

    bundle = load_run(_run_dir(run_id))
    results = run_all(bundle, which, question=question,
                      dry_run=dry_run, out_root=OUT_ROOT)
    return {"run": bundle.run_id, "dry_run": dry_run,
            "wyniki": [r.as_dict() for r in results]}


ROUTES_GET: dict[str, Callable[[dict[str, list[str]]], dict[str, Any]]] = {
    "/api/health": api_health,
    "/api/stats": api_stats,
    "/api/snapshot": api_snapshot,
    "/api/runs": api_runs,
    "/api/run": api_run,
    "/api/personas": api_personas,
    "/api/ai": api_ai_output,
    "/api/flights": api_flights,
    "/api/board": api_board,
}

ROUTES_POST: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "/api/run": post_run,
    "/api/ai": post_ai,
}


# ---------------------------------------------------------------- serwer


class Handler(BaseHTTPRequestHandler):
    server_version = "LOTIS/1.0"

    def log_message(self, fmt: str, *args: Any) -> None:
        if self.server.quiet:                               # type: ignore[attr-defined]
            return
        print(f"  {self.command} {self.path} -> {args[1] if len(args) > 1 else ''}")

    # ---- odpowiedzi ----

    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, payload: dict[str, Any], status: int = 200) -> None:
        """Serializacja przez `to_jsonable` -- ten sam kod, co raporty nodes.

        `json.dumps(default=str)` wygladalo na wystarczajace i nie bylo: `Money`
        wychodzil jako napis "1234.56 PLN", a `ExecutionCard` jako repr obiektu.
        Tekst wyswietlal sie poprawnie, wiec blad byl niewidoczny -- ale slupki
        rankingu liczyly szerokosc z `Number("1234.56 PLN")`, czyli z NaN,
        i wszystkie mialy zero pikseli.
        """
        blob = json.dumps(to_jsonable(payload), ensure_ascii=False,
                          default=str).encode("utf-8")
        self._send(status, blob, "application/json; charset=utf-8")

    def _dispatch(self, handler: Callable[[Any], dict[str, Any]], argument: Any) -> None:
        try:
            self._json(handler(argument))
        except ApiError as exc:
            self._json({"blad": str(exc)}, exc.status)
        except FileNotFoundError as exc:
            self._json({"blad": str(exc)}, 404)
        except Exception as exc:
            traceback.print_exc()
            self._json({"blad": f"{type(exc).__name__}: {exc}"}, 500)

    # ---- metody ----

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in ("/", "/index.html"):
            try:
                self._send(200, INDEX.read_bytes(), "text/html; charset=utf-8")
            except OSError as exc:
                self._send(500, f"brak {INDEX}: {exc}".encode(), "text/plain; charset=utf-8")
            return
        route = ROUTES_GET.get(parsed.path)
        if route is None:
            self._json({"blad": f"nieznana sciezka: {parsed.path}"}, 404)
            return
        self._dispatch(route, parse_qs(parsed.query))

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        route = ROUTES_POST.get(parsed.path)
        if route is None:
            self._json({"blad": f"nieznana sciezka: {parsed.path}"}, 404)
            return
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            body = json.loads(raw.decode("utf-8") or "{}")
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            self._json({"blad": f"cialo zadania nie jest JSON-em: {exc}"}, 400)
            return
        if not isinstance(body, dict):
            self._json({"blad": "cialo zadania musi byc obiektem JSON"}, 400)
            return
        self._dispatch(route, body)


class DashboardServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, host: str = "127.0.0.1", port: int = 8765,
                 quiet: bool = False) -> None:
        self.quiet = quiet
        super().__init__((host, port), Handler)

    @property
    def url(self) -> str:
        host, port = self.server_address[0], self.server_address[1]
        return f"http://{'127.0.0.1' if host in ('0.0.0.0', '') else host}:{port}/"


def serve(host: str = "127.0.0.1", port: int = 8765,
          open_browser: bool = True, quiet: bool = False) -> int:
    server = DashboardServer(host, port, quiet)
    print("=" * 72)
    print("LOTIS -- dashboard")
    print("=" * 72)
    print(f"  adres        {server.url}")
    print(f"  raporty      {REPORTS_ROOT}")
    print(f"  wyniki AI    {OUT_ROOT}")
    if host not in ("127.0.0.1", "localhost"):
        print(f"  UWAGA: nasluch na {host} -- dashboard widoczny poza ta maszyna")
    print("\n  Ctrl+C konczy\n")
    if open_browser:
        import webbrowser
        threading.Timer(0.5, lambda: webbrowser.open(server.url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nzatrzymany")
    finally:
        server.server_close()
    return 0


# ---------------------------------------------------------------- pomocnicze


def _int(query: dict[str, list[str]], key: str, default: int,
         low: int, high: int) -> int:
    raw = (query.get(key) or [None])[0]
    if raw is None:
        return default
    try:
        value = int(raw)
    except ValueError as exc:
        raise ApiError(f"{key} musi byc liczba calkowita, jest {raw!r}") from exc
    if not low <= value <= high:
        raise ApiError(f"{key}={value} poza zakresem {low}-{high}")
    return value


def _str(query: dict[str, list[str]], key: str) -> str:
    value = (query.get(key) or [""])[0].strip()
    if not value:
        raise ApiError(f"brak parametru {key}")
    return value


def _run_dir(run_id: str) -> Path:
    """Katalog runu. Odrzuca wszystko, co probuje wyjsc poza `reports/`."""
    name = run_id if run_id.startswith("run_") else f"run_{run_id}"
    target = (REPORTS_ROOT / name).resolve()
    if target.parent != REPORTS_ROOT.resolve():
        raise ApiError(f"nieprawidlowy identyfikator runu: {run_id!r}")
    if not target.is_dir():
        raise ApiError(f"nie ma runu {run_id}", 404)
    return target
