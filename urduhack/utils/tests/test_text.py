"""Test Case"""

from ..text import get_code_point, load_vocab


def test_load_vocab():
    """Test Case"""
    assert len(load_vocab()) == 2
    char2idx, idx2char = load_vocab()
    assert isinstance(char2idx, dict)
    assert isinstance(idx2char, dict)
    _extra_vocab = "㐐㑈㒏"
    char2idx, idx2char = load_vocab(_extra_vocab)
    for char in _extra_vocab:
        assert char in char2idx.keys()
        assert char in idx2char.values()

    assert isinstance(idx2char, dict)


def test_get_code_point():
    """Test Case"""
    char = "ﺑ"
    assert isinstance(get_code_point(char), str)
