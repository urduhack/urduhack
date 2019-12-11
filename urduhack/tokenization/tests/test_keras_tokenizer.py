
from ..keras_tokenizer import load_vocab, preprocess_sentences


def test_load_vocab(tmpdir):
    """Test Case"""
    file_name = str(tmpdir.join("vocab.txt"))
    with open(file_name, "w") as f:
        f.write("abcdefghijklmnopqrstuvwxyz")
        f.write("\n")

    assert isinstance(file_name, str) is True
    assert len(load_vocab(file_name)) == 2
    char2idx, idx2char = load_vocab(file_name)
    assert isinstance(char2idx, dict) is True
    assert isinstance(idx2char, dict) is True


def test_preprocess_sentences(tmpdir):
    """Test Case"""
    sentence = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    file_name = str(tmpdir.join("vocab.txt"))
    with open(file_name, "w") as f:
        f.write("ءصأژلضپجعڈفٹگآرنوؤہںاےطھچحۂبغیشزختثڑمئۓذسظقدکۃةABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789،؛٪۔؟٫۸۶۳۷۹۵۲۰۴۱<>=+-*&%^$#@!ﷺٴ`ـ±ﷲﹰ")
        f.write("\n")
    char2idx, _ = load_vocab(file_name)
    assert len(preprocess_sentences(sentence, 46, char2idx)) == 2
    inp_, out_ = preprocess_sentences(sentence, 46, char2idx)
    assert inp_.shape == out_.shape


def test_predict():
    """Test Case"""
    sentence = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    assert isinstance(sentence, str) or isinstance(sentence, list) is True

