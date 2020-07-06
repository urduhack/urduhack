# coding: utf8
"""Urdu Lemmatizer"""

import json

from urduhack.config import LEMMA_LOOKUP_TABLE_PATH

_WORD2LEMMA = None


def lemma_lookup(text: str, lookup_path: str = LEMMA_LOOKUP_TABLE_PATH) -> list:
    """
    Get lemma of the word from lookup table

    Args:
        text (str): Urdu tokenized text
        lookup_path (str): path to the lookup json file

    Returns:
        list: A list containing tuple of word and its lemma
    """

    tokens = text.split()
    global _WORD2LEMMA
    if _WORD2LEMMA is None:
        with open(lookup_path, "r", encoding="utf-8") as file:
            _WORD2LEMMA = json.load(file)

    return [(word, _WORD2LEMMA[word]) if word in _WORD2LEMMA else (word, word) for word in tokens]
