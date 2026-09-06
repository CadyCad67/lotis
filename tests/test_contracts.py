"""Model dziedzinowy. Niezmienniki, ktore maja wybuchac glosno.

`ContractViolation` znaczy blad w kodzie, nie w danych, wiec kazdy z tych
testow opisuje sytuacje, ktora nigdy nie powinna przejsc przez konstruktor.
"""

import unittest
from datetime import UTC, datetime, timedelta

from lotis.kernel.contracts import (
    Basket, CrewRole, Disruption, DisruptionType, Flight, Itinerary, Option,
    OptionKind, PaxOutcome, PaxOutcomeKind, Scope,
)
from lotis.kernel.errors import ContractViolation

from ._helpers import (
    aircraft_type, airport, crew_member, flight, itinerary, passenger, tiny_snapshot,
)


class TestKoszyk(unittest.TestCase):
    def test_jest_dokladnie_szesnascie_koszykow(self):
        """Blok 3 tablicy: 2 klasy x 2 typy podrozy x 2 momenty zakupu x 2 statusy."""
        self.assertEqual(len(Basket.all()), 16)
        self.assertEqual(len({b.key for b in Basket.all()}), 16)

    def test_klucz_i_parsowanie_sa_odwracalne(self):
        for basket in Basket.all():
            with self.subTest(key=basket.key):
                self.assertEqual(Basket.parse(basket.key), basket)

    def test_nieznany_klucz_wybucha(self):
        for bad in ("", "X-DIR-EAR-BAS", "Y-DIR-EAR", "kompletne smieci"):
            with self.subTest(key=bad), self.assertRaises(ContractViolation):
                Basket.parse(bad)

    def test_koszyk_jest_hashowalny(self):
        self.assertEqual(len(set(Basket.all())), 16)


class TestPasazer(unittest.TestCase):
    def test_wartosc_to_taryfa_plus_ancillary(self):
        pax = passenger(fare=100_00, anc=25_00)
        self.assertEqual(pax.value.minor, 125_00)

    def test_podroz_bez_odcinkow_wybucha(self):
        with self.assertRaises(ContractViolation):
            Itinerary(id="OD1", origin="WAW", destination="KRK", segments=())

    def test_podroz_z_odcinkami_przechodzi(self):
        self.assertEqual(len(itinerary(segments=("F1", "F2")).segments), 2)


class TestRejs(unittest.TestCase):
    def test_przylot_przed_odlotem_wybucha(self):
        with self.assertRaises(ContractViolation):
            flight(block_min=-10)

    def test_zerowy_blok_wybucha(self):
        with self.assertRaises(ContractViolation):
            flight(block_min=0)

    def test_czas_bez_strefy_wybucha(self):
        naive = datetime(2026, 8, 21, 6, 0)
        with self.assertRaises(ContractViolation):
            Flight(id="F", number="F", dep="WAW", arr="KRK",
                   std=naive, sta=naive + timedelta(minutes=60),
                   aircraft_reg="SP-LIA", type_code="E75S", rotation_id="R", seq=0)

    def test_blok_liczy_sie_w_minutach(self):
        self.assertEqual(flight(block_min=95).block_min, 95)

    def test_rejs_jest_mrozony(self):
        with self.assertRaises((AttributeError, TypeError)):
            flight().dep = "KRK"


class TestZaklocenie(unittest.TestCase):
    def zaklocenie(self, delta_min: int) -> Disruption:
        at = datetime(2026, 8, 21, 6, 0, tzinfo=UTC)
        return Disruption(
            id="D1", type=DisruptionType.TECHNICAL, scope=Scope.FLIGHT,
            flight_id="F1", rotation_id="R1", at=at,
            decision_deadline=at + timedelta(minutes=delta_min),
        )

    def test_termin_po_zdarzeniu_przechodzi(self):
        self.assertEqual(self.zaklocenie(30).iteration, 0)

    def test_termin_przed_zdarzeniem_wybucha(self):
        with self.assertRaises(ContractViolation):
            self.zaklocenie(-30)

    def test_termin_rowny_zdarzeniu_wybucha(self):
        """Zero minut na decyzje to nie jest termin, tylko blad danych."""
        with self.assertRaises(ContractViolation):
            self.zaklocenie(0)


