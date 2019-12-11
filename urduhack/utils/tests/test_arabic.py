# coding: utf8
"""text test cases"""

from urduhack.arabic.text import find_arabic_words


def test_find_arabic_words():
    """Text case"""
    text: str = "ﺧﯿﺎﻝ ﻧﯿﮏ ﻣﺴﻌﻮﺩ ﺗﯿﺮﺍ ﻴ ﮐﮭﮍﯼ ﮔﺰﺭ ﻩ ﺩﺭﺧﻮﺍﺳﺖ ﺍﻭﻗﺎﺕ ﺭﮦ ﺭﺍﺣﺖ ﺑﮭﺎﺋﯿﻮﮞ ﺧﻮﺑﺼﻮﺭﺕ ﻣﻌﺘﺮﻑ ﻣﻈﺎﺑﻖ ﭘﻮﺗﻮﮞ"
    assert len(find_arabic_words(text)) == 17
    assert isinstance(find_arabic_words(text), list)
