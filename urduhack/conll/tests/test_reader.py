"""Test Cases"""

from urduhack.conll.reader import CoNLL
from .test_parser import CONLL_SENTENCE


def test_iter_string():
    """Test Case"""
    for sentence in CoNLL.iter_string(CONLL_SENTENCE):
        sentence_meta, tokens = sentence
        assert isinstance(tokens, list)
        assert sentence_meta['text'] == "والدین معمولی زخمی ہوئے ہےں۔"


def test_load_file(tmpdir):
    """Test Case"""
    file_name = tmpdir.join("test_conll.txt")
    with open(file_name, "w") as file:
        file.write(CONLL_SENTENCE)
    con_reader = CoNLL()
    data = con_reader.load_file(file_name=file_name)
    assert data[0][0]['text'] == "والدین معمولی زخمی ہوئے ہےں۔"


def test_iter_file(tmpdir):
    """Test Case"""
    file_name = tmpdir.join("test_conll.txt")
    with open(file_name, "w") as file:
        file.write(CONLL_SENTENCE)
    con_reader = CoNLL()
    data_iter = con_reader.iter_file(file_name=file_name)
    for data in data_iter:
        sentence = data[0]
        assert sentence['text'] == 'والدین معمولی زخمی ہوئے ہےں۔'
