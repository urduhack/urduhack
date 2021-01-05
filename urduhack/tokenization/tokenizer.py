# coding: utf8
"""
This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""

from typing import List

from .eos import _generate_sentences
from .wtk import _load_model, _is_model_available, _is_token
from ..config import WORD_TOKENIZER_MODEL_PATH

from ..preprocessing import preprocess
from ..normalization import normalize
from ..tokenization.words import fix_join_words

_WORD_TOKENIZER_MODEL = None


def sentence_tokenizer(text: str) -> List[str]:
    """
    Convert ``Urdu`` text into possible sentences.
    If successful, this function returns a :py:class:`List` object containing multiple urdu :py:class:`String`
    sentences.

    Args:
        text (str): ``Urdu`` text
    Returns:
        list: Returns a ``list`` object containing multiple urdu sentences type ``str``.
    Raises:
        TypeError: If text is not a str Type
    Examples:
        >>> from urduhack.tokenization import sentence_tokenizer
        >>> text = "عراق اور شام نے اعلان کیا ہے دونوں ممالک جلد اپنے اپنے سفیروں کو واپس بغداد اور دمشق بھیج دیں گے؟"
        >>> sentences = sentence_tokenizer(text)
        >>> sentences
        ["دونوں ممالک جلد اپنے اپنے سفیروں کو واپس بغداد اور دمشق بھیج دیں گے؟" ,"عراق اور شام نے اعلان کیا ہے۔"]
    """
    if not isinstance(text, str):
        raise TypeError("text parameter must be str type.")

    return _generate_sentences(text)


def word_tokenizer(sentence: str) -> List[str]:
    """
    To convert the raw Urdu text into tokens, we need to use :py:func:`~urduhack.tokenization.word_tokenizer` function.
    Before doing this we need to normalize our sentence as well. For normalizing the urdu sentence use
    :py:func:`urduhack.normalization.normalize` function.
    If the word_tokenizer runs successfully, this function returns a :py:class:`List` object containing
    urdu :py:class:`String` word tokens.

    Args:
        sentence (str): ``urdu`` text or list of text
    Return:
        list: Returns a ``List[str]`` containing urdu tokens
    Examples:
        >>> sent = 'عراق اور شام نے اعلان کیا ہے دونوں ممالک جلد اپنے اپنے سفیروں کو واپس بغداد اور دمشق بھیج دیں گے؟'
        >>> from urduhack.tokenization import word_tokenizer
        >>> word_tokenizer(sent)
        Tokens:  ['عراق', 'اور', 'شام', 'نے', 'اعلان', 'کیا', 'ہے', 'دونوں', 'ممالک', 'جلد', 'اپنے', 'اپنے', 'سفیروں', 'کو', 'واپس', 'بغداد', 'اور', 'دمشق', 'بھیج', 'دیں', 'گے', '؟']
    """

    global _WORD_TOKENIZER_MODEL

    if _WORD_TOKENIZER_MODEL is None:
        _is_model_available(WORD_TOKENIZER_MODEL_PATH)
        _WORD_TOKENIZER_MODEL = _load_model(WORD_TOKENIZER_MODEL_PATH)

    text = fix_join_words(preprocess(normalize(sentence)))

    spm_pieces = _WORD_TOKENIZER_MODEL.EncodeAsPieces(text)
    filtered = _is_token(spm_pieces)
    tokens = _WORD_TOKENIZER_MODEL.DecodePieces(filtered).split()

    return tokens
