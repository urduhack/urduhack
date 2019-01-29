# coding: utf8
"""Text Utils"""

import regex as re

from ..urdu_characters import URDU_DIACRITICS

DIACRITICS_RE = re.compile(f'[{"".join(URDU_DIACRITICS)}]', flags=re.U | re.M | re.I)


def get_code_point(char: str) -> str:
    """
    Get Character unicode codepoint

    Args:
        char (str): single character

    Returns:
        str

    """
    return '%04x' % ord(char)


def remove_diacritics(text: str) -> str:
    """
    Remove Urdu diacritics from text

    Args:
        text (str): base string

    Returns:
        str
    """
    return DIACRITICS_RE.sub('', text)
