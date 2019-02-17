# coding: utf8
"""
Text Preprocessing module
--------------------------

The pre-processing of Urdu text is necessary to make it useful for the machine
learning tasks.
This module provides the following functionality:

    - Normalize whitespace
    - Replace urls,emails,number,phone_no,currency_symbols
"""
from .util import (normalize_whitespace, replace_urls, replace_emails, replace_numbers, replace_phone_numbers,
                   replace_currency_symbols, )

__all__ = ["normalize_whitespace", "replace_urls",
           "replace_emails", "replace_numbers", "replace_phone_numbers",
           "replace_currency_symbols"]
