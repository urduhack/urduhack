# coding: utf8
"""test case"""
from urduhack.urdu_characters import URDU_ALPHABETS

from ..eos import URDU_CONJUNCTIONS, URDU_NEWLINE_WORDS


def test_conjunctions_newline_words():
    """Test case"""
    for word in URDU_CONJUNCTIONS:
        for char in word:
            assert char in URDU_ALPHABETS

    for word in URDU_NEWLINE_WORDS:
        for char in word:
            assert char in URDU_ALPHABETS
