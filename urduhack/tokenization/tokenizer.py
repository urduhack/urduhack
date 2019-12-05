# coding: utf8
"""
This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""
import os
from pathlib import Path
from typing import List, Union

from .eos import _generate_sentences
from .keras_tokenizer import predict
from ..utils.io import download_from_url, extract_weights

WEIGHTS_URL: str = 'https://sgp1.digitaloceanspaces.com/urduhack/models/tokenizer/word/weights_v1.zip'
file_name = WEIGHTS_URL.split('/')[-1]

home = str(Path.home())
SUB_DIR = "/urduhack/models/"

MODEL_DIR = home + SUB_DIR
file_path = f"{MODEL_DIR}/{file_name}"
extract_file = f"{MODEL_DIR}/{file_name}/{file_name}"

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
        return download_from_url(WEIGHTS_URL, file_path)


def word_tokenizer(sentence: Union[str, list]) -> List[str]:
    """
    Generate words tokens from Urdu sentence

    Args:
        sentence (str)|(list): Raw ``urdu`` text or list of text

    Return:
        list: returns a ``list`` containing urdu tokens

    """
    download_from_url(WEIGHTS_URL, file_path)
    extract_weights(extract_file, MODEL_DIR, file_path)
    return predict(sentence, MODEL_PATH, VOCAB_PATH)
