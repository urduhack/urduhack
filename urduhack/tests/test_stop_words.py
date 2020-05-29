# coding: utf8
""" Test cases updated"""

from urduhack.normalization.character import COMBINE_URDU_CHARACTERS
from ..stop_words import STOP_WORDS
from ..urdu_characters import URDU_ALPHABETS


def test_stop_words():
    """ Test case"""
    for word in STOP_WORDS:
        for chars in COMBINE_URDU_CHARACTERS:
            assert len(chars) == 2
            assert chars not in word

        for character in word:
            assert character in URDU_ALPHABETS, F"Incorrect word: {word} and char: {character}"
