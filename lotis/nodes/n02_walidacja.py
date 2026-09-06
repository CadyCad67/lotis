"""Node 02 -- WALIDACJA DANYCH.

Odpowiedz na luke 11 tablicy. Tablica zakladala, ze snapshot jest kompletny;
w praktyce nigdy nie jest, a silnik, ktory liczy na polu bez wartosci, oddaje
liczbe wygladajaca tak samo jak dobra. Dlatego kazde pole dostaje tu poziom
pewnosci:

  KNOWN      licz normalnie,
  ESTIMATED  licz, ale rozszerz widelki w node 11,
  UNKNOWN    zablokuj opcje zalezne od tego pola.

Node niczego nie naprawia. Naprawianie danych w locie znaczyloby, ze raport
opisuje swiat, ktorego nie bylo -- a caly sens logu z node 16 polega na tym,
ze da sie wrocic do tego, co system naprawde widzial.
"""

from __future__ import annotations

from itertools import pairwise

from ..kernel.contracts import Confidence, Snapshot
from ..kernel.node import Node, NodeOutput, RunContext
from ..kernel.report import Status

#: Ponizej tylu minut zapasu FDP zaloga nie utrzyma zadnego opoznienia.
FDP_MARGIN_MIN = 30

#: Odsetek zepsutych rekordow, powyzej ktorego pole schodzi do UNKNOWN.
UNKNOWN_THRESHOLD = 0.02


class WalidacjaNode(Node):
    id = "02"
    name = "walidacja"
    title = "DATA ENGINE"
    consumes = ("snapshot",)
    produces = "confidence"

    def run(self, ctx: RunContext) -> NodeOutput:
        snap: Snapshot = ctx.require("snapshot")
        report = self.new_report()

        # Niezmienniki: ich zlamanie znaczy, ze dane sa zle, i obniza pewnosc pola.
        checks = {
            "porty_rejsow": _unknown_airports(snap),
            "typy_statkow": _unknown_types(snap),
            "ciaglosc_rotacji": _rotation_breaks(snap),
            "zapas_fdp": _crew_without_margin(snap),
            "obsadzenie": _overbooked(snap),
            "kwalifikacje_zalogi": _crew_rating_mismatch(snap),
        }

        # Obserwacje: fakty o rozkladzie, ktore silnik musi znac, ale ktore
        # bledem nie sa. Nie dotykaja poziomu pewnosci -- kontrola oznaczajaca
        # wszystko na czerwono przestaje cokolwiek znaczyc po drugim uruchomieniu.
        observations = {
            "operacje_w_ciszy_nocnej": _curfew_operations(snap),
            "rejsy_bez_numeru_handlowego": _callsign_only(snap),
        }

        total_flights = max(1, len(snap.flights))
        confidence: dict[str, Confidence] = dict(snap.confidence)

        for name, issues in checks.items():
            share = len(issues) / total_flights
            level = (
                Confidence.KNOWN if not issues
                else Confidence.UNKNOWN if share > UNKNOWN_THRESHOLD
                else Confidence.ESTIMATED
            )
            confidence[name] = level
            report.number(f"{name}_bledow", len(issues), "szt")
            if issues:
                report.findings[name] = issues[:20]
                if len(issues) > 20:
                    report.findings[f"{name}_pominietych"] = len(issues) - 20

        for name, rows in observations.items():
            report.number(name, len(rows), "szt")
            if rows:
                report.findings[name] = rows[:20]
                if len(rows) > 20:
                    report.findings[f"{name}_pominietych"] = len(rows) - 20

        blocked = sorted(k for k, v in confidence.items() if v is Confidence.UNKNOWN)
        estimated = sorted(k for k, v in confidence.items() if v is Confidence.ESTIMATED)

        report.number("pol_znanych", sum(1 for v in confidence.values()
                                         if v is Confidence.KNOWN), "szt")
        report.number("pol_szacowanych", len(estimated), "szt")
        report.number("pol_nieznanych", len(blocked), "szt")

        report.findings["poziomy_pewnosci"] = {k: v.value for k, v in sorted(confidence.items())}

        curfew = observations["operacje_w_ciszy_nocnej"]
        report.summary = (
            f"Sprawdzono {len(checks)} rodzin niezmiennikow na {len(snap.flights)} rejsach. "
            + (f"Pola zablokowane: {', '.join(blocked)}." if blocked
               else "Zadne pole nie schodzi do UNKNOWN.")
            + (f" Osobno: {len(curfew)} operacji w oknie ciszy nocnej typu 1 "
               "-- to rozklad, nie blad danych." if curfew else "")
        )
        if curfew:
            report.decide(
                f"{len(curfew)} operacji lezy w oknie zakazu planowania -- node 05 "
                "traktuje je jako istniejace, ale nie wolno na nich planowac nowych"
            )

        bez_numeru = observations["rejsy_bez_numeru_handlowego"]
        if bez_numeru:
            report.data_gaps.append(
                f"{len(bez_numeru)} rejsow ma tylko znak wywolawczy, bez numeru handlowego "
                "-- zrodlo nie rozstrzyga, czy to loty techniczne (dolot, przebazowanie), "
                "czy rejsy handlowe, ktorym eksport zgubil numer"
            )
            report.decide(
                "manifest pasazerski dla tych rejsow jest niepewny: lot techniczny "
                "nie ma pasazerow, a wiec nie ma tez ekspozycji z Art. 7 EU261"
            )

        for field in blocked:
            report.warn(f"pole `{field}` na poziomie UNKNOWN "
                        "-- opcje od niego zalezne beda blokowane")
            report.decide(f"opcje zalezne od `{field}` sa niedopuszczalne "
                          "do czasu uzupelnienia danych")
        for field in estimated:
            report.decide(f"pole `{field}` liczone jako ESTIMATED -- node 11 rozszerza widelki")

        report.assume("zaloga", "derived", 0.7,
                      "sklad i limity FDP wyliczone z tabel EASA, nie z grafiku operatora")
        report.assume("obsadzenie", "synthetic", 0.6,
                      "manifest z rozkladow bazy, tozsamosci pasazerow modelowane")

        if blocked:
            report.status = Status.DEGRADED

        return NodeOutput(report, {
            "confidence": confidence,
            "walidacja": {k: len(v) for k, v in checks.items()},
        })


