"""Test Case"""

from ..text import get_code_point


def test_get_code_point():
    """Test Case"""
    chr = "ﺑ"
    assert isinstance(get_code_point(chr), str)