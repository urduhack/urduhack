# coding: utf8
"""about.py test cases"""
import regex as re

from ..about import __version__, __description__, __author__, __author_email__, __license__, __url__, get_info


def test_version():
    """Version test cases"""
    assert isinstance(__version__, str)
    assert re.match(r'\b\d{1,2}\.\d{1,2}\.\d{1,2}\b', __version__)


def test_description():
    """test cases"""
    assert isinstance(__description__, str)


def test_author():
    """test cases"""
    assert isinstance(__author__, str)


def test_author_email():
    """test cases"""
    assert isinstance(__author_email__, str)
    assert "@" in __author_email__


def test_license():
    """test cases"""
    assert isinstance(__license__, str)


def test_url():
    """test cases"""
    assert isinstance(__url__, str)
    assert '.' in __url__


def test_get_info():
    """Test get info function"""
    data = get_info()
    assert isinstance(data, dict)
    for value in data.values():
        assert isinstance(value, str)
    keys = ("Urduhack version", "Location", "Python version", "Platform")
    for _key in keys:
        assert _key in data.keys()
