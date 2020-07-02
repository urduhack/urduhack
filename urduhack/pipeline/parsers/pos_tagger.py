# coding: utf8
"""Parser for performing normalization"""

from urduhack.conll import CoNLL
from urduhack.models.pos_tagger import predict_tags

from ..parser import Parser


class PosTaggerParser(Parser):
    """This parser add pos tags for Urdu text."""

    def _set_up(self, config):
        """pass"""

    def parse(self, document):
        """Function to normalize|preprocess text"""

        for sentence in document.sentences:
            tags = predict_tags(sentence.text)

            assert len(tags) == len(sentence.words), " Error in post tags"
            for tag, word in zip(tags, sentence.words):
                if tag[0] == word.text:
                    setattr(word, CoNLL.UPOS, tag[1])

        return document
