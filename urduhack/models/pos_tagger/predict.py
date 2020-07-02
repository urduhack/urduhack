# coding: utf8
"""POS Tag Prediction Pipeline"""

import json
from typing import Tuple

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from urduhack.config import POS_TAGGER_WEIGHTS_PATH, POS_WORD2IDX_PATH, POS_TAG2IDX_PATH
from urduhack.models.pos_tagger.model import _bi_lstm_crf_model

_POS_TAGGER_MODEL, _WORD2IDX, _IDX2TAG = None, None, None


def _load_metadata(model_path: str, word2idx_path: str,
                   tag2idx_path: str, max_len: int = 50) -> Tuple[tf.keras.Model, dict, dict]:
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


def predict_tags(text: str) -> list:
    """
    Predicts POS Tags

    Args:
        text (str): Input text string

    Returns:
        list: Containing words their tags
    """

    global _POS_TAGGER_MODEL, _WORD2IDX, _IDX2TAG
    if _POS_TAGGER_MODEL is None:
        _POS_TAGGER_MODEL, _WORD2IDX, _IDX2TAG = _load_metadata(POS_TAGGER_WEIGHTS_PATH,
                                                                POS_WORD2IDX_PATH, POS_TAG2IDX_PATH)

    tokens = text.split()
    encoded = [[_WORD2IDX[word] if word in _WORD2IDX else _WORD2IDX["UNK"] for word in tokens]]
    padded = pad_sequences(sequences=encoded, maxlen=50, value=_WORD2IDX['PAD'], padding='post')
    predictions = _POS_TAGGER_MODEL.predict(padded)
    pred_tags = np.argmax(predictions, axis=2).reshape(predictions.shape[1])
    word_tags = [(word, _IDX2TAG[idx]) for word, idx in zip(tokens, pred_tags)]
    return word_tags
