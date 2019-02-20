# coding: utf8
"""
Tokenizer module
-------------------------------

This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""
from typing import List

from .eos import _generate_sentences


def sentence_tokenizer(text: str) -> List[str]:
    """
    Convert ``urdu`` text into possible sentences.

    Args:
        text (str): raw ``urdu`` text

    Returns:
        list: returns a ``list`` object containing multiple urdu sentences type ``str``.
    """
    return _generate_sentences(text)
