"""Osiemnascie nodes.

Zestaw buduje jeden pelny przeplyw i sprawdza na nim niezmienniki, ktore musza
zachodzic niezaleznie od danych. Osobno ida testy jednostkowe funkcji
pomocniczych i sciezek wyjatkowych.

Najwazniejsze testy w tym pliku to nie te, ktore sprawdzaja liczby, tylko te,
ktore sprawdzaja ZALEZNOSCI: ze filtr prawny nie pisze do rejestru kosztow,
ze kasacja nie wychodzi darmowa, ze SWAP wchodzi jako para rejsow, ze zaden
pasazer nie znika bez sladu. Kazdy z nich odpowiada bledowi, ktory nie objawia
sie wyjatkiem, tylko liczba wygladajaca poprawnie.
"""

from __future__ import annotations

import tempfile
import unittest
from functools import lru_cache
from pathlib import Path

from lotis.kernel.contracts import (
    Baseline, DisruptionType, OptionKind, PaxOutcomeKind, Trigger,
)
from lotis.kernel.errors import NoLawfulOption
from lotis.kernel.money import Money, money_sum
from lotis.kernel.node import Pipeline, RunContext
from lotis.kernel.report import Status
from lotis.nodes import NODE_CLASSES, Decision, build_pipeline
from lotis.kernel.prorate import distance_shares
from lotis.nodes.n04_zaklocenie import _pick_flight
from lotis.nodes.n07_scenariusze import _oal_wait, _own_alternatives
from lotis.nodes.n09_koszt import _is_compensable

from ._helpers import db, snapshot


@lru_cache(maxsize=4)
def przebieg(delay: int = 180, decision: str = "ACCEPT", fail_step: str | None = None):
    """Jeden pelny run, wspoldzielony przez caly zestaw. Trwa ~2.5 s."""
    tmp = tempfile.TemporaryDirectory()
    ctx = RunContext("t", reports_root=Path(tmp.name))
    reports = Pipeline(build_pipeline(
        weekday=4, delay_min=delay, decision=Decision(decision), fail_step=fail_step,
    )).run(ctx)
    return ctx, reports, tmp


