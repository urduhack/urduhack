# coding: utf8
"""test case"""
from urduhack.tokenization.tokenizer import MODEL_PATH
from pathlib import Path


def test_keras_tokenizer_predict():
    """Test Case"""
    assert MODEL_PATH == str(Path.home()) + "urduhack/models/word_tokenizer.h5"
