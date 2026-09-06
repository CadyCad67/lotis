"""Wycena -- jedyne miejsce, ktore zamienia stawki bazy na kwoty silnika.

Baza `loops.jsx` podaje stawki w EUR. Silnik liczy w PLN, w groszach, na `int`.
Konwersja siedzi tutaj i nigdzie indziej: gdyby kazdy node przeliczal sam,
kurs rozjechalby sie miedzy nodes przy pierwszej zmianie, a raporty przestalyby
sie sumowac.

Kurs `K.fx.EUR_PLN` jest w bazie **oznaczony jako placeholder**. Kazdy node,
ktory podaje kwote, raportuje to jako jawne zalozenie -- inaczej liczba
wygladalaby na zmierzona.

Zrodla stawek, wszystkie z sekcji `K` bazy:
  `tac`    koszt minuty opoznienia wg typu (University of Westminster 2015)
  `care`   hotel, posilek, transport, telekomunikacja (Art. 9 EU261)
  `reb`    taryfa jednokierunkowa wg sektora, mnozniki klas, voucher dla ochotnika
  `crew`   nadgodziny, wezwanie z rezerwy, hotel zalogi, deadhead
  `grd`    obsluga naziemna: odladzanie, holowanie, postoj
  `cxl`    kasacja: utrata przychodu, ferry, ryzyko serii slotow
  `div`    diversion
  `mc99`   roszczenia z Konwencji montrealskiej
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property

from ..adapters.lot_db import LotDB, load_lot_db
from .money import Money

#: Poziom partnera -> mnoznik kosztu rebookingu (sekcja TF bazy).
#: 0 wlasny, 1 codeshare, 2 Star Alliance, 3 interline, 4 bez umowy.
TRANSFER_LEVEL_OWN = 0

#: Sektory, dla ktorych baza podaje taryfy i stawki.
SECTORS = ("domestic", "schengen", "europe", "mid", "longhaul")


@dataclass(frozen=True, slots=True)
class Rate:
    """Stawka z bazy razem z tym, skad pochodzi. Node cytuje oba."""

    eur: float
    path: str
    status: str = ""

    def pln(self, fx: float) -> Money:
        return Money.from_major(round(self.eur * fx, 2))


class Pricing:
    """Wycena skladnikow kosztu. Wszystko wychodzi jako `Money` w PLN."""

    def __init__(self, db: LotDB | None = None, fx: float | None = None) -> None:
        self.db = db or load_lot_db()
        self._fx_override = fx

    # ---- kurs ----

    @cached_property
    def fx(self) -> float:
        if self._fx_override is not None:
            return self._fx_override
        return float(self.db.costs["fx"]["EUR_PLN"])

    @property
    def fx_status(self) -> str:
        """Baza sama oznacza kurs jako placeholder -- node ma to raportowac."""
        return str(self.db.costs["fx"].get("status", ""))

    def eur(self, amount: float) -> Money:
        return Money.from_major(round(float(amount) * self.fx, 2))

    # ---- odszkodowanie i opieka (EU261) ----

    def compensation(self, tier: str) -> Money:
        """Art. 7 -- pelna kwota. Zaniżanie jej jest zakazane (CF.hard, UOKiK)."""
        return self.eur(self.db.compensation_eur(tier))

    def compensation_reduced(self, tier: str) -> Money:
        """Art. 7 ust. 2 -- obnizka o 50% przy zmianie planu w progu kategorii."""
        return self.compensation(tier) / 2

    def care_threshold_min(self, tier: str) -> int:
        return self.db.care_threshold_min(tier)

    def reroute_window_min(self, tier: str) -> int:
        for row in self.db.eu261["tiers"]:
            if row["tier"] == tier:
                return int(row["reduction_if_reroute_arrival_within_min"])
        raise KeyError(f"nieznany tier EU261: {tier}")

    @property
    def compensation_threshold_min(self) -> int:
        """Prog 3 h liczony na PRZYLOCIE do miejsca docelowego pasazera."""
        return int(self.db.eu261["delay"]["compensation_threshold_min"])

    @property
    def reimbursement_threshold_min(self) -> int:
        """Od 5 h pasazer moze zrezygnowac i zadac zwrotu (Art. 8 ust. 1 lit. a)."""
        return int(self.db.eu261["delay"]["reimbursement_threshold_min"])

    # ---- opieka (Art. 9) ----

    def hotel_night(self, region: str = "europe") -> Money:
        table = self.db.costs["care"]["hotel_night_eur"]
        return self.eur(table.get(region, table["europe"]))

    @property
    def pax_per_room(self) -> float:
        return float(self.db.costs["care"]["pax_per_room"])

    def meal(self, wait_min: int) -> Money:
        """Posilek 'adekwatny do czasu oczekiwania' -- baza ma dwa progi."""
        table = self.db.costs["care"]["meal_voucher_eur"]
        key = "long_wait" if wait_min >= 240 else "short_wait"
        return self.eur(table[key])

    @property
    def transport_to_hotel(self) -> Money:
        return self.eur(self.db.costs["care"]["transport_hotel_eur"])

    @property
    def telecom(self) -> Money:
        """Dwie rozmowy albo e-maile na pasazera (Art. 9)."""
        return self.eur(self.db.costs["care"]["telecom_eur"])

    def care_per_pax(self, wait_min: int, nights: int, region: str = "europe") -> Money:
        """Pelny koszt opieki na jednego pasazera.

        Hotel dzieli sie przez `pax_per_room`, bo rodziny zajmuja jeden pokoj --
        liczenie pokoju na glowe zawyzaloby nocleg o polowe.

        Kolejnosc dziala na wynik: `(hotel / obsadzenie) * noce` zaokragla po
        dzieleniu i mnozy blad przez liczbe nocy, `(hotel * noce) / obsadzenie`
        zaokragla raz na koncu. Roznica to grosz na pasazera i noc -- niby nic,
        ale caly modul pieniedzy stoi na tym, ze zaokraglenie ma jedno miejsce
        i jest jawne.
        """
        total = self.meal(wait_min) + self.telecom
        if nights > 0:
            total = total + (self.hotel_night(region) * nights) / self.pax_per_room
            total = total + self.transport_to_hotel
        return total

    # ---- rebooking ----

    def one_way_fare(self, sector: str) -> Money:
        table = self.db.costs["reb"]["one_way_fare_estimate_eur"]
        return self.eur(table.get(sector, table["europe"]))

    def rebook_own(self, sector: str) -> Money:
        """Wlasny rejs kosztuje tylko utracona sprzedaz miejsca (spill)."""
        pct = float(self.db.costs["reb"]["own_flight_opportunity_cost_pct"]) / 100.0
        return self.one_way_fare(sector) * pct

    def rebook_oal(self, sector: str, transfer_level: int, cabin: str = "Y") -> Money:
        """Rebooking na obcego przewoznika: taryfa x poziom partnera x klasa.

        Bez mnoznika poziomu partnera rebooking na OAL zawsze wychodzi tanszy
        niz jest naprawde i silnik wybiera go za czesto (Blok 5 tablicy).
        """
        base = self.one_way_fare(sector)
        level = self.db.transfer_levels.get(str(transfer_level))
        factor = float(level[1]) if level else 1.4
        cabin_factor = {
            "C": float(self.db.costs["reb"]["business_multiplier"]),
            "P": float(self.db.costs["reb"]["premium_multiplier"]),
        }.get(cabin, 1.0)
        return base * factor * cabin_factor

    def volunteer_voucher(self, tier: str) -> Money:
        """Rekompensata dla ochotnika -- zawsze tansza niz odmowa wbrew woli."""
        table = self.db.costs["reb"]["denied_boarding_volunteer_voucher_eur"]
        return self.eur(table.get(tier, table["B"]))

    # ---- zaloga ----

    def crew_overtime(self, minutes: int, cockpit: int, cabin: int) -> Money:
        rates = self.db.costs["crew"]
        hours = minutes / 60.0
        cockpit_cost = self.eur(float(rates["overtime_cockpit_eur_h"]) * hours * cockpit)
        cabin_cost = self.eur(float(rates["overtime_cabin_eur_h"]) * hours * cabin)
        return cockpit_cost + cabin_cost

    @property
    def standby_callout(self) -> Money:
        return self.eur(self.db.costs["crew"]["standby_callout_eur"])

    @property
    def crew_hotel_night(self) -> Money:
        return self.eur(self.db.costs["crew"]["crew_hotel_night_eur"])

    def deadhead_seat(self, sector: str) -> Money:
        table = self.db.costs["crew"]["deadhead_seat_eur"]
        key = "longhaul" if sector == "longhaul" else (
            "domestic" if sector == "domestic" else "europe")
        return self.eur(table[key])

    # ---- opoznienie ----

    def delay_minute(self, type_code: str, delay_min: int) -> Money:
        """Koszt jednej minuty opoznienia dla typu, przy danym czasie trwania.

        Krzywa jest wypukla: minuta przy 30 minutach kosztuje wielokrotnie
        wiecej niz przy 5, bo dochodzi propagacja i obsluga pasazera.
        """
        from ..adapters.aircraft_perf import delay_cost_eur_per_min
        return self.eur(delay_cost_eur_per_min(type_code, delay_min))

    def delay_total(self, type_code: str, delay_min: int) -> Money:
        return self.delay_minute(type_code, delay_min) * delay_min

    @property
    def atfm_minute(self) -> Money:
        return self.eur(self.db.costs["atfm"]["avg_cost_per_min_eur"])

    @property
    def ctot_loss_extra_min(self) -> int:
        """Typowe przesuniecie po utracie okna startowego w szczycie."""
        return int(self.db.costs["atfm"]["new_ctot_expected_extra_min"]["value"])

    # ---- kasacja i obsluga ----

    def ferry_per_block_min(self, category: str) -> Money:
        table = self.db.costs["cxl"]["ferry_flight_cost_per_block_min_eur"]
        return self.eur(table.get(_size(category), table["narrowbody"]))

    def slot_series_risk(self, slot_level: int) -> Money:
        """Ryzyko utraty serii slotow -- realne tylko w porcie koordynowanym."""
        table = self.db.costs["cxl"]["slot_series_risk_eur"]
        return self.eur(table.get(f"L{slot_level}", 0))

    @property
    def recovery_rebooked_own_pct(self) -> float:
        return float(self.db.costs["cxl"]["recovery_pct_rebooked_own"]) / 100.0

    def diversion(self, category: str) -> Money:
        table = self.db.costs["div"]["fixed_eur"]
        return self.eur(table.get(_size(category), table["narrowbody"]))

    def stand_parking_hour(self, category: str) -> Money:
        table = self.db.costs["grd"]["stand_parking_eur_per_h"]
        return self.eur(table.get(_size(category), table["narrowbody"]))

    @property
    def priority_turnaround(self) -> Money:
        return self.eur(self.db.costs["grd"]["priority_turnaround_extra_eur"])

    @property
    def towing(self) -> Money:
        return self.eur(self.db.costs["grd"]["towing_eur"])

    # ---- Konwencja montrealska ----

    def montreal_expected(self, transfer_pax: int) -> Money:
        """Oczekiwane roszczenia z MC99 dla pasazerow transferowych powyzej 3 h.

        Niezalezne od EU261 -- to osobna podstawa i osobna kwota.
        """
        row = self.db.costs["mc99"]
        probability = float(row["claim_probability_pct"]) / 100.0
        return self.eur(float(row["avg_claim_eur"]) * probability * transfer_pax)

    # ---- przejrzystosc ----

    def assumptions(self) -> list[tuple[str, str, float, str]]:
        """Stawki oznaczone w bazie jako szacunek. Node wypisuje je jako zalozenia."""
        out: list[tuple[str, str, float, str]] = [
            ("kurs EUR/PLN", "policy", 0.5, f"{self.fx} -- {self.fx_status}"),
        ]
        for section in ("care", "reb", "crew", "grd", "cxl", "div", "mc99"):
            status = str(self.db.costs.get(section, {}).get("status", ""))
            if status and status != "public":
                out.append((f"stawki K.{section}", "policy", 0.6, status))
        return out


def _size(category: str) -> str:
    """Kategoria typu z bazy -> klucz tabeli stawek naziemnych."""
    lowered = (category or "").lower()
    if "szeroko" in lowered:
        return "widebody"
    if "regional" in lowered:
        return "regional"
    return "narrowbody"


_CACHE: Pricing | None = None


def pricing() -> Pricing:
    global _CACHE
    if _CACHE is None:
        _CACHE = Pricing()
    return _CACHE
