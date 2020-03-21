"""Test Case"""

from ..text import get_code_point, load_vocab


def test_load_vocab(tmpdir):
    """Test Case"""
    assert len(load_vocab()) == 2
    char2idx, idx2char = load_vocab()
    assert isinstance(char2idx, dict)
    assert isinstance(idx2char, dict)


def test_get_code_point():
    """Test Case"""
    chr = "ﺑ"
    assert isinstance(get_code_point(chr), str)
