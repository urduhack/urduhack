"""
Test cases for tokenizer
"""

import pytest
import tensorflow as tf
import sentencepiece as spm

from ..wtk import _is_model_available, _is_token, _load_model
from ..tokenizer import sentence_tokenizer, word_tokenizer
from ...config import WORD_TOKENIZER_MODEL_PATH


def test_sentence_tokenizer():
    """Test Case"""
    text = "ہم اس کیلئے تیار ہیں لیکن پھرسسٹم لپیٹاجائے ؟کیجئے گا۔قومی " \
           "اسمبلی کے اجلاس میں خطاب کرتے ہوئے۔ایسے رویوں سے تشدد کی لہر شروع ہوگی۔"
    sentences = sentence_tokenizer(text)
    assert isinstance(sentences, list)


def test_word_tokenizer():
    """
    Test Case
    """
    sentence = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    # sentence2 = "وزیراعظم عمران خان کی مولانا طارق جمیل کو خوش آمدیدکہتے ہوئے " \
    #             "تصاویر انٹرنیٹ پر وائرل ہو گئی ہیں جس میں دیکھا جا سکتا ہے " \
    #             "کہ دونوں رہنماﺅں کے درمیان مناسب فاصلہ ہے اور دونوں ایک دوسرے کو دیکھ کر مسرت کا " \
    #             "اظہار کر رہے ہیں جبکہ وزیراعظم عمران خان نے دل پر ہاتھ رکھ کر ان کا استقبال کیا " \
    #             "۔عمومی طور پر دل پر ہاتھ رکھ کر یا سینے اپنے سینے پر تھپکی دے کر سلام کرنے " \
    #             "کی روایت ترکوں کی ہے جو کہ صدیوں سے چلی آرہی ہے اور یہ نہایت خوبصورت بھی ہے ۔"
    assert isinstance(sentence, str)
    tokens = word_tokenizer(sentence)
    assert isinstance(tokens, list)
    for token in tokens:
        assert isinstance(token, str)
    # with pytest.raises(ValueError):
    #     word_tokenizer(sentence2, 20)


def test_is_token():
    """Test Case"""
    text = "ہم اس کیلئے تیار ہیں لیکن پھرسسٹم لپیٹاجائے ؟کیجئےگا۔"

    model = _load_model(WORD_TOKENIZER_MODEL_PATH)
    pieces = _is_token(model.EncodeAsPieces(text))
    assert "گا" in pieces


def test_is_model_available():
    """Test Case"""
    with pytest.raises(FileNotFoundError):
        _is_model_available(model_path="urduhack/unknown_path_to_models")


def test_load_model():
    """Test Case"""
    model = _load_model(WORD_TOKENIZER_MODEL_PATH)
    assert isinstance(model, spm.SentencePieceProcessor)
