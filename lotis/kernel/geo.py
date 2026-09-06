"""Geometria potrzebna do proraty O&D.

Node 03 dzieli wartosc itinerary miedzy odcinki wedlug dystansu, wiec dystans
musi byc liczony jednym wzorem w calym systemie -- inaczej suma po siatce
przestaje sie zgadzac.
"""

from __future__ import annotations

from math import asin, cos, radians, sin, sqrt

EARTH_RADIUS_KM = 6371.0088


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Dystans po wielkim kole w kilometrach."""
    p1, p2 = radians(lat1), radians(lat2)
    dp = p2 - p1
    dl = radians(lon2 - lon1)
    a = sin(dp / 2) ** 2 + cos(p1) * cos(p2) * sin(dl / 2) ** 2
    return 2 * EARTH_RADIUS_KM * asin(min(1.0, sqrt(a)))
