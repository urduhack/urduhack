# coding: utf8
"""Text Utils"""


def get_code_point(char: str) -> str:
    """
    Get Character unicode codepoint

    Args:
        char (str): single character

    Returns:
        str

    """
    return '%04x' % ord(char)
