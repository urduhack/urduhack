# coding: utf8
"""A minimal module to parse CoNLL files."""

from enum import Enum

from urduhack.conll.parser import _iter_lines


class CoNLL(Enum):
    """A Conll class to easily load conll-u formats. This module can also load resources by iterating over string.
    This module is the main entrance to pyconll's functionalities."""
    ID = 'id'
    TEXT = 'text'
    LEMMA = 'lemma'
    UPOS = 'upos'
    XPOS = 'xpos'
    FEATS = 'feats'
    HEAD = 'head'
    DEPREL = 'deprel'
    DEPS = 'deps'
    MISC = 'misc'

    @staticmethod
    def load_from_file(file_name: str):
        """
        Load a CoNLL-U file given its location.

        Args:
            file_name (str): The location of the file.

        Returns:
            A Conll object equivalent to the provided file.

        Raises:
            IOError: If there is an error opening the given filename.
            ParseError: If there is an error parsing the input into a Conll object.
        """
        _sentences = []
        with open(file_name, encoding='utf8') as file:
            for sentence in _iter_lines(file):
                _sentences.append(sentence)

        return _sentences
