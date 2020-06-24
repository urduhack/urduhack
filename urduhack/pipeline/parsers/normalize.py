# coding: utf8
"""Parser for performing normalization"""

from urduhack.normalization import normalize
from urduhack.preprocessing import normalize_whitespace
from ..parser import Parser


class NormalizeParser(Parser):
    """This parser normalize Urdu text."""

    def _set_up(self, config):
        """pass"""

    def parse(self, document):
        """Function to normalize text"""
        return normalize_whitespace(normalize(document))
