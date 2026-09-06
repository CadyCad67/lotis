"""Budowa snapshotu -- miejsce, w ktorym oba zrodla spotykaja sie w jeden stan.

Test odcisku jest tu najwazniejszy. Odcisk cytuje kazdy raport, wiec jesli
nie jest stabilny, log przestaje dowodzic, czym byl policzony run, a jesli
nie jest wrazliwy na zmiane, przestaje ja odrozniac.
"""

import unittest

from lotis.adapters.network import REPORT_BEFORE_MIN, _digest
from lotis.kernel.contracts import Confidence, CrewRole

from ._helpers import snapshot


class TestBudowa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snap, cls.build = snapshot(4)

    def test_snapshot_ma_rejsy_rotacje_i_zaloge(self):
        self.assertGreater(len(self.snap.flights), 100)
        self.assertGreater(len(self.snap.rotations), 10)
        self.assertGreater(len(self.snap.crew), 100)

    def test_kazdy_rejs_nalezy_do_istniejacej_rotacji(self):
        sieroty = [f.id for f in self.snap.flights.values()
                   if f.rotation_id not in self.snap.rotations]
        self.assertEqual(sieroty, [])

    def test_kazda_rotacja_wskazuje_istniejace_rejsy(self):
        zle = [(r.id, f) for r in self.snap.rotations.values()
               for f in r.flight_ids if f not in self.snap.flights]
        self.assertEqual(zle, [])

    def test_identyfikatory_rejsow_sa_unikalne(self):
        self.assertEqual(len(self.snap.flights), len(set(self.snap.flights)))

    def test_kazdy_rejs_ma_dodatni_blok(self):
        for f in self.snap.flights.values():
            with self.subTest(rejs=f.id):
                self.assertGreater(f.block_min, 0)

    def test_kazdy_rejs_ma_znany_port_wylotu_i_przylotu(self):
        nieznane = {i for f in self.snap.flights.values()
                    for i in (f.dep, f.arr) if i not in self.snap.airports}
        self.assertEqual(nieznane, set())

    def test_kazdy_rejs_ma_znany_typ(self):
        nieznane = {f.type_code for f in self.snap.flights.values()
                    if f.type_code not in self.snap.aircraft_types}
        self.assertEqual(nieznane, set())

    def test_numeracja_w_rotacji_jest_chronologiczna(self):
        for rot in self.snap.rotations.values():
            legs = [self.snap.flights[f] for f in rot.flight_ids]
            with self.subTest(rotacja=rot.id):
                self.assertEqual([leg.seq for leg in legs], sorted(leg.seq for leg in legs))
                self.assertEqual([leg.std for leg in legs], sorted(leg.std for leg in legs))

    def test_maszyna_stoi_tam_gdzie_zaczyna_dobe(self):
        for rot in self.snap.rotations.values():
            pierwszy = self.snap.flights[rot.flight_ids[0]]
            with self.subTest(reg=rot.aircraft_reg):
                self.assertEqual(self.snap.aircraft[rot.aircraft_reg].position, pierwszy.dep)


