# coding: utf8
"""
Preprocess utilities
"""

import sys
import unicodedata

import regex as re

CURRENCIES = {'$': 'USD', 'zł': 'PLN', '£': 'GBP', '¥': 'JPY', '฿': 'THB',
              '₡': 'CRC', '₦': 'NGN', '₩': 'KRW', '₪': 'ILS', '₫': 'VND',
              '€': 'EUR', '₱': 'PHP', '₲': 'PYG', '₴': 'UAH', '₹': 'INR'}

EMAIL_REGEX = re.compile(
        r"(?:^|(?<=[^\w@.)]))([\w+-](\.(?!\.))?)*?[\w+-]@(?:\w-?)*?\w+(\.([a-z]{2,})){1,3}(?:$|(?=\b))",
        flags=re.IGNORECASE | re.UNICODE)
PHONE_REGEX = re.compile(r'(?:^|(?<=[^\w)]))(\+?1[ .-]?)?(\(?\d{3}\)?[ .-]?)?(\d{3}[ .-]?\d{4})(\s?(?:ext\.?'
                         r'|[#x-])\s?\d{2,6})?(?:$|(?=\W))')
NUMBERS_REGEX = re.compile(r'(?:^|(?<=[^\w,.]))[+–-]?(([1-9]\d{0,2}(,\d{3})+(\.\d*)?)|([1-9]\d{0,2}([ .]\d{3})+(,\d*)?)'
                           r'|(\d*?[.,]\d+)|\d+)(?:$|(?=\b))')
CURRENCY_REGEX = re.compile('({})+'.format('|'.join(re.escape(c) for c in CURRENCIES)))
LINEBREAK_REGEX = re.compile(r'((\r\n)|[\n\v])+')
NONBREAKING_SPACE_REGEX = re.compile(r'(?!\n)\s+')
URL_REGEX = re.compile(r"(?:^|(?<![\w/.]))"
                       # protocol identifier
                       # r"(?:(?:https?|ftp)://)"  <-- alt?
                       r"(?:(?:https?://|ftp://|www\d{0,3}\.))"
                       # user:pass authentication
                       r"(?:\S+(?::\S*)?@)?"
                       r"(?:"
                       # IP address exclusion
                       # private & local networks
                       r"(?!(?:10|127)(?:\.\d{1,3}){3})"
                       r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
                       r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
                       # IP address dotted notation octets
                       # excludes loopback network 0.0.0.0
                       # excludes reserved space >= 224.0.0.0
                       # excludes network & broadcast addresses
                       # (first & last IP address of each class)
                       r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
                       r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
                       r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
                       r"|"
                       # host name
                       r"(?:(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)"
                       # domain name
                       r"(?:\.(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*"
                       # TLD identifier
                       r"(?:\.(?:[a-z\u00a1-\uffff]{2,}))"
                       r")"
                       # port number
                       r"(?::\d{2,5})?"
                       # resource path
                       r"(?:/\S*)?"
                       r"(?:$|(?![\w?!+&/]))",
                       flags=re.UNICODE | re.IGNORECASE)  # source: https://gist.github.com/dperini/729294
SHORT_URL_REGEX = re.compile(r"(?:^|(?<![\w/.]))"
                             # optional scheme
                             r"(?:(?:https?://)?)"
                             # domain
                             r"(?:\w-?)*?\w+(?:\.[a-z]{2,12}){1,3}"
                             r"/"
                             # hash
                             r"[^\s.,?!'\"|+]{2,12}"
                             r"(?:$|(?![\w?!+&/]))",
                             flags=re.IGNORECASE)

PUNCTUATION_TRANSLATE_UNICODE = dict.fromkeys((i for i in range(sys.maxunicode)
                                               if unicodedata.category(chr(i)).startswith('P')), u' ')


