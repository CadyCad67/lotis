"""Interfejs terminalowy LOTIS.

    lotis doctor              sprawdz srodowisko od zera do snapshotu
    lotis dashboard           panel w przegladarce
    lotis run --day 4         uruchom przeplyw nodes, zapisz raporty
    lotis ai --dry-run        warstwa AI na raportach ostatniego runu
    lotis snapshot --day 4    zbuduj snapshot rzeczywistej doby
    lotis analiza             weryfikacja dekodu + analiza jakosci danych
    lotis models --free       zywa lista modeli z OpenRouter
    lotis test                uruchom testy

`doctor` jest wazniejszy niz wyglada: kazda kontrola sprawdza jeden konkretny
powod, dla ktorego system moze nie ruszyc, i mowi wprost, co zrobic. Zamiast
sledzic traceback przez cztery warstwy, dostajesz zdanie.
"""

from __future__ import annotations

import argparse
import platform
import sys
import traceback
from pathlib import Path
from collections.abc import Callable

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OK = "  ✓ "
WARN = "  △ "
FAIL = "  ✗ "


class Check:
    """Zbiera wyniki kontroli i pilnuje kodu wyjscia."""

    def __init__(self) -> None:
        self.failed = 0
        self.warned = 0

    def ok(self, label: str, detail: str = "") -> None:
        print(f"{OK}{label}" + (f"  -- {detail}" if detail else ""))

    def warn(self, label: str, detail: str = "") -> None:
        self.warned += 1
        print(f"{WARN}{label}" + (f"  -- {detail}" if detail else ""))

    def fail(self, label: str, detail: str = "", fix: str = "") -> None:
        self.failed += 1
        print(f"{FAIL}{label}" + (f"  -- {detail}" if detail else ""))
        if fix:
            print(f"      napraw: {fix}")

    def run(self, label: str, fn: Callable[[], str], fix: str = "",
            fatal: bool = True) -> bool:
        try:
            detail = fn()
        except Exception as exc:
            (self.fail if fatal else self.warn)(
                label, f"{type(exc).__name__}: {exc}", fix if fatal else "")
            return False
        self.ok(label, detail)
        return True


# ------------------------------------------------------------------ doctor


