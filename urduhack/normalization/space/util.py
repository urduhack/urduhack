# coding: utf8
"""Space utils"""
import regex as re
from urduhack.urdu_characters import URDU_ALL_CHARACTERS, URDU_PUNCTUATIONS

# Add spaces before|after numeric number and urdu words
# 18سالہ  , 20فیصد
SPACE_BEFORE_DIGITS_RE = re.compile(r"(?<=[" + "".join(URDU_ALL_CHARACTERS) + "])(?=[0-9])", flags=re.U | re.M | re.I)
SPACE_AFTER_DIGITS_RE = re.compile(r"(?<=[0-9])(?=[" + "".join(URDU_ALL_CHARACTERS) + "])", flags=re.U | re.M | re.I)
# Add spaces after ., if there is number then not Ex (9.00)
SPACE_AFTER_PUNCTUATIONS_RE = re.compile(
        r"(?<=[" + "".join(URDU_PUNCTUATIONS) + "])(?=[^" + "".join(URDU_PUNCTUATIONS) + "0-9 ])",
        flags=re.U | re.M | re.I)


def digits_space(text: str) -> str:
    """
    Add spaces before|after numeric number and urdu words

    Args:
        text (str): text

    Returns:
        str
    """
    text = SPACE_BEFORE_DIGITS_RE.sub(' ', text)
    text = SPACE_AFTER_DIGITS_RE.sub(' ', text)

    return text


def punctuations_space(text: str) -> str:
    """
    Add spaces after punctuation  and urdu words

    Args:
        text (str): text

    Returns:
        str
    """
    return SPACE_AFTER_PUNCTUATIONS_RE.sub(' ', text)