class TestOpcja(unittest.TestCase):
    def opcja(self, **kw) -> Option:
        base = dict(id="O1", kind=OptionKind.MODIFYING, generator="test",
                    label="test", affected_flights=("F1",))
        base.update(kw)
        return Option(**base)

    def test_opcja_bez_rejsow_wybucha(self):
        with self.assertRaises(ContractViolation):
            self.opcja(affected_flights=())

    def test_swap_musi_dotyczyc_obu_rejsow_pary(self):
        """Blok 5 tablicy: policzony sam rejs A zawsze wychodzi na minus."""
        with self.assertRaises(ContractViolation) as ctx:
            self.opcja(affected_flights=("F1",), aircraft_swap=("F1", "F2"))
        self.assertIn("F2", str(ctx.exception))

    def test_poprawny_swap_przechodzi(self):
        opt = self.opcja(affected_flights=("F1", "F2"), aircraft_swap=("F1", "F2"))
        self.assertEqual(opt.aircraft_swap, ("F1", "F2"))

    def test_max_opoznienie_z_pustego_slownika_to_zero(self):
        self.assertEqual(self.opcja().max_delay_min, 0)

    def test_max_opoznienie_bierze_najwieksze(self):
        self.assertEqual(self.opcja(delay_min={"F1": 30, "F2": 75}).max_delay_min, 75)


class TestWynikPasazera(unittest.TestCase):
    def test_ujemne_opoznienie_wybucha(self):
        with self.assertRaises(ContractViolation):
            PaxOutcome(PaxOutcomeKind.DELAYED, delay_min=-1)

    def test_ujemne_noce_wybuchaja(self):
        with self.assertRaises(ContractViolation):
            PaxOutcome(PaxOutcomeKind.DELAYED, care_nights=-1)

    def test_rebooking_na_oal_zachowuje_przychod(self):
        """Bez tego rozliczenie interline nie ma sie do czego doliczyc."""
        self.assertTrue(PaxOutcomeKind.REBOOKED_OAL.keeps_revenue)

    def test_zwrot_i_offload_nie_zachowuja_przychodu(self):
        for kind in (PaxOutcomeKind.CANCELLED_REFUND,
                     PaxOutcomeKind.OFFLOADED_VOLUNTARY,
                     PaxOutcomeKind.OFFLOADED_INVOLUNTARY):
            with self.subTest(kind=kind):
                self.assertFalse(kind.keeps_revenue)

    def test_pasazer_zabrany_nie_potrzebuje_opieki(self):
        self.assertFalse(PaxOutcomeKind.KEPT.needs_care)

    def test_kazdy_inny_wynik_potrzebuje_opieki(self):
        for kind in PaxOutcomeKind:
            if kind is not PaxOutcomeKind.KEPT:
                with self.subTest(kind=kind):
                    self.assertTrue(kind.needs_care)


