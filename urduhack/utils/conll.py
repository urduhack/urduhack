# coding: utf8
"""Conll-u format reader {https://universaldependencies.org/format.html}"""

import pyconll
from pyconll.unit.conll import Conll


class CoNLL:
    """Conll format reader"""

    @staticmethod
    def load_from_file(file_name: str) -> Conll:
        """
        Load a CoNLL-U file given its location.

        Args:
            file_name (str): The location of the file.

        Returns:
            A Conll object equivalent to the provided file.
        """
        return pyconll.load_from_file(file_name)
