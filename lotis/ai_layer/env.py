"""Zgodnosciowy alias -- prawdziwy modul siedzi w `lotis.kernel.env`.

Przeniesiony, bo adaptery tez konfiguruja sciezki przez `.env`, a nie moga
zalezec od warstwy AI.
"""

from ..kernel.env import (
    DEFAULT_ENV,
    PROJECT_ROOT,
    get,
    get_int,
    load_env,
    parse_env,
    require,
)

__all__ = ["DEFAULT_ENV", "PROJECT_ROOT", "get", "get_int", "load_env", "parse_env", "require"]
