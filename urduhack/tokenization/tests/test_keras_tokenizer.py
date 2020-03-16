"""
Test cases for tokenizer
"""

import tensorflow as tf
from ..tokenizer import word_tokenizer
from ..keras_tokenizer import _load_vocab, _preprocess_sentence, _retrieve_words
from ...config import MODEL_PATH, VOCAB_PATH


def test_load_vocab(tmpdir):
    """Test Case"""
    file_name = str(tmpdir.join("vocab.txt"))
    with open(file_name, "w") as f:
        f.write("abcdefghijklmnopqrstuvwxyz")
        f.write("\n")

    assert isinstance(file_name, str)
    assert len(_load_vocab(file_name)) == 2
    char2idx, idx2char = _load_vocab(file_name)
    assert isinstance(char2idx, dict)
    assert isinstance(idx2char, dict)


def test_preprocess_sentence(tmpdir):
    """Test Case"""
    sentence = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    assert isinstance(sentence, str)
    file_name = str(tmpdir.join("vocab.txt"))
    with open(file_name, "w") as f:
        f.write("ءصأژلضپجعڈفٹگآرنوؤہںاےطھچحۂبغیشزختثڑمئۓذسظقدکۃةABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789،؛٪۔؟٫۸۶۳۷۹۵۲۰۴۱<>=+-*&%^$#@!ﷺٴ`ـ±ﷲﹰ")
        f.write("\n")
    char2idx, _ = _load_vocab(file_name)
    assert len(_preprocess_sentence(sentence, char2idx, 46)) == 2
    inp_, out_ = _preprocess_sentence(sentence, char2idx, 46)
    assert inp_.shape == out_.shape


def test_retrieve_words():
    """
    Test Case
    """
    sentence = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    assert isinstance(sentence, str)
    model = tf.keras.models.load_model(MODEL_PATH)
    char2idx, idx2char = _load_vocab(VOCAB_PATH)
    inp_, _ = _preprocess_sentence(sentence, char2idx, max_len=256)
    predictions = model.predict(inp_)
    word_tokens = _retrieve_words(inp_[0, :], predictions[0, :], idx2char)
    assert isinstance(word_tokens, list)
    for word in word_tokens:
        assert isinstance(word, str)


def test_word_tokenizer():
    """
    Test Case
    """
    sentence = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    assert isinstance(sentence, str)
    tokens = word_tokenizer(sentence)
    assert isinstance(tokens, list)
    for token in tokens:
        assert isinstance(token, str)
