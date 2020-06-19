# coding: utf8
"""
Pipeline that runs tokenize
"""
from typing import Dict, List

from .parsers.normalize import NormalizeParser
from .parsers.tokenize import TokenizeParser

NORMALIZE: str = 'normalize'
TOKENIZE: str = 'tokenize'

PIPELINE_NAMES: List = [NORMALIZE, TOKENIZE]
REGISTERED_PARSERS: Dict = {NORMALIZE: NormalizeParser, TOKENIZE: TokenizeParser}


class Pipeline:
    """Pipeline to process"""

    def __init__(self):
        """Pass"""

        self.parsers = {}
        for item in REGISTERED_PARSERS:
            self.parsers[item] = REGISTERED_PARSERS[item](config={}, pipeline=self)

    @property
    def loaded_parsers(self):
        """Return all currently loaded parsers in execution order."""
        return [self.parsers[parser_name] for parser_name in PIPELINE_NAMES if self.parsers.get(parser_name)]

    def parse(self, doc):
        """Tst"""
        for parser_name in PIPELINE_NAMES:
            if self.parsers.get(parser_name):
                doc = self.parsers[parser_name].parse(doc)
        return doc

    def __call__(self, doc):
        assert any([isinstance(doc, str), isinstance(doc, list)]), 'input should be either str or list'
        doc = self.parse(doc)
        return doc
