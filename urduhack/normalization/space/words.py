# coding: utf8
"""Add words level space fixes"""
import regex as re

# Add spaces before|after numeric number and urdu words
# 18سالہ  , 20فیصد
SPACE_BEFORE_DIGITS_RE = re.compile(r"(?<=[\u0600-\u06ff])(?=[0-9])", flags=re.U | re.M | re.I)
SPACE_AFTER_DIGITS_RE = re.compile(r"(?<=[0-9])(?=[\u0600-\u06ff])", flags=re.U | re.M | re.I)
# Add spaces after ., if there is number then not Ex (9.00)
PUNCTUATIONS_AFTER_DIGITS_RE = re.compile(r"(?<=[۔،])(?=[^\s0-9۔،])", flags=re.U | re.M | re.I)


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
    return PUNCTUATIONS_AFTER_DIGITS_RE.sub(' ', text)
