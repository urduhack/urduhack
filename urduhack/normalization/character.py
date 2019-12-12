# coding: utf8
"""
Character Normalization functions
"""
from typing import Dict

# Issue to be resolved: Words like کیجئے and کیجیے appear in the same context but they have different unicodes.
# We cannot merge them neither can we have them separately. Because if we decompose ئ,
# we get unicode that are not available in our unicode list.

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
