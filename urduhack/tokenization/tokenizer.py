# coding: utf8
"""
This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""

from typing import List, Union

from .eos import _generate_sentences
from .keras_tokenizer import predict, _is_model_exist
from ..config import MODEL_PATH, VOCAB_PATH


def sentence_tokenizer(text: str) -> List[str]:
    """
    Convert ``urdu`` text into possible sentences.

    Args:
        text (str): Raw ``urdu`` text
    Returns:
        list: Returns a ``list`` object containing multiple urdu sentences type ``str``.
    """
    return _generate_sentences(text)


def word_tokenizer(sentence: Union[str, list]) -> List[str]:
    """
    Generate words tokens from Urdu sentence

    Args:
        sentence (str)|(list): Raw ``urdu`` text or list of text
    Return:
        list: Returns a ``list`` containing urdu tokens
    """
    _is_model_exist()
    return predict(sentence, MODEL_PATH, VOCAB_PATH)