# ---------------------------------------------------------------- kontrole


def _unknown_airports(snap: Snapshot) -> list[dict[str, str]]:
    out = []
    for f in sorted(snap.flights.values(), key=lambda x: x.id):
        for role, iata in (("wylot", f.dep), ("przylot", f.arr)):
            if iata not in snap.airports:
                out.append({"id": f.id, "pole": role, "port": iata})
    return out


def _unknown_types(snap: Snapshot) -> list[dict[str, str]]:
    return [
        {"id": f.id, "typ": f.type_code}
        for f in sorted(snap.flights.values(), key=lambda x: x.id)
        if f.type_code not in snap.aircraft_types
    ]


def _rotation_breaks(snap: Snapshot) -> list[dict[str, object]]:
    """Kolejny odcinek nie startuje tam, gdzie skonczyl poprzedni.

    To nie zawsze blad danych: czesc lancuchow jest przycieta oknem eksportu.
    Ale silnik planujacy SWAP musi wiedziec, ze maszyna nie jest tam, gdzie
    wynika z poprzedniego odcinka.
    """
    out = []
    for rot in sorted(snap.rotations.values(), key=lambda r: r.id):
        legs = sorted(
            (snap.flights[f] for f in rot.flight_ids if f in snap.flights),
            key=lambda f: (f.seq, f.std),
        )
        for prev, nxt in pairwise(legs):
            if prev.arr != nxt.dep:
                out.append({
                    "id": rot.id, "z": prev.id, "do": nxt.id,
                    "konczy_w": prev.arr, "zaczyna_w": nxt.dep,
                })
            elif nxt.std < prev.sta:
                out.append({
                    "id": rot.id, "z": prev.id, "do": nxt.id,
                    "problem": "odlot przed przylotem poprzedniego odcinka",
                })
    return out


def _crew_without_margin(snap: Snapshot) -> list[dict[str, object]]:
    return [
        {"id": c.id, "zapas_min": c.fdp_remaining_min, "baza": c.base}
        for c in sorted(snap.crew.values(), key=lambda x: x.id)
        if c.fdp_remaining_min < FDP_MARGIN_MIN
    ]