class TestZaloga(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snap, cls.build = snapshot(4)

    def test_kazdy_rejs_ma_przypisana_zaloge(self):
        bez = [f.id for f in self.snap.flights.values() if not f.crew_ids]
        self.assertEqual(bez, [])

    def test_zaloga_z_rejsu_istnieje_w_snapshocie(self):
        nieznani = {c for f in self.snap.flights.values()
                    for c in f.crew_ids if c not in self.snap.crew}
        self.assertEqual(nieznani, set())

    def test_kazdy_rejs_ma_kapitana_i_pierwszego_oficera(self):
        for f in list(self.snap.flights.values())[:100]:
            role = [self.snap.crew[c].role for c in f.crew_ids]
            with self.subTest(rejs=f.id):
                self.assertIn(CrewRole.CAPTAIN, role)
                self.assertIn(CrewRole.FIRST_OFFICER, role)

    def test_zaloga_ma_uprawnienie_na_typ(self):
        """Zaloga bez uprawnienia to rejs, ktorego nie da sie wykonac."""
        bledy = []
        for f in self.snap.flights.values():
            spec = self.snap.aircraft_types.get(f.type_code)
            if not spec or not spec.rating:
                continue
            for c in f.crew_ids:
                if spec.rating not in self.snap.crew[c].qualifications:
                    bledy.append((f.id, c, spec.rating))
        self.assertEqual(bledy, [])

    def test_limity_fdp_pochodza_z_tabeli_easa(self):
        for c in list(self.snap.crew.values())[:300]:
            with self.subTest(zaloga=c.id):
                self.assertTrue(480 <= c.fdp_limit_min <= 900, c.fdp_limit_min)

    def test_personel_pokladowy_ma_dluzszy_fdp(self):
        """ORO.FTL.205 lit. e -- personel pokladowy zglasza sie pozniej."""
        pokladowi = [c.fdp_limit_min for c in self.snap.crew.values()
                     if c.role is CrewRole.CABIN]
        piloci = [c.fdp_limit_min for c in self.snap.crew.values()
                  if c.role is CrewRole.CAPTAIN]
        self.assertGreater(sum(pokladowi) / len(pokladowi), sum(piloci) / len(piloci))

    def test_zaloga_zglasza_sie_przed_odlotem(self):
        for rot in list(self.snap.rotations.values())[:50]:
            pierwszy = self.snap.flights[rot.flight_ids[0]]
            for c in pierwszy.crew_ids:
                with self.subTest(rotacja=rot.id):
                    delta = (pierwszy.std - self.snap.crew[c].duty_start).total_seconds() / 60
                    self.assertEqual(delta, REPORT_BEFORE_MIN)

    def test_baza_zalogi_jest_realnym_portem(self):
        for c in list(self.snap.crew.values())[:200]:
            with self.subTest(zaloga=c.id):
                self.assertIn(c.base, self.snap.airports)


class TestOdcisk(unittest.TestCase):
    def test_odcisk_ma_prefiks_i_dlugosc(self):
        snap, _ = snapshot(4)
        self.assertTrue(snap.digest.startswith("sha256:"))
        self.assertEqual(len(snap.digest), len("sha256:") + 32)

    def test_ten_sam_dzien_daje_ten_sam_odcisk(self):
        """Warunek odtwarzalnosci: dwa uruchomienia opisuja ten sam stan."""
        from lotis.adapters.network import build_snapshot
        a, _ = build_snapshot(weekday=3, seed=2026)
        b, _ = build_snapshot(weekday=3, seed=2026)
        self.assertEqual(a.digest, b.digest)

    def test_inny_dzien_daje_inny_odcisk(self):
        self.assertNotEqual(snapshot(2)[0].digest, snapshot(3)[0].digest)

    def test_odcisk_reaguje_na_zmiane_liczby_pasazerow(self):
        import dataclasses
        snap, _ = snapshot(4)
        okrojony = dataclasses.replace(
            snap, passengers=dict(list(snap.passengers.items())[:100]))
        self.assertNotEqual(_digest(snap), _digest(okrojony))

    def test_odcisk_reaguje_na_zmiane_rejsu(self):
        import dataclasses
        snap, _ = snapshot(4)
        klucz = next(iter(snap.flights))
        zmieniony = dataclasses.replace(
            snap,
            flights={**snap.flights,
                     klucz: dataclasses.replace(snap.flights[klucz], aircraft_reg="SP-ZZZ")},
        )
        self.assertNotEqual(_digest(snap), _digest(zmieniony))


class TestRaportBudowy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snap, cls.build = snapshot(4)

    def test_liczniki_zgadzaja_sie_ze_snapshotem(self):
        self.assertEqual(self.build.flights, len(self.snap.flights))
        self.assertEqual(self.build.rotations, len(self.snap.rotations))
        self.assertEqual(self.build.crew, len(self.snap.crew))
        self.assertEqual(self.build.passengers, len(self.snap.passengers))

    def test_udzial_transferowych_w_zakresie(self):
        self.assertTrue(0.0 <= self.build.connecting_share <= 1.0)

    def test_zalozenia_sa_wypisane(self):
        self.assertTrue(self.build.assumptions)
        self.assertTrue(any("FDP" in a for a in self.build.assumptions))

    def test_pewnosc_pol_jest_ustawiona(self):
        self.assertIs(self.snap.confidence["flights"], Confidence.KNOWN)
        self.assertIs(self.snap.confidence["crew"], Confidence.ESTIMATED)
        self.assertIs(self.snap.confidence["passengers"], Confidence.ESTIMATED)

    def test_kazda_doba_tygodnia_daje_sie_zbudowac(self):
        from lotis.adapters.network import build_snapshot
        for day in range(7):
            with self.subTest(dzien=day):
                snap, rep = build_snapshot(weekday=day, seed=2026)
                self.assertGreater(rep.flights, 0)
                self.assertEqual(snap.taken_at.date().isoformat(), rep.day)


if __name__ == "__main__":
    unittest.main()
