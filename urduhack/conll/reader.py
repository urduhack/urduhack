# coding: utf8
"""A minimal module to parse CoNLL files."""

from urduhack.conll.parser import _iter_lines


class CoNLL:
    """
    A Conll class to easily load conll-u formats. This module can also load resources by iterating over string.
    This module is the main entrance to pyconll's functionalities.

    Example:
        >>> from urduhack.conll import CoNLL
        >>> conll_reader = CoNLL()
        >>> conll_data = conll_reader.load_file(file_name='example.conll')
    """
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
    def load_file(file_name: str) -> list:
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

    @staticmethod
    def iter_file(file_name: str) -> str:
        """
        Iterate over a CoNLL-U file's sentences.

        Args:
            file_name (str): The name of the file whose sentences should be iterated over.

        Yields:
            The sentences that make up the CoNLL-U file.

        Raises:
            IOError if there is an error opening the file.
            ParseError: If there is an error parsing the input into a Conll object.
        """
        with open(file_name, encoding='utf8') as file:
            for sentence in _iter_lines(file):
                yield sentence

    @staticmethod
    def iter_from_string(text: str) -> str:
        """
        Iterate over a CoNLL-U string's sentences.

        Use this method if you only need to iterate over the CoNLL-U file once and
        do not need to create or store the Conll object.

        Args:
            text (str): The CoNLL-U string.

        Yields:
            The sentences that make up the CoNLL-U file.

        Raises:
            ParseError: If there is an error parsing the input into a Conll object.
        """
        lines = text.splitlines()
        for sentence in _iter_lines(lines):
            yield sentence
