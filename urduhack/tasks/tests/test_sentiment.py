"""
Test Cases
"""
import numpy as np
from ..sentiment import predict_label, predict_id, model, tokenizer
from .._backend._sentiment import predict_pipeline


def test_predict_label():
    """
    Test Case
    """
    text = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    assert isinstance(text, str)
    label = predict_label(text)
    assert isinstance(label, str)


def test_predict_id():
    """
    Test Case
    """
    text = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    assert isinstance(text, str)
    label = predict_id(text)
    assert isinstance(label, np.int64)


def test_predict_pipeline():
    """
    Test Case
    """
    text = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    assert isinstance(text, str)
    predictions = predict_pipeline(text=text, model=model, tokenizer=tokenizer)
    assert predictions.shape == (1, 2)
