# coding: utf8
"""
Sentence and Word Tokenization module
-------------------------------------
This module is another crucial part of the Urduhack. This module performs tokenization on sentence. It separates
different sentence from each other and converts each string into a complete **sentence token**. Note here you must not
confuse yourself with the word token. They are two completely different things.

The tokenization of Urdu text is necessary to make it useful for the NLP tasks.
This module provides the following functionality:

    - Sentence Tokenization
    - Word Tokenization
"""
from .tokenizer import sentence_tokenizer, word_tokenizer

__all__ = ["sentence_tokenizer", "word_tokenizer"]
