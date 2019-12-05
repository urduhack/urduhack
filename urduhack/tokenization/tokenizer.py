# coding: utf8
"""
This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""
import os
from pathlib import Path
from typing import List, Union

from .eos import _generate_sentences
from .keras_tokenizer import predict
from ..utils.io import download_weights

WEIGHTS_URL: str = 'https://sgp1.digitaloceanspaces.com/urduhack/models/tokenizer/word/weights_v1.zip'
file_name = WEIGHTS_URL.split('/')[-1]
SUB_DIR = "urduhack/models/"

home = str(Path.home())
MODEL_DIR = home + SUB_DIR
MODEL_PATH = MODEL_DIR + "word_tokenizer.h5"
VOCAB_PATH = MODEL_DIR + "vocab.txt"


def sentence_tokenizer(text: str) -> List[str]:
    """
    Convert ``urdu`` text into possible sentences.

    Args:
        text (str): raw ``urdu`` text

    Returns:
        list: returns a ``list`` object containing multiple urdu sentences type ``str``.
    """
    return _generate_sentences(text)


def download_keras_weights():
    """
    Download keras model weights

    Return: Download model weights and vocab.txt
    """
    if not os.path.exists(MODEL_PATH):
        return download_weights(WEIGHTS_URL, file_name, MODEL_DIR)


def word_tokenizer(sentence: Union[str, list]) -> List[str]:
    """
    Generate words tokens from Urdu sentence

    Args:
        sentence (str)|(list): Raw ``urdu`` text or list of text

    Return:
        list: returns a ``list`` containing urdu tokens

    """
    return predict(sentence, MODEL_PATH, VOCAB_PATH)
