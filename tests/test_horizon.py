"""Horyzont propagacji.

Tablica stawia warunek wprost: liczymy do konca doby operacyjnej albo do
powrotu maszyny do bazy, co nastapi pierwsze. Node 10 i node 13 musza uzywac
tej samej definicji, inaczej network impact i koszt siatki opisuja rozne
kawalki tej samej doby.
"""

import unittest

from lotis.kernel.horizon import connecting_passengers, downstream_flights

from ._helpers import flight, itinerary, passenger, tiny_snapshot


def rotacja(*trasy: tuple[str, str], start_min: int = 0, block: int = 60,
            przerwa: int = 60):
    """Lancuch odcinkow, kazdy o `block` minut, z `przerwa` postoju."""
    legs = []
    offset = start_min
    for seq, (dep, arr) in enumerate(trasy):
        legs.append(flight(f"F{seq}", dep, arr, offset, block, seq=seq))
        offset += block + przerwa
    return legs


class TestDownstream(unittest.TestCase):
    def test_nieznany_rejs_wybucha(self):
        with self.assertRaises(KeyError):
            downstream_flights(tiny_snapshot(), "NIE-MA", "WAW")

    def test_zwraca_kolejne_odcinki_tej_samej_maszyny(self):
        snap = tiny_snapshot(rotacja(("WAW", "KRK"), ("KRK", "GDN"), ("GDN", "POZ")))
        result = downstream_flights(snap, "F0", "LHR")
        self.assertEqual([f.id for f in result.flights], ["F1", "F2"])

    def test_ostatni_odcinek_nie_ma_nastepnikow(self):
        snap = tiny_snapshot(rotacja(("WAW", "KRK"), ("KRK", "WAW")))
        result = downstream_flights(snap, "F1", "LHR")
        self.assertEqual(result.flights, ())
        self.assertEqual(result.stop_reason, "ROTATION_END")

    def test_powrot_do_bazy_konczy_horyzont(self):
        """Po powrocie do WAW dalsze odcinki juz nie propaguja tego zaklocenia."""
        snap = tiny_snapshot(rotacja(("WAW", "KRK"), ("KRK", "WAW"), ("WAW", "GDN")))
        result = downstream_flights(snap, "F0", "WAW")
        self.assertEqual([f.id for f in result.flights], ["F1"])
        self.assertEqual(result.stop_reason, "BASE_RETURN")

    def test_koniec_doby_konczy_horyzont(self):
        """Odcinek startujacy po 04:00 nastepnego dnia to juz inna doba pracy."""
        legs = [flight("F0", "WAW", "KRK", 0, 60, seq=0),
                flight("F1", "KRK", "GDN", 24 * 60, 60, seq=1)]
        snap = tiny_snapshot(legs)
        result = downstream_flights(snap, "F0", "LHR")
        self.assertEqual(result.flights, ())
        self.assertEqual(result.stop_reason, "END_OF_DAY")

    def test_limit_odcinkow(self):
        snap = tiny_snapshot(rotacja(*[("WAW", "KRK")] * 8, przerwa=10, block=30))
        result = downstream_flights(snap, "F0", "LHR", max_legs=3)
        self.assertEqual(len(result.flights), 3)
        self.assertEqual(result.stop_reason, "MAX_LEGS")

    def test_rejs_bez_rotacji_daje_pusty_horyzont(self):
        snap = tiny_snapshot([flight("F0", "WAW", "KRK", rotation_id="SIEROTA")],
                             rotations={})
        result = downstream_flights(snap, "F0", "WAW")
        self.assertEqual(result.flights, ())
        self.assertEqual(result.stop_reason, "ROTATION_END")

    def test_kolejnosc_wynika_z_seq_a_nie_z_kolejnosci_w_slowniku(self):
        legs = [flight("F1", "KRK", "GDN", 120, 60, seq=1),
                flight("F0", "WAW", "KRK", 0, 60, seq=0)]
        snap = tiny_snapshot(legs)
        self.assertEqual([f.id for f in downstream_flights(snap, "F0", "LHR").flights], ["F1"])

    def test_cutoff_jest_koncem_doby_operacyjnej(self):
        snap = tiny_snapshot(rotacja(("WAW", "KRK")))
        result = downstream_flights(snap, "F0", "LHR")
        self.assertEqual(result.cutoff.hour, 2)     # 04:00 lokalnie przy UTC+2


class TestPasazerowieTransferowi(unittest.TestCase):
    def snapshot_z_pasazerami(self):
        return tiny_snapshot(
            passengers={
                "P1": passenger("P1", "OD1"),
                "P2": passenger("P2", "OD2"),
                "P3": passenger("P3", "OD3"),
            },
            itineraries={
                "OD1": itinerary("OD1", ("F1", "F2")),   # transferowy
                "OD2": itinerary("OD2", ("F1",)),        # bezposredni
                "OD3": itinerary("OD3", ("F2",)),        # nie dotyczy F1
            },
        )

    def test_znajduje_tylko_tych_z_dalszym_odcinkiem(self):
        self.assertEqual(connecting_passengers(self.snapshot_z_pasazerami(), "F1"), ["P1"])

    def test_ostatni_odcinek_nie_ma_transferowych(self):
        self.assertEqual(connecting_passengers(self.snapshot_z_pasazerami(), "F2"), [])

    def test_wynik_jest_posortowany(self):
        snap = tiny_snapshot(
            passengers={f"P{i}": passenger(f"P{i}", f"OD{i}") for i in (3, 1, 2)},
            itineraries={f"OD{i}": itinerary(f"OD{i}", ("F1", "F2")) for i in (3, 1, 2)},
        )
        self.assertEqual(connecting_passengers(snap, "F1"), ["P1", "P2", "P3"])

    def test_pasazer_bez_podrozy_jest_pomijany(self):
        snap = tiny_snapshot(passengers={"P1": passenger("P1", "SIEROTA")}, itineraries={})
        self.assertEqual(connecting_passengers(snap, "F1"), [])


if __name__ == "__main__":
    unittest.main()
