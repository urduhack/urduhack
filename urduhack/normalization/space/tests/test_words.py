# coding: utf8
"""test case"""
from urduhack.normalization.space.words import digits_space


def test_digits_space():
    """Test cases"""
    data = {"20فیصد": "20 فیصد",
            "18سالہ": "18 سالہ",
            "سالہ18": "سالہ 18",
            " 44 سالہ20فیصد30": " 44 سالہ 20 فیصد 30",
            }
    for key, value in data.items():
        assert value == digits_space(key)


def test_punctuations_space():
    """Test cases"""
