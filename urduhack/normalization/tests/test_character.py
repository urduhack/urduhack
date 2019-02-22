# coding: utf8
"""Test cases for character class"""

from urduhack import normalize
from urduhack.urdu_characters import URDU_ALL_CHARACTERS, URDU_ALPHABETS, URDU_DIGITS

from ..character import normalize_characters, CORRECT_URDU_CHARACTERS, normalize_combine_characters, \
    COMBINE_URDU_CHARACTERS


def test_normalize():
    """ Testing main function"""
    text = "پاکستان ﻤﯿﮟ وسائل کی کوئی کمی نہیں ﮨﮯ۔"
    expected = normalize(text)
    assert isinstance(expected, str)
    for char in expected:
        if char == " ":
            continue
        assert char in URDU_ALL_CHARACTERS


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
                   "ﺭﺍﮦ ﺳﮯ": "راہ سے",
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
                   "ﺍﺭﺍﺩﮦ ﺑﺘﺎﯾﺎ": "ارادہ بتایا",
                   "ﺑﺎﭖ": "باپ",
                   "ﻟﮕﯿﮟ": "لگیں",
                   "ﺷﺨﺺ": "شخص",
                   "ﺭﮨﺘﺎﮨﮯ": "رہتاہے",
                   "ﻗﺪﺭﺕ": "قدرت",
                   "ﻣﺮﺿﯽ": "مرضی",
                   "ﮔﯿﺎﺍﻭﺭ": "گیااور",
                   "ﮐﭽﮫ": "کچھ",
                   "ﻟﮑﮫ": "لکھ",
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
                   "ﮐﮧ ﺭﺍﺳﺘﮯ": "کہ راستے",
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
                   "اشیاﺀ": "اشیاء",
                   "کیلﺌے": "کیلئے",
                   "باعﺚ": "باعث",
                   "كيا خطا": "کیا خطا",
                   "حم مر كر": "حم مر کر",
                   "تم كيا كر": "تم کیا کر",
                   "كن فا يا كن": "کن فا یا کن",
                   "مر كر ﻓﺎﺋﺪﮦ": "مر کر فائدہ",
                   "تم كيا كرو": "تم کیا کرو",
                   "تم کیا کر": "تم کیا کر",
                   "گنہگار مر": "گنہگار مر",
                   "کر موت": "کر موت",
                   "کیا خطا": "کیا خطا",
                   "قريب": "قریب",
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

    for _list in CORRECT_URDU_CHARACTERS.values():
        for char in _list:
            assert char not in URDU_ALL_CHARACTERS

    for key in CORRECT_URDU_CHARACTERS:
        for char in key:
            assert char in URDU_ALL_CHARACTERS


def test_normalize_combine_characters():
    """Test case"""
    words: dict = {
        "آزاد": "آزاد",
        "آپ": "آپ",
        "آدھے": "آدھے",
        "آج": "آج",
        "آرام": "آرام",
        "جرأت": "جرأت",
        "کوجرأت": "کوجرأت",
        "أعظم": "أعظم",
    }
    for key, val in words.items():
        norm = normalize_combine_characters(key)
        assert val == norm
        for char in norm:
            assert char in URDU_ALL_CHARACTERS, norm


def test_combine_urdu_characters():
    """ Test case """
    for chars in COMBINE_URDU_CHARACTERS:
        assert len(chars) == 2
        for char in chars:
            assert char in URDU_ALL_CHARACTERS

    for char in COMBINE_URDU_CHARACTERS.values():
        assert len(char) == 1
        assert char in URDU_ALL_CHARACTERS
        assert char in CORRECT_URDU_CHARACTERS

    for key, value in COMBINE_URDU_CHARACTERS.items():
        assert len(key) == 2
        assert len(value) == 1
