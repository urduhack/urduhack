# coding: utf8
"""Normalization module"""
from .character import normalize_characters, normalize_combine_characters
from .util import punctuations_space, digits_space, remove_diacritics

__all__ = ["normalize_characters", "normalize_combine_characters",
           "punctuations_space", "digits_space", "normalize",
           "remove_diacritics"]


def normalize(text: str) -> str:
    """
    Main function to normalize Urdu text.

    Args:
        text (str): base str

    Returns:
        str
    """
    text = normalize_characters(text)
    text = normalize_combine_characters(text)
    text = digits_space(text)
    text = punctuations_space(text)
    text = remove_diacritics(text)
    return text
