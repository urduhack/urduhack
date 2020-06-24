# coding: utf8
"""
Text PreProcessing
===================

The pre-processing of Urdu text is necessary to make it useful for the machine
learning tasks.
This module provides the following functionality:

    - Normalize whitespace
    - Replace urls
    - Replace emails
    - Replace number
    - Replace phone_number
    - Replace currency_symbols

You can look for all the different functions that come with pre-process
module in the reference here :py:mod:`~urduhack.preprocess`.

"""
from .util import (normalize_whitespace, replace_urls, replace_emails, replace_numbers, replace_phone_numbers,
                   replace_currency_symbols, remove_punctuation, remove_accents, remove_english_alphabets)

__all__ = ["normalize_whitespace", "remove_punctuation", "remove_accents", "replace_urls",
           "replace_emails", "replace_numbers", "replace_phone_numbers",
           "replace_currency_symbols", "remove_english_alphabets", ]