def cmd_doctor(args: argparse.Namespace) -> int:
    print("=" * 72)
    print("LOTIS -- kontrola srodowiska")
    print("=" * 72)
    c = Check()

    print("\n[1] Interpreter")
    version = sys.version_info
    if version >= (3, 11):
        c.ok(f"Python {platform.python_version()}", sys.executable)
    else:
        c.fail(f"Python {platform.python_version()} jest za stary",
               "wymagane 3.11+ (skladnia `X | None`, StrEnum, zoneinfo)",
               "utworz nowe srodowisko na Pythonie 3.11 albo nowszym")

    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        c.ok("srodowisko wirtualne", sys.prefix)
    else:
        c.warn("uruchamiasz interpreter bazowy",
               "zalecane osobne .venv, zeby nie mieszac pakietow")

    print("\n[2] Strefy czasowe")

    def _tz() -> str:
        from datetime import datetime
        from zoneinfo import ZoneInfo
        summer = ZoneInfo("Europe/Warsaw").utcoffset(datetime(2026, 8, 21, 12))
        winter = ZoneInfo("Europe/Warsaw").utcoffset(datetime(2026, 1, 21, 12))
        return f"Europe/Warsaw lato {summer}, zima {winter}"

    c.run("baza IANA dostepna", _tz,
          fix="pip install tzdata   (Windows nie ma systemowej bazy stref)")

    print("\n[3] Konfiguracja")

    def _env() -> str:
        from .kernel.env import DEFAULT_ENV, parse_env
        if not DEFAULT_ENV.exists():
            raise FileNotFoundError(f"brak {DEFAULT_ENV}")
        keys = parse_env(DEFAULT_ENV.read_text(encoding="utf-8"))
        return f"{DEFAULT_ENV.name}, {len(keys)} wpisow"

    c.run(".env wczytany", _env, fix="copy .env.example .env")

    def _model() -> str:
        from .kernel.env import get
        model = get("LOTIS_AI_MODEL", "")
        if not model:
            raise ValueError("LOTIS_AI_MODEL nie ustawiony")
        return model

    c.run("model AI wybrany", _model, fatal=False)

    from .kernel.env import get as env_get
    if env_get("OPENROUTER_API_KEY", ""):
        c.ok("klucz OpenRouter obecny", "warstwa AI gotowa")
    else:
        c.warn("brak OPENROUTER_API_KEY",
               "silnik dziala; warstwa AI tylko w trybie --dry-run")

    print("\n[4] Zrodla danych")

    def _db() -> str:
        from .adapters.lot_db import load_lot_db
        db = load_lot_db()
        s = db.summary()
        return (f"loops.jsx v{db.version} ({db.generated}): "
                f"{s['porty']} portow, {s['trasy']} tras, {s['flota']} maszyn")

    db_ok = c.run("baza parametryczna", _db,
                  fix="wskaz plik przez LOTIS_LOOPS_JSX w .env")

    def _siatka() -> str:
        from .adapters.siatka import load_siatka
        sn = load_siatka()
        s = sn.summary()
        return (f"{s['doby_tygodnia']} dob, {s['rejsow_w_tygodniu']} rejsow, "
                f"{s['operacji']} operacji w statystyce")

    siatka_ok = c.run("baza operacyjna", _siatka,
                      fix="wskaz plik przez LOTIS_SIATKA_JSON w .env")

    print("\n[5] Moduly")
    modules = [
        "lotis.kernel.money", "lotis.kernel.geo", "lotis.kernel.clock",
        "lotis.kernel.budget", "lotis.kernel.contracts", "lotis.kernel.report",
        "lotis.kernel.node", "lotis.kernel.horizon", "lotis.kernel.policy_store",
        "lotis.kernel.versions", "lotis.kernel.env",
        "lotis.adapters.lot_db", "lotis.adapters.siatka", "lotis.adapters.airports",
        "lotis.adapters.aircraft_perf", "lotis.adapters.pax_model",
        "lotis.adapters.network", "lotis.adapters.airline", "lotis.kernel.pricing",
        "lotis.nodes",
        "lotis.ai_layer.openrouter_client", "lotis.ai_layer.personas",
        "lotis.ai_layer.prompt_builder", "lotis.ai_layer.guard",
        "lotis.ai_layer.run_ai", "lotis.dashboard.server",
    ]
    from .nodes import NODE_CLASSES
    modules += [f"lotis.nodes.{cls.__module__.rsplit('.', 1)[-1]}" for cls in NODE_CLASSES]
    broken: list[str] = []
    for name in modules:
        try:
            __import__(name)
        except Exception as exc:
            broken.append(f"{name}: {type(exc).__name__}: {exc}")
    if broken:
        c.fail(f"{len(broken)}/{len(modules)} modulow nie importuje sie")
        for line in broken:
            print(f"      {line}")
    else:
        c.ok(f"wszystkie {len(modules)} modulow importuje sie")

    print("\n[6] Pelny przebieg")
    if db_ok and siatka_ok:
        def _snapshot() -> str:
            from .adapters.network import build_snapshot
            snap, rep = build_snapshot(weekday=4)
            if not snap.flights:
                raise RuntimeError("snapshot bez rejsow")
            return (f"{rep.day}: {rep.flights} rejsow, {rep.rotations} rotacji, "
                    f"{rep.crew} zalogi, {rep.passengers} pasazerow")

        c.run("snapshot rzeczywistej doby", _snapshot)

        def _report() -> str:
            import tempfile
            from .kernel.report import Report, ReportWriter
            with tempfile.TemporaryDirectory() as tmp:
                w = ReportWriter("doctor", Path(tmp))
                r = Report("00", "doctor", "KONTROLA")
                r.number("kontrola", 1, "szt")
                path = w.write(r)
                w.write_manifest()
                md = path.with_suffix(".md")
                if not (path.exists() and md.exists()):
                    raise RuntimeError("raport nie zapisal obu plikow")
            return "para .json + .md + manifest"

        c.run("zapis raportu", _report)

        holder: dict[str, object] = {}

        def _pipeline() -> str:
            """Pelny przeplyw 18 nodes w katalogu tymczasowym -- bez smiecenia w reports/."""
            import tempfile
            from .kernel.node import Pipeline, RunContext
            from .nodes import build_pipeline
            tmp = tempfile.TemporaryDirectory()
            holder["tmp"] = tmp
            ctx = RunContext("doctor", reports_root=tmp.name)
            reports = Pipeline(build_pipeline(weekday=4)).run(ctx)
            holder["dir"] = Path(tmp.name) / "run_doctor"
            blocked = [r.node_id for r in reports if r.status.value == "blocked"]
            if blocked:
                raise RuntimeError(f"nodes zablokowane: {', '.join(blocked)}")
            degraded = sum(1 for r in reports if r.status.value == "degraded")
            ranking = ctx.get("ranking") or []
            return (f"{len(reports)} etapow ({degraded} degradowanych), "
                    f"{len(ranking)} opcji, rekomendacja "
                    f"{ranking[0].option_id if ranking else '-'}")

        pipeline_ok = c.run("przeplyw 18 nodes", _pipeline)

        def _ai() -> str:
            """Prompt na sucho -- sprawdza cala warstwe AI bez wywolania modelu."""
            from .ai_layer import personas
            from .ai_layer.prompt_builder import build_prompt, load_run
            bundle = load_run(holder["dir"])
            rozmiary = []
            for name in personas.names():
                system, user = build_prompt(bundle, personas.get(name))
                rozmiary.append(len(system) + len(user))
            return (f"{len(rozmiary)} person, prompty "
                    f"{min(rozmiary)}-{max(rozmiary)} znakow")

        if pipeline_ok:
            c.run("warstwa AI na sucho", _ai)
            holder["tmp"].cleanup()          # type: ignore[union-attr]
        else:
            c.warn("pominieto warstwe AI", "brak raportow z przeplywu")
    else:
        c.warn("pominieto przebieg", "brak danych wejsciowych")

    def _dashboard() -> str:
        from .dashboard.server import INDEX
        if not INDEX.exists():
            raise FileNotFoundError(f"brak pliku widoku: {INDEX}")
        return f"{INDEX.name}, {INDEX.stat().st_size // 1024} KB"

    c.run("widok dashboardu", _dashboard, fatal=False)

    print("\n[7] Katalogi zapisu")
    for name in ("reports", "out", "calibration"):
        target = PROJECT_ROOT / name
        try:
            target.mkdir(parents=True, exist_ok=True)
            probe = target / ".write-test"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink()
            c.ok(f"{name}/ zapisywalny")
        except OSError as exc:
            c.fail(f"{name}/ niezapisywalny", str(exc))

    print("\n" + "=" * 72)
    if c.failed:
        print(f"WYNIK: {c.failed} bledow, {c.warned} ostrzezen -- system NIE jest gotowy")
        return 1
    if c.warned:
        print(f"WYNIK: gotowy, z {c.warned} ostrzezeniami (nie blokuja silnika)")
        return 0
    print("WYNIK: wszystko dziala")
    return 0


