# coding: utf8
"""
keras_tokenizer module
-------------------------------

This module create tokens using a pre-trained sequence model .
"""
from pathlib import Path
from typing import Tuple

import numpy as np
import tensorflow as tf
from numpy import ndarray


def _load_vocab(vocab_path: str) -> Tuple[dict, dict]:
    """
    Maps characters to integers and vice versa
    Args:
        vocab_path (str): path to the vocab file
    Returns:
        Two dictionaries containing character to integer mapping and integer to character mapping
    """

    with open(vocab_path, "r", encoding="UTF-8") as vocab_file:
        vocab = vocab_file.readline()
    vocab = list('_' + vocab)
    char2idx = {char: idx for idx, char in enumerate(vocab)}
    idx2char = {idx: char for idx, char in enumerate(vocab)}  # pylint: disable=unnecessary-comprehension
    return char2idx, idx2char


def _preprocess_sentence(sentence: str, char2idx: dict, max_len: int) -> Tuple[ndarray, ndarray]:
    """
    Makes the input and output arrays for the data explaining where is a character or a space

    Args:
        sentence (str): Sentence to be tokenized
        char2idx (dict): Dict containing character to integer mapping
        max_len (int): integer
    Returns:
        Input and Output arrays representing features and labels
    """

    input_ = np.zeros((len(sentence), max_len,), dtype=int)
    output_ = np.zeros((len(sentence), max_len,))
    char_index = 0
    for letter in sentence:
        if letter == ' ':
            output_[0, char_index - 1] = 1
        elif letter in char2idx:
            input_[0, char_index] = char2idx[letter]
            char_index += 1
            if char_index == max_len:
                break
    return input_, output_


def _retrieve_words(features, labels, idx2char, thresh=0.5) -> list:
    """
    Retrieve the original words from predicted and actual arrays as per char2idx mapping

    Args:
        features (array): Input array
        labels (array): Output array
        idx2char (dict): Dict mapping integer to character
        thresh (float): Confidence to tell whether prediction is a character or space
    Returns:
        list : Containing ``urdu`` word tokens
    """
    mask = features != 0
    letters = features[mask]
    spaces = labels[mask]
    final = ''
    tokens = []
    for letter in range(letters.shape[0]):
        idx = letters[letter]
        if idx != 0:
            final += idx2char[idx]
        if spaces[letter] >= thresh:
            tokens.append(final)
            final = ''
    tokens.append(final)
    return tokens


def _load_model(model_path: str, vocab_path: str):
    """
    Loads pre_trained keras model and vocab file

    Args:
        model_path (str): Path to the model file
        vocab_path (str): Path to the vocab file
    Returns:
        tuple: contains object
    """
    model_ = tf.keras.models.load_model(model_path)
    char2idx_, idx2char_ = _load_vocab(vocab_path)
    return model_, char2idx_, idx2char_


def _is_model_exist(model_path: str, vocab_path: str) -> None:
    """
    Check if the models file exist.

    Args:
        model_path (str): path to the tokenizer model file
        vocab_path (str): Path to the tokenizer vocab file
    Raises:
        FileNotFoundError: If model_path does not exist
    Returns: None
    """
    if not Path(model_path).exists() and not Path(vocab_path).exists():
        _error = "Word tokenizer Model not found!" \
                 "Please run 'urduhack download' in terminal." \
                 "Doc: https://urduhack.readthedocs.io/en/stable/installation.html#downloading-models"
        raise FileNotFoundError(_error)
