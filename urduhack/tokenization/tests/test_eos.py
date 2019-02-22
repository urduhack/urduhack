# coding: utf8
"""test case"""
from urduhack.urdu_characters import URDU_ALPHABETS, URDU_ALL_CHARACTERS

from ..eos import URDU_CONJUNCTIONS, URDU_NEWLINE_WORDS
from ..words import WORDS_SPACE


def test_conjunctions_newline_words():
    """Test case"""
    for word in URDU_CONJUNCTIONS:
        for char in word:
            assert char in URDU_ALPHABETS

    for word in URDU_NEWLINE_WORDS:
        for char in word:
            assert char in URDU_ALPHABETS


def test_words_space():
    """Test case"""
    for key, value in WORDS_SPACE.items():
        for char in key:
            if char == ' ':
                continue
            assert char in URDU_ALL_CHARACTERS
        for char in value:
            if char == ' ':
                continue
            assert char in URDU_ALL_CHARACTERS
