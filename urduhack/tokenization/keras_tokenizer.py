# coding: utf8
"""
keras_tokenizer module
-------------------------------

This module create tokens using a pre-trained sequence model .
"""

import numpy as np
import tensorflow as tf

from pathlib import Path
from ..normalization import normalize
from ..utils.io import download_from_url, extract_zip, remove_file

WORD_TOKENIZER_WEIGHTS_URL: str = 'https://sgp1.digitaloceanspaces.com/urduhack/models/tokenizer/word/weights_v1.zip'
WORD_TOKENIZER_FILE_NAME = WORD_TOKENIZER_WEIGHTS_URL.split('/')[-1]

USER_HOME = str(Path.home())
SUB_DIR = "/urduhack/models/"
MODELS_DIR = f"{USER_HOME}/{SUB_DIR}"
WORD_TOKENIZER_FILE_PATH = f"{MODELS_DIR}/{WORD_TOKENIZER_FILE_NAME}"
EXTRACT_FILE = f"{MODELS_DIR}/{WORD_TOKENIZER_FILE_NAME}"

MODEL_PATH = f"{MODELS_DIR}word_tokenizer.h5"
VOCAB_PATH = f"{MODELS_DIR}vocab.txt"


def load_vocab(vocab_path: str):
    """
    Maps characters to integers and vice versa

    Args:
        vocab_path (str): path to the vocab file

    Returns:
        Two dictionaries containing character to integer mapping and integer to character mapping
    """

    vocab_file = open(vocab_path)
    vocab = vocab_file.readline()
    vocab = list('_' + vocab)
    vocab.remove('\n')
    char2idx = {char: idx for idx, char in enumerate(vocab)}
    idx2char = {idx: char for idx, char in enumerate(vocab)}
    return char2idx, idx2char


def preprocess_sentences(sentences: list, max_len: int, char2idx: dict):
    """
    Makes the input and output arrays for the data explaining where is a character or a space

    Args:
        sentences (str): Sentence to be tokenized
        max_len (int): integer
        char2idx (dict): Dict containing character to integer mapping

    Returns:
        Input and Output arrays representing features and labels
    """

    input_ = np.zeros((len(sentences), max_len), dtype=int)
    output_ = np.zeros((len(sentences), max_len))
    for i, sentence in enumerate(sentences):
        char_index = 0
        for letter in sentence:
            if letter == ' ':
                output_[i, char_index - 1] = 1
            elif letter in char2idx:
                input_[i, char_index] = char2idx[letter]
                char_index += 1
    return input_, output_


def retrieve_words(features, labels, idx2char, thresh):
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


def _download_model() -> None:
    """
    Used privately by tokenizer
    Download and extracts the model file if it does not already exists

    Returns: None

    """
    if not Path(MODEL_PATH).exists() and Path(VOCAB_PATH).exists():
        download_from_url(WORD_TOKENIZER_WEIGHTS_URL, MODELS_DIR)
        extract_zip(EXTRACT_FILE, MODELS_DIR)

    remove_file(EXTRACT_FILE)


def predict(sentence: str, weight_file: str, vocab_path: str, max_len: int = 256, thresh: float = 0.5):
    """
    Predicts tokens based on Pre-trained Keras Model

    Args:
        sentence (str): Sentence to be tokenized
        weight_file (str): path to the model weights file
        vocab_path (str): path to the vocab file
        max_len (int): Maximum length of the tokens vector
        thresh (float): Confidence needed to predict a character/space

    Returns:
        list: list containing urdu tokens
    """
    sentences = []
    if isinstance(sentence, str):
        sentence = normalize(sentence)
        sentences.append(sentence)
    else:
        sentences = sentence
    model = tf.keras.models.load_model(weight_file)
    char2idx, idx2char = load_vocab(vocab_path)
    inp_, _ = preprocess_sentences(sentences, max_len, char2idx)
    example_letters = inp_[:, :]
    predictions = model.predict(example_letters)
    for i in range(inp_.shape[0]):
        print("Sentence: ", sentences[i])
        print("Tokens: ", retrieve_words(example_letters[i, :], predictions[i, :], idx2char, thresh=thresh))
