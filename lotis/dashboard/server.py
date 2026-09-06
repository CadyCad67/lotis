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

#: Pamiec podreczna snapshotow. Widoki operacyjne panelu -- rejsy, zalogi,
#: rotacje -- pokazuja rozne ciecia tego samego stanu doby. Bez cache kazde
#: przejscie miedzy zakladkami budowaloby doba od nowa, a `_ENGINE_LOCK`
#: ustawialby te przebiegi w kolejce, wiec interfejs staralby sie na kilka
#: sekund przy kazdym klinieciu. Trzymamy trzy ostatnie doby, bo tyle wystarcza
#: na porownywanie i nie rozdyma pamieci.
_SNAP_CACHE: dict[tuple[int, int], Any] = {}
_SNAP_ORDER: list[tuple[int, int]] = []
_SNAP_MAX = 3


def _snapshot(day: int, seed: int):
    """Snapshot doby, zbudowany raz na (doba, ziarno)."""
    key = (day, seed)
    with _ENGINE_LOCK:
        hit = _SNAP_CACHE.get(key)
        if hit is not None:
            return hit
        from ..adapters.network import build_snapshot
        value = build_snapshot(weekday=day, seed=seed)
        _SNAP_CACHE[key] = value
        _SNAP_ORDER.append(key)
        while len(_SNAP_ORDER) > _SNAP_MAX:
            _SNAP_CACHE.pop(_SNAP_ORDER.pop(0), None)
        return value


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
    from ..adapters.siatka import WEEKDAYS_PL

    day = _int(query, "day", 4, 0, 6)
    seed = _int(query, "seed", 2026, 0, 10**9)
    snap, rep = _snapshot(day, seed)

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


# -------------------------------------------- doba dla widokow operacyjnych


def _pax_index(snap) -> dict[str, dict]:
    """Jedno przejscie po pasazerach zamiast jednego na rejs.

    Kazdy widok operacyjny pyta o to samo: ilu pasazerow siedzi na odcinku,
    ilu leci dalej, ilu przylecialo dowozem. Liczenie tego osobno dla kazdego
    z czterystu rejsow oznaczaloby czterysta przebiegow po tej samej kolekcji
    trzydziestu tysiecy pasazerow. Raz, do slownikow, i widoki tylko czytaja.
    """
    seated: dict[str, int] = {}
    cabins: dict[str, dict[str, int]] = {}
    onward: dict[str, dict[str, int]] = {}
    inbound: dict[str, dict[str, int]] = {}
    ssr: dict[str, dict[str, int]] = {}
    ranks: dict[str, dict[str, int]] = {}
    local: dict[str, int] = {}

    def bump(store: dict[str, dict[str, int]], fid: str, key: str) -> None:
        row = store.setdefault(fid, {})
        row[key] = row.get(key, 0) + 1

    for pax in snap.passengers.values():
        itin = snap.itineraries.get(pax.itinerary_id)
        if itin is None:
            continue
        segs = itin.segments
        cabin, status = str(pax.basket.cabin), str(pax.basket.status)
        for i, fid in enumerate(segs):
            seated[fid] = seated.get(fid, 0) + 1
            bump(cabins, fid, cabin)
            bump(ranks, fid, status)
            for need in pax.specials:
                bump(ssr, fid, SSR_KOD.get(str(need), str(need)))
            if i + 1 < len(segs):
                bump(onward, fid, segs[i + 1])
            else:
                local[fid] = local.get(fid, 0) + 1
            if i > 0:
                bump(inbound, fid, segs[i - 1])

    return {"seated": seated, "cabins": cabins, "onward": onward,
            "inbound": inbound, "ssr": ssr, "ranks": ranks, "local": local}


