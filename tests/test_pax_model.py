"""Manifest pasazerski -- jedyna warstwa, ktora nadal jest generowana.

Determinizm jest tu warunkiem koniecznym, a nie wygoda: bez niego dwa
uruchomienia tego samego snapshotu daja rozny koszt, a log przestaje
czegokolwiek dowodzic.
"""

import unittest

from lotis.adapters.pax_model import (
    ANCILLARY_SHARE, FARE_FAMILY_SHARE, PaxModel, _special_for,
)
from lotis.kernel.contracts import Cabin, SpecialNeed, TripType

from ._helpers import db, snapshot


class TestUdzialy(unittest.TestCase):
    def test_udzialy_rodzin_taryfowych_sumuja_sie_do_jedynki(self):
        self.assertAlmostEqual(sum(FARE_FAMILY_SHARE.values()), 1.0, places=6)

    def test_ancillary_ma_sensowne_widelki(self):
        for cabin, (low, high) in ANCILLARY_SHARE.items():
            with self.subTest(kabina=cabin):
                self.assertLessEqual(low, high)
                self.assertGreaterEqual(low, 0.0)
                self.assertLess(high, 1.0)

    def test_klasa_ekonomiczna_ma_najwyzszy_udzial_ancillary(self):
        """Business ma bagaz i wybor miejsca w cenie, economy dokupuje."""
        self.assertGreater(ANCILLARY_SHARE["Y"][1], ANCILLARY_SHARE["C"][1])


class TestMapowanieSSR(unittest.TestCase):
    def test_kategoria_wygrywa_z_kodem(self):
        self.assertIs(_special_for("XXXX", "mobility"), SpecialNeed.REDUCED_MOBILITY)

    def test_kody_wozkow(self):
        for code in ("WCHR", "WCHS", "WCHC", "WCMP", "BLND", "DEAF"):
            with self.subTest(kod=code):
                self.assertIs(_special_for(code, ""), SpecialNeed.REDUCED_MOBILITY)

    def test_maloletni_bez_opieki(self):
        self.assertIs(_special_for("UMNR", ""), SpecialNeed.UNACCOMPANIED_MINOR)

    def test_medyczne(self):
        for code in ("MEDA", "STCR", "OXYG"):
            with self.subTest(kod=code):
                self.assertIs(_special_for(code, ""), SpecialNeed.MEDICAL_ASSIST)

    def test_zwierzeta(self):
        for code in ("PETC", "AVIH", "SVAN"):
            with self.subTest(kod=code):
                self.assertIs(_special_for(code, ""), SpecialNeed.PET_IN_HOLD)

    def test_nieznany_kod_daje_none(self):
        self.assertIsNone(_special_for("ZZZZ", ""))


