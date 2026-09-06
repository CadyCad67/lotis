"""Wycena -- jedyne miejsce, ktore zamienia stawki bazy na kwoty silnika.

Kazdy blad tutaj mnozy sie przez liczbe pasazerow. Dlatego testy sprawdzaja
nie tylko, czy stawka sie odczytuje, ale czy zachowuje relacje, ktore musza
zachodzic: ochotnik zawsze tanszy od odmowy wbrew woli, rebooking na obcego
zawsze drozszy od wlasnego, kategoria C zawsze drozsza od A.
"""

import unittest

from lotis.kernel.money import Money
from lotis.kernel.pricing import Pricing, _size, pricing

from ._helpers import db


class TestKurs(unittest.TestCase):
    def setUp(self):
        self.p = Pricing(db=db())

    def test_kurs_jest_dodatni(self):
        self.assertGreater(self.p.fx, 0)

    def test_kurs_da_sie_nadpisac(self):
        self.assertEqual(Pricing(db=db(), fx=4.0).fx, 4.0)

    def test_kurs_jest_oznaczony_jako_placeholder(self):
        """Baza sama tak go opisuje -- node ma to raportowac jako zalozenie."""
        self.assertIn("placeholder", self.p.fx_status.lower())

    def test_konwersja_eur_na_pln(self):
        self.assertEqual(Pricing(db=db(), fx=4.0).eur(100).minor, 400_00)

    def test_konwersja_zaokragla_do_grosza(self):
        self.assertEqual(Pricing(db=db(), fx=4.3).eur(0.001).minor, 0)

    def test_zalozenia_wypisuja_kurs_i_szacunki(self):
        pola = [a[0] for a in self.p.assumptions()]
        self.assertIn("kurs EUR/PLN", pola)
        self.assertGreater(len(pola), 1)


class TestOdszkodowanie(unittest.TestCase):
    def setUp(self):
        self.p = Pricing(db=db())

    def test_kategorie_rosna(self):
        a, b, c = (self.p.compensation(t) for t in "ABC")
        self.assertLess(a, b)
        self.assertLess(b, c)

    def test_redukcja_to_polowa(self):
        """Art. 7 ust. 2 -- obnizka o 50% przy zmianie planu w oknie kategorii."""
        for tier in "ABC":
            with self.subTest(tier=tier):
                self.assertEqual(self.p.compensation_reduced(tier) * 2,
                                 self.p.compensation(tier))

    def test_progi_opieki_rosna_z_kategoria(self):
        progi = [self.p.care_threshold_min(t) for t in "ABC"]
        self.assertEqual(progi, sorted(progi))

    def test_okno_redukcji_rosnie_z_kategoria(self):
        okna = [self.p.reroute_window_min(t) for t in "ABC"]
        self.assertEqual(okna, sorted(okna))

    def test_prog_odszkodowania_to_trzy_godziny(self):
        self.assertEqual(self.p.compensation_threshold_min, 180)

    def test_prog_zwrotu_to_piec_godzin(self):
        self.assertEqual(self.p.reimbursement_threshold_min, 300)

    def test_prog_zwrotu_jest_wyzszy_niz_odszkodowania(self):
        self.assertGreater(self.p.reimbursement_threshold_min,
                           self.p.compensation_threshold_min)

    def test_nieznana_kategoria_wybucha(self):
        for method in (self.p.compensation, self.p.care_threshold_min,
                       self.p.reroute_window_min):
            with self.subTest(metoda=method.__name__), self.assertRaises(KeyError):
                method("Z")


