# coding: utf8
"""Test Cases"""

from urduhack.conll.reader import CoNLL
from .test_parser import CONLL_SENTENCE


def test_get_fields():
    """Test Case"""
    fields = CoNLL.get_fields()
    assert isinstance(fields, list)
    for item in fields:
        assert isinstance(item, str)
    assert len(fields) == 10


def test_iter_string():
    """Test Case"""
    for sentence in CoNLL.iter_string(CONLL_SENTENCE):
        assert isinstance(sentence, tuple)
        sentence_meta, tokens = sentence
        assert isinstance(sentence_meta, dict)
        assert isinstance(tokens, list)
        assert sentence_meta['text'] == "والدین معمولی زخمی ہوئے ہےں۔"
        for token in tokens:
            assert isinstance(token, dict)
            for key, value in token.items():
                assert isinstance(key, str)
                assert isinstance(value, str)

            assert "id" in token.keys()
            assert "text" in token.keys()


def test_load_file(tmpdir):
    """Test Case"""
    file_name = tmpdir.join("test_conll.conll")
    with open(file_name, "w", encoding="utf8") as file:
        file.write(CONLL_SENTENCE)

    data = CoNLL.load_file(file_name=file_name)
    assert isinstance(data, list)
    assert data[0][0]['text'] == "والدین معمولی زخمی ہوئے ہےں۔"


def test_iter_file(tmpdir):
    """Test Case"""
    file_name = tmpdir.join("test_conll.txt")
    with open(file_name, "w", encoding="utf8") as file:
        file.write(CONLL_SENTENCE)

    data_iter = CoNLL.iter_file(file_name=file_name)
    for data in data_iter:
        sentence = data[0]
        assert sentence['text'] == 'والدین معمولی زخمی ہوئے ہےں۔'
