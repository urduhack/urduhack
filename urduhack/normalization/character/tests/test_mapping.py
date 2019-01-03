# coding: utf8
"""Test cases for mapping"""

from urduhack.normalization.character.mapping import normalize_characters, CORRECT_URDU_CHARACTERS
from urduhack.urdu_characters import URDU_ALL_CHARACTERS, URDU_ALPHABETS, URDU_DIGITS


def test_normalize_characters():
    """Normalize characters Test case arabic words : Urdu words"""
    words: dict = {"ﻣﯿﺎﮞ": "میاں",
                   "ﺗﮭﺎ": "تھا",
                   "ﻧﮩﯽ": "نہی",
                   "ﺩﺭﺑﺎﻥ": "دربان",
                   "ﺷﺮﯾﮏ": "شریک",
                   "ﻭﺯﯾﺮ": "وزیر",
                   "ﮐﻮﻧﮯ": "کونے",
                   "ﺭﺍﺿﯽ": "راضی",
                   "ﻣﺠﮭ": "مجھ",
                   "ﭼﮭﭙﺮ": "چھپر",
                   "ﻧﻮﺟﻮﺍﻥ": "نوجوان",
                   "ﻣﻨﺰﻝ": "منزل",
                   "ﻟﮕﺎﺗﮯ": "لگاتے",
                   "ﺟﻮﻧﻌﻤﺖ": "جونعمت",
                   "ﻣﺴﻨﺪﻭﮞ": "مسندوں",
                   "ﭘﺎﮎ": "پاک",
                   "ﻋﺎﻓﯿﺖ": "عافیت",
                   "ﺑﺬﺍﺕ": "بذات",
                   "ﻧﮑﻠﻮ": "نکلو",
                   "ﭘﯿﺪﺍ": "پیدا",
                   "ﺗﻮﮌﺍ": "توڑا",
                   "ﮔﯿﺎ": "گیا",
                   "ﺧﯿﺮ": "خیر",
                   "ﺑﻌﺪ": "بعد",
                   "ﭼﺮﺑﯽ": "چربی",
                   "ﺧﺎﻣﻮﺷﯽ": "خاموشی",
                   "ﮨﭩﮯ": "ہٹے",
                   "ﺍﻭﻻﺩ": "اولاد",
                   "ﺩﯾﻨﯽ": "دینی",
                   "ﭼﺎﮨﮯ": "چاہے",
                   "ﮐﮩﺎ": "کہا",
                   "ﺧﺎﻟﯽ": "خالی",
                   "ﻣﺎﻧﮕﯿﮟ": "مانگیں",
                   "ﺭﮨﺘﮯ": "رہتے",
                   "ﻣﻔﻠﺴﯽ": "مفلسی",
                   "ﺩﺭﺑﺎﺭﯼ": "درباری",
                   "ﺑﺘﺎﺋﯿﮟ": "بتائیں",
                   "ﮨﻤﺖ": "ہمت",
                   "ﻣﺮﺩ": "مرد",
                   "ﺩﻭﺳﺖ": "دوست",
                   "ﻋﺎﺷﻘﻮ": "عاشقو",
                   "ﺟﻠﻮﮦ": "جلوہ",
                   "ﺭﮨﺘﺎ": "رہتا",
                   "ﮈﺍﮐﭩﺮ": "ڈاکٹر",
                   "ﺭﻫﺘﯽ": "رھتی",
                   "ﺍﯾﺴﮯ": "ایسے",
                   "ﺻﺎﻑ": "صاف",
                   "ﺗﻌﻠﯿﻢ": "تعلیم",
                   "ﺁﭘﮑﺎ": "آپکا",
                   "ﻣﺮﺩﺍﻥ": "مردان",
                   "ﺣﺮﺍﻣﯽ": "حرامی",
                   "ﻧﮑ": "نک",
                   "ﺯﯾﺎﺩﮦ": "زیادہ",
                   "ﻧﻮﺟﻮﻥ": "نوجون",
                   "ﺧﺎﻧﮯ": "خانے",
                   "ﺭﺍﮦﺳﮯ": "راہسے",
                   "ﻣﺤﺘﺮﻣﮧ": "محترمہ",
                   "ﺟﺎﻧﻮﺭ": "جانور",
                   "ﻧﮯﺍﯾﮏ": "نےایک",
                   "ﻣﺤﺒﻮﺏ": "محبوب",
                   "ﺧﻮﺵ": "خوش",
                   "ﺳﺎﺋﻞ": "سائل",
                   "ﮐﺮ": "کر",
                   "ﮐﮩﺎﮐﮧ": "کہاکہ",
                   "ﻧﺴﻮﺍﻧﯽ": "نسوانی",
                   "ﮨﻤﯿﮟ ﺑﻬﯽ": "ہمیں بھی",
                   "ﺍﺭﺍﺩﮦﺑﺘﺎﯾﺎ": "ارادہبتایا",
                   "ﺑﺎﭖ": "باپ",
                   "ﻟﮕﯿﮟ": "لگیں",
                   "ﺷﺨﺺ": "شخص",
                   "ﺭﮨﺘﺎﮨﮯ": "رہتاہے",
                   "ﻗﺪﺭﺕ": "قدرت",
                   "ﻣﺮﺿﯽ": "مرضی",
                   "ﮔﯿﺎﺍﻭﺭ": "گیااور",
                   "ﮐﭽﮫ": "کچہ",
                   "ﻟﮑﮫ": "لکہ",
                   "ﺍﻋﻈﻢ": "اعظم",
                   "ﺷﺨﺼﯿﺖ": "شخصیت",
                   "ﺧﻼﻑ": "خلاف",
                   "ﻏﯿﺮ": "غیر",
                   "ﺳﻮﺩ": "سود",
                   "ﺑﮩﺘﺮ": "بہتر",
                   "ﻫﻮﺋﮯ": "ھوئے",
                   "ﺳﻼﻣﺖ": "سلامت",
                   "ﺭﺍﺑﻄﮧ": "رابطہ",
                   "ﮨﻮﮔﯽ": "ہوگی",
                   "ﻣﺮﺽ": "مرض",
                   "ﺳﻔﺮ": "سفر",
                   "ﻣﻔﺴﺮ": "مفسر",
                   "ﻧﺼﻒ": "نصف",
                   "ﮨﻮﮞ ﺟﺲ": "ہوں جس",
                   "ﭘﯿﭙﺮﺯ": "پیپرز",
                   "ﺑﻦ": "بن",
                   "ﮔﻨﮩﮕﺎﺭ": "گنہگار",
                   "ﺭﮨﯽ": "رہی",
                   "ﻣ": "م",
                   "ﺧﺎﻭﻧﺪ": "خاوند",
                   "ﺩﮐﮭﺎﺗﺎ": "دکھاتا",
                   "ﺟﺎﺳﮑﺘﮯ": "جاسکتے",
                   "ﺣﻞ": "حل",
                   "ﺗﺠﺮﺑﮧ": "تجربہ",
                   "ﮨﺎﺭﻧﮯ": "ہارنے",
                   "ﺳﺠﺎ": "سجا",
                   "ﺭﻭﻧﻖ": "رونق",
                   "ﺑﻨﻮﮞ": "بنوں",
                   "ﺳﮑﺘﯽ": "سکتی",
                   "ﮐﮧﺭﺍﺳﺘﮯ": "کہراستے",
                   "ﻭﺍﻟﯽ": "والی",
                   "ﺣﻔﺎﻇﺖ": "حفاظت",
                   "ﺳﯿﺪﮬﺎ": "سیدھا",
                   "ﺍﻭﻧﭩﻨﯽ": "اونٹنی",
                   "ﺟﺎﻧﮯ": "جانے",
                   "ﺑﻼﯾﺎ": "بلایا",
                   "ﻓﺎﺋﺪﮦ": "فائدہ",
                   "ﮔﺎﺋﮯ": "گائے",
                   "ﻻﮨﻮﺭ": "لاہور",
                   "ﺑﭩﮭﺎﺅﮞ": "بٹھاؤں",
                   }

    for key, val in words.items():
        norm = normalize_characters(key)
        assert val == norm
        for char in norm:
            if char == " ":
                continue
            if len(char) == 1:
                assert char in URDU_ALL_CHARACTERS, norm
            else:
                for inner_char in char:
                    assert inner_char in URDU_ALL_CHARACTERS


def test_correct_urdu_characters():
    """ Test case """
    for char in URDU_ALPHABETS:
        assert char in CORRECT_URDU_CHARACTERS

    for char in URDU_DIGITS:
        assert char in CORRECT_URDU_CHARACTERS
