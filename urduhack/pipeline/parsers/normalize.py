# coding: utf8
"""Parser for performing normalization"""

from urduhack.normalization import normalize
from urduhack.preprocessing import preprocess, normalize_whitespace
from ..parser import Parser


class NormalizeParser(Parser):
    """This parser normalize Urdu text."""

    def _set_up(self, config):
        """Basic setup for parser"""

    def parse(self, document: str) -> str:
        """
        Normalize|Preprocess text

        Args:
            document (str): Urdu text

        Returns:
            str: Return complete urdu document
        """
        return preprocess(normalize(normalize_whitespace(document)))
