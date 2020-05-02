"""
sentiment module
----------------
Performs sentiment analysis on textual data
"""
from pathlib import Path
import numpy as np
import tensorflow as tf
from transformers import XLMRobertaTokenizer, TFXLMRobertaModel
from tensorflow.keras.layers import Conv1D, Concatenate, Dense, Dropout, MaxPooling1D, Flatten, Input

from ...utils import pickle_load
from ...config import LAYERS_WEIGHTS_PATH


def compile_model(weights: str, maxlen: int = 512, filter_size: list = [3, 5, 7],
                  num_filters: int = 6, n_classes: int = 2, lang_model: None = None):
    """
    Compiles a pre-trained keras model

    Args:
        maxlen (int): Maximum Sequence Length
        filter_size (list): Filter sizes used in the convolution layers
        num_filters (int): Number of Filters used in convolution layers
        n_classes (int): Number of classes
        lang_model (None): Pre_trained language model
        weights (str): Path to the weights file
    Returns:
        Compiled keras model
    """
    weights = pickle_load(weights)
    sequence_input = Input(shape=(maxlen,), dtype='int32')
    embedded_sequences, _ = lang_model(sequence_input)
    conv_blocks = []
    for k_size in filter_size:
        conv = Conv1D(filters=num_filters,
                      kernel_size=k_size,
                      padding="valid",
                      activation="relu",
                      strides=1)(embedded_sequences)
        conv = Dropout(0.25)(conv)
        conv = MaxPooling1D(pool_size=maxlen - k_size + 1)(conv)
        conv = Flatten()(conv)
        conv_blocks.append(conv)
    concat = Concatenate()(conv_blocks) if len(conv_blocks) > 1 else conv_blocks[0]
    dense = Dropout(0.2)(concat)
    dense = Dense(512, activation="relu")(dense)
    preds = Dense(n_classes, activation="softmax")(dense)

    model = tf.keras.Model(sequence_input, preds)
    model.compile(loss='categorical_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(learning_rate=0.0003),
                  metrics=['acc'])

    for i, layer in enumerate(model.layers[2:]):
        layer.set_weights(weights[i])

    return model


def predict_pipeline(text: str, max_seq_len: int = 512, model: None = None, tokenizer: None = None) -> bytearray:
    """
    Predict sentiment of a text sentence

    Args:
        text (str): input text
        max_seq_len (int): maximum length of the encoded text sequence
        model (None): Pre_trained keras model
        tokenizer (None): Tokenizer to encode the input text
    Returns:
        Probabilities of sentiment labels
    """
    encoded = tokenizer.encode(text, add_special_tokens=True, max_length=max_seq_len, pad_to_max_length=True)
    encoded = np.asarray([encoded])
    predictions = model.predict(encoded)
    return predictions


def load_models(layers_weights: str = LAYERS_WEIGHTS_PATH, pre_trained: str = "jplu/tf-xlm-roberta-large"):
    """
    Downloads and load a pretrained language model as well as layer weights for classifier

    Args:
        layers_weights (str): Path to the layers weight file
        pre_trained (str): Name or path to the pretrained language model
    Returns:
        None
    """

    tokenizer_ = XLMRobertaTokenizer.from_pretrained(pre_trained)
    lang_model = TFXLMRobertaModel.from_pretrained(pre_trained)
    if Path(layers_weights).exists():
        model_ = compile_model(weights=layers_weights, lang_model=lang_model)
    return model_, tokenizer_
