# coding: utf8
"""
Tokenization module
---------------------

The tokenization of Urdu text is necessary to make it useful for the NLP tasks.
This module provides the following functionality:

    - Sentence Tokenization
    - Word Tokenization
"""
from .tokenizer import sentence_tokenizer

__all__ = ["sentence_tokenizer"]
