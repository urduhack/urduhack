"""
Sentiment Module
---------------
Predict whether a sentiment is Positive, Negative or Neutral
"""

from ..normalization import normalize
from ..tokenization import word_tokenizer
from ..config import SENTIMENT_MODEL_PATH, SENTIMENT_VOCAB_PATH, MAX_SEQUENCE_LENGTH
from ..utils.io import pickle_load

import tensorflow as tf
import numpy as np


def convert_word_to_index(tokens: list, word_index: dict):
    """
    Converts word tokens to respective indexes according to model vocabulary

    Args:
        tokens (list): list of word tokens
        word_index (dict): Model vocab containing words and their indexes
    Returns:
        list of word indexes
    """
    sequences = []
    for token in tokens:
        for i, word in enumerate(token):
            if word not in word_index.keys():
                token[i] = word_index["<UK>"]
            else:
                token[i] = word_index[word]
        sequences.append(token)
    return sequences


def pad_sequences(sequences: list, max_len: int = MAX_SEQUENCE_LENGTH):
    """
    Pad sequences to make them all of a fixed equal length

    Args:
        sequences (list): list containing word indexes
        max_len (int): Maximum length to pad sequences
    Returns:
        padded sequences array
    """
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_len, padding="post", truncating="post")
    return padded_sequences


def predict_sentiment(text: str, model_path: str, vocab_path: str):
    """
    Predict Sentiment using keras model

    Args:
        text (str): sentiment to be analyzed
        model_path (str): Path to the sentiment model file
        vocab_path (str): Path to the model vocab file
    Returns:
        Probabilities of all the sentiments
    """
    model = tf.keras.models.load_model(model_path)
    word_index = pickle_load(vocab_path)
    normal_text = normalize(text)
    word_tokens = word_tokenizer(normal_text)
    sequences = convert_word_to_index(word_tokens, word_index)
    padded_sequence = pad_sequences(sequences)
    predictions = model.predict(padded_sequence)
    return predictions


def get_sentiment_label(text: str):
    """
    Converts Prediction probabilities to actual labels

    Args:
        text (str): Text sentiment to be predicted
    Returns:
        list containing sentiment label
    """
    predictions = predict_sentiment(text, SENTIMENT_MODEL_PATH, SENTIMENT_VOCAB_PATH)
    encoded = np.argmax(predictions, axis=1)
    label_dict = {0: "Negative", 1: "Neutral", 2: "Positive"}
    label = [label_dict[word] for word in encoded]
    return np.array(label)


def get_sentiment_probability(text: str):
    """
    Returns Sentiment Probabilities for Negative, Neutral and Positive sentiments

    Args:
         text (str): Text sentiment to be predicted
    Returns:
        Prediction Probabilities for Negative, Neutral and Positive Sentiment
    """
    predictions = predict_sentiment(text, SENTIMENT_MODEL_PATH, SENTIMENT_VOCAB_PATH)
    return predictions
