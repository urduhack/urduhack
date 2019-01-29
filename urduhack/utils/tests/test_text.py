# coding: utf8
"""Test cases for text.py file"""

from urduhack.urdu_characters import URDU_DIACRITICS, URDU_ALPHABETS
from ..text import remove_diacritics


def test_remove_diacritics():
    """remove_diacritics Test case"""
    words: dict = {"اب": "اَب",
                   "شیر پنجاب": "شیرِ پنجاب",
                   "اوگول": "اُوگول",
                   "ای": "اِی",
                   "اباوگل": "اَباُوگل",
                   "شرپن": "شرِپن",
                   "ااایول": "اَاُاِیول",
                   "اے": "اَے",
                   "اوشیر": "اُوشیر",
                   "او": "اَو",
                   }

    for key, val in words.items():
        norm = remove_diacritics(val)
        assert key == norm
        for char in norm:
            assert char not in URDU_DIACRITICS, norm

            if char != ' ':
                assert char in URDU_ALPHABETS, norm
