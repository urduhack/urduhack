# coding: utf8
"""Test cases"""

from ..util import (normalize_whitespace, replace_urls, replace_emails, replace_phone_numbers, replace_numbers,
                    replace_currency_symbols, remove_accents, remove_punctuation, )


def test_normalize_whitespace():
    """Test case"""
    text = "میاں, صاف!  میاں...\t \tصاف?\n\nمیاں:\r\n\n\nصاف. "
    proc_text = "میاں, صاف! میاں... صاف?\nمیاں:\nصاف."
    assert normalize_whitespace(text) == proc_text


def test_replace_urls():
    """Test case"""
    text = "www.stackoverflow.com || http://wikipedia.org"
    proc_text = "*URL* || *URL*"
    assert replace_urls(text, '*URL*') == proc_text


def test_replace_emails():
    """Test case"""
    text = "یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ username@example.com میں ہوا تھا"
    proc_text = "یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ *EMAIL* میں ہوا تھا"
    assert replace_emails(text, '*EMAIL*') == proc_text


def test_replace_phone_numbers():
    """Test case"""
    text = "یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ 555-123-4567 میں ہوا تھا"
    proc_text = "یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ *PHONE* میں ہوا تھا"
    assert replace_phone_numbers(text, '*PHONE*') == proc_text


def test_replace_numbers():
    """Test case"""
    text = "یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ 2003 میں ہوا 33 تھا۔"
    proc_text = "یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ *NUM* میں ہوا *NUM* تھا۔"
    assert replace_numbers(text, '*NUM*') == proc_text


def test_replace_currency_symbols():
    """Test case"""
    tests = [
        ('$1.00 equals £0.67 equals €0.91.',
         'USD1.00 equals GBP0.67 equals EUR0.91.',
         '*CUR* 1.00 equals *CUR* 0.67 equals *CUR* 0.91.'),
        ('this zebra costs $100.',
         'this zebra costs USD100.',
         'this zebra costs *CUR* 100.'),
    ]
    for text, proc_text1, proc_text2 in tests:
        assert replace_currency_symbols(text, replace_with=None) == proc_text1
        assert replace_currency_symbols(text, replace_with='*CUR* ') == proc_text2


def test_remove_accents():
    """Test case"""
    text = "دالتِ عظمیٰ درخواست"
    proc_text = "دالت عظمی درخواست"
    assert remove_accents(text) == proc_text


def test_remove_punctuation():
    """Test case"""
    text = "کر  ؟ سکتی ہے۔ علینا نے"
    proc_text = "کر    سکتی ہے  علینا نے"
    assert remove_punctuation(text) == proc_text
