# coding: utf8
"""Project Entry point"""
from .about import __version__
from .normalization import normalize
from .stop_words import STOP_WORDS

__all__ = ["__version__", "normalize", "STOP_WORDS"]
