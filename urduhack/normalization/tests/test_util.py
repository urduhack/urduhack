# coding: utf8
"""test case"""
from urduhack.urdu_characters import URDU_DIACRITICS, URDU_ALPHABETS
from .. import digits_space, punctuations_space, remove_diacritics, english_characters_space


def test_english_space():
    """Test cases"""
    data = {
        "سکیورٹی حکام کے مطابق جنوبی صوبےLahj میں رات گئے۔": "سکیورٹی حکام کے مطابق جنوبی صوبے Lahj میں رات گئے۔",
        "اس جوڑے کی دو نوجوان Amna and Aliyaبیٹیاں ہیں۔": "اس جوڑے کی دو نوجوان Amna and Aliya بیٹیاں ہیں۔",
        "جو ان تمام واقعات سے لاعلمIgnorantہیں۔": "جو ان تمام واقعات سے لاعلم Ignorant ہیں۔",
        "خاتون Aliyaنے بچوںUzma and Aliyaکے قتل کا اعترافConfession کیا ہے۔": "خاتون Aliya نے بچوں Uzma and Aliya کے"
                                                                              " قتل کا اعتراف Confession کیا ہے۔",
    }
    for key, value in data.items():
        assert value == english_characters_space(key)


def test_digits_space():
    """Test cases"""
    data = {"20فیصد": "20 فیصد",
            "18سالہ": "18 سالہ",
            "18.30سالہ": "18.30 سالہ",
            "سالہ18": "سالہ 18",
            "سالہ30.18": "سالہ 30.18",
            " 44 سالہ20فیصد30": " 44 سالہ 20 فیصد 30",
            "ان میں 1990ء30": "ان میں 1990ء 30",
            "ان میں 1990ء کے": "ان میں 1990ء کے",
            "ان میں ء1990ء کے": "ان میں ء 1990ء کے",
            }
    for key, value in data.items():
        assert value == digits_space(key)


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
