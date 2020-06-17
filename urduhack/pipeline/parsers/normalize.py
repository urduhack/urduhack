# coding: utf8
"""Parser for performing normalization"""

from urduhack import normalize
from ..parser import Parser


# class for running the tokenizer
class NormalizeParser(Parser):
    """Test"""

    def _set_up(self, config):
        pass

    def parse(self, text):
        """nothing"""
        return normalize(text)
