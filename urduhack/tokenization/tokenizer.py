# coding: utf8
"""
Tokenizer module
-------------------------------

This module provides the functionality to generate tokens (both sentence and word wise) from Urdu text.
"""
import os
from typing import List
from pathlib import Path
from .eos import _generate_sentences
from .keras_tokenizer import predict
from ..utils.io import download_weights

WEIGHTS_URL = 'https://sgp1.digitaloceanspaces.com/urduhack/models/tokenizer/word/weights_v1.zip'
file_name = WEIGHTS_URL.split('/')[-1]
SUB_DIR = "urduhack/models/"

home = str(Path.home())
MODEL_DIR = home + SUB_DIR
MODEL_PATH = MODEL_DIR + "word_tokenizer.h5"


def sentence_tokenizer(text: str) -> List[str]:
    """
    Convert ``urdu`` text into possible sentences.

    Args:
        text (str): raw ``urdu`` text

    Returns:
        list: returns a ``list`` object containing multiple urdu sentences type ``str``.
    """
    return _generate_sentences(text)


def keras_tokenizer_predict(sentence: str, model_dir: str, model_path: str) ->List[str]:
    """
    Converts an Urdu Sentence into tokens bases on a Deep Learning Model

    Args:
        sentence (str): raw ``urdu`` text
        model_dir (str): path to the model file
        model_path (str): full path to the weights file

    Return:
        list: returns a ``list`` containing urdu tokens

    """
    if not os.path.exists(model_dir):
        download_weights(url=WEIGHTS_URL, file_name=file_name, path=model_dir)
    predict(sentence, model_path)
