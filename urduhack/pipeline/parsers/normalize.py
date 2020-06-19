# coding: utf8
"""Parser for performing normalization"""

from urduhack import normalize
from ..parser import Parser


# class for running the tokenizer
class NormalizeParser(Parser):
    """pass"""

    def _set_up(self, config):
        """pass"""


    def parse(self, document):
        """pass"""
        return normalize(document)
