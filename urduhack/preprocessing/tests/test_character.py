# coding: utf8
"""Test cases for character class"""

from urduhack.preprocessing.character import digits_space, english_characters_space


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
