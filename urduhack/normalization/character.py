# coding: utf8
"""
Character Normalization functions
provides functionality to put proper spaces before and after numeric digits, urdu digits
and punctuations.
"""
from typing import Dict

import regex as re

from urduhack.urdu_characters import URDU_ALL_CHARACTERS, URDU_PUNCTUATIONS, URDU_DIACRITICS

# Contains wrong Urdu characters mapping to correct characters
CORRECT_URDU_CHARACTERS: Dict = {'آ': ['ﺁ', 'ﺂ'],
                                 'أ': ['ﺃ'],
                                 'ا': ['ﺍ', 'ﺎ', ],
                                 'ب': ['ﺏ', 'ﺐ', 'ﺑ', 'ﺒ'],
                                 'پ': ['ﭖ', 'ﭘ', 'ﭙ', ],
                                 'ت': ['ﺕ', 'ﺖ', 'ﺗ', 'ﺘ'],
                                 'ٹ': ['ﭦ', 'ﭧ', 'ﭨ', 'ﭩ'],
                                 'ث': ['ﺛ', 'ﺜ', 'ﺚ'],
                                 'ج': ['ﺝ', 'ﺞ', 'ﺟ', 'ﺠ'],
                                 'ح': ['ﺡ', 'ﺣ', 'ﺤ', 'ﺢ'],
                                 'خ': ['ﺧ', 'ﺨ', 'ﺦ'],
                                 'د': ['ﺩ', 'ﺪ'],
                                 'ذ': ['ﺬ', 'ﺫ'],
                                 'ر': ['ﺭ', 'ﺮ'],
                                 'ز': ['ﺯ', 'ﺰ', ],
                                 'س': ['ﺱ', 'ﺲ', 'ﺳ', 'ﺴ', ],
                                 'ش': ['ﺵ', 'ﺶ', 'ﺷ', 'ﺸ'],
                                 'ص': ['ﺹ', 'ﺺ', 'ﺻ', 'ﺼ', ],
                                 'ض': ['ﺽ', 'ﺾ', 'ﺿ', 'ﻀ'],
                                 'ط': ['ﻃ', 'ﻄ'],
                                 'ظ': ['ﻅ', 'ﻇ', 'ﻈ'],
                                 'ع': ['ﻉ', 'ﻊ', 'ﻋ', 'ﻌ', ],
                                 'غ': ['ﻍ', 'ﻏ', 'ﻐ', ],
                                 'ف': ['ﻑ', 'ﻒ', 'ﻓ', 'ﻔ', ],
                                 'ق': ['ﻕ', 'ﻖ', 'ﻗ', 'ﻘ', ],
                                 'ل': ['ﻝ', 'ﻞ', 'ﻟ', 'ﻠ', ],
                                 'م': ['ﻡ', 'ﻢ', 'ﻣ', 'ﻤ', ],
                                 'ن': ['ﻥ', 'ﻦ', 'ﻧ', 'ﻨ', ],
                                 'چ': ['ﭺ', 'ﭻ', 'ﭼ', 'ﭽ'],
                                 'ڈ': ['ﮈ', 'ﮉ'],
                                 'ڑ': ['ﮍ', 'ﮌ'],
                                 'ژ': ['ﮋ', ],
                                 'ک': ['ﮎ', 'ﮏ', 'ﮐ', 'ﮑ', 'ﻛ', 'ك'],
                                 'گ': ['ﮒ', 'ﮓ', 'ﮔ', 'ﮕ'],
                                 'ں': ['ﮞ', 'ﮟ'],
                                 'و': ['ﻮ', 'ﻭ', 'ﻮ', ],
                                 'ؤ': ['ﺅ'],
                                 'ھ': ['ﮪ', 'ﮬ', 'ﮭ', 'ﻬ', 'ﻫ', 'ﮫ'],
                                 'ہ': ['ﻩ', 'ﮦ', 'ﻪ', 'ﮧ', 'ﮩ', 'ﮨ', 'ه', ],
                                 'ۂ': [],
                                 'ۃ': ['ة'],
                                 'ء': ['ﺀ'],
                                 'ی': ['ﯼ', 'ى', 'ﯽ', 'ﻰ', 'ﻱ', 'ﻲ', 'ﯾ', 'ﯿ', 'ي'],
                                 'ئ': ['ﺋ', 'ﺌ', ],
                                 'ے': ['ﮮ', 'ﮯ', 'ﻳ', 'ﻴ', ],
                                 'ۓ': [],
                                 '۰': ['٠'],
                                 '۱': ['١'],
                                 '۲': ['٢'],
                                 '۳': ['٣'],
                                 '۴': ['٤'],
                                 '۵': ['٥'],
                                 '۶': ['٦'],
                                 '۷': ['٧'],
                                 '۸': ['٨'],
                                 '۹': ['٩'],
                                 '۔': [],
                                 '؟': [],
                                 '٫': [],
                                 '،': [],
                                 'لا': ['ﻻ', 'ﻼ'],
                                 '': ['ـ']

                                 }

