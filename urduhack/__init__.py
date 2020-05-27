# coding: utf8
"""Project Entry point"""
from .about import __version__, get_info
from .normalization import normalize
from .stop_words import STOP_WORDS
from .utils.resources import download

__all__ = ["__version__", "get_info", "normalize", "STOP_WORDS", "download"]