# ------------------------------------------------------------------ reszta


def cmd_snapshot(args: argparse.Namespace) -> int:
    from .adapters.network import build_snapshot
    from .adapters.siatka import WEEKDAYS_PL

    snap, rep = build_snapshot(weekday=args.day, seed=args.seed)
    print(f"Doba: {WEEKDAYS_PL[args.day]} {rep.day}")
    print(f"  snapshot        {snap.digest}")
    print(f"  rejsy           {rep.flights}")
    print(f"  rotacje         {rep.rotations}  (przerwane lancuchy: {rep.broken_rotations})")
    print(f"  maszyny         {rep.aircraft}")
    print(f"  zaloga          {rep.crew}")
    print(f"  pasazerowie     {rep.passengers}")
    print(f"  transferowi     {rep.connecting_share:.1%}")
    if rep.assumptions:
        print("\n  zalozenia:")
        for a in rep.assumptions:
            print(f"    - {a}")
    if rep.gaps:
        print("\n  braki:")
        for g in rep.gaps:
            print(f"    - {g}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Pelny przeplyw 18 nodes. Zapisuje raporty do reports/run_<id>/."""
    from datetime import UTC, datetime

    from .kernel.budget import RunBudget
    from .kernel.env import get_int
    from .kernel.node import Pipeline, RunContext
    from .nodes import Decision, build_pipeline

    run_id = args.id or datetime.now(UTC).strftime("%Y%m%dT%H%M%S")
    ctx = RunContext(
        run_id,
        budget=RunBudget(total_ms=float(args.budget or get_int("LOTIS_BUDGET_MS", 20_000))),
        reports_root=PROJECT_ROOT / "reports",
        seed=args.seed,
    )
    nodes = build_pipeline(
        weekday=args.day, seed=args.seed,
        flight_id=args.flight, delay_min=args.delay, delay_code=args.code,
        decision=Decision(args.decision), chosen_option=args.option,
        reason_code=args.reason or "", fail_step=args.fail_step,
        actual_delay_min=args.actual,
    )
    reports = Pipeline(nodes).run(ctx)

    print(f"run {run_id}   snapshot {ctx.snapshot_digest}")
    print(f"\n{'node':<6}{'status':<11}{'ms':>9}  tytul")
    print("-" * 78)
    for r in reports:
        print(f"{r.node_id:<6}{r.status.value:<11}{r.duration_ms:>9.1f}  {r.node_title}")
        if r.summary and args.verbose:
            for line in _wrap(r.summary, 70):
                print(f"        {line}")
        for w in r.warnings:
            print(f"        △ {w}")
        for g in r.data_gaps:
            print(f"        ! {g}")

    ranking = ctx.get("ranking") or []
    if ranking:
        print(f"\n{'#':<3}{'opcja':<16}{'strata':>16}{'min':>15}{'max':>15}")
        print("-" * 78)
        for r in ranking:
            print(f"{r.rank:<3}{r.option_id:<16}{r.loss!s:>16}"
                  f"{r.band.low!s:>15}{r.band.high!s:>15}")
        card = ctx.get("karta")
        if card is not None:
            print(f"\nKARTA WYKONANIA -- {card.label}")
            for line in card.what_changes:
                print(f"  - {line}")
            print(f"  koszt: {card.cost_low} / {card.cost_expected} / {card.cost_high}")
            print(f"  autoryzacja: {card.authorization_role}"
                  + (" + drugi podpis" if card.second_signature else ""))
            print(f"  {card.threshold_note}")

    print(f"\nraporty: {ctx.writer.dir}")
    if ctx.halted:
        print(f"PRZEPLYW ZATRZYMANY: {ctx.halt_reason}")
        return 1
    return 0


def _wrap(text: str, width: int) -> list[str]:
    import textwrap
    return textwrap.wrap(text, width) or [""]


def cmd_ai(args: argparse.Namespace) -> int:
    """Warstwa AI na raportach runu."""
    from .ai_layer import personas
    from .ai_layer.prompt_builder import latest_run, load_run
    from .ai_layer.run_ai import api_key_present, run_all

    reports_root = PROJECT_ROOT / "reports"
    if args.run:
        name = args.run if args.run.startswith("run_") else f"run_{args.run}"
        directory = reports_root / name
    else:
        directory = latest_run(reports_root)
        if directory is None:
            print("nie ma zadnego runu. Uruchom najpierw: lotis run", file=sys.stderr)
            return 1

    dry_run = args.dry_run or not api_key_present()
    if dry_run and not args.dry_run:
        print("brak OPENROUTER_API_KEY -- przechodze w tryb na sucho\n")

    bundle = load_run(directory)
    which = args.persona or personas.names()
    results = run_all(bundle, which, question=args.question or "",
                      dry_run=dry_run, out_root=PROJECT_ROOT / "out")

    print(f"run {bundle.run_id}   raporty: {', '.join(r.stem for r in bundle.reports)}")
    print(f"tryb: {'na sucho (bez wywolania modelu)' if dry_run else 'wywolanie modelu'}\n")
    failed = 0
    for r in results:
        if r.error:
            failed += 1
            print(f"  ✗ {r.persona:<14} {r.error}")
            continue
        if dry_run:
            print(f"  ✓ {r.persona:<14} prompt {len(r.user):>6} znakow  -> {r.files[0]}")
        else:
            mark = "✓" if (r.guard and r.guard.clean) else "△"
            print(f"  {mark} {r.persona:<14} {r.completion_tokens:>5} tok  "
                  f"{r.guard.summary() if r.guard else ''}")
    print(f"\nwyniki: {PROJECT_ROOT / 'out' / f'run_{bundle.run_id}'}")
    return 1 if failed else 0


def cmd_dashboard(args: argparse.Namespace) -> int:
    from .dashboard.server import serve
    return serve(host=args.host, port=args.port,
                 open_browser=not args.no_open, quiet=args.quiet)


def cmd_analiza(args: argparse.Namespace) -> int:
    sys.path.insert(0, str(PROJECT_ROOT))
    from tools.analiza_danych import main as analiza_main
    return analiza_main()


def cmd_models(args: argparse.Namespace) -> int:
    from .ai_layer.openrouter_client import OpenRouterClient, OpenRouterError
    client = OpenRouterClient()
    try:
        models = client.list_models(free_only=args.free)
    except OpenRouterError as exc:
        print(f"nie udalo sie pobrac listy: {exc}", file=sys.stderr)
        return 1
    print(f"aktualnie wybrany: {client.model}\n")
    print(f"{len(models)} modeli" + (" darmowych" if args.free else "") + ":")
    for m in models[: args.limit]:
        ctx = m.get("context_length", "?")
        print(f"  {m.get('id', '?'):<58} kontekst {ctx}")
    if len(models) > args.limit:
        print(f"  ... i {len(models) - args.limit} wiecej (--limit)")
    print("\nWklej wybrany slug do LOTIS_AI_MODEL w .env")
    return 0


def cmd_test(args: argparse.Namespace) -> int:
    import unittest
    loader = unittest.TestLoader()
    suite = loader.discover(str(PROJECT_ROOT / "tests"), top_level_dir=str(PROJECT_ROOT))
    runner = unittest.TextTestRunner(verbosity=2 if args.verbose else 1)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


# ------------------------------------------------------------------ wejscie


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="lotis", description="LOTIS V1 -- system wspomagania decyzji IROPS"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("doctor", help="sprawdz srodowisko").set_defaults(func=cmd_doctor)

    p_snap = sub.add_parser("snapshot", help="zbuduj snapshot doby")
    p_snap.add_argument("--day", type=int, default=4, choices=range(7),
                        help="0=poniedzialek ... 6=niedziela (domyslnie 4=piatek)")
    p_snap.add_argument("--seed", type=int, default=2026)
    p_snap.set_defaults(func=cmd_snapshot)

    p_run = sub.add_parser("run", help="uruchom pelny przeplyw 18 nodes")
    p_run.add_argument("--day", type=int, default=4, choices=range(7),
                       help="0=poniedzialek ... 6=niedziela (domyslnie 4=piatek)")
    p_run.add_argument("--seed", type=int, default=2026)
    p_run.add_argument("--id", help="wlasny identyfikator runu (domyslnie znacznik czasu)")
    p_run.add_argument("--budget", type=int, help="budzet czasu w ms (domyslnie z .env)")
    p_run.add_argument("--flight", help="id rejsu z zakloceniem (domyslnie wybor automatyczny)")
    p_run.add_argument("--delay", type=int, default=180, help="szacowane opoznienie w minutach")
    p_run.add_argument("--code", default="41", help="kod opoznienia AHM 730")
    p_run.add_argument("--decision", default="ACCEPT",
                       choices=("ACCEPT", "MODIFY", "REJECT"))
    p_run.add_argument("--option", help="opcja wybrana przez czlowieka (przy MODIFY)")
    p_run.add_argument("--reason", help="kod przyczyny odrzucenia (przy REJECT)")
    p_run.add_argument("--fail-step", dest="fail_step",
                       help="zasymuluj porazke kroku wykonania, np. potwierdzenie_partnera")
    p_run.add_argument("--actual", type=int,
                       help="rzeczywiste opoznienie w minutach (domyslnie z rozkladu)")
    p_run.add_argument("-v", "--verbose", action="store_true", help="wypisz podsumowania")
    p_run.set_defaults(func=cmd_run)

    p_ai = sub.add_parser("ai", help="warstwa AI na raportach runu")
    p_ai.add_argument("--run", help="identyfikator runu (domyslnie ostatni)")
    p_ai.add_argument("--persona", action="append",
                      help="persona; mozna podac wielokrotnie (domyslnie wszystkie)")
    p_ai.add_argument("--question", help="pytanie dodatkowe do modelu")
    p_ai.add_argument("--dry-run", action="store_true",
                      help="zloz prompt i zapisz do pliku, nie wolaj modelu")
    p_ai.set_defaults(func=cmd_ai)

    p_dash = sub.add_parser("dashboard", help="panel w przegladarce")
    p_dash.add_argument("--port", type=int, default=8765)
    p_dash.add_argument("--host", default="127.0.0.1",
                        help="domyslnie tylko ta maszyna; 0.0.0.0 wystawia na siec")
    p_dash.add_argument("--no-open", action="store_true", help="nie otwieraj przegladarki")
    p_dash.add_argument("--quiet", action="store_true", help="bez logu zadan")
    p_dash.set_defaults(func=cmd_dashboard)

    sub.add_parser("analiza", help="weryfikacja dekodu i analiza danych"
                   ).set_defaults(func=cmd_analiza)

    p_models = sub.add_parser("models", help="lista modeli OpenRouter")
    p_models.add_argument("--free", action="store_true", help="tylko darmowe")
    p_models.add_argument("--limit", type=int, default=40)
    p_models.set_defaults(func=cmd_models)

    p_test = sub.add_parser("test", help="uruchom testy")
    p_test.add_argument("-v", "--verbose", action="store_true")
    p_test.set_defaults(func=cmd_test)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nprzerwane", file=sys.stderr)
        return 130
    except Exception:
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
