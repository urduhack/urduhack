# coding: utf8
"""Vocab utils"""

from urduhack.urdu_characters import URDU_ALL_CHARACTERS

_VOCAB_SOURCES = {
    "urdu": "".join(URDU_ALL_CHARACTERS),
    "arabic": "ﷲﷺ",
    "english": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "digits": "0123456789",
    "symbol": r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~",
    "extra": "",
}


def get_char_vocab() -> set:
    """
    Complete vocab used by models. Maps characters to integers and vice versa

    Returns:
        set: return string of set
    """
    vocab: set = set()
    for value in _VOCAB_SOURCES.values():
        for char in value:
            vocab.add(char)

    return vocab