def api_day(query: dict[str, list[str]]) -> dict[str, Any]:
    """Cala doba w jednym wywolaniu: rejsy, rotacje, zaloga, porty, typy.

    Widoki operacyjne to rozne ciecia jednego stanu doby. Gdyby kazdy pytal
    osobnym endpointem, kazdy placilby za budowe snapshotu jeszcze raz, bo
    przebiegi ida szeregowo pod blokada silnika. Jedno wywolanie plus pamiec
    podreczna sprawiaja, ze przelaczanie zakladek jest natychmiastowe.
    """
    from ..adapters.lot_db import load_lot_db
    from ..adapters.siatka import WEEKDAYS_PL
    from ..kernel.geo import haversine_km
    from ..kernel.pricing import Pricing

    day = _int(query, "day", 4, 0, 6)
    seed = _int(query, "seed", 2026, 0, 10**9)
    snap, rep = _snapshot(day, seed)

    db = load_lot_db()
    price = Pricing(db)
    idx = _pax_index(snap)
    seated, cabins, onward, inbound = idx["seated"], idx["cabins"], idx["onward"], idx["inbound"]

    #: Rejsy zalogi wyprowadzamy z przypisan na rejsach -- kontrakt zalogi ich
    #: nie trzyma, bo zaloga nie wie o rotacji, tylko rotacja wie o zalodze.
    crew_flights: dict[str, list[str]] = {}
    for flight in snap.flights.values():
        for cid in flight.crew_ids:
            crew_flights.setdefault(cid, []).append(flight.id)

    def minutes(a, b) -> int:
        return int((b - a).total_seconds() // 60)

    rejsy = []
    for f in sorted(snap.flights.values(), key=lambda x: x.std):
        pa, pb = snap.airports.get(f.dep), snap.airports.get(f.arr)
        km = round(haversine_km(pa.lat, pa.lon, pb.lat, pb.lon)) if pa and pb else 0
        port_a, port_b = db.ports.get(f.dep), db.ports.get(f.arr)
        intra = bool(port_a and port_b and port_a.eu and port_b.eu)
        tier = db.eu261_tier_for(km, intra)
        typ = snap.aircraft_types.get(f.type_code)
        miejsca = typ.seats_total if typ else 0
        obsadzone = seated.get(f.id, 0)

        dalej = []
        for nxt_id, ile in sorted(onward.get(f.id, {}).items(), key=lambda kv: -kv[1]):
            nxt = snap.flights.get(nxt_id)
            if nxt is None:
                continue
            dalej.append({"id": nxt.id, "nr": nxt.number, "cel": nxt.arr,
                          "pax": ile, "zapas": minutes(f.sta, nxt.std)})
        dowozy = []
        for prv_id, ile in sorted(inbound.get(f.id, {}).items(), key=lambda kv: -kv[1]):
            prv = snap.flights.get(prv_id)
            if prv is None:
                continue
            dowozy.append({"id": prv.id, "nr": prv.number, "z": prv.dep,
                           "pax": ile, "zapas": minutes(prv.sta, f.std)})

        rejsy.append({
            "id": f.id, "nr": f.number, "z": f.dep, "do": f.arr,
            "std": f.std.isoformat(timespec="minutes"),
            "sta": f.sta.isoformat(timespec="minutes"),
            "blok": f.block_min, "typ": f.type_code, "reg": f.aircraft_reg,
            "rotacja": f.rotation_id, "seq": f.seq,
            "km": km, "intra": intra, "tier": tier,
            "odszkodowanie": db.compensation_eur(tier),
            "prog_opieki": price.care_threshold_min(tier),
            "pax": obsadzone, "miejsca": miejsca,
            "lf": round(100 * obsadzone / miejsca, 1) if miejsca else 0,
            "kabiny": cabins.get(f.id, {}), "ssr": idx["ssr"].get(f.id, {}),
            "statusy": idx["ranks"].get(f.id, {}), "lokalni": idx["local"].get(f.id, 0),
            "dalej": dalej, "dowozy": dowozy,
            "zaloga": list(f.crew_ids),
        })

    rotacje = []
    for rot in snap.rotations.values():
        legs = sorted((snap.flights[i] for i in rot.flight_ids if i in snap.flights),
                      key=lambda x: x.seq)
        if not legs:
            continue
        rotacje.append({
            "id": rot.id, "reg": rot.aircraft_reg, "typ": legs[0].type_code,
            "odcinki": [x.id for x in legs],
            "od": legs[0].std.isoformat(timespec="minutes"),
            "do": legs[-1].sta.isoformat(timespec="minutes"),
            "porty": [legs[0].dep] + [x.arr for x in legs],
        })
    rotacje.sort(key=lambda r: (r["typ"], r["reg"]))

    zaloga = []
    for c in snap.crew.values():
        moje = sorted((snap.flights[i] for i in crew_flights.get(c.id, []) if i in snap.flights),
                      key=lambda x: x.std)
        zaloga.append({
            "id": c.id, "rola": str(c.role), "baza": c.base,
            "kwalifikacje": sorted(c.qualifications),
            "start_sluzby": c.duty_start.isoformat(timespec="minutes"),
            "fdp_limit": c.fdp_limit_min, "fdp_uzyte": c.duty_used_min,
            "fdp_zostalo": c.fdp_remaining_min, "odpoczynek_ok": c.rest_ok,
            #: Snapshot nie modeluje sluzby sprzed doby, wiec `duty_used_min`
            #: jest zerem dla wszystkich. Czas blokowy tej doby jest liczba,
            #: ktora naprawde cos mowi o obciazeniu wobec limitu.
            "blok_doby": sum(x.block_min for x in moje),
            "okno_sluzby": (
                int((moje[-1].sta - moje[0].std).total_seconds() // 60) if moje else 0),
            "rejsy": [x.number for x in moje],
            "trasa": "-".join([moje[0].dep] + [x.arr for x in moje]) if moje else "",
            "reg": moje[0].aircraft_reg if moje else "",
        })
    zaloga.sort(key=lambda z: (not z["rejsy"], z["id"]))

    porty = {}
    for iata, a in snap.airports.items():
        porty[iata] = {
            "iata": a.iata, "icao": a.icao, "nazwa": a.name, "tz": a.tz,
            #: Offset jest juz rozwiazany dla doby snapshotu, wiec panel moze
            #: pokazywac czasy lokalne bez znajomosci kalendarza zmian czasu.
            "tz_offset": a.tz_offset_min,
            "lat": a.lat, "lon": a.lon, "schengen": a.schengen, "eu261": a.eu261,
            "poziom_slotu": a.slot_level, "otwarcie": a.opens_min, "zamkniecie": a.closes_min,
            "cisza": None if a.curfew_start_min is None else {
                "od": a.curfew_start_min, "do": a.curfew_end_min, "rodzaj": a.curfew_kind},
        }

    typy = {code: {"kod": t.code, "nazwa": t.name, "miejsca": t.seats_total,
                   "j": t.seats_j, "pe": t.seats_pe, "y": t.seats_y,
                   "zasieg": t.range_km, "kategoria": t.category,
                   "uprawnienie": t.rating, "personel": t.cabin_crew}
            for code, t in snap.aircraft_types.items()}

    return {
        "dzien": day, "nazwa_dnia": WEEKDAYS_PL[day], "doba": rep.day,
        "odcisk": snap.digest, "ziarno": seed,
        "liczby": {
            "rejsy": rep.flights, "rotacje": rep.rotations,
            "rotacje_przerwane": rep.broken_rotations, "maszyny": rep.aircraft,
            "zaloga": rep.crew, "pasazerowie": rep.passengers,
            "podroze": rep.itineraries,
            "udzial_transferowych": round(rep.connecting_share * 100, 1),
            "porty": len(snap.airports), "typy": len(snap.aircraft_types),
        },
        "zalozenia": list(rep.assumptions), "braki": list(rep.gaps),
        "rejsy": rejsy, "rotacje": rotacje, "zaloga": zaloga,
        "porty": porty, "typy": typy,
    }


#: Wewnetrzne kategorie `SpecialNeed` na kody SSR wg IATA PSCRM. Silnik operuje
#: piecioma kategoriami, bo tylko one zmieniaja kolejnosc przy odmowie przyjecia
#: (etap 12). Operacyjnie mowi sie kodem, nie kategoria, wiec panel pokazuje kod.
SSR_KOD = {
    "REDUCED_MOBILITY": "WCHR",
    "UNACCOMPANIED_MINOR": "UMNR",
    "GROUP": "GRPF",
    "PET_IN_HOLD": "AVIH",
    "MEDICAL_ASSIST": "MEDA",
}


def api_slowniki(_: dict[str, list[str]]) -> dict[str, Any]:
    """Slowniki operacyjne: kody opoznien AHM730, SSR i klasy rezerwacyjne.

    Panel pokazywal wczesniej cztery recznie wpisane kody opoznien. Baza ma ich
    siedemdziesiat szesc, z sekcja i klasyfikacja EU261 przy kazdym, wiec nie ma
    powodu ich powtarzac w interfejsie ani wybierac za uzytkownika.
    """
    from ..adapters.lot_db import load_lot_db

    db = load_lot_db()
    sekcje: dict[str, list[dict[str, Any]]] = {}
    for kod, row in sorted(db.delay_codes.items()):
        opis, klasa, _waga, sekcja, alfa = row[0], row[1], row[2], row[3], row[4]
        sekcje.setdefault(sekcja, []).append({
            "kod": kod, "alfa": alfa, "opis": opis, "klasa": klasa,
        })
    return {
        "kody_opoznien": sekcje,
        "klasy_eu261": {
            "c": "odpowiedzialność przewoźnika, odszkodowanie należne",
            "n": "okoliczność nadzwyczajna, odszkodowanie nienależne, opieka nadal obowiązuje",
            "d": "kod reakcyjny, dziedziczy klasyfikację przyczyny pierwotnej",
        },
        "ssr": {k: {"kod": k, "opis": v[3], "grupa": v[4] if len(v) > 4 else "",
                    "chroniony": bool(v[5]) if len(v) > 5 else False}
                for k, v in sorted(db.ssr.items())},
        "ssr_mapa": SSR_KOD,
        "klasy_rezerwacyjne": {k: {"klasa": k, "kabina": v[0], "mnoznik": v[1],
                                   "priorytet": v[2], "zwrot_pct": v[3], "taryfa": v[4]}
                               for k, v in sorted(db.booking_classes.items())},
    }


def api_config(_: dict[str, list[str]]) -> dict[str, Any]:
    """Polityka, ktora silnik stosuje: presety wag, twarde filtry, autoryzacje."""
    from ..kernel.policy_store import PolicyStore

    store = PolicyStore()
    #: Wiekszosc wejsc `PolicyStore` to properties, a nie metody. Wywolanie ich
    #: nawiasem konczylo sie `TypeError: 'list' object is not callable`.
    return {
        "presety": store.presets,
        "twarde_filtry": store.hard_filters,
        "autoryzacja": store.authorization,
        "eskalacja": store.escalation,
        "sop": store.sop,
        "koszt": store.cost,
        "prawo": store.legal,
        "ftl": store.ftl,
        "kurs_eur_pln": store.eur_pln,
        "nadpisania_zadeklarowane": store.declared_overrides(),
        "nadpisania_zastosowane": store.applied_overrides(),
    }


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
    overbooking = int(body.get("overbooking", 0))
    priority = int(body.get("priority", 50))
    if not 0 <= day <= 6:
        raise ApiError(f"dzien tygodnia poza zakresem 0-6: {day}")
    if not 0 <= delay <= 24 * 60:
        raise ApiError(f"opoznienie poza zakresem 0-1440 min: {delay}")
    if not 0 <= overbooking <= 500:
        raise ApiError(f"nadsprzedaz poza zakresem 0-500: {overbooking}")
    if not 0 <= priority <= 100:
        raise ApiError(f"priorytet poza zakresem 0-100: {priority}")
    if delay == 0 and overbooking == 0:
        raise ApiError(
            "nie ma czego liczyc: ustaw opoznienie albo nadsprzedaz")
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
        # Pusty kod znaczy "bez kodu". Node 04 sam dobierze 14 PO dla samej
        # nadsprzedazy, zamiast liczyc cene opoznienia, ktorego nie ma.
        delay_code=(body.get("code") or None),
        overbooking=overbooking,
        priority=priority,
        preset=str(body.get("preset") or "STANDARD"),
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
    day = _int(query, "day", 4, 0, 6)
    snap, _ = _snapshot(day, _int(query, "seed", 2026, 0, 10**9))

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
    "/api/day": api_day,
    "/api/config": api_config,
    "/api/slowniki": api_slowniki,
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
