"""Baza parametryczna z `loops.jsx`.

Najwazniejsza rodzina testow w calym projekcie. Baza jest zakodowana tablicowo,
a zly dekod nie wywala sie -- po cichu podstawia inna liczbe. `L[3]` zamiast
`L[5]` to nie blad skladni, tylko odszkodowanie naliczone wedlug przynaleznosci
do UE zamiast wedlug objecia rozporzadzeniem.

Dlatego testy nizej nie sprawdzaja, ze pole sie odczytuje. Sprawdzaja, ze
odczytane pole odtwarza regule, ktora baza deklaruje osobno.
"""

import unittest

from lotis.adapters.lot_db import Curfew, _extract_db, _hm

from ._helpers import db


class TestEkstrakcja(unittest.TestCase):
    def test_wycina_literal_obiektu(self):
        self.assertEqual(_extract_db('const DB = {"a": 1};\n'), {"a": 1})

    def test_nawias_w_napisie_nie_konczy_skanu(self):
        """Naiwne szukanie `};` lamie sie na nawiasie w opisie kodu opoznienia."""
        source = 'const DB = {"opis": "kod } w tekscie", "b": 2};'
        self.assertEqual(_extract_db(source), {"opis": "kod } w tekscie", "b": 2})

    def test_escapowany_cudzyslow_nie_konczy_napisu(self):
        source = r'const DB = {"a": "cytat \" i } nawias", "b": 2};'
        self.assertEqual(_extract_db(source)["b"], 2)

    def test_zagniezdzone_obiekty(self):
        self.assertEqual(
            _extract_db('const DB = {"a": {"b": {"c": 1}}};')["a"]["b"]["c"], 1)

    def test_niedomkniety_literal_wybucha(self):
        with self.assertRaises(ValueError):
            _extract_db('const DB = {"a": 1')

    def test_brak_kotwicy_wybucha(self):
        with self.assertRaises(ValueError):
            _extract_db("nie ma tu zadnej bazy")


class TestGodzina(unittest.TestCase):
    def test_konwersja(self):
        self.assertEqual(_hm("00:00"), 0)
        self.assertEqual(_hm("05:30"), 330)
        self.assertEqual(_hm("23:59"), 1439)


class TestCurfew(unittest.TestCase):
    def test_okno_zwykle(self):
        c = Curfew(60, 300, 1, True)
        self.assertTrue(c.covers(120))
        self.assertFalse(c.covers(400))

    def test_okno_przez_polnoc(self):
        c = Curfew(23 * 60 + 30, 5 * 60 + 30, 1, True)
        self.assertTrue(c.covers(0))
        self.assertTrue(c.covers(23 * 60 + 45))
        self.assertFalse(c.covers(12 * 60))

    def test_typ_1_to_zakaz_planowania(self):
        self.assertTrue(Curfew(60, 300, 1, True).hard_planning_ban)
        self.assertFalse(Curfew(60, 300, 2, True).hard_planning_ban)

    def test_blokuje_tylko_przy_planowaniu(self):
        """Maszyna opozniona z przyczyn niezaleznych moze operowac."""
        c = Curfew(60, 300, 1, True)
        self.assertTrue(c.blocks(120, planning=True))
        self.assertFalse(c.blocks(120, planning=False))


