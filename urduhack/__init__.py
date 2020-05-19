# coding: utf8
"""Project Entry point"""
from .about import __version__
from .normalization import normalize
from .stop_words import STOP_WORDS
from .utils.resources import download

__all__ = ["__version__", "normalize", "STOP_WORDS", "download"]
