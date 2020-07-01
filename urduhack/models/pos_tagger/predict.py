"""POS Tag Prediction Pipeline"""

from urduhack.models.pos_tagger.model import bi_lstm_crf_model
from urduhack.tokenization import word_tokenizer
from urduhack.config import POS_TAGGER_WEIGHTS_PATH, POS_WORD2IDX_PATH, POS_TAG2IDX_PATH

from tensorflow.keras.preprocessing.sequence import pad_sequences
from typing import Tuple

import tensorflow as tf
import numpy as np
import json


def load_metadata(model_path: str, word2idx_path: str,
                  tag2idx_path: str, max_len: int = 50) -> Tuple[tf.keras.Model, dict, dict, dict, dict]:
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
    with open(word2idx_path, "r") as w2i, open(tag2idx_path, "r") as t2i:
        w2i = json.load(w2i)
        t2i = json.load(t2i)

    n_words = len(w2i)
    n_tags = len(t2i)
    i2w = {i: w for w, i in w2i.items()}
    i2t = {i: w for w, i in t2i.items()}

    model_arch = bi_lstm_crf_model(n_words, n_tags, max_len)
    model_arch.load_weights(model_path)

    return model_arch, w2i, t2i, i2w, i2t


model, word2idx, tag2idx, idx2word, idx2tag = load_metadata(POS_TAGGER_WEIGHTS_PATH,
                                                            POS_WORD2IDX_PATH, POS_TAG2IDX_PATH)


def predict_tags(tokens: str, max_len: int = 50) -> list:
    """
    Predicts POS Tags

    Args:
        tokens (str): Input text string
        max_len (int): Maximum sequence length

    Returns:
        List containing words their tags
    """
    tokens = tokens.split()
    encoded = [[word2idx[word] if word in word2idx else word2idx["UNK"] for word in tokens]]
    padded = pad_sequences(sequences=encoded, maxlen=max_len, value=word2idx['PAD'], padding='post')
    predictions = model.predict(padded)
    pred_tags = np.argmax(predictions, axis=2).reshape(predictions.shape[1])
    tags = []
    for word, t_idx in zip(tokens, pred_tags):
        tags.append((word, idx2tag[t_idx]))
    return tags
