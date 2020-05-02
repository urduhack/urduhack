# coding: utf8
"""Text Utils"""

from typing import Tuple

from urduhack.urdu_characters import URDU_ALL_CHARACTERS

_VOCAB_SOURCES = {
    "urdu": "".join(URDU_ALL_CHARACTERS),
    "arabic": "ﷲﷺ",
    "english": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "math": "0123456789",
    "symbol": "<>=+-*&%^$#@!",
    "extra": "",

}


def load_vocab(extra_vocab: str = None) -> Tuple[dict, dict]:
    """
    Complete vocab used by models. Maps characters to integers and vice versa

    Args:
        extra_vocab (str): extra vocab text
    Returns:
        tuple: Two dictionaries containing character to integer mapping and integer to character mapping
    """
    vocab: str = ""
    for value in _VOCAB_SOURCES.values():
        vocab += value

    if extra_vocab is not None and isinstance(extra_vocab, str):
        vocab += extra_vocab

    char2idx, idx2char = {}, {}
    for index, char in enumerate(vocab):
        char2idx[char] = index
        idx2char[index] = char
    return char2idx, idx2char


def get_code_point(char: str) -> str:
    """
    Get Character unicode codepoint

    Args:
        char (str): single character

    Returns:
        str

    """
    return '%04x' % ord(char)
