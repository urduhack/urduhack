# coding: utf8
"""test case"""
import pytest

from urduhack.urdu_characters import URDU_ALPHABETS, URDU_ALL_CHARACTERS

from ..eos import URDU_CONJUNCTIONS, URDU_NEWLINE_WORDS, _generate_sentences
from ..words import WORDS_SPACE, fix_join_words


def test_conjunctions_newline_words():
    """Test case"""
    for word in URDU_CONJUNCTIONS:
        for char in word:
            assert char in URDU_ALPHABETS

    for word in URDU_NEWLINE_WORDS:
        for char in word:
            assert char in URDU_ALPHABETS


def test_words_space():
    """Test case"""
    for key, value in WORDS_SPACE.items():
        for char in key:
            if char == ' ':
                continue
            assert char in URDU_ALL_CHARACTERS
        for char in value:
            if char == ' ':
                continue
            assert char in URDU_ALL_CHARACTERS


def test_generate_sentences():
    """Test Case"""
    text = "ہم اس کیلئے تیار ہیں لیکن پھرسسٹم لپیٹاجائے ؟کیجئے گا۔قومی اسمبلی کے اجلاس میں خطاب کرتے ہوئے۔ایسے رویوں سے تشدد کی لہر شروع ہوگی۔"
    text1 = ""
    text2 = "ہم اس کیلئے تیار ہیں لیکن پھرسسٹم لپیٹاجائےکیجئے گا n\ ۔"
    assert len(_generate_sentences(text1)) == 0
    assert isinstance(text, str)
    assert isinstance(text2, str)
    sentences = _generate_sentences(text)
    sentences2 = _generate_sentences(text2)
    assert isinstance(sentences, list)
    assert isinstance(sentences2, list)
    with pytest.raises(TypeError, match=r'[E001]'):
        _generate_sentences(text=123)


def test_fix_join_words():
    """Test Case"""
    text = "پرویز خٹک اس کیلئے تیار ہیں"
    joined = fix_join_words(text)
    assert isinstance(joined, str)