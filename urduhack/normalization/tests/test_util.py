# coding: utf8
"""test case"""
from urduhack.normalization.util import WORDS_SPACE
from urduhack.urdu_characters import URDU_ALL_CHARACTERS, URDU_DIACRITICS, URDU_ALPHABETS
from .. import digits_space, punctuations_space, remove_diacritics


def test_digits_space():
    """Test cases"""
    data = {"20فیصد": "20 فیصد",
            "18سالہ": "18 سالہ",
            "18.30سالہ": "18.30 سالہ",
            "سالہ18": "سالہ 18",
            "سالہ30.18": "سالہ 30.18",
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
    data = {"ہوتا۔ انہوں": "ہوتا۔ انہوں",
            "ہوتا،انہوں": "ہوتا، انہوں",
            "۔۔۔۔۔۔۔۔۔": "۔۔۔۔۔۔۔۔۔",
            "۔۔۔۔،،۔۔۔۔۔": "۔۔۔۔،،۔۔۔۔۔",
            "ہوتا ہے ۔ ٹائپ": "ہوتا ہے۔ ٹائپ",
            "ہوتا ہے ۔ٹائپ": "ہوتا ہے۔ ٹائپ",
            "ہوتا ہے؟ٹائپ": "ہوتا ہے؟ ٹائپ",
            "ہوتا ہے،ٹائپ": "ہوتا ہے، ٹائپ",
            "ہوتا ہے ؟ٹائپ": "ہوتا ہے؟ ٹائپ",
            "ہوتا ہے   ؟  ٹائپ": "ہوتا ہے؟  ٹائپ",

            "ہوتا ہے۔ٹائپ": "ہوتا ہے۔ ٹائپ",
            "ہوتا ہے   ۔  ٹائپ": "ہوتا ہے۔  ٹائپ",
            "ہوتا ہے   ،  ٹائپ": "ہوتا ہے،  ٹائپ",
            "ہوتا ہے،\n": "ہوتا ہے،\n",

            }
    for key, value in data.items():
        assert value == punctuations_space(key)


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