_TRANSLATOR = {}
for key, value in CORRECT_URDU_CHARACTERS.items():
    _TRANSLATOR.update(dict.fromkeys(map(ord, value), key))


def normalize_characters(text: str) -> str:
    """
    The most important function in the UrduHack normalize_characters. You can use this function separately to normalize
    a piece of text to a proper specified Urdu range (0600-06FF). This provides the functionality
    to replace wrong arabic characters with correct urdu characters and fixed the combine|join characters issue.

    Replace ``urdu`` text characters with correct ``unicode`` characters.

    Args:
        text (str): raw ``urdu`` text
    Returns:
        str: returns a ``str`` object containing normalized text.
    Examples:
        >>> from urduhack.normalization import normalize_characters
        >>> text = normalize_characters("پاکستان ﻤﯿﮟ وسائل کی کوئی کمی نہیں ﮨﮯ۔")
        پاکستان ﻤﯿﮟ وسائل کی کوئی کمی نہیں ﮨﮯ۔
    """
    return text.translate(_TRANSLATOR)


COMBINE_URDU_CHARACTERS: Dict[str, str] = {"آ": "آ",
                                           "أ": "أ",
                                           "ۓ": "ۓ",
                                           }


def normalize_combine_characters(text: str) -> str:
    """
    Replace combine|join ``urdu`` characters with single unicode character

    Args:
        text (str): raw ``urdu`` text
    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    for _key, _value in COMBINE_URDU_CHARACTERS.items():
        text = text.replace(_key, _value)
    return text


# Add spaces before|after numeric number and urdu words
# 18سالہ  , 20فیصد
_EXCEPT_HAMZA = list(filter(lambda c: c != '\u0621', URDU_ALL_CHARACTERS))
_SPACE_BEFORE_DIGITS_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[0-9])",
                                     flags=re.U | re.M | re.I)
_SPACE_AFTER_DIGITS_RE = re.compile(r"(?<=[0-9])(?=[" + "".join(_EXCEPT_HAMZA) + "])", flags=re.U | re.M | re.I)


# Issue to be resolved: Words like کیجئے and کیجیے appear in the same context but they have different unicodes.
# We cannot merge them neither can we have them separately. Because if we decompose ئ,
# we get unicode that are not available in our unicode list.

def digits_space(text: str) -> str:
    """
    Add spaces before|after numeric and urdu digits

    Args:
        text (str): raw ``urdu`` text
    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    text = _SPACE_BEFORE_DIGITS_RE.sub(' ', text)
    text = _SPACE_AFTER_DIGITS_RE.sub(' ', text)

    return text


# Add spaces after ., if there is number then not Ex (9.00)
_SPACE_AFTER_PUNCTUATIONS_RE = re.compile(
    r"(?<=[" + "".join(URDU_PUNCTUATIONS) + "])(?=[^" + "".join(URDU_PUNCTUATIONS) + "0-9 \n])",
    flags=re.U | re.M | re.I)
_REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE = re.compile(r'\s+([' + "".join(URDU_PUNCTUATIONS) + '])',
                                                  flags=re.U | re.M | re.I)


def punctuations_space(text: str) -> str:
    """
    Add spaces after punctuations used in ``urdu`` writing

    Args:
        text (str): raw ``urdu`` text
    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    text = _SPACE_AFTER_PUNCTUATIONS_RE.sub(' ', text)
    text = _REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE.sub(r'\1', text)
    return text


# Add spaces before|after english characters and urdu words
# ikramسالہ  , abفیصد
_SPACE_BEFORE_ENG_CHAR_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[a-zA-Z])",
                                       flags=re.U | re.M | re.I)
_SPACE_AFTER_ENG_CHAR_RE = re.compile(r"(?<=[a-zA-Z])(?=[" + "".join(URDU_ALL_CHARACTERS) + "])",
                                      flags=re.U | re.M | re.I)


def english_characters_space(text: str) -> str:
    """
    Add spaces before|after ``english`` characters and ``urdu`` digits

    Args:
        text (str): raw ``urdu`` text
    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    text = _SPACE_BEFORE_ENG_CHAR_RE.sub(' ', text)
    text = _SPACE_AFTER_ENG_CHAR_RE.sub(' ', text)

    return text


_DIACRITICS_RE = re.compile(f'[{"".join(URDU_DIACRITICS)}]', flags=re.U | re.M | re.I)


def remove_diacritics(text: str) -> str:
    """
    Remove ``urdu`` diacritics from text

    Args:
        text (str): raw ``urdu`` text
    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    return _DIACRITICS_RE.sub('', text)


def normalize(text: str) -> str:
    """
    To normalize some text, all you need to do pass ``unicode`` text. It will return a ``str``
    with normalized characters both single and combined, proper spaces after digits and punctuations
    and diacritics removed.

    Args:
        text (str): raw ``unicode`` Urdu text

    Returns:
        str: normalized urdu text
    """
    text = normalize_characters(text)
    text = normalize_combine_characters(text)
    text = digits_space(text)
    text = punctuations_space(text)
    text = remove_diacritics(text)
    text = english_characters_space(text)
    return text


ENG_URDU_DIGITS_MAP: Dict = {
    '0': ['۰'],
    '1': ['۱'],
    '2': ['۲'],
    '3': ['۳'],
    '4': ['۴'],
    '5': ['۵'],
    '6': ['۶'],
    '7': ['۷'],
    '8': ['۸'],
    '9': ['۹']
}

_ENG_DIGITS_TRANSLATOR = {}
for key, value in ENG_URDU_DIGITS_MAP.items():
    _ENG_DIGITS_TRANSLATOR.update(dict.fromkeys(map(ord, value), key))

URDU_ENG_DIGITS_MAP: Dict = {
    '۰': ['0'],
    '۱': ['1'],
    '۲': ['2'],
    '۳': ['3'],
    '۴': ['4'],
    '۵': ['5'],
    '۶': ['6'],
    '۷': ['7'],
    '۸': ['8'],
    '۹': ['9']
}

_URDU_DIGITS_TRANSLATOR = {}
for key, value in URDU_ENG_DIGITS_MAP.items():
    _URDU_DIGITS_TRANSLATOR.update(dict.fromkeys(map(ord, value), key))


def replace_digits(text: str, with_eng: bool = True) -> str:
    """
    Replace urdu digits with English digits and vice versa

    Args:
        text (str): urdu text string
        with_eng (bool): Boolean to convert digits from one language to other
    Returns:
        Text string with replaced digits
    """
    if with_eng:
        return text.translate(_ENG_DIGITS_TRANSLATOR)
    return text.translate(_URDU_DIGITS_TRANSLATOR)
