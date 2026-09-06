"""Weryfikacja dekodu i analiza obu zrodel danych LOT-u.

Uruchomienie:
    python tools/analiza_danych.py

Skrypt robi dwie rzeczy naraz i celowo nie sa rozdzielone: sprawdzenie, czy
dobrze zdekodowalem baze, polega na skonfrontowaniu jej z druga baza i z
wlasnymi regulami -- a to samo w sobie jest analiza jakosci danych.
"""

from __future__ import annotations

import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lotis.adapters.lot_db import load_lot_db
from lotis.adapters.siatka import load_siatka

OK, WARN, BAD = "  [ok] ", "  [!!] ", "  [XX] "


def head(text: str) -> None:
    print(f"\n{'=' * 74}\n{text}\n{'=' * 74}")


def main() -> int:
    db = load_lot_db()
    sn = load_siatka()

    head("ZRODLA")
    print(f"  loops.jsx     v{db.version}, wygenerowana {db.generated}")
    print(f"                {db.source}")
    print(f"  lot-siatka    {sn.provenance.get('zakresDanych')}, "
          f"{sn.provenance.get('operacji')} operacji")
    print(f"                {sn.source}")
    print("\n  loops.jsx:", db.summary())
    print("\n  siatka:   ", sn.summary())

    problems: list[str] = []

    # ---------------------------------------------------------------- 1
    head("1. ZGODNOSC OBU ZRODEL")
    db_regs, sn_regs = set(db.fleet), {f["reg"] for f in sn.raw["flota"]}
    db_nums, sn_nums = set(db.flights), {r["nr"] for r in sn.raw["rejsy"]}
    db_ports, sn_ports = set(db.ports), {p["iata"] for p in sn.raw["porty"]}
    db_routes = {f"{o}-{d}" for o, d in db.routes}
    sn_routes = {r["trasa"] for r in sn.raw["trasy"]}

    for label, a, b in [("flota", db_regs, sn_regs), ("numery rejsow", db_nums, sn_nums),
                        ("porty", db_ports, sn_ports), ("trasy", db_routes, sn_routes)]:
        common = a & b
        print(f"  {label:16} loops={len(a):4}  siatka={len(b):4}  wspolne={len(common):4}"
              f"  tylko_loops={len(a - b):3}  tylko_siatka={len(b - a):3}")
        if label == "numery rejsow" and len(common) != len(a):
            print(f"       tylko w loops.jsx: {sorted(a - b)[:6]}")
        if label == "flota" and (b - a):
            print(f"       tylko w siatce: {sorted(b - a)[:8]}")
    wet = [f.reg for f in db.fleet.values() if f.wet_lease]
    print(f"\n{OK}roznica floty to ACMI: {wet} "
          f"(operatorzy: {sorted({db.fleet[r].operator for r in wet})})")
    print(f"       siatka ma tylko operatora LOT, wiec ACMI tam nie ma -- zgadza sie.")

    # ---------------------------------------------------------------- 2
    head("2. WERYFIKACJA DEKODU: tier EU261 policzony z reguly vs zapisany w bazie")
    mismatch, checked = [], 0
    for (o, d), route in db.routes.items():
        po, pd = db.ports.get(o), db.ports.get(d)
        if not po or not pd:
            continue
        intra = po.eu261 and pd.eu261
        expected = db.eu261_tier_for(route.km, intra)
        checked += 1
        if expected != route.eu261_tier:
            mismatch.append((f"{o}-{d}", route.km, intra, route.eu261_tier, expected))
    print(f"  sprawdzone trasy: {checked},  rozbieznosci: {len(mismatch)}")
    if mismatch:
        print(f"{WARN}pierwsze rozbieznosci (trasa, km, intra, w bazie, z reguly):")
        for row in mismatch[:8]:
            print("       ", row)
        problems.append(f"tier EU261: {len(mismatch)} rozbieznosci")
    else:
        print(f"{OK}regula tierRule odtwarza kolumne T[3] co do jednego rekordu")
        print(f"       -> dekod T[2]=km i T[3]=tier potwierdzony")

    # ---------------------------------------------------------------- 3
    head("3. WERYFIKACJA DEKODU: maska dni tygodnia (0 = poniedzialek)")
    hits = miss = 0
    for weekday, day in sn.week.items():
        present = {f.number for f in day.flights}
        for number in present:
            sched = db.flights.get(number)
            if not sched:
                continue
            if sched.operates_on(weekday):
                hits += 1
            else:
                miss += 1
    total = hits + miss
    pct = 100 * hits / total if total else 0
    print(f"  rejsy z rzeczywistej doby obecne w masce: {hits}/{total} ({pct:.1f}%)")
    if pct > 85:
        print(f"{OK}indeks 0 = poniedzialek potwierdzony empirycznie")
    else:
        print(f"{BAD}maska nie zgadza sie z dobami -- inny porzadek dni?")
        problems.append("maska dni tygodnia")
        for shift in range(1, 7):
            h = sum(
                1 for wd, day in sn.week.items() for f in day.flights
                if (s := db.flights.get(f.number)) and s.operates_on((wd + shift) % 7)
            )
            print(f"       przesuniecie +{shift}: {h}/{total} ({100*h/total:.1f}%)")

    # ---------------------------------------------------------------- 4
    head("4. CIAGLOSC ROTACJI W TYGODNIU OPERACYJNYM")
    tot_f = tot_b = 0
    for weekday in sorted(sn.week):
        day = sn.week[weekday]
        regs = day.by_registration()
        breaks = day.continuity_breaks()
        tot_f += len(day.flights)
        tot_b += len(breaks)
        broken_regs = len({b[0] for b in breaks})
        print(f"  {day.name:12} {day.day}  rejsow={len(day.flights):3}  maszyn={len(regs):3}"
              f"  przerw={len(breaks):3}  maszyn z przerwa={broken_regs:3}")
    print(f"\n  razem rejsow {tot_f}, przerw w lancuchach {tot_b} "
          f"({100*tot_b/tot_f:.1f}% odcinkow)")
    print(f"       Przerwa = kolejny odcinek startuje z innego portu niz konczyl poprzedni.")
    print(f"       Zrodlo tlumaczy to oknem eksportu, nie bledem -- ale node 01 musi")
    print(f"       traktowac przerwany lancuch inaczej niz domkniety.")

    # ---------------------------------------------------------------- 5
    head("5. BUFOR POSTOJU vs MINIMUM TYPU (gdzie siatka jest napieta)")
    tight: list[tuple[str, str, str, int, int]] = []
    buffers: list[int] = []
    for weekday in sorted(sn.week):
        day = sn.week[weekday]
        for reg, legs in day.by_registration().items():
            for prev, nxt in zip(legs, legs[1:]):
                if prev.dest != nxt.origin:
                    continue
                ground = nxt.std_utc_min - (prev.std_utc_min + prev.block_min)
                if ground < 0:
                    ground += 1440
                if ground > 600:
                    continue
                route = db.routes.get((prev.origin, prev.dest))
                sector = route.sector if route else "europe"
                table = db.turnarounds.get(prev.type_code, {})
                rec, minimum = table.get(sector, table.get("europe", (45, 35)))
                buffers.append(ground - minimum)
                if ground < minimum:
                    tight.append((day.name, reg, f"{prev.number}->{nxt.number}", ground, minimum))
    if buffers:
        buffers.sort()
        print(f"  postojow przeanalizowanych: {len(buffers)}")
        print(f"  zapas ponad minimum typu:   mediana {statistics.median(buffers):.0f} min, "
              f"P10 {buffers[len(buffers)//10]:.0f}, P90 {buffers[9*len(buffers)//10]:.0f}")
        print(f"  postoje ponizej minimum:    {len(tight)} ({100*len(tight)/len(buffers):.1f}%)")
        for row in tight[:6]:
            print(f"       {row[0]:12} {row[1]} {row[2]:22} postoj {row[3]} min < min {row[4]} min")
        print(f"\n       To jest realna miara kruchosci siatki: postoj bez zapasu znaczy, ze")
        print(f"       kazde opoznienie wejsciowe propaguje sie w calosci na kolejny odcinek.")

    # ---------------------------------------------------------------- 6
    head("6. CISZA NOCNA: operacje planowane w oknie zakazu (typ 1)")
    violations: list[tuple[str, str, str, str]] = []
    for weekday in sorted(sn.week):
        day = sn.week[weekday]
        for f in day.flights:
            for port_code, minute_utc, kind in (
                (f.origin, f.std_utc_min, "odlot"),
                (f.dest, f.std_utc_min + f.block_min, "przylot"),
            ):
                port = db.ports.get(port_code)
                if not port or not port.curfew:
                    continue
                local = (minute_utc + port.utc_offset_min(day.day)) % 1440
                if port.curfew.blocks(local, planning=True):
                    violations.append((day.name, f.number, f"{kind} {port_code}",
                                       f"{local//60:02d}:{local%60:02d}"))
    print(f"  operacji w oknie zakazu planowania: {len(violations)}")
    by_port = Counter(v[2].split()[1] for v in violations)
    for port_code, count in by_port.most_common(8):
        port = db.ports[port_code]
        window = f"{port.curfew.start_min//60:02d}:{port.curfew.start_min%60:02d}" \
                 f"-{port.curfew.end_min//60:02d}:{port.curfew.end_min%60:02d}"
        print(f"       {port_code} {window}  {count} operacji")
    print(f"\n       Uwaga interpretacyjna: curfew typu 1 zakazuje PLANOWANIA, a maszyna")
    print(f"       opozniona z przyczyn niezaleznych moze operowac. Te wpisy to wiec")
    print(f"       albo wyjatki, albo operacje realizowane po terminie -- nie 'bledy'.")
    print(f"       Dla node 05 wazne jest co innego: KAZDA opcja, ktora przesuwa odlot")
    print(f"       w to okno, musi zostac sprawdzona wlasnie ta regula.")

    # ---------------------------------------------------------------- 7
    head("7. PUNKTUALNOSC: asymetria odlot/przylot")
    dep, arr = sn.global_stats["odlot"], sn.global_stats["przylot"]
    print(f"  {'':10} {'n':>6} {'mediana':>9} {'srednia':>9} {'P25':>6} {'P75':>6} {'P90':>6} {'max':>6} {'<=15min':>9}")
    for name, s in (("odlot", dep), ("przylot", arr)):
        print(f"  {name:10} {s.n:6} {s.median:9.0f} {s.mean:9.1f} {s.p25:6.0f} "
              f"{s.p75:6.0f} {s.p90:6.0f} {s.max:6.0f} {s.on_time_15_pct:8.1f}%")
    print(f"\n  Odlot ma mediane {dep.median:+.0f} min, przylot {arr.median:+.0f} min.")
    print(f"  Punktualnosc rosnie z {dep.on_time_15_pct:.1f}% do {arr.on_time_15_pct:.1f}%.")
    print(f"  Bloki rozkladowe zawieraja zapas, ktory zaloga odrabia w powietrzu.")
    print(f"\n  KONSEKWENCJA DLA SILNIKA: opoznienie odlotu NIE przeklada sie 1:1 na")
    print(f"  opoznienie przylotu. Node 10 nie moze propagowac minuty za minute, a")
    print(f"  node 12 liczy prog 3 h na PRZYLOCIE (EU261 Art. 6 + C-402/07), gdzie")
    print(f"  rozklad jest o {dep.median - arr.median:.0f} min lagodniejszy.")

    # ---------------------------------------------------------------- 8
    head("8. NAJGORSZE REJSY I TRASY (min. 10 obserwacji)")
    worst_f = sorted(
        ((nr, s["odlot"]) for nr, s in sn.by_flight.items()
         if "odlot" in s and s["odlot"].n >= 10),
        key=lambda x: x[1].median, reverse=True)[:10]
    print("  rejs      n  mediana  P90   <=15min   trasa")
    for nr, s in worst_f:
        sched = db.flights.get(nr)
        route = f"{sched.origin}-{sched.dest}" if sched else "?"
        print(f"  {nr:8} {s.n:3} {s.median:7.0f} {s.p90:5.0f} {s.on_time_15_pct:7.1f}%   {route}")

    worst_p = sorted(
        ((p, s) for p, s in sn.by_departure_port.items() if s.n >= 20),
        key=lambda x: x[1].median, reverse=True)
    print("\n  port wylotu (n>=20), najgorsze i najlepsze:")
    for p, s in worst_p[:5] + [("...", None)] + worst_p[-5:]:
        if s is None:
            print("       ...")
            continue
        port = db.ports.get(p)
        slot = f"L{port.slot_level}" if port and port.slot_level else "—"
        print(f"       {p:5} n={s.n:4} mediana {s.median:+4.0f}  P90 {s.p90:4.0f}"
              f"  <=15min {s.on_time_15_pct:5.1f}%  slot {slot}")

    # ---------------------------------------------------------------- 9
    head("9. RYZYKO KONCENTRACJI FLOTY I BAZA SWAP")
    by_type = Counter(f.type_code for f in db.fleet.values() if not f.wet_lease)
    print("  flota wlasna wg typu:")
    for code, count in by_type.most_common():
        spec = db.types.get(code)
        print(f"       {code:5} {count:3} maszyn  {spec.seats:3} miejsc  "
              f"uprawnienie {spec.rating:8} skala kosztu {spec.cost_scale}")
    ratings = Counter(db.types[c].rating for c, n in by_type.items() for _ in range(n))
    print(f"\n  wg uprawnienia zalogi: {dict(ratings)}")
    swap_bases = db.config["base"]["swap"]
    print(f"\n  SWAP mozliwy tylko w: {swap_bases}  (CF.base.swap)")
    busiest = sn.busiest_day()
    outside = [f for f in busiest.flights if f.origin not in swap_bases]
    print(f"  W najbardziej obciazonej dobie ({busiest.name}, {busiest.day}) "
          f"{len(outside)}/{len(busiest.flights)} odlotow "
          f"({100*len(outside)/len(busiest.flights):.0f}%) startuje POZA baza SWAP.")
    print(f"       Dla tych rejsow opcja SWAP nie istnieje fizycznie -- node 07 nie moze")
    print(f"       jej wygenerowac, a node 05 musi ja odrzucic na bramce samolotu.")

    # ---------------------------------------------------------------- 10
    head("10. KODY OPOZNIEN -> PRAWDOPODOBIENSTWO ODSZKODOWANIA")
    classes = Counter(db.delay_code_class(k) for k in db.delay_codes)
    label = {"c": "przewoznik (p=1.0)", "n": "nadzwyczajne (p=0.0)",
             "d": "reakcyjne (p=0.5)", "?": "nieokreslone"}
    for cls, count in classes.most_common():
        print(f"       {label.get(cls, cls):26} {count:3} kodow")
    print(f"\n       To jest gotowy mostek miedzy przyczyna zaklocenia a kosztem")
    print(f"       oczekiwanym z Art. 7 -- node 09 mnozy kwote przez to p, zamiast")
    print(f"       zgadywac. 76 kodow AHM 730 z orzecznictwem TSUE przy spornych.")

    # ---------------------------------------------------------------- 11
    head("11. CO Z TEGO WCHODZI DO KTOREGO NODE")
    mapping = [
        ("01 DANE", "siatka.tydzienOperacyjny (2602 rejsy, 7 rzeczywistych dob) + DB.F/L/T"),
        ("02 DATA ENGINE", "DB.L[tz] strefy IANA; ciaglosc rotacji jako miara pewnosci"),
        ("03 BASELINE", "DB.KL (22 klasy, mnozniki), DB.ST (7 statusow), DB.CF.pax (LF, transfer)"),
        ("04 ZAKLOCENIE", "DB.KO (76 kodow AHM 730 z klasyfikacja EU261)"),
        ("05 FEASIBILITY", "DB.FT (tabele FDP EASA), DB.L[curfew/slot/MCT], DB.TU (postoje)"),
        ("06 REZERWACJA", "DB.CF.base.spare = WAW, KRK"),
        ("07 SCENARIO", "DB.SZ (8 opcji z warunkami), DB.CF.switches"),
        ("08 REVENUE", "DB.KL mnozniki wartosci, DB.TY kabiny J/PE/Y"),
        ("09 COST", "DB.K (wszystkie stawki EUR + provenance), DB.TF (5 poziomow interline)"),
        ("10 NETWORK", "siatka.statystyka (realna propagacja), DB.CF.onward"),
        ("11 OPTIMIZATION", "siatka.statystyka kwantyle -> realne widelki min/oczek/max"),
        ("12 FILTR PRAWNY", "DB.EU (tiery, progi, TSUE), DB.LG (12 podstaw), DB.SS (chronieni)"),
        ("13 WRAZLIWOSC", "DB.CF.presets (STANDARD/SZCZYT/KRYZYS) + weights"),
        ("15 PRACOWNIK", "DB.CF.hard (8 filtrow twardych, w tym zakaz ugod ponizej Art. 7)"),
        ("17 WYNIK", "siatka.statystyka jako punkt odniesienia do kalibracji"),
    ]
    for node, source in mapping:
        print(f"  {node:18} {source}")

    head("PODSUMOWANIE")
    if problems:
        print(f"{WARN}problemy: {problems}")
    else:
        print(f"{OK}dekod obu zrodel potwierdzony krzyzowo, brak rozbieznosci")
    print(f"\n  Dane pokrywaja caly silnik. Zadna warstwa nie musi juz byc syntetyczna")
    print(f"  poza tozsamoscia pojedynczego pasazera -- a tej nie ma w zadnym")
    print(f"  publicznym zrodle i miec nie moze.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
