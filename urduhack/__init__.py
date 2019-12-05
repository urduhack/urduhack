# coding: utf8
"""Project Entry point"""
from .about import __version__
from .normalization import normalize
from .tokenization.tokenizer import download_keras_weights, keras_tokenizer_predict

__all__ = ["__version__", "normalize", "download_keras_weights", "keras_tokenizer_predict"]
