# coding: utf8
"""NER Prediction Pipeline"""

import json
from typing import Tuple

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from urduhack.config import NER_WEIGHTS_PATH, NER_WORD2IDX_PATH, NER_TAG2IDX_PATH
from urduhack.models.ner.model import _bi_lstm_crf_model

_NER_MODEL, _WORD2IDX, _IDX2TAG = None, None, None


def _load_metadata(model_path: str, word2idx_path: str,
                   tag2idx_path: str, max_len: int = 55) -> Tuple[tf.keras.Model, dict, dict]:
    """
    Loads model weights and it's metadata

    Args:
        model_path (str): Path to model weights
        word2idx_path (str): Path to word2idx json file
        tag2idx_path (str): Path to tag2idx json file
        max_len (int): Maximum input length of the sequence

    Returns:
        Model and related dictionaries
    """
    with open(word2idx_path, "r", encoding="utf8") as w2i, open(tag2idx_path, "r", encoding="utf8") as t2i:
        w2i = json.load(w2i)
        t2i = json.load(t2i)

    n_words = len(w2i)
    n_tags = len(t2i)
    i2t = {i: w for w, i in t2i.items()}

    model_arch = _bi_lstm_crf_model(n_words, n_tags, max_len)
    model_arch.load_weights(model_path)

    return model_arch, w2i, i2t


def predict_ner(text: str) -> list:
    """
    Predicts NER Tags

    Args:
        text (str): Input text string

    Returns:
        list: Containing words their tags
    """

    global _NER_MODEL, _WORD2IDX, _IDX2TAG
    if _NER_MODEL is None:
        _NER_MODEL, _WORD2IDX, _IDX2TAG = _load_metadata(NER_WEIGHTS_PATH,
                                                         NER_WORD2IDX_PATH, NER_TAG2IDX_PATH)

    tokens = text.split()
    encoded = [[_WORD2IDX[word] if word in _WORD2IDX else _WORD2IDX["UNK"] for word in tokens]]
    padded = pad_sequences(sequences=encoded, maxlen=55, value=_WORD2IDX['PAD'], padding='post')
    predictions = _NER_MODEL.predict(padded)
    pred_tags = np.argmax(predictions, axis=2).reshape(predictions.shape[1])
    word_tags = [(word, _IDX2TAG[idx]) for word, idx in zip(tokens, pred_tags)]
    return word_tags