class TestPorty(unittest.TestCase):
    def setUp(self):
        self.db = db()

    def test_wszystkie_porty_maja_wspolrzedne_w_zakresie(self):
        for iata, port in self.db.ports.items():
            with self.subTest(port=iata):
                self.assertTrue(-90 <= port.lat <= 90)
                self.assertTrue(-180 <= port.lon <= 180)

    def test_kazdy_port_ma_strefe_iana_z_ukosnikiem_lub_utc(self):
        for iata, port in self.db.ports.items():
            with self.subTest(port=iata):
                self.assertTrue("/" in port.tz or port.tz == "UTC", port.tz)

    def test_strefa_rozwiazuje_sie_dla_lata_i_zimy(self):
        """`zoneinfo` bez `tzdata` wybucha na Windows -- to test srodowiska."""
        from datetime import date
        waw = self.db.ports["WAW"]
        self.assertEqual(waw.utc_offset_min(date(2026, 8, 21)), 120)
        self.assertEqual(waw.utc_offset_min(date(2026, 1, 21)), 60)

    def test_waw_ma_curfew_typu_1(self):
        """Zasada Lokalna EPWA 1: zakaz planowania, nie zamkniecie portu."""
        curfew = self.db.ports["WAW"].curfew
        self.assertIsNotNone(curfew)
        self.assertEqual(curfew.kind, 1)

    def test_porty_maja_mct(self):
        self.assertIn("SS", self.db.ports["WAW"].mct)

    def test_schengen_poza_ue_to_dokladnie_efta(self):
        """Port Schengen spoza UE moze byc tylko w Norwegii, Islandii albo Szwajcarii.

        Gdyby kolumny `L[3]` i `L[4]` byly przestawione, ta lista wypelnilaby
        sie portami z calej Europy. Wyliczam ja wprost zamiast sprawdzac
        implikacje, bo lista, ktora sie nie zgadza, od razu pokazuje wielkosc
        rozjazdu.
        """
        efta = {"OSL", "BGO", "SVG", "TRD", "KEF", "ZRH", "GVA", "BRN", "BSL", "LUG"}
        znalezione = {k for k, p in self.db.ports.items() if p.schengen and not p.eu}
        self.assertTrue(znalezione <= efta,
                        f"Schengen poza UE i poza EFTA: {sorted(znalezione - efta)}")

    def test_kazdy_port_ue_jest_objety_eu261(self):
        """`L[3]` (UE) i `L[5]` (EU261) to rozne kolumny, ale UE implikuje EU261."""
        for iata, p in self.db.ports.items():
            if p.eu:
                with self.subTest(port=iata):
                    self.assertTrue(p.eu261, f"{iata} w UE, ale bez EU261")


class TestTrasy(unittest.TestCase):
    def setUp(self):
        self.db = db()

    def test_regula_eu261_odtwarza_kazda_trase(self):
        """Najmocniejszy test dekodu: `T[2]` i `T[3]` musza sie zgadzac na 310/310.

        Gdyby kolumna dystansu albo kategorii byla przesunieta, ten test
        rozjechalby sie natychmiast -- kategoria wynika z dystansu regula,
        ktora baza podaje osobno w `EU.tierRule`.
        """
        niezgodne = []
        for (o, d), route in self.db.routes.items():
            port_o, port_d = self.db.ports.get(o), self.db.ports.get(d)
            intra = bool(port_o and port_d and port_o.eu and port_d.eu)
            oczekiwany = self.db.eu261_tier_for(route.km, intra)
            if oczekiwany != route.eu261_tier:
                niezgodne.append((o, d, route.km, route.eu261_tier, oczekiwany))
        self.assertEqual(niezgodne, [],
                         f"{len(niezgodne)}/{len(self.db.routes)} tras nie zgadza sie")

    def test_dystanse_sa_dodatnie_i_sensowne(self):
        for key, route in self.db.routes.items():
            with self.subTest(trasa=key):
                self.assertGreater(route.km, 0)
                self.assertLess(route.km, 20100)      # polowa obwodu Ziemi

    def test_czas_bloku_rosnie_z_dystansem(self):
        """Korelacja ma byc silna -- brak korelacji znaczy przestawione kolumny."""
        pary = [(r.km, r.block_min) for r in self.db.routes.values() if r.block_min > 0]
        krotkie = [b for km, b in pary if km < 1000]
        dalekie = [b for km, b in pary if km > 5000]
        self.assertLess(sum(krotkie) / len(krotkie), sum(dalekie) / len(dalekie))

    def test_kabiny_to_znany_zestaw(self):
        for key, route in self.db.routes.items():
            with self.subTest(trasa=key):
                self.assertTrue(set(route.cabins) <= set("CPY"), route.cabins)


