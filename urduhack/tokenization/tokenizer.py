# coding: utf8
"""
This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""

from .eos import _generate_sentences
from .keras_tokenizer import _is_model_exist, _preprocess_sentence, _retrieve_words, _load_model

_is_model_exist()
_model, _char2idx, _idx2char = _load_model()


def sentence_tokenizer(text: str):
    """
    Convert ``urdu`` text into possible sentences.

    Args:
        text (str): Raw ``urdu`` text
    Returns:
        list: Returns a ``list`` object containing multiple urdu sentences type ``str``.
    """
    return _generate_sentences(text)


def word_tokenizer(sentence: str, maxlen: int = 256):
    """
    Generate words tokens from Urdu sentence

    Args:
        sentence (str): Raw ``urdu`` text or list of text
        maxlen (int): Maximum text length supported by model
    Return:
        list: Returns a ``list`` containing urdu tokens
    """
    inp_, _ = _preprocess_sentence(sentence, _char2idx, max_len=maxlen)
    predictions = _model.predict(inp_)
    word_tokens = _retrieve_words(inp_[0, :], predictions[0, :], _idx2char)
    return word_tokens
