# coding: utf8
"""
This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""
from pathlib import Path
from typing import List, Union

from .eos import _generate_sentences
from .keras_tokenizer import predict
from ..utils.io import download_from_url, extract_zip

WORD_TOKENIZER_WEIGHTS_URL: str = 'https://sgp1.digitaloceanspaces.com/urduhack/models/tokenizer/word/weights_v1.zip'
WORD_TOKENIZER_FILE_NAME = WORD_TOKENIZER_WEIGHTS_URL.split('/')[-1]

USER_HOME = str(Path.home())
SUB_DIR = "/urduhack/models/"
MODELS_DIR = f"{USER_HOME}/{SUB_DIR}"
WORD_TOKENIZER_FILE_PATH = f"{MODELS_DIR}/{WORD_TOKENIZER_FILE_NAME}"
extract_file = f"{MODELS_DIR}/{WORD_TOKENIZER_FILE_NAME}/{WORD_TOKENIZER_FILE_NAME}"

MODEL_PATH = f"{MODELS_DIR}/word_tokenizer.h5"
VOCAB_PATH = f"{MODELS_DIR}/vocab.txt"


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
    download_from_url(WORD_TOKENIZER_WEIGHTS_URL, MODELS_DIR)
    extract_zip(extract_file, MODELS_DIR)
    return predict(sentence, MODEL_PATH, VOCAB_PATH)