def _overbooked(snap: Snapshot) -> list[dict[str, object]]:
    """Wiecej pasazerow niz miejsc. Jeden przebieg po podrozach, nie po rejsach."""
    seated: dict[str, int] = {}
    for pax in snap.passengers.values():
        itin = snap.itineraries.get(pax.itinerary_id)
        if itin is None:
            continue
        for segment in itin.segments:
            seated[segment] = seated.get(segment, 0) + 1

    out = []
    for flight_id, count in sorted(seated.items()):
        flight = snap.flights.get(flight_id)
        if flight is None:
            out.append({"id": flight_id, "problem": "pasazerowie na nieznanym rejsie",
                        "osob": count})
            continue
        spec = snap.aircraft_types.get(flight.type_code)
        if spec is None:
            continue
        if count > spec.seats_total:
            out.append({"id": flight_id, "osob": count, "miejsc": spec.seats_total,
                        "nadmiar": count - spec.seats_total})
    return out


def _crew_rating_mismatch(snap: Snapshot) -> list[dict[str, object]]:
    """Zaloga przypisana do rejsu bez uprawnienia na rodzine typu.

    Rodzina, nie typ: B737 NG i MAX dziela uprawnienie, wiec SWAP miedzy nimi
    nie wymaga zmiany zalogi. E195 i E195-E2 juz tak.
    """
    out = []
    for f in sorted(snap.flights.values(), key=lambda x: x.id):
        spec = snap.aircraft_types.get(f.type_code)
        if spec is None or not spec.rating:
            continue
        for crew_id in f.crew_ids:
            member = snap.crew.get(crew_id)
            if member is None:
                out.append({"id": f.id, "zaloga": crew_id, "problem": "nieznany czlonek zalogi"})
            elif spec.rating not in member.qualifications:
                out.append({"id": f.id, "zaloga": crew_id, "typ": f.type_code,
                            "wymagane": spec.rating,
                            "posiada": sorted(member.qualifications)})
    return out


def _callsign_only(snap: Snapshot) -> list[dict[str, object]]:
    """Rejsy identyfikowane samym znakiem wywolawczym, bez numeru handlowego.

    W zrodle wystepuja jako `znak:LOT1NZ`. Nie jest to blad rekordu -- rejs ma
    komplet czasow, port i maszyne. Jest to natomiast brak informacji, ktory
    wprost wplywa na wynik: bez numeru handlowego nie wiadomo, czy na pokladzie
    jest ktokolwiek, a od tego zalezy i manifest, i ekspozycja odszkodowawcza.
    """
    return [
        {"id": f.id, "znak": f.number, "z": f.dep, "do": f.arr, "maszyna": f.aircraft_reg}
        for f in sorted(snap.flights.values(), key=lambda x: x.id)
        if not f.number.upper().startswith("LO") or f.number.lower().startswith("znak:")
    ]


def _curfew_operations(snap: Snapshot) -> list[dict[str, object]]:
    """Operacje lezace w oknie ciszy nocnej typu 1.

    To NIE jest lista bledow i dlatego nie wchodzi do niezmiennikow. Zakaz
    z typu 1 dotyczy planowania, a nie istnienia operacji: w EPWA obowiazuja
    wylaczenia dla czesci ruchu, wiec rejs w rozkladzie o 00:45 jest faktem
    operacyjnym, a nie zepsutym rekordem. Silnik musi te liste znac z innego
    powodu -- na tych godzinach nie wolno mu ZAPLANOWAC opoznionego odlotu
    ani rejsu zastepczego.

    Typ 2 (kwoty nocne) tu nie wchodzi: on podnosi ryzyko slotu, nie zakazuje.
    """
    out = []
    for f in sorted(snap.flights.values(), key=lambda x: x.id):
        for role, iata, moment in (("wylot", f.dep, f.std), ("przylot", f.arr, f.sta)):
            port = snap.airports.get(iata)
            if port is None or port.curfew_kind != 1:
                continue
            local_min = (moment.hour * 60 + moment.minute + port.tz_offset_min) % 1440
            if port.blocks_planning(local_min):
                out.append({
                    "id": f.id, "pole": role, "port": iata,
                    "lokalnie": f"{local_min // 60:02d}:{local_min % 60:02d}",
                })
    return out
