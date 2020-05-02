"""
Sentiment Analysis Module

"""

import numpy as np
from ._backend._sentiment import predict_pipeline, load_models

_MODEL, _TOKENIZER = load_models()


def predict_label(text: str, index2label: dict = {0: "Negative", 1: "Positive"}) -> str:
    """
    Predicts sentiment label

    Args:
        text (str): A text string
        index2label (dict): Dictionary mapping id to the corresponding label
    Returns:
         Any of Positive, Negative or Neutral label
    """
    predictions = predict_pipeline(text=text, model=_MODEL, tokenizer=_TOKENIZER)
    sentiment_id = np.argmax(predictions)
    return index2label[sentiment_id]


def predict_id(text: str) -> float:
    """
    Predict sentiment id
    Args:
        text (str): A text string
    Returns:
        0 if Negative and 1 if Positive
    """
    predictions = predict_pipeline(text=text, model=_MODEL, tokenizer=_TOKENIZER)
    return np.argmax(predictions)