class TestOpieka(unittest.TestCase):
    def setUp(self):
        self.p = Pricing(db=db())

    def test_hotel_zalezy_od_regionu(self):
        self.assertLess(self.p.hotel_night("WAW"), self.p.hotel_night("longhaul"))

    def test_nieznany_region_spada_na_europe(self):
        self.assertEqual(self.p.hotel_night("marsjanski"), self.p.hotel_night("europe"))

    def test_dluzsze_oczekiwanie_daje_wyzszy_posilek(self):
        """Art. 9 mowi 'adekwatnie do czasu oczekiwania' -- baza ma dwa progi."""
        self.assertGreater(self.p.meal(300), self.p.meal(60))

    def test_prog_posilku_lezy_na_czterech_godzinach(self):
        self.assertEqual(self.p.meal(239), self.p.meal(60))
        self.assertEqual(self.p.meal(240), self.p.meal(600))

    def test_opieka_bez_noclegu_to_posilek_i_telekom(self):
        self.assertEqual(self.p.care_per_pax(60, 0),
                         self.p.meal(60) + self.p.telecom)

    def test_nocleg_dodaje_hotel_i_transport(self):
        bez = self.p.care_per_pax(60, 0)
        z_noclegiem = self.p.care_per_pax(60, 1)
        self.assertGreater(z_noclegiem, bez)
        self.assertGreater(z_noclegiem - bez, self.p.transport_to_hotel)

    def test_hotel_dzieli_sie_przez_obsadzenie_pokoju(self):
        """Rodziny zajmuja jeden pokoj -- liczenie na glowe zawyzaloby nocleg."""
        self.assertGreater(self.p.pax_per_room, 1.0)
        na_osobe = self.p.care_per_pax(60, 1) - self.p.care_per_pax(60, 0)
        self.assertLess(na_osobe, self.p.hotel_night("europe") + self.p.transport_to_hotel)

    def test_dwie_noce_kosztuja_wiecej_niz_jedna(self):
        self.assertGreater(self.p.care_per_pax(60, 2), self.p.care_per_pax(60, 1))

    def test_nocleg_zaokragla_sie_raz_na_koncu(self):
        """Znalezisko audytu: `(hotel / obsadzenie) * noce` zaokraglalo po
        dzieleniu i mnozylo blad przez liczbe nocy. Poprawna kolejnosc mnozy
        najpierw, wiec zaokraglenie zostaje jedno.

        Odniesieniem jest wartosc dokladna liczona na `Decimal`, a nie wielokrotnosc
        zaokraglonej pojedynczej nocy -- ta wlasnie NIE jest juz odniesieniem
        i o to w tej poprawce chodzi.
        """
        from decimal import ROUND_HALF_UP, Decimal
        baza = self.p.care_per_pax(60, 0) + self.p.transport_to_hotel
        for noce in (1, 2, 3, 7):
            with self.subTest(noce=noce):
                policzone = self.p.care_per_pax(60, noce) - baza
                dokladne = (Decimal(self.p.hotel_night("europe").minor) * noce
                            / Decimal(str(self.p.pax_per_room)))
                oczekiwane = int(dokladne.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
                self.assertEqual(policzone.minor, oczekiwane)


class TestRebooking(unittest.TestCase):
    def setUp(self):
        self.p = Pricing(db=db())

    def test_taryfa_rosnie_z_dystansem_sektora(self):
        self.assertLess(self.p.one_way_fare("domestic"), self.p.one_way_fare("longhaul"))

    def test_nieznany_sektor_spada_na_europe(self):
        self.assertEqual(self.p.one_way_fare("kosmiczny"), self.p.one_way_fare("europe"))

    def test_wlasny_rejs_kosztuje_ulamek_taryfy(self):
        """Tylko utracona sprzedaz miejsca (spill), nie pelna taryfa."""
        self.assertLess(self.p.rebook_own("europe"), self.p.one_way_fare("europe"))

    def test_obcy_przewoznik_drozszy_od_wlasnego(self):
        """Bez mnoznika poziomu partnera OAL wychodzi za tanio i silnik go naduzywa."""
        self.assertGreater(self.p.rebook_oal("europe", 3),
                           self.p.rebook_own("europe"))

    def test_gorszy_poziom_umowy_kosztuje_wiecej(self):
        codeshare = self.p.rebook_oal("europe", 1)
        interline = self.p.rebook_oal("europe", 3)
        bez_umowy = self.p.rebook_oal("europe", 4)
        self.assertLess(codeshare, interline)
        self.assertLess(interline, bez_umowy)

    def test_klasa_biznes_kosztuje_wielokrotnie_wiecej(self):
        self.assertGreater(self.p.rebook_oal("europe", 3, "C"),
                           self.p.rebook_oal("europe", 3, "Y") * 2)

    def test_nieznany_poziom_partnera_ma_wartosc_domyslna(self):
        self.assertGreater(self.p.rebook_oal("europe", 99).minor, 0)

    def test_voucher_ochotnika_nie_przekracza_odszkodowania(self):
        """Baza ustawia voucher DOKLADNIE na poziomie kwot z Art. 7, nie ponizej.

        To jest swiadome: ochotnikowi proponuje sie tyle, ile i tak nalezaloby
        sie przy odmowie wbrew woli, bo ponizej nikt sie nie zglosi. Oszczednosc
        sciezki ochotniczej nie bierze sie z nizszej kwoty, tylko z tego, ze
        odmowa wbrew woli dokłada do niej opieke z Art. 9 i przewoz z Art. 8.
        Testujemy wiec to, co naprawde ma zachodzic: voucher nigdy nie przekracza
        odszkodowania, a pelna sciezka przymusowa jest drozsza od ochotniczej.
        """
        for tier in "ABC":
            with self.subTest(tier=tier):
                self.assertLessEqual(self.p.volunteer_voucher(tier),
                                     self.p.compensation(tier))

    def test_sciezka_wbrew_woli_jest_drozsza_od_ochotniczej(self):
        """Blok 5 tablicy: 'kilkukrotnie drozej'. Roznica to opieka i przewoz."""
        for tier in "ABC":
            with self.subTest(tier=tier):
                ochotnik = self.p.volunteer_voucher(tier)
                przymus = (self.p.compensation(tier)
                           + self.p.care_per_pax(300, 1)
                           + self.p.rebook_oal("europe", 3))
                self.assertGreater(przymus, ochotnik)

    def test_voucher_rosnie_z_kategoria(self):
        self.assertLess(self.p.volunteer_voucher("A"), self.p.volunteer_voucher("C"))


class TestZaloga(unittest.TestCase):
    def setUp(self):
        self.p = Pricing(db=db())

    def test_nadgodziny_rosna_z_czasem(self):
        self.assertGreater(self.p.crew_overtime(120, 2, 4), self.p.crew_overtime(60, 2, 4))

    def test_nadgodziny_rosna_z_liczba_osob(self):
        self.assertGreater(self.p.crew_overtime(60, 3, 8), self.p.crew_overtime(60, 2, 4))

    def test_pilot_kosztuje_wiecej_niz_personel_pokladowy(self):
        self.assertGreater(self.p.crew_overtime(60, 1, 0), self.p.crew_overtime(60, 0, 1))

    def test_zerowy_czas_daje_zero(self):
        self.assertEqual(self.p.crew_overtime(0, 2, 4), Money.zero())

    def test_deadhead_rosnie_z_sektorem(self):
        self.assertLess(self.p.deadhead_seat("domestic"), self.p.deadhead_seat("longhaul"))

    def test_wezwanie_z_rezerwy_i_hotel_sa_dodatnie(self):
        self.assertGreater(self.p.standby_callout.minor, 0)
        self.assertGreater(self.p.crew_hotel_night.minor, 0)


class TestOpoznienieINaziemne(unittest.TestCase):
    def setUp(self):
        self.p = Pricing(db=db())

    def test_koszt_calkowity_to_stawka_razy_minuty(self):
        self.assertEqual(self.p.delay_total("E195", 30),
                         self.p.delay_minute("E195", 30) * 30)

    def test_dluzsze_opoznienie_kosztuje_wiecej_niz_proporcjonalnie(self):
        """Krzywa jest wypukla -- dochodzi propagacja i obsluga pasazera."""
        krotkie = self.p.delay_total("E195", 5)
        dlugie = self.p.delay_total("E195", 30)
        self.assertGreater(dlugie.minor, krotkie.minor * 6)

    def test_nieznany_typ_daje_zero(self):
        self.assertEqual(self.p.delay_minute("XXX", 30), Money.zero())

    def test_kategoria_rozmiaru_mapuje_sie_na_klucz_stawki(self):
        self.assertEqual(_size("szerokokadlubowy"), "widebody")
        self.assertEqual(_size("regionalny"), "regional")
        self.assertEqual(_size("waskokadlubowy"), "narrowbody")
        self.assertEqual(_size(""), "narrowbody")

    def test_ferry_rosnie_z_rozmiarem(self):
        self.assertLess(self.p.ferry_per_block_min("regionalny"),
                        self.p.ferry_per_block_min("szerokokadlubowy"))

    def test_diversion_rosnie_z_rozmiarem(self):
        self.assertLess(self.p.diversion("regionalny"), self.p.diversion("szerokokadlubowy"))

    def test_ryzyko_slotow_tylko_w_porcie_koordynowanym(self):
        """Poziom 2 ma rozklad, ale nie ma serii do stracenia."""
        self.assertEqual(self.p.slot_series_risk(2), Money.zero())
        self.assertGreater(self.p.slot_series_risk(3).minor, 0)

    def test_nieznany_poziom_slotow_daje_zero(self):
        self.assertEqual(self.p.slot_series_risk(0), Money.zero())

    def test_roszczenia_mc99_rosna_z_liczba_transferowych(self):
        self.assertGreater(self.p.montreal_expected(100), self.p.montreal_expected(10))

    def test_brak_transferowych_daje_zero_roszczen(self):
        self.assertEqual(self.p.montreal_expected(0), Money.zero())


class TestWspolnyEgzemplarz(unittest.TestCase):
    def test_pricing_zwraca_ten_sam_obiekt(self):
        self.assertIs(pricing(), pricing())

    def test_wszystkie_kwoty_sa_w_pln(self):
        p = pricing()
        for value in (p.compensation("A"), p.hotel_night(), p.one_way_fare("europe"),
                      p.standby_callout, p.towing, p.priority_turnaround):
            with self.subTest(kwota=value):
                self.assertEqual(value.currency, "PLN")

    def test_zadna_stawka_nie_jest_ujemna(self):
        p = pricing()
        for value in (p.compensation("C"), p.care_per_pax(300, 1), p.rebook_oal("mid", 4),
                      p.crew_overtime(90, 3, 8), p.diversion("waskokadlubowy")):
            with self.subTest(kwota=value):
                self.assertGreaterEqual(value.minor, 0)


if __name__ == "__main__":
    unittest.main()
