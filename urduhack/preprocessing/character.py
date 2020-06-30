# coding: utf8
"""
Urduhack Character preprocess functions
"""

from .regexes import _SPACE_AFTER_ALL_PUNCTUATIONS_RE, _SPACE_BEFORE_ALL_PUNCTUATIONS_RE
from .regexes import _SPACE_AFTER_DIGITS_RE, _SPACE_BEFORE_DIGITS_RE
from .regexes import _SPACE_BEFORE_ENG_CHAR_RE, _SPACE_AFTER_ENG_CHAR_RE


def digits_space(text: str) -> str:
    """
    Add spaces before|after numeric and urdu digits

    Args:
        text (str): ``Urdu`` text
    Returns:
        str: Returns a ``str`` object containing normalized text.
    Examples:
        >>> from urduhack.preprocessing import digits_space
        >>> text = "20فیصد"
        >>> normalized_text = digits_space(text)
        >>> normalized_text
        20 فیصد
    """
    text = _SPACE_BEFORE_DIGITS_RE.sub(' ', text)
    text = _SPACE_AFTER_DIGITS_RE.sub(' ', text)

    return text


def english_characters_space(text: str) -> str:
    """
    Functionality to add spaces before and after English words in the given Urdu text. It is an important step in
    normalization of the Urdu data.

    this function returns a :py:class:`String` object which contains the original text with spaces before & after
    English words.

    Args:
        text (str): ``Urdu`` text
    Returns:
        str: Returns a ``str`` object containing normalized text.
    Examples:
        >>> from urduhack.preprocessing import english_characters_space
        >>> text = "خاتون Aliyaنے بچوںUzma and Aliyaکے قتل کا اعترافConfession کیا ہے۔"
        >>> normalized_text = english_characters_space(text)
        >>> normalized_text
        خاتون Aliya نے بچوں Uzma and Aliya کے قتل کا اعتراف Confession کیا ہے۔
    """
    text = _SPACE_BEFORE_ENG_CHAR_RE.sub(' ', text)
    text = _SPACE_AFTER_ENG_CHAR_RE.sub(' ', text)

    return text


def all_punctuations_space(text: str) -> str:
    """
    Add spaces after punctuations used in ``urdu`` writing

    Args:
        text (str): ``Urdu`` text
    Returns:
        str: Returns a ``str`` object containing normalized text.
    """
    text = _SPACE_BEFORE_ALL_PUNCTUATIONS_RE.sub(' ', text)
    text = _SPACE_AFTER_ALL_PUNCTUATIONS_RE.sub(' ', text)
    return text
