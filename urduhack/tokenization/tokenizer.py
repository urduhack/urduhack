# coding: utf8
"""
This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""

from typing import List

from .eos import _generate_sentences
from .keras_tokenizer import _is_model_exist, _preprocess_sentence, _retrieve_words, _load_model
from ..config import MODEL_PATH, VOCAB_PATH
from ..errors import Errors

_WORD_TOKENIZER_MODEL, _CHAR2IDX, _IDX2CHAR = None, None, None


def sentence_tokenizer(text: str) -> List[str]:
    """
    Convert ``urdu`` text into possible sentences.

    Args:
        text (str): Raw ``urdu`` text
    Returns:
        list: Returns a ``list`` object containing multiple urdu sentences type ``str``.
    Raises:
        TypeError: If text is not a str Type
    """
    if not isinstance(text, str):
        raise TypeError(Errors.E001.format(object_name=text, object_type=str))

    return _generate_sentences(text)


def word_tokenizer(sentence: str, max_len: int = 256) -> List[str]:
    """
    Generate words tokens from Urdu sentence

    Args:
        sentence (str): Raw ``urdu`` text or list of text
        max_len (int): Maximum text length supported by model
    Return:
        list: Returns a ``List[str]`` containing urdu tokens
    """
    global _WORD_TOKENIZER_MODEL, _CHAR2IDX, _IDX2CHAR

    if _WORD_TOKENIZER_MODEL is None:
        _is_model_exist(MODEL_PATH, VOCAB_PATH)
        _WORD_TOKENIZER_MODEL, _CHAR2IDX, _IDX2CHAR = _load_model(MODEL_PATH, VOCAB_PATH)

    inp_, _ = _preprocess_sentence(sentence, _CHAR2IDX, max_len=max_len)
    predictions = _WORD_TOKENIZER_MODEL.predict(inp_)
    word_tokens = _retrieve_words(inp_[0, :], predictions[0, :], _IDX2CHAR)
    return word_tokens
