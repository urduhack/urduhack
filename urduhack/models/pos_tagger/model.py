# coding: utf8
"""POS Tagger Tensorflow Model"""

from tf2crf import CRF

import tensorflow as tf


def _bi_lstm_crf_model(n_words: int, n_tags: int, max_len: int):
    """Model"""
    input_ = tf.keras.layers.Input(shape=(max_len,), name='input_layer')
    embedding_layer = tf.keras.layers.Embedding(input_dim=n_words + 2, output_dim=50, mask_zero=True,
                                                name='embedding_layer')(input_)
    lstm_layer = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=128, return_sequences=True,
                                                                    activation="relu",
                                                                    recurrent_dropout=0.4))(embedding_layer)
    tensor = tf.keras.layers.Dropout(0.4)(lstm_layer)
    tensor = tf.keras.layers.Dense(n_tags)(tensor)
    crf = CRF(n_tags)
    output = crf(tensor)
    model = tf.keras.models.Model(input_, output)

    return model
