# coding: utf8
"""Parser for performing ner detection"""

from urduhack.models.ner import predict_ner

from ..parser import Parser


class NerParser(Parser):
    """This parser add pos tags for Urdu text."""

    def _set_up(self, config):
        """pass"""

    def parse(self, document):
        """Function to normalize|preprocess text"""

        for sentence in document.sentences:
            tags = predict_ner(sentence.text)

            assert len(tags) == len(sentence.tokens), " Error in Ner tags"
            for tag, token in zip(tags, sentence.tokens):
                if tag[0] == token.text:
                    setattr(token, "ner", tag[1])

        return document
