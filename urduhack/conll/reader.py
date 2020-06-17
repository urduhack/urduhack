# coding: utf8
"""A minimal module to parse CoNLL files."""

from typing import Tuple, List, Iterator

from urduhack.conll.parser import _iter_lines, _load_file


class CoNLL:
    """
    A Conll class to easily load conll-u formats. This module can also load resources by iterating over string.
    This module is the main entrance to conll's functionalities.
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

    COMMENT_MARKER = '#'
    FIELD_DELIMITER = '\t'
    EMPTY = '_'

    @staticmethod
    def get_fields() -> List[str]:
        """
        Get the list of conll fields

        Returns:
            List[str]: Return list of conll fields
        """
        return [
            CoNLL.ID,
            CoNLL.TEXT,
            CoNLL.LEMMA,
            CoNLL.UPOS,
            CoNLL.XPOS,
            CoNLL.FEATS,
            CoNLL.HEAD,
            CoNLL.DEPREL,
            CoNLL.DEPS,
            CoNLL.MISC
        ]

    @staticmethod
    def load_file(file_name: str) -> List[Tuple]:
        """
        Load a CoNLL-U file given its location.

        Args:
            file_name (str): The location of the file.
        Returns:
           List[Tuple]: A Conll object equivalent to the provided file.
        Raises:
            IOError: If there is an error opening the given filename.
            ValueError: If there is an error parsing the input into a Conll object.
        """
        return _load_file(file_name)

    @staticmethod
    def iter_file(file_name: str) -> Iterator[Tuple]:
        """
        Iterate over a CoNLL-U file's sentences.

        Args:
            file_name (str): The name of the file whose sentences should be iterated over.
        Yields:
            Iterator[Tuple]: The sentences that make up the CoNLL-U file.
        Raises:
            IOError: If there is an error opening the file.
            ParseError: If there is an error parsing the input into a Conll object.
        """
        with open(file_name, encoding='utf8') as file:
            for sentence in _iter_lines(file):
                yield sentence

    @staticmethod
    def iter_string(text: str) -> Iterator[Tuple]:
        """
        Iterate over a CoNLL-U string's sentences.

        Use this method if you only need to iterate over the CoNLL-U file once and
        do not need to create or store the Conll object.

        Args:
            text (str): The CoNLL-U string.
        Yields:
            Iterator[Tuple]: The sentences that make up the CoNLL-U file.
        Raises:
            ParseError: If there is an error parsing the input into a Conll object.
        """
        lines = text.splitlines()
        for sentence in _iter_lines(lines):
            yield sentence
