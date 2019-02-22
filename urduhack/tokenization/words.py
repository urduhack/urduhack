# coding: utf8
"""Fix join words"""

from typing import Dict

WORDS_SPACE: Dict[str, str] = {"کردیا": "کر دیا",
                               "کردی": "کر دی",
                               "ہوگیا": "ہو گیا",
                               "کرگئے": "کر گئے",
                               "جاسکتے": "جا سکتے",
                               "کرلیا": "کر لیا",
                               "ہوچکا": "ہو چکا",
                               "کرادی": "کرا دی",
                               "ہوگئی": "ہو گئی",
                               "جارہا": "جا رہا",
                               "ہوجاتے": "ہو جاتے",
                               "ہوچکی": "ہو چکی",
                               "اڑادیا": "اڑا دیا",
                               "کردیئے": "کر دیئے",
                               "ہوگئے": "ہو گئے",
                               "ہوجائے": "ہو جائے",
                               "کردیے": "کر دیے",
                               "کرسکیں": "کر سکیں",
                               "بتایاہے": "بتایا ہے",
                               "رہاہے": "رہا ہے",
                               "ہےکہ": "ہے کہ",
                               "بالاترہے": "بالاتر ہے",
                               "کہاہے": "کہا ہے",
                               "جاتاہے": "جاتا ہے",
                               "بلایاہے": "بلایا ہے",
                               "جارہاہے": "جا رہا ہے",
                               "دیاہے": "دیا ہے",
                               "کررہے": "کر رہے",
                               "ہوگا": "ہو گا",
                               "کیاتھا": "کیا تھا",
                               "کرلی۔": "کر لی۔",
                               "کیاگیا": "کیا گیا",
                               "گیاتھا": "گیا تھا",
                               "کےلئے": "کے لئے",
                               "کےلئے۔": "کے لئے۔",
                               "لگادیا": "لگا دیا",
                               "ہوجانا": "ہو جانا",
                               "گا۔انہوں": "گا۔ انہوں",
                               "کردئیے": "کر دئیے",
                               "کیاجائے": "کیا جائے",
                               "آرہا": "آ رہا",
                               "دیاگیا": "دیا گیا",
                               "ہے۔آپ": "ہے۔ آپ",
                               "کاکہناہے": "کا کہنا ہے",
                               "ہے۔لیکن": "ہے۔ لیکن",
                               "بتایاگیا": "بتایا گیا",
                               "ہے۔ایسے": "ہے۔ ایسے",
                               "ہے۔ترجمان": "ہے۔ ترجمان",
                               "دیکھاجاسکتاہے": "دیکھا جا سکتا ہے",
                               "کامقدمہ": "کا مقدمہ",
                               "نظرآنے": "نظر آنے",
                               "گی۔فلم": "گی۔ فلم",
                               "بوگی": "بو گی",
                               "چھوڑدیں": "چھوڑ دیں",
                               "گا۔ماہرین": "گا۔ ماہرین",
                               "بتاسکتی": "بتا سکتی",
                               "ہے۔بہت": "ہے۔ بہت",
                               "تھے۔جب": "تھے۔ جب",
                               "ہیں۔شاہ": "ہیں۔ شاہ",
                               "گیا۔محکمہ": "گیا۔ محکمہ",
                               "تھے۔لیکن": "تھے۔ لیکن",
                               "تھی۔ذرائع": "تھی۔ ذرائع",
                               "کرلیں۔اس": "کرلیں۔ اس",
                               "ہواہے۔": "ہوا ہے۔",
                               "کرارہے": "کرا رہے",
                               "ہے۔کئی": "ہے۔ کئی",
                               "کرناہو": "کرنا ہو",
                               "کرسکتے": "کر سکتے",
                               "جارہی": "جا رہی",
                               "کہناتھا": "کہنا تھا",
                               "کےلیے": "کے لیے",
                               "کاکہناتھاکہ": "کا کہنا تھا کہ",
                               "جاکر": "جا کر",
                               "کیاہے": "کیا ہے",
                               "کودیا": "کو دیا",
                               "توحکومت": "تو حکومت",
                               "کومعاف": "کو معاف",
                               "کوخبردارکیا": "کو خبردار کیا",
                               "کوجانے": "کو جانے",
                               "کواپنے": "کو اپنے",
                               "اگرکوئی": "اگر کوئی",
                               "کوپھانسی": "کو پھانسی",
                               "کواستعمال": "کو استعمال",
                               "ہےجب": "ہے جب",
                               "رکھاگیا": "رکھا گیا",
                               "دکھایاگیا": "دکھایا گیا",
                               "کےنتیجے": "کے نتیجے",
                               "کیاجاسکتا": "کیا جا سکتا",
                               "تھاکہ": "تھا کہ",
                               "کہاکہ": "کہا کہ",
                               "کےبعد": "کے بعد",
                               "کرکے": "کر کے",
                               "گیاہے": "گیا ہے",
                               "کررہا": "کر رہا",
                               "کاکہنا": "کا کہنا",
                               "ہوتاہے": "ہوتا ہے",
                               "گئےہیں": "گئے ہیں",
                               "آگئے": "آ گئے",
                               "ہوجاتی": "ہو جاتی",
                               "جاسکتا": "جا سکتا",
                               "کرناہے": "کرنا ہے",
                               }


def fix_join_words(text: str) -> str:
    """
    Replace all join ``urdu`` words with separate words

    Args:
        text (str): raw ``urdu`` text

    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    for key, value in WORDS_SPACE.items():
        text = text.replace(key, value)

    return text
