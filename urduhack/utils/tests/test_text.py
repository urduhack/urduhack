# coding: utf8
"""Test cases for text.py file"""

from urduhack.urdu_characters import URDU_DIACRITICS
from ..text import remove_diacritics


def test_remove_diacritics():
    """remove_diacritics Test case"""
    words: dict = {"اب": "اَب",

                   }

    for key, val in words.items():
        norm = remove_diacritics(key)
        assert val == norm
        for char in norm:
            assert char not in URDU_DIACRITICS, norm
