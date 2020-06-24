# coding: utf8
"""List of Regex"""

import regex as re

from urduhack.urdu_characters import URDU_ALL_CHARACTERS

# Add spaces before|after numeric number and urdu words
# 18سالہ  , 20فیصد
_EXCEPT_HAMZA = list(filter(lambda c: c != '\u0621', URDU_ALL_CHARACTERS))
_SPACE_BEFORE_DIGITS_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[0-9])", flags=re.U | re.M | re.I)
_SPACE_AFTER_DIGITS_RE = re.compile(r"(?<=[0-9])(?=[" + "".join(_EXCEPT_HAMZA) + "])", flags=re.U | re.M | re.I)
