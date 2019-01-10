# coding: utf8
"""test case"""
from urduhack.normalization.space.util import digits_space
from urduhack.normalization.space.words import WORDS_SPACE
from urduhack.urdu_characters import URDU_ALL_CHARACTERS


def test_digits_space():
    """Test cases"""
    data = {"20فیصد": "20 فیصد",
            "18سالہ": "18 سالہ",
            "سالہ18": "سالہ 18",
            " 44 سالہ20فیصد30": " 44 سالہ 20 فیصد 30",
            }
    for key, value in data.items():
        assert value == digits_space(key)


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


def test_punctuations_space():
    """Test cases"""
