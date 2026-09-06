"""Dashboard -- obsluga systemu z przegladarki.

Stoi na `http.server` ze stdlib, wiec nie dokladamy Flaska ani FastAPI dla
czterech endpointow. Serwer sluzy jeden plik HTML i kilka odpowiedzi JSON.

Nasluchuje domyslnie na 127.0.0.1. To nie jest przypadek: dashboard pokazuje
manifesty pasazerskie, stawki kosztowe i pozwala wywolac platne API, wiec nie
ma powodu, zeby byl widoczny poza ta maszyna. `--host 0.0.0.0` jest mozliwe,
ale trzeba je napisac swiadomie.
"""

from .server import DashboardServer, serve

__all__ = ["DashboardServer", "serve"]
