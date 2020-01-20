"""
sentiment module
----------------
Performs sentiment analysis on textual data
"""
import tensorflow as tf
from tensorflow.keras.layers import Conv1D, Concatenate, Dense, Dropout, MaxPooling1D, Flatten, Input

from ..utils import pickle_load


def compile_model(weights: str, maxlen: int= 128, filter_size: list = [3, 5, 7], num_filters: int = 25,
                  n_classes: int = 3, lang_model: None = None):
    """
    Compiles a pre-trained keras model

    Args:
        maxlen (int): Maximum Sequence Length
        filter_size (list): Filter sizes used in the convolution layers
        num_filters (int): Number of Filters used in convolution layers
        n_classes (int): Number of classes
        lang_model (None): Pretrained language model
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
    x = Dropout(0.2)(concat)
    x = Dense(256, activation="relu")(x)
    preds = Dense(n_classes, activation="softmax")(x)

    model = tf.keras.Model(sequence_input, preds)
    model.compile(loss='categorical_crossentropy',
                  optimizer=tf.keras.optimizers.Adam(learning_rate=0.0075),
                  metrics=['acc'])

    for i, layer in enumerate(model.layers[2:]):
        layer.set_weights(weights[i])

    return model


def predict_pipeline(text: str, maxlen: int = 128, model: None = None, tokenizer: None = None):
    """
    Predict sentiment of a text sentence

    Args:
        text (str): input text
        maxlen (int): maximum length of the encoded text sequence
        model (None): Pretrained keras model
        tokenizer (None): Tokenizer to encode the input text
    Returns:
        Probabilities of sentiment labels
    """
    encoded = tokenizer.encode(text, add_special_tokens=True)
    padded_sequence = tf.keras.preprocessing.sequence.pad_sequences([encoded], maxlen=maxlen, padding="post",
                                                                    truncating="post")
    predictions = model.predict(padded_sequence)
    return predictions




