# coding: utf8
"""
Urdu Characters Normalization Module
------------------------------------
This modules fixes the problem of correct encodings for the Urdu characters as well as replace Arabic
characters with correct Urdu characters. This module brings all the characters in the specified unicode range
(0600-06FF) for Urdu language.

It also fixes the problem of joining of different Urdu words. By joining we mean that when space between two Urdu words
is removed, they must not make a new word. Their rendering must not change and even after the removal of space
they should look the same.

You can use the library to normalize the Urdu text for correct unicode characters.
By normalization we mean to end the confusion between Urdu and Arabic characters,
to replace two words with one word keeping in mind the context they are used in.
Like the character 'ﺁ' and 'ﺂ' are to be replaced by 'آ'. All this is done using regular expressions.

The normalization of Urdu text is necessary to make it useful for the machine learning tasks.
This module provides the following functionality:

    - Normalizing Single Characters
    - Normalizing Combine Characters
    - Put Spaces Before & After Digits
    - Put Spaces After Urdu Punctuations
    - Put Spaces Before & After English Words
    - Removal of Diacritics from Urdu Text
"""

from .character import normalize_characters, normalize_combine_characters
from .util import punctuations_space, digits_space, remove_diacritics, \
    english_characters_space

__all__ = ["normalize_characters", "normalize_combine_characters",
           "english_characters_space",
           "punctuations_space", "digits_space", "remove_diacritics",
           "normalize"]


def normalize(text: str) -> str:
    """
    To normalize some text, all you need to do pass ``unicode`` text. It will return a ``str``
    with normalized characters both single and combined, proper spaces after digits and punctuations
    and diacritics removed.

    Args:
        text (str): raw ``unicode`` Urdu text

    Returns:
        str: normalized urdu text
    """
    text = normalize_characters(text)
    text = normalize_combine_characters(text)
    text = digits_space(text)
    text = punctuations_space(text)
    text = remove_diacritics(text)
    text = english_characters_space(text)
    return text
