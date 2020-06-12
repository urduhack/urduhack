# coding: utf8
"""
Holds custom conll errors. These errors include parsing errors when reading and writing CoNLL objects.
"""


class ParseError(ValueError):
    """
    Error that results from an improper value into a parsing routine.
    """
