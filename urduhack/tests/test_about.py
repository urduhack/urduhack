# coding: utf8
"""about.py test cases"""
import regex as re
from urduhack.about import __version__, DESCRIPTION


def test_version():
    """Version test cases"""
    assert isinstance(__version__, str)
    assert re.match(r'\b\d{1,2}\.\d{1,2}\.\d{1,2}\b', __version__)


def test_description():
    """test cases"""
    assert isinstance(DESCRIPTION, str)
