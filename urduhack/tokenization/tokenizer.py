# coding: utf8
"""
This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""

from typing import List, Union

from .eos import _generate_sentences
from .keras_tokenizer import predict, _download_model, MODEL_PATH, VOCAB_PATH


def sentence_tokenizer(text: str) -> List[str]:
    """
    Convert ``urdu`` text into possible sentences.

    Args:
        text (str): raw ``urdu`` text

    Returns:
        list: returns a ``list`` object containing multiple urdu sentences type ``str``.
    """
    return _generate_sentences(text)


def word_tokenizer(sentence: Union[str, list]) -> List[str]:
    """
    Generate words tokens from Urdu sentence

    Args:
        sentence (str)|(list): Raw ``urdu`` text or list of text

    Return:
        list: returns a ``list`` containing urdu tokens

    """
    _download_model()
    return predict(sentence, MODEL_PATH, VOCAB_PATH)