def normalize_whitespace(text: str):
    """
    Given ``text`` str, replace one or more spacings with a single space, and one
    or more linebreaks with a single newline. Also strip leading/trailing whitespace.

    Args:
        text (str): raw ``urdu`` text

    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    return NONBREAKING_SPACE_REGEX.sub(' ', LINEBREAK_REGEX.sub(r'\n', text)).strip()


def replace_urls(text: str, replace_with='*URL*'):
    """
    Replace all URLs in ``text`` str with ``replace_with`` str.

    Args:
        text (str): raw ``urdu`` text
        replace_with (str): replace string

    Returns:
        str: returns a ``str`` object replace url with ``replace_with`` text.
    """
    return URL_REGEX.sub(replace_with, SHORT_URL_REGEX.sub(replace_with, text))


def replace_emails(text: str, replace_with='*EMAIL*'):
    """
    Replace all emails in ``text`` str with ``replace_with`` str.

    Args:
        text (str): raw ``urdu`` text
        replace_with (str): replace string

    Returns:
        str: returns a ``str`` object replace emails with ``replace_with`` text.
    """
    return EMAIL_REGEX.sub(replace_with, text)


def replace_phone_numbers(text: str, replace_with='*PHONE*'):
    """
    Replace all phone numbers in ``text`` str with ``replace_with`` str.

    Args:
        text (str): raw ``urdu`` text
        replace_with (str): replace string

    Returns:
        str: returns a ``str`` object replace number_no with ``replace_with`` text.
    """
    return PHONE_REGEX.sub(replace_with, text)


def replace_numbers(text: str, replace_with='*NUMBER*'):
    """
    Replace all numbers in ``text`` str with ``replace_with`` str.

    Args:
        text (str): raw ``urdu`` text
        replace_with (str): replace string

    Returns:
        str: returns a ``str`` object replace number with ``replace_with`` text.
    """
    return NUMBERS_REGEX.sub(replace_with, text)


def replace_currency_symbols(text: str, replace_with=None):
    """
    Replace all currency symbols in ``text`` str with string specified by ``replace_with`` str.

    Args:
        text (str): raw text
        replace_with (str): if None (default), replace symbols with
            their standard 3-letter abbreviations (e.g. '$' with 'USD', '£' with 'GBP');
            otherwise, pass in a string with which to replace all symbols
            (e.g. "*CURRENCY*")
    Returns:
        str: returns a ``str`` object containing normalized text.
    """
    if replace_with is None:
        for key, value in CURRENCIES.items():
            text = text.replace(key, value)
        return text

    return CURRENCY_REGEX.sub(replace_with, text)


def remove_punctuation(text: str, marks=None):
    """
    Remove punctuation from ``text`` by replacing all instances of ``marks``
    with whitespace.

    Args:
        text (str): raw text
        marks (str): If specified, remove only the characters in this string,
            e.g. ``marks=',;:'`` removes commas, semi-colons, and colons.
            Otherwise, all punctuation marks are removed.

    Returns:
        str

    Note:
        When ``marks=None``, Python's built-in :meth:`str.translate()` is
        used to remove punctuation; otherwise, a regular expression is used
        instead. The former's performance is about 5-10x faster.
    """
    if marks:
        return re.sub('[{}]+'.format(re.escape(marks)), ' ', text, flags=re.UNICODE)

    return text.translate(PUNCTUATION_TRANSLATE_UNICODE)


def remove_accents(text: str):
    """
    Remove accents from any accented unicode characters in ``text`` str, either by
    transforming them into ascii equivalents or removing them entirely.

    Args:
        text (str): raw urdu text

    Returns:
        str
    """
    return ''.join(c for c in text if not unicodedata.combining(c))


def remove_english_alphabets(text: str):
    """
    Removes ``English`` words and digits from a ``text``

    Args:
         text (str): raw urdu text

    Returns:
        str: ``str`` object with english alphabets removed
    """
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    table = str.maketrans({key: None for key in characters})
    return text.translate(table)
