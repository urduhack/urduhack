# coding: utf8
"""Project Entry point"""
from .about import __version__, get_info
from .conll import CoNLL
from .normalization import normalize
from .pipeline.core import Pipeline
from .stop_words import STOP_WORDS
from .utils.resources import download

__all__ = ["__version__", "get_info", "normalize", "STOP_WORDS", "download", "CoNLL", "Pipeline"]