class TestPrzeplyw(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_jest_osiemnascie_nodes(self):
        self.assertEqual(len(NODE_CLASSES), 18)
        self.assertEqual(len(self.reports), 18)

    def test_identyfikatory_sa_unikalne_i_w_kolejnosci_tablicy(self):
        ids = [r.node_id for r in self.reports]
        self.assertEqual(len(set(ids)), 18)
        self.assertEqual(ids[0], "01")
        self.assertEqual(ids[-1], "17")
        self.assertIn("15b", ids)

    def test_zaden_node_nie_jest_zablokowany(self):
        blocked = [r.node_id for r in self.reports if r.status is Status.BLOCKED]
        self.assertEqual(blocked, [])

    def test_kazdy_node_ma_podsumowanie_i_liczby(self):
        for r in self.reports:
            with self.subTest(node=r.node_id):
                self.assertTrue(r.summary, f"{r.node_id} bez podsumowania")
                self.assertTrue(r.numbers, f"{r.node_id} bez liczb")

    def test_kazdy_node_ma_nazwe_pliku_bez_kolizji(self):
        stems = {f"{r.node_id}_{r.node_name}" for r in self.reports}
        self.assertEqual(len(stems), 18)

    def test_przeplyw_nie_zostal_zatrzymany(self):
        self.assertFalse(self.ctx.halted, self.ctx.halt_reason)

    def test_stan_niesie_wszystkie_produkty(self):
        for key in ("snapshot", "confidence", "baseline", "disruption", "feasibility",
                    "resources", "options", "revenue", "costs", "network",
                    "evaluations", "lawful", "ranking", "checks", "decision",
                    "execution", "audit", "calibration"):
            with self.subTest(klucz=key):
                self.assertIn(key, self.ctx.state)

    def test_manifest_zawiera_statusy_wszystkich(self):
        import json
        manifest = json.loads(
            (self.ctx.writer.dir / "_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(len(manifest["statuses"]), 18)


class TestBaseline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_prorata_domyka_sie_co_do_grosza(self):
        """Luka 8: suma po odcinkach musi rownac sie sumie po podrozach.

        Gdyby pasazer transferowy wnosil pelna wartosc na kazdym odcinku,
        baseline calej siatki bylby zawyzony o wartosc ruchu transferowego.
        """
        baseline: Baseline = self.ctx.require("baseline")
        self.assertEqual(money_sum(baseline.per_flight.values()), baseline.total)
        self.assertEqual(money_sum(baseline.per_itinerary.values()), baseline.total)

    def test_baseline_jest_dodatni(self):
        self.assertGreater(self.ctx.require("baseline").total.minor, 0)

    def test_udzialy_dystansu_sumuja_sie_do_jedynki(self):
        snap, _ = snapshot(4)
        itin = next(i for i in snap.itineraries.values() if len(i.segments) == 2)
        shares = distance_shares(snap,itin.segments)
        self.assertAlmostEqual(sum(shares), 1.0, places=9)

    def test_pojedynczy_odcinek_dostaje_calosc(self):
        snap, _ = snapshot(4)
        itin = next(i for i in snap.itineraries.values() if len(i.segments) == 1)
        self.assertEqual(distance_shares(snap,itin.segments), [1.0])

    def test_odcinek_bez_portow_nie_wywala_proraty(self):
        snap, _ = snapshot(4)
        shares = distance_shares(snap,("NIE-ISTNIEJE", "TEZ-NIE"))
        self.assertAlmostEqual(sum(shares), 1.0, places=9)

    def test_baseline_ma_wpis_dla_rejsu_z_pasazerami(self):
        baseline: Baseline = self.ctx.require("baseline")
        snap = self.ctx.require("snapshot")
        z_pasazerami = [f for f in snap.flights if baseline.pax_per_flight.get(f)]
        self.assertGreater(len(z_pasazerami), 0)
        for flight_id in z_pasazerami[:50]:
            with self.subTest(rejs=flight_id):
                self.assertGreater(baseline.of(flight_id).minor, 0)

    def test_nieznany_rejs_daje_zero(self):
        self.assertEqual(self.ctx.require("baseline").of("NIE-MA"), Money.zero())


class TestZaklocenie(unittest.TestCase):
    def test_wybrany_rejs_ma_odcinki_ponizej(self):
        """Zaklocenie ostatniego odcinka doby nie ma czego propagowac."""
        snap, _ = snapshot(4)
        flight_id = _pick_flight(snap)
        flight = snap.flights[flight_id]
        rotation = snap.rotations[flight.rotation_id]
        legs = sorted((snap.flights[f] for f in rotation.flight_ids), key=lambda f: f.seq)
        self.assertLess(flight.seq, legs[-1].seq)

    def test_wybor_jest_deterministyczny(self):
        snap, _ = snapshot(4)
        self.assertEqual(_pick_flight(snap), _pick_flight(snap))

    def test_termin_decyzji_jest_po_zdarzeniu(self):
        ctx, _, _ = przebieg()
        d = ctx.require("disruption")
        self.assertGreater(d.decision_deadline, d.at)

    def test_domyslny_kod_daje_odpowiedzialnosc_przewoznika(self):
        """Kod 41 = usterka techniczna, klasa `c`, p = 1.0 -- najostrozniejsze zalozenie."""
        self.assertEqual(db().delay_code_class("41"), "c")
        self.assertEqual(db().compensation_probability("41"), 1.0)

    def test_nieznany_rejs_blokuje_node(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(
                weekday=4, flight_id="NIE-ISTNIEJE")).run(ctx)
            self.assertIs(reports[3].status, Status.BLOCKED)
            self.assertTrue(ctx.halted)

    def test_wyzwalacz_poczatkowy(self):
        ctx, _, _ = przebieg()
        self.assertIs(ctx.require("disruption").trigger, Trigger.INITIAL)

    def test_typ_domyslny_to_usterka(self):
        ctx, _, _ = przebieg()
        self.assertIs(ctx.require("disruption").type, DisruptionType.TECHNICAL)


class TestFeasibility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_sa_cztery_bramki(self):
        gates = self.ctx.require("feasibility")["gates"]
        self.assertEqual(set(gates), {"samolot", "zaloga", "port", "miejsca"})

    def test_kazda_bramka_ma_uzasadnienie(self):
        for name, gate in self.ctx.require("feasibility")["gates"].items():
            with self.subTest(bramka=name):
                self.assertIn("passed", gate)
                self.assertTrue(gate["reason"])

    def test_swap_dozwolony_tylko_gdy_bramka_samolotu_przeszla(self):
        f = self.ctx.require("feasibility")
        self.assertEqual(f["allowed_kinds"]["SWAP"], f["gates"]["samolot"]["passed"])

    def test_swap_tylko_w_bazie_glownej(self):
        """`CF.base.swap` dopuszcza wylacznie WAW -- poza baza nie ma czym podmienic."""
        self.assertEqual(list(db().config["base"]["swap"]), ["WAW"])

    def test_bramka_samolotu_odrzuca_poza_baza(self):
        from lotis.nodes.n05_feasibility import _gate_aircraft
        snap, _ = snapshot(4)
        poza_baza = next(f for f in snap.flights.values() if f.dep != "WAW")
        gate = _gate_aircraft(snap, db(), poza_baza, 180)
        self.assertFalse(gate.passed)
        self.assertIn("baza SWAP", gate.reason)


class TestScenariusze(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_powstalo_kilka_opcji(self):
        self.assertGreaterEqual(len(self.ctx.require("options")), 3)

    def test_identyfikatory_opcji_sa_unikalne(self):
        options = self.ctx.require("options")
        self.assertEqual(len({o.id for o in options}), len(options))

    def test_kazda_opcja_dotyka_rejsu_zrodlowego(self):
        source = self.ctx.require("disruption").flight_id
        for option in self.ctx.require("options"):
            with self.subTest(opcja=option.id):
                self.assertIn(source, option.affected_flights)

    def test_kazda_opcja_ma_los_kazdego_pasazera(self):
        """Pasazer bez losu zniknalby z rachunku bezkosztowo -- opcja wygladalaby
        na tania dokladnie dlatego, ze o kims zapomniala."""
        snap = self.ctx.require("snapshot")
        source = self.ctx.require("disruption").flight_id
        expected = {p.id for p in snap.passengers_on(source)}
        for option in self.ctx.require("options"):
            with self.subTest(opcja=option.id):
                self.assertEqual(set(option.pax_outcomes), expected)

    def test_swap_zawsze_jako_para_rejsow(self):
        """Blok 5: liczony sam rejs A zawsze wychodzi na minus."""
        for option in self.ctx.require("options"):
            if option.aircraft_swap:
                a, b = option.aircraft_swap
                with self.subTest(opcja=option.id):
                    self.assertIn(a, option.affected_flights)
                    self.assertIn(b, option.affected_flights)
                    self.assertNotEqual(a, b)

    def test_tryby_liczenia_sa_przypisane(self):
        by_id = {o.id: o.kind for o in self.ctx.require("options")}
        self.assertIs(by_id["HOLD"], OptionKind.MODIFYING)
        self.assertIs(by_id["CANCEL"], OptionKind.MODIFYING)
        for oid in ("REBOOK-OWN", "REBOOK-OAL", "OVERNIGHT"):
            if oid in by_id:
                with self.subTest(opcja=oid):
                    self.assertIs(by_id[oid], OptionKind.RESTRUCTURING)

    def test_kasacja_nie_zostawia_pasazerow_bez_oczekiwania(self):
        """Zerowy czas oczekiwania czynil kasacje najtansza opcja: nie generowala
        ani opieki, ani ekspozycji odszkodowawczej."""
        cancel = next(o for o in self.ctx.require("options") if o.id == "CANCEL")
        for outcome in cancel.pax_outcomes.values():
            with self.subTest():
                self.assertGreater(outcome.delay_min, 0)

    def test_oal_i_split_licza_oczekiwanie_tak_samo(self):
        """Ta sama operacja wyceniana dwoma sposobami dawala SPLITowi przewage."""
        options = {o.id: o for o in self.ctx.require("options")}
        if "SPLIT" not in options or "REBOOK-OAL" not in options:
            self.skipTest("brak obu opcji w tym runie")
        oal = {o.delay_min for o in options["REBOOK-OAL"].pax_outcomes.values()}
        split_oal = {o.delay_min for o in options["SPLIT"].pax_outcomes.values()
                     if o.kind is PaxOutcomeKind.REBOOKED_OAL}
        self.assertTrue(split_oal <= oal)

    def test_oczekiwanie_oal_pochodzi_z_bazy(self):
        snap, _ = snapshot(4)
        flight = snap.flights[_pick_flight(snap)]
        wait, frequency = _oal_wait(snap, db(), flight)
        banks = db().config["onward"]["next_bank_min"]
        extra = db().config["onward"]["partner_mct_extra"]
        self.assertIn(wait - extra, [int(v) for v in banks.values()])
        self.assertGreater(frequency, 0)

    def test_alternatywy_sa_pozniejsze_i_w_tej_samej_relacji(self):
        snap, _ = snapshot(4)
        flight = snap.flights[_pick_flight(snap)]
        for other in _own_alternatives(snap, flight):
            with self.subTest(rejs=other.id):
                self.assertGreater(other.std, flight.std)
                self.assertEqual((other.dep, other.arr), (flight.dep, flight.arr))


class TestRevenueIKoszt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_kazda_opcja_ma_przychod_i_koszt(self):
        options = self.ctx.require("options")
        revenue, costs = self.ctx.require("revenue"), self.ctx.require("costs")
        for option in options:
            with self.subTest(opcja=option.id):
                self.assertIn(option.id, revenue)
                self.assertIn(option.id, costs)

    def test_skladniki_kosztu_sumuja_sie_do_calosci(self):
        for option_id, cost in self.ctx.require("costs").items():
            with self.subTest(opcja=option_id):
                self.assertEqual(money_sum(cost.components.values()), cost.total)

    def test_zaden_koszt_nie_jest_ujemny(self):
        for option_id, cost in self.ctx.require("costs").items():
            for name, value in cost.components.items():
                if name != "roznica_kosztu_typu":     # downgauge moze byc ujemny
                    with self.subTest(opcja=option_id, skladnik=name):
                        self.assertGreaterEqual(value.minor, 0)

    def test_kasacja_nie_jest_darmowa(self):
        """Odszkodowanie z Art. 5 nalezy sie za sam fakt odwolania, bez progu."""
        costs = self.ctx.require("costs")
        self.assertGreater(costs["CANCEL"].total.minor, 0)
        self.assertIn("odszkodowanie_art7", costs["CANCEL"].components)

    def test_odwolanie_jest_kompensowalne_bez_progu_czasowego(self):
        from lotis.kernel.contracts import PaxOutcome
        from lotis.kernel.pricing import pricing
        price = pricing()
        self.assertTrue(_is_compensable(
            PaxOutcome(PaxOutcomeKind.CANCELLED_REFUND, delay_min=0), price))
        self.assertFalse(_is_compensable(
            PaxOutcome(PaxOutcomeKind.DELAYED, delay_min=60), price))
        self.assertTrue(_is_compensable(
            PaxOutcome(PaxOutcomeKind.DELAYED, delay_min=200), price))

    def test_tryb_kosztu_zgadza_sie_z_rodzajem_opcji(self):
        options = {o.id: o for o in self.ctx.require("options")}
        for option_id, cost in self.ctx.require("costs").items():
            with self.subTest(opcja=option_id):
                self.assertIs(cost.mode, options[option_id].kind)

    def test_kwoty_sa_w_zlotych(self):
        for cost in self.ctx.require("costs").values():
            with self.subTest():
                self.assertEqual(cost.total.currency, "PLN")

    def test_rebooking_na_oal_zachowuje_przychod(self):
        """Przychod zostaje, rozliczenie interline jest osobnym kosztem."""
        revenue = self.ctx.require("revenue")
        if "REBOOK-OAL" in revenue:
            self.assertGreaterEqual(revenue["REBOOK-OAL"].kept.minor, 0)
            self.assertIn("rozliczenie_interline",
                          self.ctx.require("costs")["REBOOK-OAL"].components)

    def test_zaden_skladnik_przychodu_nie_jest_ujemny(self):
        """Znalezisko audytu: `przychod rejsow niedotknietych` wychodzil ujemny
        w 30 przypadkach na siedmiu dobach, bo odejmowal prorate dystansowa
        od proraty po liczbie odcinkow. Przychod z rejsu nie moze byc ujemny."""
        for option_id, rev in self.ctx.require("revenue").items():
            with self.subTest(opcja=option_id):
                self.assertGreaterEqual(rev.kept.minor, 0, "przychod ujemny")
                self.assertGreaterEqual(rev.lost.minor, 0)
                for nazwa, wartosc in rev.components.items():
                    self.assertGreaterEqual(wartosc.minor, 0, f"skladnik {nazwa} ujemny")

    def test_przychod_nie_przekracza_baseline_dotknietych(self):
        baseline = self.ctx.require("baseline")
        for option in self.ctx.require("options"):
            rev = self.ctx.require("revenue")[option.id]
            touched = money_sum(baseline.of(f) for f in option.affected_flights)
            with self.subTest(opcja=option.id):
                self.assertLessEqual(rev.kept, touched)
                self.assertEqual(rev.kept + rev.lost, touched)

    def test_opcja_bez_strat_zachowuje_caly_baseline(self):
        """HOLD nikogo nie przestawia, wiec przychod ma zostac nienaruszony."""
        baseline = self.ctx.require("baseline")
        hold = next(o for o in self.ctx.require("options") if o.id == "HOLD")
        rev = self.ctx.require("revenue")["HOLD"]
        touched = money_sum(baseline.of(f) for f in hold.affected_flights)
        self.assertEqual(rev.kept, touched)
        self.assertEqual(rev.lost, Money.zero())


class TestSiecIOptymalizacja(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_horyzont_ma_powod_zatrzymania(self):
        znane = {"BASE_RETURN", "END_OF_DAY", "ROTATION_END", "MAX_LEGS"}
        for impact in self.ctx.require("network").values():
            with self.subTest():
                # Opcja opozniajaca dwa rejsy (para SWAPu) ma dwa horyzonty,
                # wiec powod bywa zlozony.
                self.assertTrue(set(impact.stop_reason.split("+")) <= znane,
                                impact.stop_reason)

    def test_propagacja_nie_przekracza_opoznienia_zrodlowego(self):
        """Bufory postoju wchlaniaja opoznienie -- nie moze ono rosnac.

        Sprawdzamy gorne ograniczenie, a nie kolejnosc w slowniku: po poprawce
        audytowej propagacja idzie od KAZDEGO opoznionego rejsu, wiec wpisy
        pochodza z kilku lancuchow i nie musza byc uporzadkowane.
        """
        for option in self.ctx.require("options"):
            impact = self.ctx.require("network")[option.id]
            najwieksze = max(option.delay_min.values(), default=0)
            for flight_id, minut in impact.delay_propagated_min.items():
                with self.subTest(opcja=option.id, rejs=flight_id):
                    self.assertLessEqual(minut, najwieksze)
                    self.assertGreaterEqual(minut, 0)

    def test_swap_propaguje_takze_odcinki_ponizej_rejsu_B(self):
        """Znalezisko audytu: horyzont liczyl sie wylacznie od rejsu zrodlowego,
        wiec rejs B przejmowal cale opoznienie, a jego dalsze odcinki dziedziczyly
        zero. Opcja, ktora silnik najchetniej rekomenduje, byla zanizana."""
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            Pipeline(build_pipeline(weekday=0, delay_min=180)).run(ctx)
        snap = ctx.require("snapshot")
        swapy = [o for o in ctx.require("options") if o.aircraft_swap]
        if not swapy:
            self.skipTest("w tej dobie nie ma pary do podmiany")
        for option in swapy:
            _, donor_id = option.aircraft_swap
            donor = snap.flights[donor_id]
            rot = snap.rotations.get(donor.rotation_id)
            ponizej = [f for f in (rot.flight_ids if rot else ())
                       if snap.flights[f].seq > donor.seq]
            if not ponizej:
                continue
            widziane = set(ctx.require("network")[option.id].delay_propagated_min)
            with self.subTest(opcja=option.id):
                self.assertTrue(set(ponizej) & widziane,
                                "zaden odcinek ponizej rejsu B nie wszedl do propagacji")

    def test_kazda_opcja_ma_ocene(self):
        for option in self.ctx.require("options"):
            with self.subTest(opcja=option.id):
                self.assertIn(option.id, self.ctx.require("evaluations"))

    def test_widelki_obejmuja_wartosc_oczekiwana(self):
        for option_id, ev in self.ctx.require("evaluations").items():
            with self.subTest(opcja=option_id):
                self.assertLessEqual(ev.band.low, ev.band.expected)
                self.assertLessEqual(ev.band.expected, ev.band.high)

    def test_widelki_trzymaja_porzadek_takze_przy_ujemnej_stracie(self):
        """Znalezisko audytu: mnozenie kwoty przez wspolczynnik odwraca porzadek,
        gdy kwota jest ujemna. Dla straty -500 zl wychodzilo `0 <= -500 <= -600`.

        Opcja przynoszaca oszczednosc netto jest w tym systemie normalna
        (SWAP ratujacy rejs B), wiec nie wolno na tym polegac, ze strata
        zawsze jest dodatnia.
        """
        from lotis.nodes.n11_optymalizacja import _band
        for kwota in (-500_00, -1, 0, 1, 500_00, 1_000_000_00):
            for low_f, high_f in ((0.9, 1.2), (1.0, 1.0), (0.55, 2.2)):
                with self.subTest(kwota=kwota, low=low_f, high=high_f):
                    band = _band(Money(kwota), low_f, high_f)
                    self.assertLessEqual(band.low, band.expected)
                    self.assertLessEqual(band.expected, band.high)

    def test_widelki_nie_schodza_ponizej_zera_przy_dodatniej_stracie(self):
        from lotis.nodes.n11_optymalizacja import _band
        band = _band(Money(100), 0.0, 3.0)
        self.assertGreaterEqual(band.low.minor, 0)

    def test_widelki_ujemnej_straty_zostaja_ujemne(self):
        """Przyciecie do zera zjadaloby wartosc oczekiwana."""
        from lotis.nodes.n11_optymalizacja import _band
        band = _band(Money(-500_00), 0.9, 1.2)
        self.assertLess(band.low.minor, 0)
        self.assertLess(band.expected.minor, 0)

    def test_widelki_nie_sa_zerowe(self):
        """Zerowa rozpietosc to deklaracja pewnosci, ktorej nie mamy."""
        for option_id, ev in self.ctx.require("evaluations").items():
            if ev.loss.minor:
                with self.subTest(opcja=option_id):
                    self.assertGreater(ev.band.spread.minor, 0)

    def test_dolne_widelki_nie_sa_ujemne(self):
        for option_id, ev in self.ctx.require("evaluations").items():
            with self.subTest(opcja=option_id):
                self.assertGreaterEqual(ev.band.low.minor, 0)

    def test_ranking_wstepny_jest_posortowany_wg_straty(self):
        evaluations = self.ctx.require("evaluations")
        kolejnosc = self.ctx.require("ranking_wstepny")
        straty = [evaluations[oid].loss.minor for oid in kolejnosc]
        self.assertEqual(straty, sorted(straty))


class TestFiltrPrawny(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_filtr_nie_pisze_do_rejestru_kosztow(self):
        """NIEZMIENNIK ARCHITEKTURY.

        Gdyby filtr dopisywal cene zamiast usuwac opcje, najtansza opcja byloby
        zdjac pasazerow wbrew woli i wpisac odszkodowanie w koszty. Raport
        node 12 nie ma prawa zawierac zadnej pozycji kosztowej.
        """
        report = next(r for r in self.reports if r.node_id == "12")
        for key in report.numbers:
            with self.subTest(pole=key):
                self.assertNotIn("koszt", key.lower())
                self.assertNotIn("strata", key.lower())

    def test_dopuszczalne_sa_podzbiorem_wszystkich(self):
        wszystkie = {o.id for o in self.ctx.require("options")}
        self.assertTrue(set(self.ctx.require("lawful")) <= wszystkie)

    def test_kazda_opcja_ma_werdykt(self):
        verdicts = self.ctx.get("verdicts", {})
        for option in self.ctx.require("options"):
            with self.subTest(opcja=option.id):
                self.assertIn(option.id, verdicts)

    def test_odrzucona_opcja_ma_podana_regule(self):
        for verdict in self.ctx.get("verdicts", {}).values():
            if not verdict.lawful:
                with self.subTest(opcja=verdict.option_id):
                    self.assertTrue(verdict.rules_failed)
                    for podstawa, powod in verdict.rules_failed:
                        self.assertTrue(podstawa)
                        self.assertTrue(powod)

    def test_dopuszczalna_opcja_nie_ma_zlamanych_regul(self):
        verdicts = self.ctx.get("verdicts", {})
        for option_id in self.ctx.require("lawful"):
            with self.subTest(opcja=option_id):
                self.assertEqual(verdicts[option_id].rules_failed, ())

    def test_brak_dopuszczalnej_opcji_niesie_pakiet_eskalacyjny(self):
        """Luka 5: galaz bez adresata, terminu i tresci. Wszystkie trzy sa w pakiecie."""
        from lotis.nodes.n12_filtr_prawny import FiltrPrawnyNode
        ctx, _, _ = przebieg()
        options = ctx.require("options")

        # Zmuszamy filtr do odrzucenia wszystkiego: kazdy pasazer zdjety wbrew
        # woli, bez wezwania ochotnikow (naruszenie Art. 4).
        import dataclasses
        from lotis.kernel.contracts import PaxOutcome
        zle = tuple(
            dataclasses.replace(o, pax_outcomes={
                pid: PaxOutcome(PaxOutcomeKind.OFFLOADED_INVOLUNTARY, delay_min=200)
                for pid in o.pax_outcomes})
            for o in options)

        with tempfile.TemporaryDirectory() as tmp:
            sub = RunContext("t2", reports_root=Path(tmp))
            sub.snapshot_digest = ctx.snapshot_digest
            for key in ("snapshot", "disruption", "evaluations", "eu261_tier"):
                sub.put(key, ctx.get(key))
            sub.put("options", zle)
            with self.assertRaises(NoLawfulOption) as raised:
                FiltrPrawnyNode().run(sub)
        packet = raised.exception.packet
        self.assertTrue(packet["addressee"]["role"])
        self.assertGreater(packet["sla_minutes"], 0)
        self.assertTrue(packet["rejected_options"])
        self.assertTrue(all(r["rule_that_killed_it"] for r in packet["rejected_options"]))

    def test_node_zamienia_brak_opcji_na_zatrzymanie(self):
        """`execute` nie propaguje `NoLawfulOption` -- zamienia na raport i halt."""
        from lotis.nodes.n12_filtr_prawny import FiltrPrawnyNode
        ctx, _, _ = przebieg()
        import dataclasses
        from lotis.kernel.contracts import PaxOutcome
        zle = tuple(
            dataclasses.replace(o, pax_outcomes={
                pid: PaxOutcome(PaxOutcomeKind.OFFLOADED_INVOLUNTARY, delay_min=200)
                for pid in o.pax_outcomes})
            for o in ctx.require("options"))
        with tempfile.TemporaryDirectory() as tmp:
            sub = RunContext("t3", reports_root=Path(tmp))
            for key in ("snapshot", "disruption", "evaluations", "eu261_tier"):
                sub.put(key, ctx.get(key))
            sub.put("options", zle)
            report = FiltrPrawnyNode().execute(sub)
        self.assertIs(report.status, Status.BLOCKED)
        self.assertTrue(sub.halted)
        self.assertIsNotNone(sub.escalation)


class TestWrazliwoscIKarta(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_ranking_obejmuje_tylko_dopuszczalne(self):
        lawful = set(self.ctx.require("lawful"))
        for r in self.ctx.require("ranking"):
            with self.subTest(opcja=r.option_id):
                self.assertIn(r.option_id, lawful)

    def test_pozycje_sa_kolejne_od_jedynki(self):
        ranking = self.ctx.require("ranking")
        self.assertEqual([r.rank for r in ranking], list(range(1, len(ranking) + 1)))

    def test_ranking_jest_monotoniczny_wzgledem_wskaznika(self):
        scores = [r.score for r in self.ctx.require("ranking")]
        self.assertEqual(scores, sorted(scores))

    def test_karta_opisuje_rekomendacje(self):
        card, ranking = self.ctx.get("karta"), self.ctx.require("ranking")
        self.assertIsNotNone(card)
        self.assertEqual(card.option_id, ranking[0].option_id)

    def test_karta_ma_komplet_pol(self):
        card = self.ctx.get("karta")
        self.assertTrue(card.what_changes)
        self.assertTrue(card.crew_actions)
        self.assertTrue(card.authorization_role)
        self.assertTrue(card.threshold_note)
        self.assertIsNotNone(card.valid_until)

    def test_widelki_karty_zgadzaja_sie_z_rankingiem(self):
        card, best = self.ctx.get("karta"), self.ctx.require("ranking")[0]
        self.assertEqual((card.cost_low, card.cost_expected, card.cost_high),
                         (best.band.low, best.band.expected, best.band.high))

    def test_test_wrazliwosci_ma_trzy_kroki(self):
        sensitivity = self.ctx.require("sensitivity")
        self.assertEqual([s["krok_min"] for s in sensitivity], [30, 60, 120])

    def test_kazdy_krok_ma_lidera(self):
        for step in self.ctx.require("sensitivity"):
            with self.subTest(krok=step["krok_min"]):
                self.assertTrue(step["lider"])
                self.assertTrue(step["ranking"])

    def test_opcja_domyslna_jest_dopuszczalna(self):
        default = self.ctx.require("default_option")
        self.assertIn(default, self.ctx.require("lawful"))

    def test_oszczednosc_liczy_sie_wzgledem_domyslnej(self):
        ranking = self.ctx.require("ranking")
        default = self.ctx.require("default_option")
        wpis = next(r for r in ranking if r.option_id == default)
        self.assertEqual(wpis.saving_vs_default, Money.zero())

    def test_chronieni_pasazerowie_schodza_ostatni(self):
        """Kolejnosc przy odmowie przyjecia: PRM, UMNR i asysta medyczna na koncu."""
        from lotis.kernel.contracts import SpecialNeed
        from lotis.nodes.n13_wrazliwosc import _offload_order
        snap = self.ctx.require("snapshot")
        chroniony = next((p.id for p in snap.passengers.values()
                          if p.specials & {SpecialNeed.REDUCED_MOBILITY,
                                           SpecialNeed.UNACCOMPANIED_MINOR,
                                           SpecialNeed.MEDICAL_ASSIST}), None)
        if chroniony is None:
            self.skipTest("brak chronionego pasazera w manifescie")
        zwykly = next(p.id for p in snap.passengers.values() if not p.specials)
        order = _offload_order(snap, [chroniony, zwykly])
        self.assertEqual(order[-1], chroniony)


class TestKontroleISpojnosc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_wszystkie_kontrole_przechodza(self):
        nieudane = [c for c in self.ctx.require("checks") if not c["ok"]]
        self.assertEqual(nieudane, [], nieudane)

    def test_kontrole_pokrywaja_kluczowe_niezmienniki(self):
        ids = {c["id"] for c in self.ctx.require("checks")}
        for wymagana in ("kolejnosc_rankingu", "widelki", "karta_wykonania",
                         "suma_skladnikow", "kompletnosc_pasazerow"):
            with self.subTest(kontrola=wymagana):
                self.assertIn(wymagana, ids)

    def test_uzasadnienie_cytuje_liczby(self):
        report = next(r for r in self.reports if r.node_id == "14")
        uzasadnienie = report.findings["uzasadnienie"]
        self.assertTrue(uzasadnienie["wybrana"])
        self.assertIn("strata", uzasadnienie)
        self.assertTrue(uzasadnienie["najwieksze_skladniki_kosztu"])

    def test_warstwa_ai_nie_jest_etapem_przeplywu(self):
        """Silnik konczy run bez modelu jezykowego -- to jest warunek OUTPUT 2."""
        self.assertNotIn("ai_response", self.ctx.state)
        self.assertIn("audit", self.ctx.state)


class TestDecyzjaIWykonanie(unittest.TestCase):
    def test_przyjecie_rekomendacji(self):
        ctx, _, _ = przebieg()
        decision = ctx.require("decision")
        self.assertEqual(decision["rodzaj"], "ACCEPT")
        self.assertFalse(decision["odstepstwo"])
        self.assertEqual(decision["opcja"], ctx.require("ranking")[0].option_id)

    def test_rola_autoryzujaca_pochodzi_z_pasma_kwotowego(self):
        ctx, _, _ = przebieg()
        self.assertTrue(ctx.require("decision")["rola"])

    def test_odrzucenie_zatrzymuje_przeplyw(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(
                weekday=4, decision=Decision.REJECT,
                reason_code="DECYZJA_HANDLOWA")).run(ctx)
        self.assertTrue(ctx.halted)
        self.assertIs(reports[15].status, Status.BLOCKED)   # 15b nie rusza

    def test_odrzucenie_bez_kodu_daje_ostrzezenie(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(
                weekday=4, decision=Decision.REJECT)).run(ctx)
        report = next(r for r in reports if r.node_id == "15")
        self.assertTrue(any("kodu przyczyny" in w for w in report.warnings))

    def test_czlowiek_nie_wykona_opcji_odrzuconej_przez_prawo(self):
        """NAJPOWAZNIEJSZE ZNALEZISKO AUDYTU.

        Node 12 odrzucal HOLD za naruszenie Art. 9, a `--option HOLD` przechodzil
        przez node 15 ze statusem `ok`, bez ani jednego ostrzezenia, i byl
        WYKONYWANY przez node 15b. System dokumentowalby wlasne naruszenie prawa
        jako zwykla decyzje operacyjna.

        Przyczyna: sciezka decyzji czytala pelna liste opcji zamiast `lawful`.
        Zasada nadrzedna stawia "prawo blokuje" PRZED "czlowiek decyduje".
        """
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            Pipeline(build_pipeline(weekday=0, delay_min=900)).run(ctx)
        odrzucone = {o.id for o in ctx.require("options")} - set(ctx.require("lawful"))
        if not odrzucone:
            self.skipTest("filtr prawny nic nie odrzucil w tej dobie")
        cel = sorted(odrzucone)[0]

        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(
                weekday=0, delay_min=900,
                decision=Decision.MODIFY, chosen_option=cel)).run(ctx)

        r15 = next(r for r in reports if r.node_id == "15")
        self.assertIs(r15.status, Status.BLOCKED)
        self.assertIn(cel, r15.summary)
        self.assertIsNone(ctx.get("execution"), "opcja niedopuszczalna zostala wykonana")
        self.assertTrue(ctx.halted)
        self.assertIsNotNone(ctx.escalation)
        self.assertTrue(ctx.escalation["addressee"].get("role"))

    def test_node_15b_broni_sie_niezaleznie_od_node_15(self):
        """Gwarancja filtru prawnego nie moze wisiec na jednym wywolujacym.

        15b jest ostatnim miejscem przed zmiana stanu w swiecie zewnetrznym,
        wiec sprawdza `lawful` sam, nawet gdy decyzja juz przeszla.
        """
        from lotis.nodes.n15b_wykonanie import WykonanieNode
        ctx, _, _ = przebieg()
        with tempfile.TemporaryDirectory() as tmp:
            sub = RunContext("t", reports_root=Path(tmp))
            sub.put("options", ctx.require("options"))
            sub.put("lawful", ())          # nic nie jest dopuszczalne
            sub.put("decision", {"opcja": ctx.require("ranking")[0].option_id})
            report = WykonanieNode().execute(sub)
        self.assertIs(report.status, Status.BLOCKED)
        self.assertIsNone(sub.get("execution"))
        self.assertTrue(sub.halted)

    def test_nieznana_opcja_w_decyzji_zatrzymuje_z_lista_dostepnych(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(
                weekday=4, decision=Decision.MODIFY,
                chosen_option="NIE-MA-TAKIEJ")).run(ctx)
        r15 = next(r for r in reports if r.node_id == "15")
        self.assertIs(r15.status, Status.BLOCKED)
        self.assertTrue(r15.data_gaps)
        self.assertIn("dostepne", r15.findings)
        self.assertIsNone(ctx.get("execution"))

    def test_pasmo_autoryzacji_liczy_sie_z_wybranej_opcji(self):
        """Wczesniej przy nieznanej opcji `chosen` cofalo sie do rekomendacji,
        wiec kwota autoryzacji nalezala do INNEJ opcji niz zapisana decyzja."""
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(
                weekday=4, decision=Decision.MODIFY,
                chosen_option="OVERNIGHT")).run(ctx)
        ranking = {r.option_id: r for r in ctx.require("ranking")}
        if "OVERNIGHT" not in ranking:
            self.skipTest("OVERNIGHT nie wszedl do rankingu")
        r15 = next(r for r in reports if r.node_id == "15")
        kwota = r15.numbers["kwota_do_autoryzacji"]["value"]
        self.assertEqual(kwota["minor"], ranking["OVERNIGHT"].band.high.minor)

    def test_modyfikacja_zapisuje_odstepstwo(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            Pipeline(build_pipeline(
                weekday=4, decision=Decision.MODIFY, chosen_option="CANCEL")).run(ctx)
        self.assertTrue(ctx.require("decision")["odstepstwo"])
        self.assertEqual(ctx.require("decision")["opcja"], "CANCEL")

    def test_wykonanie_ma_kroki_z_wykonawcami(self):
        ctx, _, _ = przebieg()
        kroki = ctx.require("execution")["kroki"]
        self.assertTrue(kroki)
        for krok in kroki:
            with self.subTest(krok=krok["id"]):
                self.assertTrue(krok["wykonawca"])
                self.assertTrue(krok["opis"])

    def test_porazka_wykonania_prosi_o_przeliczenie(self):
        """Luka 1: bez tego node 17 nie odroznilby bledu modelu od nieudanej realizacji."""
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(
                weekday=4, fail_step="powiadomienie_pax")).run(ctx)
        report = next(r for r in reports if r.node_id == "15b")
        self.assertIs(report.status, Status.DEGRADED)
        self.assertEqual(ctx.recalc_trigger, "EXECUTION_FAILED")
        self.assertIn("execution_failure", ctx.state)
        self.assertFalse(ctx.halted)

    def test_nieznany_krok_porazki_nie_wywala_node(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(
                weekday=4, fail_step="nie-ma-takiego-kroku")).run(ctx)
        report = next(r for r in reports if r.node_id == "15b")
        self.assertIsNot(report.status, Status.BLOCKED)


class TestLogIWynik(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx, cls.reports, cls._tmp = przebieg()

    def test_log_zapisuje_wszystkie_rozwazone_opcje(self):
        audit = self.ctx.require("audit")
        self.assertEqual(len(audit["opcje_rozwazone"]), len(self.ctx.require("options")))

    def test_log_niesie_powod_odrzucenia_kazdej_odrzuconej(self):
        for wpis in self.ctx.require("audit")["opcje_rozwazone"]:
            if wpis["dopuszczalna"] is False:
                with self.subTest(opcja=wpis["id"]):
                    self.assertTrue(wpis["powod_odrzucenia"])

    def test_log_ma_wersje_i_odcisk(self):
        audit = self.ctx.require("audit")
        self.assertTrue(audit["odcisk"].startswith("sha256:"))
        self.assertIn("engine", audit["wersje"])
        self.assertIn("data", audit["wersje"])

    def test_odcisk_logu_zalezy_od_tresci(self):
        from lotis.nodes.n16_log import _digest
        audit = dict(self.ctx.require("audit"))
        inny = dict(audit, run_id="INNY")
        self.assertNotEqual(_digest(audit), _digest(inny))

    def test_wynik_klasyfikuje_rozjazd(self):
        actual = self.ctx.require("actual")
        self.assertIn(actual["rodzaj_bledu"],
                      {"ZGODNY", "BLAD_MODELU", "BLAD_WYKONANIA",
                       "ODSTEPSTWO_CZLOWIEKA", "BRAK_PROGNOZY"})

    def test_blad_wykonania_nie_kalibruje_modelu(self):
        """Luka 3: model uczylby sie na cudzych pomylkach."""
        # `powiadomienie_pax` wystepuje w kazdej opcji -- krok wybrany pod
        # konkretna opcje (np. potwierdzenie partnera) zostalby po cichu
        # pominiety, gdyby rekomendacja okazala sie inna.
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            Pipeline(build_pipeline(
                weekday=4, fail_step="powiadomienie_pax")).run(ctx)
        self.assertEqual(ctx.require("actual")["rodzaj_bledu"], "BLAD_WYKONANIA")
        self.assertEqual(ctx.require("calibration")["poprawki"], [])

    def test_odstepstwo_czlowieka_nie_kalibruje_modelu(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            Pipeline(build_pipeline(
                weekday=4, decision=Decision.MODIFY, chosen_option="CANCEL")).run(ctx)
        self.assertEqual(ctx.require("actual")["rodzaj_bledu"], "ODSTEPSTWO_CZLOWIEKA")
        self.assertEqual(ctx.require("calibration")["poprawki"], [])

    def test_duzy_rozjazd_daje_poprawki_z_tlumieniem(self):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            Pipeline(build_pipeline(
                weekday=4, delay_min=180, actual_delay_min=600)).run(ctx)
        calibration = ctx.require("calibration")
        if calibration["poprawki"]:
            self.assertEqual(calibration["tlumienie"], 0.20)
            for poprawka in calibration["poprawki"]:
                with self.subTest(parametr=poprawka["parametr"]):
                    self.assertIn(poprawka["kierunek"], {"w gore", "w dol"})


class TestOdpornosc(unittest.TestCase):
    """Sciezki wyjatkowe: skrajne wartosci i dane, ktorych nie ma."""

    def uruchom(self, **kw):
        with tempfile.TemporaryDirectory() as tmp:
            ctx = RunContext("t", reports_root=Path(tmp))
            reports = Pipeline(build_pipeline(weekday=4, **kw)).run(ctx)
            return ctx, reports

    def test_zerowe_opoznienie(self):
        ctx, _ = self.uruchom(delay_min=0)
        self.assertTrue(ctx.require("ranking"))

    def test_skrajne_opoznienie(self):
        ctx, _ = self.uruchom(delay_min=1440)
        self.assertTrue(ctx.require("ranking"))

    def test_okolicznosc_nadzwyczajna_zeruje_ekspozycje_art7(self):
        """Kod klasy `n` -- odszkodowanie nie przysluguje, opieka nadal tak."""
        ctx, _ = self.uruchom(delay_code="71")
        self.assertEqual(db().compensation_probability("71"), 0.0)
        costs = ctx.require("costs")
        for option_id, cost in costs.items():
            with self.subTest(opcja=option_id):
                self.assertNotIn("odszkodowanie_art7", cost.components)

    def test_okolicznosc_nadzwyczajna_zachowuje_opieke(self):
        ctx, _ = self.uruchom(delay_code="71")
        costs = ctx.require("costs")
        self.assertTrue(any("opieka_art9" in c.components for c in costs.values()))

    def test_nieznany_kod_daje_polowe_i_ostrzezenie(self):
        _, reports = self.uruchom(delay_code="ZZZ")
        report = next(r for r in reports if r.node_id == "04")
        self.assertEqual(report.numbers["p_odszkodowania"]["value"], 0.5)
        self.assertTrue(report.warnings)

    def test_kazda_doba_tygodnia_przechodzi(self):
        for day in range(7):
            with self.subTest(dzien=day), tempfile.TemporaryDirectory() as tmp:
                ctx = RunContext("t", reports_root=Path(tmp))
                reports = Pipeline(build_pipeline(weekday=day)).run(ctx)
                self.assertFalse(ctx.halted)
                self.assertTrue(ctx.require("ranking"))
                self.assertEqual(len(reports), 18)


if __name__ == "__main__":
    unittest.main()