class TestPort(unittest.TestCase):
    def test_curfew_w_zwyklym_oknie(self):
        port = airport(curfew_start_min=60, curfew_end_min=300, curfew_kind=1)
        self.assertFalse(port.in_curfew(59))
        self.assertTrue(port.in_curfew(60))
        self.assertTrue(port.in_curfew(299))
        self.assertFalse(port.in_curfew(300))

    def test_curfew_przez_polnoc(self):
        """EPWA 23:30-05:30. Bez obslugi zawiniecia okno byloby puste."""
        port = airport(curfew_start_min=23 * 60 + 30, curfew_end_min=5 * 60 + 30, curfew_kind=1)
        self.assertTrue(port.in_curfew(23 * 60 + 45))
        self.assertTrue(port.in_curfew(0))
        self.assertTrue(port.in_curfew(5 * 60))
        self.assertFalse(port.in_curfew(12 * 60))

    def test_minuta_powyzej_doby_jest_zawijana(self):
        port = airport(curfew_start_min=60, curfew_end_min=300, curfew_kind=1)
        self.assertTrue(port.in_curfew(1440 + 120))

    def test_typ_1_blokuje_planowanie_a_typ_2_nie(self):
        """Maszyna opozniona moze operowac przy typie 1 -- zakaz dotyczy planowania."""
        typ1 = airport(curfew_start_min=60, curfew_end_min=300, curfew_kind=1)
        typ2 = airport(curfew_start_min=60, curfew_end_min=300, curfew_kind=2)
        self.assertTrue(typ1.blocks_planning(120))
        self.assertFalse(typ2.blocks_planning(120))

    def test_brak_curfew_nigdy_nie_blokuje(self):
        port = airport()
        self.assertFalse(port.in_curfew(120))
        self.assertFalse(port.blocks_planning(120))

    def test_polowiczne_dane_curfew_nie_blokuja(self):
        port = airport(curfew_start_min=60, curfew_end_min=None, curfew_kind=1)
        self.assertFalse(port.in_curfew(120))

    def test_koordynacja_slotow_od_poziomu_3(self):
        self.assertFalse(airport(slot_level=2).slot_controlled)
        self.assertTrue(airport(slot_level=3).slot_controlled)


class TestTypStatku(unittest.TestCase):
    def test_suma_kabin_wygrywa_gdy_jest_podzial(self):
        t = aircraft_type(seats_declared=999, seats_j=16, seats_pe=21, seats_y=213)
        self.assertEqual(t.seats_total, 250)
        self.assertTrue(t.has_fixed_cabin)

    def test_bez_podzialu_liczy_sie_pojemnosc_deklarowana(self):
        """Euro Business ma ruchoma kurtyne -- podzial J/Y zalezy od sprzedazy."""
        t = aircraft_type(seats_declared=186, seats_j=0, seats_pe=0, seats_y=0)
        self.assertEqual(t.seats_total, 186)
        self.assertFalse(t.has_fixed_cabin)


class TestZaloga(unittest.TestCase):
    def test_zapas_fdp(self):
        self.assertEqual(crew_member(limit=780, used=600).fdp_remaining_min, 180)

    def test_przekroczony_fdp_daje_wartosc_ujemna(self):
        """Ujemna wartosc ma byc widoczna, a nie przyciecia do zera."""
        self.assertEqual(crew_member(limit=780, used=800).fdp_remaining_min, -20)

    def test_role_sa_rozlaczne(self):
        self.assertEqual(len(set(CrewRole)), 3)


class TestSnapshot(unittest.TestCase):
    def test_flights_of_zwraca_odcinki_rotacji(self):
        snap = tiny_snapshot()
        self.assertEqual([f.id for f in snap.flights_of("ROT1")], ["F1", "F2"])

    def test_flights_of_nieznanej_rotacji_daje_pusto(self):
        self.assertEqual(tiny_snapshot().flights_of("NIE-MA"), [])

    def test_passengers_on_znajduje_po_odcinku(self):
        snap = tiny_snapshot(
            passengers={"P1": passenger("P1", "OD1")},
            itineraries={"OD1": itinerary("OD1", ("F1", "F2"))},
        )
        self.assertEqual([p.id for p in snap.passengers_on("F1")], ["P1"])
        self.assertEqual([p.id for p in snap.passengers_on("F2")], ["P1"])
        self.assertEqual(snap.passengers_on("F3"), [])

    def test_pasazer_bez_podrozy_nie_wywraca_wyszukiwania(self):
        snap = tiny_snapshot(passengers={"P1": passenger("P1", "SIEROTA")}, itineraries={})
        self.assertEqual(snap.passengers_on("F1"), [])


if __name__ == "__main__":
    unittest.main()
