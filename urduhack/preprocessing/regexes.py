# coding: utf8
"""List of Regex for preprocess"""

import regex as re

from urduhack.urdu_characters import URDU_ALL_CHARACTERS

# Add spaces before|after numeric number and urdu words
# 18سالہ  , 20فیصد
_EXCEPT_HAMZA = list(filter(lambda c: c != '\u0621', URDU_ALL_CHARACTERS))
_SPACE_BEFORE_DIGITS_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[0-9])", flags=re.U | re.M | re.I)
_SPACE_AFTER_DIGITS_RE = re.compile(r"(?<=[0-9])(?=[" + "".join(_EXCEPT_HAMZA) + "])", flags=re.U | re.M | re.I)

# Add spaces before|after english characters and urdu words
# ikramسالہ  , abفیصد
_SPACE_BEFORE_ENG_CHAR_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[a-zA-Z])",
                                       flags=re.U | re.M | re.I)
_SPACE_AFTER_ENG_CHAR_RE = re.compile(r"(?<=[a-zA-Z])(?=[" + "".join(URDU_ALL_CHARACTERS) + "])",
                                      flags=re.U | re.M | re.I)
