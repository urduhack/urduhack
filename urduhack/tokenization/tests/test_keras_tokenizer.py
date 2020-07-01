"""
Test cases for tokenizer
"""

import pytest
import tensorflow as tf

from ..keras_tokenizer import _load_vocab, _preprocess_sentence, _retrieve_words, _is_model_exist
from ..tokenizer import sentence_tokenizer, word_tokenizer
from ...config import WORD_TOKENIZER_MODEL_PATH, WORD_TOKENIZER_VOCAB_PATH


def test_load_vocab(tmpdir):
    """Test Case"""
    file_name = str(tmpdir.join("vocab.txt"))
    with open(file_name, "w", encoding="utf-8") as tmp_file:
        tmp_file.write("abcdefghijklmnopqrstuvwxyz")
        tmp_file.write("\n")

    assert isinstance(file_name, str)
    assert len(_load_vocab(file_name)) == 2
    assert isinstance(_load_vocab(file_name), tuple)
    char2idx, idx2char = _load_vocab(file_name)
    assert isinstance(char2idx, dict)
    assert isinstance(idx2char, dict)


def test_preprocess_sentence(tmpdir):
    """Test Case"""
    sentence = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    assert isinstance(sentence, str)
    file_name = str(tmpdir.join("vocab.txt"))
    with open(file_name, "w", encoding="utf-8") as tmp_file:
        tmp_file.write("ءصأژلضپجعڈفٹگآرنوؤہںاےطھچحۂبغیشزختثڑمئۓذسظقدکۃةABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij"
                       "klmnopqrstuvwxyz0123456789،؛٪۔؟٫۸۶۳۷۹۵۲۰۴۱<>=+-*&%^$#@!ﷺٴ`ـ±ﷲﹰ")
        tmp_file.write("\n")
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
    model = tf.keras.models.load_model(WORD_TOKENIZER_MODEL_PATH)
    char2idx, idx2char = _load_vocab(WORD_TOKENIZER_VOCAB_PATH)
    inp_, _ = _preprocess_sentence(sentence, char2idx, max_len=256)
    predictions = model.predict(inp_)
    word_tokens = _retrieve_words(inp_[0, :], predictions[0, :], idx2char)
    assert isinstance(word_tokens, list)
    for word in word_tokens:
        assert isinstance(word, str)


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


def test_is_model_exist():
    """Test Case"""
    with pytest.raises(FileNotFoundError):
        _is_model_exist(model_path="urduhack/unknown_path_to_models", vocab_path="urduhack/unknown_path_to_models")