class TestRejsy(unittest.TestCase):
    def setUp(self):
        self.db = db()

    def test_maska_dni_ma_siedem_znakow_zero_jeden(self):
        for number, f in self.db.flights.items():
            with self.subTest(rejs=number):
                self.assertEqual(len(f.weekday_mask), 7)
                self.assertTrue(set(f.weekday_mask) <= {"0", "1"})

    def test_kazdy_rejs_lata_przynajmniej_raz_w_tygodniu(self):
        for number, f in self.db.flights.items():
            with self.subTest(rejs=number):
                self.assertGreaterEqual(f.days_per_week, 1)

    def test_operates_on_zgadza_sie_z_maska(self):
        f = next(iter(self.db.flights.values()))
        for day in range(7):
            self.assertEqual(f.operates_on(day), f.weekday_mask[day] == "1")

    def test_flights_on_zwraca_podzbior(self):
        for day in range(7):
            with self.subTest(dzien=day):
                loty = self.db.flights_on(day)
                self.assertTrue(0 < len(loty) <= len(self.db.flights))

    def test_wszystkie_numery_naleza_do_lot(self):
        """System jest zawezony do jednej linii -- to sprawdza, ze zrodlo tez."""
        obce = [n for n in self.db.flights if not n.upper().startswith("LO")]
        self.assertEqual(obce, [])


class TestFlotaITypy(unittest.TestCase):
    def setUp(self):
        self.db = db()

    def test_kazda_maszyna_ma_znany_typ(self):
        for reg, ac in self.db.fleet.items():
            with self.subTest(reg=reg):
                self.assertIn(ac.type_code, self.db.types)

    def test_maszyny_wlasne_maja_rejestracje_sp(self):
        for reg, ac in self.db.fleet.items():
            if not ac.wet_lease:
                with self.subTest(reg=reg):
                    self.assertTrue(reg.startswith("SP-"), reg)

    def test_acmi_sa_wyroznione(self):
        """Maszyn w wet-lease nie wolno uzywac do podmian -- musza byc oznaczone."""
        self.assertTrue(any(ac.wet_lease for ac in self.db.fleet.values()))

    def test_typy_maja_pojemnosc_zasieg_i_uprawnienie(self):
        for code, spec in self.db.types.items():
            with self.subTest(typ=code):
                self.assertGreater(spec.seats, 0)
                self.assertGreater(spec.range_km, 0)
                self.assertTrue(spec.rating)
                self.assertGreater(spec.cabin_crew, 0)

    def test_podzial_kabiny_nie_przekracza_pojemnosci(self):
        for code, spec in self.db.types.items():
            suma = sum(spec.cabin)
            if suma:
                with self.subTest(typ=code):
                    self.assertLessEqual(suma, spec.seats + 2)   # tolerancja na jump seat

    def test_szerokokadlubowce_maja_wiekszy_zasieg(self):
        szerokie = [s for s in self.db.types.values() if s.category == "szerokokadlubowy"]
        waskie = [s for s in self.db.types.values() if s.category != "szerokokadlubowy"]
        if szerokie and waskie:
            self.assertGreater(min(s.range_km for s in szerokie),
                               max(s.range_km for s in waskie))


