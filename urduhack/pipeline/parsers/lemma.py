# coding: utf8
"""Parser for lemmatization"""

from urduhack.conll import CoNLL
from urduhack.models.lemmatizer.lemmatizer import lemma_lookup

from ..parser import Parser


class LemmaParser(Parser):
    """This parser add pos tags for Urdu text."""

    def _set_up(self, config):
        """pass"""

    def parse(self, document):
        """Function to normalize|preprocess text"""

        for sentence in document.sentences:
            lemmas = lemma_lookup(sentence.text)

            assert len(lemmas) == len(sentence.words), " Error in post tags"
            for lemma, word in zip(lemmas, sentence.words):
                if lemma[0] == word.text:
                    setattr(word, CoNLL.LEMMA, lemma[1])

        return document
