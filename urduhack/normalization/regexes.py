# coding: utf8
"""List of Regex"""

import string

import regex as re

from urduhack.urdu_characters import URDU_ALL_CHARACTERS, URDU_PUNCTUATIONS, URDU_DIACRITICS

# Moved into preprocessing module
# Add spaces before|after numeric number and urdu words
# 18سالہ  , 20فیصد
# _EXCEPT_HAMZA = list(filter(lambda c: c != '\u0621', URDU_ALL_CHARACTERS))
# _SPACE_BEFORE_DIGITS_RE=re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[0-9])", flags=re.U | re.M | re.I)
# _SPACE_AFTER_DIGITS_RE = re.compile(r"(?<=[0-9])(?=[" + "".join(_EXCEPT_HAMZA) + "])", flags=re.U | re.M | re.I)

# Add spaces after ., if there is number then not Ex (9.00)
_SPACE_AFTER_PUNCTUATIONS_RE = re.compile(
    r"(?<=[" + "".join(URDU_PUNCTUATIONS) + "])(?=[^" + "".join(URDU_PUNCTUATIONS) + "0-9 \n])",
    flags=re.U | re.M | re.I)
_REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE = re.compile(r'\s+([' + "".join(URDU_PUNCTUATIONS) + '])',
                                                  flags=re.U | re.M | re.I)

# Add spaces before|after english characters and urdu words
# ikramسالہ  , abفیصد
_SPACE_BEFORE_ENG_CHAR_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[a-zA-Z])",
                                       flags=re.U | re.M | re.I)
_SPACE_AFTER_ENG_CHAR_RE = re.compile(r"(?<=[a-zA-Z])(?=[" + "".join(URDU_ALL_CHARACTERS) + "])",
                                      flags=re.U | re.M | re.I)

_DIACRITICS_RE = re.compile(f'[{"".join(URDU_DIACRITICS)}]', flags=re.U | re.M | re.I)

# add space before and after all PUNCTUATIONS
_ALL_PUNCTUATIONS: str = "".join(URDU_PUNCTUATIONS) + "".join(string.punctuation)
_SPACE_BEFORE_ALL_PUNCTUATIONS_RE = re.compile(
    r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[" + "".join(_ALL_PUNCTUATIONS) + "])",
    flags=re.U | re.M | re.I)
_SPACE_AFTER_ALL_PUNCTUATIONS_RE = re.compile(
    r"(?<=[" + "".join(_ALL_PUNCTUATIONS) + "])(?=[^" + "".join(_ALL_PUNCTUATIONS) + "0-9 \n])",
    flags=re.U | re.M | re.I)