class TestPrawoIParametry(unittest.TestCase):
    def setUp(self):
        self.db = db()

    def test_kategorie_eu261_rosna_z_dystansem(self):
        a, b, c = (self.db.compensation_eur(t) for t in "ABC")
        self.assertLess(a, b)
        self.assertLess(b, c)

    def test_nieznana_kategoria_wybucha(self):
        with self.assertRaises(KeyError):
            self.db.compensation_eur("Z")

    def test_progi_opieki_rosna_z_dystansem(self):
        progi = [self.db.care_threshold_min(t) for t in "ABC"]
        self.assertEqual(progi, sorted(progi))

    def test_regula_kategorii_na_granicach(self):
        self.assertEqual(self.db.eu261_tier_for(1500, False), "A")
        self.assertEqual(self.db.eu261_tier_for(1501, False), "B")
        self.assertEqual(self.db.eu261_tier_for(3500, False), "B")
        self.assertEqual(self.db.eu261_tier_for(3501, False), "C")

    def test_lot_wewnatrz_ue_zostaje_w_kategorii_b(self):
        """Nawet 5000 km wewnatrz UE to kategoria B -- to jest sedno reguly."""
        self.assertEqual(self.db.eu261_tier_for(5000, True), "B")
        self.assertEqual(self.db.eu261_tier_for(5000, False), "C")

    def test_prawdopodobienstwo_odszkodowania_wg_klasy_kodu(self):
        self.assertEqual({"c": 1.0, "n": 0.0, "d": 0.5}["c"],
                         self.db.compensation_probability(
                             next(k for k, v in self.db.delay_codes.items() if v[1] == "c")))
        self.assertEqual(0.0, self.db.compensation_probability(
            next(k for k, v in self.db.delay_codes.items() if v[1] == "n")))

    def test_nieznany_kod_daje_polowe(self):
        """Nieznany kod nie moze dawac ani zera, ani jedynki -- obie sa twierdzeniem."""
        self.assertEqual(self.db.compensation_probability("ZZZ"), 0.5)
        self.assertEqual(self.db.delay_code_class("ZZZ"), "?")

    def test_kody_opoznien_maja_znane_klasy(self):
        for code, row in self.db.delay_codes.items():
            with self.subTest(kod=code):
                self.assertIn(row[1], {"c", "n", "d", "", None, "?"})

    def test_fdp_krotszy_przy_wiekszej_liczbie_sektorow(self):
        """Kazdy dodatkowy sektor skraca dopuszczalny czas sluzby."""
        rano = 8 * 60
        limity = [self.db.max_fdp_min(rano, s) for s in range(2, 10)]
        self.assertEqual(limity, sorted(limity, reverse=True))

    def test_fdp_krotszy_przy_zgloszeniu_w_nocy(self):
        dzien = self.db.max_fdp_min(8 * 60, 2)
        noc = self.db.max_fdp_min(3 * 60, 2)
        self.assertLess(noc, dzien)

    def test_fdp_miesci_sie_w_ramach_easa(self):
        for godzina in range(24):
            for sektory in (1, 2, 6, 12):
                with self.subTest(h=godzina, s=sektory):
                    limit = self.db.max_fdp_min(godzina * 60, sektory)
                    self.assertTrue(480 <= limit <= 840, limit)

    def test_fdp_zawija_minute_powyzej_doby(self):
        self.assertEqual(self.db.max_fdp_min(8 * 60, 2),
                         self.db.max_fdp_min(1440 + 8 * 60, 2))

    def test_fdp_przycina_liczbe_sektorow(self):
        """Powyzej 10 sektorow tabela sie konczy -- ma przyciac, nie wybuchnac."""
        self.assertEqual(self.db.max_fdp_min(8 * 60, 10), self.db.max_fdp_min(8 * 60, 50))

    def test_kurs_walutowy_jest_dodatni(self):
        self.assertGreater(self.db.eur_pln, 0)


class TestRotacjeIPostoje(unittest.TestCase):
    def setUp(self):
        self.db = db()

    def test_rotacje_maja_dni_od_zera_do_szesciu(self):
        for reg, by_day in self.db.rotations.items():
            with self.subTest(reg=reg):
                self.assertTrue(set(by_day) <= set(range(7)))

    def test_odcinki_rotacji_sa_w_minutach_doby(self):
        for reg, by_day in self.db.rotations.items():
            for day, legs in by_day.items():
                for leg in legs:
                    with self.subTest(reg=reg, dzien=day, rejs=leg.number):
                        self.assertTrue(0 <= leg.std_minute < 1440)

    def test_brak_czasu_przylotu_daje_none_a_nie_zero(self):
        """Zero znaczyloby rejs o zerowym bloku. None znaczy: nie wiemy."""
        wartosci = {leg.block_min for by_day in self.db.rotations.values()
                    for legs in by_day.values() for leg in legs}
        self.assertNotIn(0, wartosci)

    def test_postoje_maja_minimum_ponizej_rekomendacji(self):
        for code, sectors in self.db.turnarounds.items():
            for sector, (rekomendowany, minimum) in sectors.items():
                with self.subTest(typ=code, sektor=sector):
                    self.assertLessEqual(minimum, rekomendowany)
                    self.assertGreater(minimum, 0)


class TestPodsumowanie(unittest.TestCase):
    def test_summary_ma_niezerowe_liczniki(self):
        s = db().summary()
        for key in ("porty", "trasy", "numery_rejsow", "flota", "typy",
                    "kody_opoznien", "podstawy_prawne"):
            with self.subTest(pole=key):
                self.assertGreater(s[key], 0)

    def test_wersja_i_data_sa_ustawione(self):
        self.assertNotEqual(db().version, "?")
        self.assertNotEqual(db().generated, "?")


if __name__ == "__main__":
    unittest.main()