class TestGenerowanie(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snap, cls.build = snapshot(4)

    def test_manifest_nie_jest_pusty(self):
        self.assertGreater(len(self.snap.passengers), 1000)
        self.assertGreater(len(self.snap.itineraries), 1000)

    def test_kazdy_pasazer_ma_istniejaca_podroz(self):
        sieroty = [p.id for p in self.snap.passengers.values()
                   if p.itinerary_id not in self.snap.itineraries]
        self.assertEqual(sieroty, [])

    def test_kazdy_odcinek_podrozy_jest_istniejacym_rejsem(self):
        zle = [(i.id, s) for i in self.snap.itineraries.values()
               for s in i.segments if s not in self.snap.flights]
        self.assertEqual(zle, [])

    def test_taryfa_i_ancillary_sa_nieujemne(self):
        for pax in list(self.snap.passengers.values())[:2000]:
            with self.subTest(pax=pax.id):
                self.assertGreaterEqual(pax.fare.minor, 0)
                self.assertGreaterEqual(pax.ancillary.minor, 0)

    def test_wartosc_pasazera_jest_dodatnia(self):
        zerowi = [p.id for p in self.snap.passengers.values() if p.value.minor <= 0]
        self.assertEqual(zerowi, [])

    def test_zaden_rejs_nie_jest_przepelniony(self):
        """Kluczowy niezmiennik: pasazer transferowy zajmuje miejsce na obu odcinkach."""
        seated: dict[str, int] = {}
        for pax in self.snap.passengers.values():
            for segment in self.snap.itineraries[pax.itinerary_id].segments:
                seated[segment] = seated.get(segment, 0) + 1
        for flight_id, count in seated.items():
            spec = self.snap.aircraft_types.get(self.snap.flights[flight_id].type_code)
            if spec:
                with self.subTest(rejs=flight_id):
                    self.assertLessEqual(count, spec.seats_total)

    def test_transferowi_maja_dwa_odcinki(self):
        transferowi = [i for i in self.snap.itineraries.values() if len(i.segments) > 1]
        self.assertGreater(len(transferowi), 0)
        for itin in transferowi[:200]:
            with self.subTest(podroz=itin.id):
                self.assertEqual(len(itin.segments), 2)

    def test_transferowi_maja_spojny_lancuch(self):
        """Drugi odcinek musi startowac tam, gdzie konczy pierwszy."""
        for itin in list(self.snap.itineraries.values())[:5000]:
            if len(itin.segments) == 2:
                first, second = (self.snap.flights[s] for s in itin.segments)
                with self.subTest(podroz=itin.id):
                    self.assertEqual(first.arr, second.dep)
                    self.assertGreater(second.std, first.sta)

    def test_cel_podrozy_zgadza_sie_z_ostatnim_odcinkiem(self):
        for itin in list(self.snap.itineraries.values())[:2000]:
            ostatni = self.snap.flights[itin.segments[-1]]
            with self.subTest(podroz=itin.id):
                self.assertEqual(itin.destination, ostatni.arr)
                self.assertEqual(itin.origin, self.snap.flights[itin.segments[0]].dep)

    def test_koszyk_transferowego_jest_oznaczony_jako_connecting(self):
        for pax in list(self.snap.passengers.values())[:5000]:
            itin = self.snap.itineraries[pax.itinerary_id]
            oczekiwany = TripType.CONNECTING if len(itin.segments) > 1 else TripType.DIRECT
            with self.subTest(pax=pax.id):
                self.assertIs(pax.basket.trip, oczekiwany)

    def test_wystepuja_obie_kabiny(self):
        kabiny = {p.basket.cabin for p in self.snap.passengers.values()}
        self.assertIn(Cabin.ECONOMY, kabiny)
        self.assertIn(Cabin.BUSINESS, kabiny)

    def test_business_kosztuje_wiecej_niz_economy(self):
        biznes = [p.fare.minor for p in self.snap.passengers.values()
                  if p.basket.cabin is Cabin.BUSINESS]
        eko = [p.fare.minor for p in self.snap.passengers.values()
               if p.basket.cabin is Cabin.ECONOMY]
        self.assertGreater(sum(biznes) / len(biznes), sum(eko) / len(eko))

    def test_bilet_przez_punkt_kosztuje_wiecej_niz_bezposredni(self):
        """Taryfa przez punkt nie jest suma dwoch odcinkow, ale jest wyzsza od jednego."""
        transfer = [p.fare.minor for p in self.snap.passengers.values()
                    if p.basket.trip is TripType.CONNECTING]
        prosty = [p.fare.minor for p in self.snap.passengers.values()
                  if p.basket.trip is TripType.DIRECT]
        self.assertGreater(sum(transfer) / len(transfer), sum(prosty) / len(prosty))

    def test_zgloszenia_specjalne_sa_mniejszoscia(self):
        ze_zgloszeniem = sum(1 for p in self.snap.passengers.values() if p.specials)
        self.assertGreater(ze_zgloszeniem, 0)
        self.assertLess(ze_zgloszeniem / len(self.snap.passengers), 0.20)


class TestDeterminizm(unittest.TestCase):
    def test_to_samo_ziarno_daje_ten_sam_manifest(self):
        """Bez tego testy golden-file nie maja sensu, a porownania wersji
        silnika sa zaszumione losowoscia."""
        from lotis.adapters.aircraft_perf import build_types
        base = db()
        snap, _ = snapshot(4)
        flights, routes, types = snap.flights, base.routes, build_types()

        a = PaxModel(base, seed=2026).build(flights, routes, types)
        b = PaxModel(base, seed=2026).build(flights, routes, types)
        self.assertEqual(len(a.passengers), len(b.passengers))
        self.assertEqual(
            [(p.id, p.fare.minor, p.ancillary.minor) for p in list(a.passengers.values())[:500]],
            [(p.id, p.fare.minor, p.ancillary.minor) for p in list(b.passengers.values())[:500]],
        )

    def test_inne_ziarno_daje_inny_manifest(self):
        from lotis.adapters.aircraft_perf import build_types
        base = db()
        snap, _ = snapshot(4)
        a = PaxModel(base, seed=1).build(snap.flights, base.routes, build_types())
        b = PaxModel(base, seed=2).build(snap.flights, base.routes, build_types())
        self.assertNotEqual(
            [p.fare.minor for p in list(a.passengers.values())[:200]],
            [p.fare.minor for p in list(b.passengers.values())[:200]],
        )

    def test_zalozenia_sa_zadeklarowane(self):
        """Kazde wlasne zalozenie ma trafic do raportu node 01."""
        from lotis.adapters.aircraft_perf import build_types
        base = db()
        snap, _ = snapshot(4)
        manifest = PaxModel(base).build(snap.flights, base.routes, build_types())
        self.assertGreaterEqual(len(manifest.assumptions), 3)
        self.assertTrue(all(isinstance(a, str) and a for a in manifest.assumptions))


if __name__ == "__main__":
    unittest.main()
