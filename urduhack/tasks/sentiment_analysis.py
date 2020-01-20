"""
sentiment_analysis module
------------------------
Predict sentiment labels or ids
"""

import numpy as np
from transformers import RobertaTokenizer, TFRobertaModel

from .sentiment import compile_model, predict_pipeline
from ..config import LAYERS_WEIGHTS_PATH

pretrained = "roberta-large-mnli"
tokenizer = RobertaTokenizer.from_pretrained(pretrained)
lang_model = TFRobertaModel.from_pretrained(pretrained)

model = compile_model(weights=LAYERS_WEIGHTS_PATH, lang_model=lang_model)


def predict_sentiment_label(text: str, index2label: dict = {0: "Negative", 1: "Positive", 2: "Neutral"}):
    """
    Predicts sentiment label

    Args:
        text (str): A text string
        index2label (dict): Dictionary mapping id to the corresponding label
    Returns:
         Any of Positive, Negative or Neutral label
    """
    predictions = predict_pipeline(text=text, model=model, tokenizer=tokenizer)
    sentiment_id = np.argmax(predictions)
    return index2label[sentiment_id]


def predict_sentiment_id(text: str):
    """
    Predict sentiment id

    Args:
        text (str): A text string
    Returns:
        Any of 0, 1, 2 sentiment label
    """
    predictions = predict_pipeline(text=text, model=model, tokenizer=tokenizer)
    return np.argmax(predictions)