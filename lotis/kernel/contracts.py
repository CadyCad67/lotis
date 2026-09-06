"""Model dziedzinowy. Wszystkie dataclasses sa mrozone.

Zasada: nic w tym pliku nie liczy. To sa ksztalty danych, ktore przeplywaja
miedzy nodes. Logika siedzi w nodes, zeby dalo sie ja testowac po kawalku.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from itertools import product
from typing import Any

from .errors import ContractViolation
from .money import Money

# ---------------------------------------------------------------- koszyki


class Cabin(StrEnum):
    BUSINESS = "J"
    ECONOMY = "Y"


class TripType(StrEnum):
    DIRECT = "DIRECT"
    CONNECTING = "CONNECTING"


class Purchase(StrEnum):
    EARLY = "EARLY"
    LATE = "LATE"


class PaxStatus(StrEnum):
    BASE = "BASE"
    LOYALTY = "LOYALTY"


@dataclass(frozen=True, slots=True)
class Basket:
    """Jeden z 16 koszykow wartosci pasazera (Blok 3 tablicy).

    klasa (2) x typ podrozy (2) x moment zakupu (2) x status (2) = 16.
    """

    cabin: Cabin
    trip: TripType
    purchase: Purchase
    status: PaxStatus

    @property
    def key(self) -> str:
        return f"{self.cabin}-{self.trip[:3]}-{self.purchase[:3]}-{self.status[:3]}"

    @classmethod
    def all(cls) -> tuple["Basket", ...]:
        return tuple(
            cls(c, t, p, s)
            for c, t, p, s in product(Cabin, TripType, Purchase, PaxStatus)
        )

    @classmethod
    def parse(cls, key: str) -> "Basket":
        try:
            cab, trip, pur, sta = key.split("-")
            return cls(
                Cabin(cab),
                TripType.DIRECT if trip == "DIR" else TripType.CONNECTING,
                Purchase.EARLY if pur == "EAR" else Purchase.LATE,
                PaxStatus.BASE if sta == "BAS" else PaxStatus.LOYALTY,
            )
        except (ValueError, KeyError) as exc:
            raise ContractViolation(f"nieznany koszyk: {key!r}") from exc


# ---------------------------------------------------------------- pasazer


class SpecialNeed(StrEnum):
    """PAX SPECIAL -- wplywa na kolejnosc przy odmowie przyjecia (node 12)."""

    REDUCED_MOBILITY = "REDUCED_MOBILITY"
    UNACCOMPANIED_MINOR = "UNACCOMPANIED_MINOR"
    GROUP = "GROUP"
    PET_IN_HOLD = "PET_IN_HOLD"
    MEDICAL_ASSIST = "MEDICAL_ASSIST"


@dataclass(frozen=True, slots=True)
class Passenger:
    id: str
    itinerary_id: str
    basket: Basket
    fare: Money
    ancillary: Money
    specials: frozenset[SpecialNeed] = frozenset()

    @property
    def value(self) -> Money:
        """Wartosc pasazera = wartosc biletu + ancillary (Blok 3B)."""
        return self.fare + self.ancillary


@dataclass(frozen=True, slots=True)
class Itinerary:
    """Podroz O&D. Wartosc pasazera wisi tutaj, nie na odcinku (luka 8)."""

    id: str
    origin: str
    destination: str
    segments: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.segments:
            raise ContractViolation(f"itinerary {self.id} bez odcinkow")


# ---------------------------------------------------------------- sprzet


@dataclass(frozen=True, slots=True)
class AircraftType:
    """Typ statku powietrznego.

    Kabina bywa zerowa i to nie jest brak danych: na waskokadlubowcach LOT-u
    Euro Business ma ruchoma kurtyne, wiec podzial J/Y zalezy od sprzedazy.
    Wtedy `seats_declared` jest jedyna sensowna pojemnoscia.
    """

    code: str
    name: str = ""
    seats_declared: int = 0
    seats_j: int = 0
    seats_pe: int = 0
    seats_y: int = 0
    range_km: int = 0
    category: str = ""
    rating: str = ""           # rodzina uprawnien zalogi, np. EJET / B737 / B787
    cabin_crew: int = 0        # minimum personelu pokladowego wg typu
    cost_proxy: str = ""       # typ odniesienia w tabeli kosztu minutowego
    cost_scale: float = 1.0

    @property
    def seats_total(self) -> int:
        split = self.seats_j + self.seats_pe + self.seats_y
        return split or self.seats_declared

    @property
    def has_fixed_cabin(self) -> bool:
        return (self.seats_j + self.seats_pe + self.seats_y) > 0


@dataclass(frozen=True, slots=True)
class Aircraft:
    reg: str
    icao24: str
    type_code: str
    position: str
    mel_items: tuple[str, ...] = ()
    etops_certified: bool = False
    available_from: datetime | None = None


@dataclass(frozen=True, slots=True)
class Airport:
    """Port w kontekscie konkretnej doby.

    `tz_offset_min` jest juz rozwiazane dla dnia snapshotu z nazwy strefy IANA
    (`tz`), wiec silnik nie musi znac kalendarza zmian czasu. Nazwa strefy
    zostaje, zeby dalo sie przeliczyc inna dobe bez wracania do zrodla.
    """

    iata: str
    icao: str
    tz_offset_min: int
    lat: float
    lon: float
    tz: str = "UTC"
    name: str = ""
    schengen: bool = False
    eu261: bool = False
    opens_min: int = 0            # minuty od lokalnej polnocy
    closes_min: int = 24 * 60
    curfew_start_min: int | None = None
    curfew_end_min: int | None = None
    curfew_kind: int = 0          # 1 = zakaz planowania, 2 = ograniczenia nocne
    slot_level: int = 0           # poziom WSG: 0 brak, 2 z rozkladem, 3 koordynowany
    mct: dict[str, int] = field(default_factory=dict)   # DD/SS/SN/NN/XL

    @property
    def slot_controlled(self) -> bool:
        return self.slot_level >= 3

    def in_curfew(self, local_minute: int) -> bool:
        if self.curfew_start_min is None or self.curfew_end_min is None:
            return False
        start, end, minute = self.curfew_start_min, self.curfew_end_min, local_minute % 1440
        return (start <= minute < end) if start < end else (minute >= start or minute < end)

    def blocks_planning(self, local_minute: int) -> bool:
        """Curfew typu 1 zakazuje PLANOWANIA operacji w oknie.

        Maszyna opozniona z przyczyn niezaleznych moze operowac -- dlatego
        to nie jest to samo co zamkniecie portu. Rozroznienie pochodzi wprost
        z Zasady Lokalnej EPWA 1 i jest odwzorowane w bazie jako `curfew_kind`.
        """
        return self.curfew_kind == 1 and self.in_curfew(local_minute)


# ---------------------------------------------------------------- zaloga


class CrewRole(StrEnum):
    CAPTAIN = "CAPTAIN"
    FIRST_OFFICER = "FIRST_OFFICER"
    CABIN = "CABIN"


@dataclass(frozen=True, slots=True)
class CrewMember:
    id: str
    role: CrewRole
    base: str
    qualifications: frozenset[str]
    duty_start: datetime
    fdp_limit_min: int
    duty_used_min: int = 0
    rest_ok: bool = True

    @property
    def fdp_remaining_min(self) -> int:
        return self.fdp_limit_min - self.duty_used_min


# ---------------------------------------------------------------- rejsy


@dataclass(frozen=True, slots=True)
class Flight:
    id: str
    number: str
    dep: str
    arr: str
    std: datetime          # scheduled time of departure, UTC
    sta: datetime          # scheduled time of arrival, UTC
    aircraft_reg: str
    type_code: str
    rotation_id: str
    seq: int               # pozycja w rotacji, od 0
    crew_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.sta <= self.std:
            raise ContractViolation(f"rejs {self.id}: STA nie jest po STD")
        if self.std.tzinfo is None or self.sta.tzinfo is None:
            raise ContractViolation(f"rejs {self.id}: czasy bez strefy")

    @property
    def block_min(self) -> int:
        return int((self.sta - self.std).total_seconds() // 60)


@dataclass(frozen=True, slots=True)
class Rotation:
    id: str
    aircraft_reg: str
    flight_ids: tuple[str, ...]


# ---------------------------------------------------------------- zaklocenie


class DisruptionType(StrEnum):
    TECHNICAL = "TECHNICAL"
    CREW = "CREW"
    WEATHER = "WEATHER"
    ATC_SLOT = "ATC_SLOT"
    AIRPORT = "AIRPORT"
    PAX = "PAX"
    SECURITY = "SECURITY"


class Scope(StrEnum):
    FLIGHT = "FLIGHT"
    ROTATION = "ROTATION"
    STATION = "STATION"


class Trigger(StrEnum):
    """Powod wejscia (albo ponownego wejscia) w node 04."""

    INITIAL = "INITIAL"
    ETA_CHANGE = "ETA_CHANGE"
    OPTION_EXPIRED = "OPTION_EXPIRED"
    NEW_DISRUPTION = "NEW_DISRUPTION"
    EXECUTION_FAILED = "EXECUTION_FAILED"


@dataclass(frozen=True, slots=True)
class Disruption:
    id: str
    type: DisruptionType
    scope: Scope
    flight_id: str
    rotation_id: str
    at: datetime
    decision_deadline: datetime
    detail: str = ""
    iteration: int = 0
    trigger: Trigger = Trigger.INITIAL
    estimated_delay_min: int = 0

    def __post_init__(self) -> None:
        if self.decision_deadline <= self.at:
            raise ContractViolation(
                f"zaklocenie {self.id}: termin decyzji nie jest po zdarzeniu"
            )


# ---------------------------------------------------------------- opcje


class OptionKind(StrEnum):
    """Steruje trybem liczenia kosztu w node 09 (box poboczny przy COST ENGINE)."""

    MODIFYING = "MODIFYING"          # koszt = roznica wobec sytuacji bez zaklocenia
    RESTRUCTURING = "RESTRUCTURING"  # koszt = pelny nowy zestaw minus stary


class PaxOutcomeKind(StrEnum):
    KEPT = "KEPT"
    DELAYED = "DELAYED"
    REBOOKED_OWN = "REBOOKED_OWN"
    REBOOKED_OAL = "REBOOKED_OAL"
    OFFLOADED_VOLUNTARY = "OFFLOADED_VOLUNTARY"
    OFFLOADED_INVOLUNTARY = "OFFLOADED_INVOLUNTARY"
    CANCELLED_REFUND = "CANCELLED_REFUND"

    @property
    def keeps_revenue(self) -> bool:
        """Czy linia zachowuje przychod z biletu.

        Rebooking na OAL zachowuje przychod, ale placi rozliczenie interline
        -- to jest dokladnie ta pozycja, bez ktorej OAL wychodzi za tanio.
        """
        return self in {
            PaxOutcomeKind.KEPT,
            PaxOutcomeKind.DELAYED,
            PaxOutcomeKind.REBOOKED_OWN,
            PaxOutcomeKind.REBOOKED_OAL,
        }

    @property
    def needs_care(self) -> bool:
        return self in {
            PaxOutcomeKind.DELAYED,
            PaxOutcomeKind.REBOOKED_OWN,
            PaxOutcomeKind.REBOOKED_OAL,
            PaxOutcomeKind.OFFLOADED_VOLUNTARY,
            PaxOutcomeKind.OFFLOADED_INVOLUNTARY,
            PaxOutcomeKind.CANCELLED_REFUND,
        }


@dataclass(frozen=True, slots=True)
class PaxOutcome:
    kind: PaxOutcomeKind
    delay_min: int = 0
    care_nights: int = 0

    def __post_init__(self) -> None:
        if self.delay_min < 0:
            raise ContractViolation("ujemne opoznienie pasazera")
        if self.care_nights < 0:
            raise ContractViolation("ujemna liczba nocy hotelowych")


@dataclass(frozen=True, slots=True)
class Option:
    """Jedna mozliwosc rozwiazania zaklocenia.

    `affected_flights` jest kluczowe: node 09, 10 i 11 sumuja po tej krotce.
    Dla SWAPu zawsze zawiera obydwa rejsy pary -- liczony sam rejs A zawsze
    wychodzi na minus i silnik nigdy by go nie wybral (Blok 5 tablicy).
    """

    id: str
    kind: OptionKind
    generator: str
    label: str
    affected_flights: tuple[str, ...]
    delay_min: dict[str, int] = field(default_factory=dict)
    cancelled: frozenset[str] = frozenset()
    pax_outcomes: dict[str, PaxOutcome] = field(default_factory=dict)
    aircraft_swap: tuple[str, str] | None = None
    new_type: dict[str, str] = field(default_factory=dict)
    expires_at: datetime | None = None
    resources: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.affected_flights:
            raise ContractViolation(f"opcja {self.id} nie dotyka zadnego rejsu")
        if self.aircraft_swap is not None:
            a, b = self.aircraft_swap
            missing = {a, b} - set(self.affected_flights)
            if missing:
                raise ContractViolation(
                    f"opcja {self.id}: SWAP musi dotyczyc obu rejsow pary, "
                    f"brakuje {sorted(missing)}"
                )

    @property
    def max_delay_min(self) -> int:
        return max(self.delay_min.values(), default=0)


# ---------------------------------------------------------------- zasoby


class ResourceKind(StrEnum):
    SPARE_AIRCRAFT = "SPARE_AIRCRAFT"
    RESERVE_CREW = "RESERVE_CREW"
    PARTNER_SEATS = "PARTNER_SEATS"
    SLOT = "SLOT"


@dataclass(frozen=True, slots=True)
class Resource:
    kind: ResourceKind
    key: str
    quantity: int = 1
    contested: bool = False


# ---------------------------------------------------------------- snapshot


class Confidence(StrEnum):
    """Poziom pewnosci pola po walidacji w node 02 (luka 11)."""

    KNOWN = "KNOWN"          # licz normalnie
    ESTIMATED = "ESTIMATED"  # licz, ale rozszerz widelki
    UNKNOWN = "UNKNOWN"      # zablokuj opcje zalezne od tego pola


# ---------------------------------------------------------------- wycena opcji


@dataclass(frozen=True, slots=True)
class Baseline:
    """Revenue sprzed zaklocenia -- punkt odniesienia dla kazdej opcji.

    `per_flight` niesie wartosc PROROWANA po dystansie, nie pelna wartosc
    podrozy. To jest odpowiedz na luke 8 tablicy: box WYNIK mowil "wartosc
    przypisana do O&D", a box WARTOSC PASAZERA "wartosc obu odcinkow" --
    przy sumowaniu po siatce bilet liczylby sie dwa razy.
    """

    per_flight: dict[str, Money]
    per_itinerary: dict[str, Money]
    pax_per_flight: dict[str, int]
    total: Money
    computed_at: datetime | None = None
    anchor_disruption: str = ""     # przy kilku zakloceniach: pierwsze w rotacji

    def of(self, flight_id: str) -> Money:
        return self.per_flight.get(flight_id, Money.zero())


@dataclass(frozen=True, slots=True)
class GateResult:
    """Wynik jednej bramki wykonalnosci (node 05)."""

    gate: str                  # 'samolot' | 'zaloga' | 'port' | 'miejsca'
    passed: bool
    reason: str = ""
    detail: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class RevenueBreakdown:
    """Przychod opcji rozbity na skladniki (node 08)."""

    kept: Money
    lost: Money
    refunded: Money
    components: dict[str, Money] = field(default_factory=dict)

    @property
    def total(self) -> Money:
        return self.kept


@dataclass(frozen=True, slots=True)
class CostBreakdown:
    """Koszt opcji rozbity na skladniki (node 09).

    `mode` decyduje, czym jest liczba: przy MODIFYING to roznica wobec sytuacji
    bez zaklocenia, przy RESTRUCTURING pelny nowy zestaw minus stary. Zmieszanie
    obu sprawia, ze dwie opcje przestaja byc porownywalne.
    """

    mode: OptionKind
    components: dict[str, Money] = field(default_factory=dict)

    @property
    def total(self) -> Money:
        total = Money.zero()
        for value in self.components.values():
            total = total + value
        return total

    def largest(self, top: int = 3) -> list[tuple[str, Money]]:
        return sorted(self.components.items(), key=lambda kv: -kv[1].minor)[:top]


@dataclass(frozen=True, slots=True)
class NetworkImpact:
    """Propagacja poza rejs zrodlowy (node 10)."""

    downstream_flights: tuple[str, ...]
    stop_reason: str
    delay_propagated_min: dict[str, int]
    connections_missed: int
    pax_affected: int
    crew_over_fdp: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Band:
    """Widelki min / oczekiwane / max. Puste widelki to zawyzona pewnosc."""

    low: Money
    expected: Money
    high: Money

    @property
    def spread(self) -> Money:
        return self.high - self.low

    def overlaps(self, other: "Band") -> bool:
        return self.low <= other.high and other.low <= self.high


@dataclass(frozen=True, slots=True)
class OptionEvaluation:
    """Komplet wyceny jednej opcji (node 11 zbiera 08 + 09 + 10)."""

    option_id: str
    revenue: RevenueBreakdown
    cost: CostBreakdown
    network: NetworkImpact | None
    loss: Money
    band: Band
    notes: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class LegalVerdict:
    """Wynik filtru prawnego (node 12).

    Filtr USUWA opcje, nigdy ich nie przecenia. Gdyby odszkodowanie bylo
    zwykla pozycja kosztowa, najtansza opcja byloby zdjac pasazerow wbrew
    woli i wpisac odszkodowanie w koszty -- silnik wybralby to, bo tak kaze
    arytmetyka (Blok 5 tablicy).
    """

    option_id: str
    lawful: bool
    rules_failed: tuple[tuple[str, str], ...] = ()   # (podstawa, powod)
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class RankedOption:
    """Pozycja w rankingu koncowym (node 13)."""

    option_id: str
    rank: int
    loss: Money
    band: Band
    saving_vs_default: Money
    score: float = 0.0
    policy_note: str = ""


@dataclass(frozen=True, slots=True)
class ExecutionCard:
    """KARTA WYKONANIA -- produkt koncowy systemu.

    Powstaje deterministycznie z wyniku silnika. Model moze dopisac komentarz
    obok, ale nie ma sciezki zapisu do srodka (luka 7 tablicy).
    """

    option_id: str
    label: str
    what_changes: tuple[str, ...]
    pax_offloaded: int
    pax_order: tuple[str, ...]
    rebooked_to: dict[str, str]
    crew_actions: tuple[str, ...]
    valid_until: datetime | None
    cost_low: Money
    cost_expected: Money
    cost_high: Money
    threshold_note: str = ""
    authorization_role: str = ""
    second_signature: bool = False


# ---------------------------------------------------------------- snapshot


@dataclass(frozen=True, slots=True)
class Snapshot:
    """Zamrozony stan swiata. Jego hash cytuje kazdy nastepny raport."""

    taken_at: datetime
    flights: dict[str, Flight]
    rotations: dict[str, Rotation]
    airports: dict[str, Airport]
    aircraft: dict[str, Aircraft]
    aircraft_types: dict[str, AircraftType]
    crew: dict[str, CrewMember]
    passengers: dict[str, Passenger]
    itineraries: dict[str, Itinerary]
    confidence: dict[str, Confidence] = field(default_factory=dict)
    digest: str = ""

    def flights_of(self, rotation_id: str) -> list[Flight]:
        rot = self.rotations.get(rotation_id)
        if rot is None:
            return []
        return [self.flights[f] for f in rot.flight_ids if f in self.flights]

    def passengers_on(self, flight_id: str) -> list[Passenger]:
        out = []
        for pax in self.passengers.values():
            itin = self.itineraries.get(pax.itinerary_id)
            if itin and flight_id in itin.segments:
                out.append(pax)
        return out
