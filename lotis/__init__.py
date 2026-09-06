"""LOTIS V1 -- Lot Intelligence System.

System wspomagania decyzji dla IROPS. Zasada nadrzedna:
silnik liczy -> prawo blokuje -> AI wyjasnia -> czlowiek decyduje -> log pamieta.

Silnik (`kernel`, `nodes`) uzywa wylacznie biblioteki standardowej.
Zaleznosci zewnetrzne zyja tylko w `adapters`.
"""

from .kernel.versions import ENGINE_VERSION

__all__ = ["ENGINE_VERSION"]
__version__ = ENGINE_VERSION
