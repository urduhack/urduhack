# coding: utf8
"""
Normalization Util module
-------------------------------

The util module provides functionality to put proper spaces before and after numeric digits, urdu digits
and punctuations.
"""

import regex as re

from urduhack.urdu_characters import URDU_ALL_CHARACTERS, URDU_PUNCTUATIONS, URDU_DIACRITICS

# Add spaces before|after numeric number and urdu words
# 18سالہ  , 20فیصد
EXCEPT_HAMZA = list(filter(lambda c: c != '\u0621', URDU_ALL_CHARACTERS))
SPACE_BEFORE_DIGITS_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[0-9])",
                                    flags=re.U | re.M | re.I)
SPACE_AFTER_DIGITS_RE = re.compile(r"(?<=[0-9])(?=[" + "".join(EXCEPT_HAMZA) + "])", flags=re.U | re.M | re.I)


def digits_space(text: str) -> str:
    """
    Add spaces before|after numeric and urdu digits

    Args:
        text (str): raw ``urdu`` text

    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    text = SPACE_BEFORE_DIGITS_RE.sub(' ', text)
    text = SPACE_AFTER_DIGITS_RE.sub(' ', text)

    return text


# Add spaces after ., if there is number then not Ex (9.00)
SPACE_AFTER_PUNCTUATIONS_RE = re.compile(
        r"(?<=[" + "".join(URDU_PUNCTUATIONS) + "])(?=[^" + "".join(URDU_PUNCTUATIONS) + "0-9 \n])",
        flags=re.U | re.M | re.I)
REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE = re.compile(r'\s+([' + "".join(URDU_PUNCTUATIONS) + '])',
                                                 flags=re.U | re.M | re.I)


def punctuations_space(text: str) -> str:
    """
    Add spaces after punctuations used in ``urdu`` writing

    Args:
        text (str): raw ``urdu`` text

    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    text = SPACE_AFTER_PUNCTUATIONS_RE.sub(' ', text)
    text = REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE.sub(r'\1', text)
    return text


# Add spaces before|after english characters and urdu words
# ikramسالہ  , abفیصد
SPACE_BEFORE_ENG_CHAR_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[a-zA-Z])",
                                      flags=re.U | re.M | re.I)
SPACE_AFTER_ENG_CHAR_RE = re.compile(r"(?<=[a-zA-Z])(?=[" + "".join(URDU_ALL_CHARACTERS) + "])",
                                     flags=re.U | re.M | re.I)


def english_characters_space(text: str) -> str:
    """
    Add spaces before|after ``english`` characters and ``urdu`` digits

    Args:
        text (str): raw ``urdu`` text

    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    text = SPACE_BEFORE_ENG_CHAR_RE.sub(' ', text)
    text = SPACE_AFTER_ENG_CHAR_RE.sub(' ', text)

    return text


DIACRITICS_RE = re.compile(f'[{"".join(URDU_DIACRITICS)}]', flags=re.U | re.M | re.I)


def remove_diacritics(text: str) -> str:
    """
    Remove ``urdu`` diacritics from text

    Args:
        text (str): raw ``urdu`` text

    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    return DIACRITICS_RE.sub('', text)
