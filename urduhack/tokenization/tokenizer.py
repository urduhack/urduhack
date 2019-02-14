# coding: utf8
"""Main module reasonable for tokenization task"""

from typing import List

from .eos import _generate_sentences


def sentence_tokenizer(text: str) -> List[str]:
    """
    Convert raw Urdu text into possible sentences.

    Args:
        text (str): base str

    Returns:
        list
    """
    return _generate_sentences(text)
