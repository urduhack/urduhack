# coding: utf8
"""test cases"""

from ..vocab import create_char_vocab


def test_create_char_vocab():
    """test case"""
    vocab = create_char_vocab()
    assert isinstance(vocab, set)
    for char in vocab:
        assert len(char) == 1

    assert "=" in vocab
    assert "M" in vocab
    assert "(" in vocab
    assert "ﷺ" in vocab
