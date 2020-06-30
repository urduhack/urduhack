# coding: utf8
"""
Urduhack Character preprocess functions
"""

from .regexes import _SPACE_AFTER_DIGITS_RE, _SPACE_BEFORE_DIGITS_RE


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
