# coding: utf8
"""Test Cases for words"""

from urduhack.tokenization.words import WORDS_SPACE
from urduhack.urdu_characters import URDU_ALPHABETS


def test_words():
    """Test Case"""
    for key, value in WORDS_SPACE.items():
        for char in key:
            if char != ' ':
                assert char in URDU_ALPHABETS
        for char in value:
            if char != ' ':
                assert char in URDU_ALPHABETS
