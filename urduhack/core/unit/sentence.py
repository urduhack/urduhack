# coding: utf8
"""
Basic data structures
"""

import io
import json
from typing import Tuple
from urduhack.conll.conllable import Conllable

from urduhack.conll import CoNLL
from .token import Token, Word


class Sentence(Conllable):
    """ A sentence class that stores attributes of a sentence and carries a list of tokens.
    """

    def __init__(self, sentence: Tuple[dict, list], doc=None):
        """ Construct a sentence given a dict object which contain sentence meta and
        tokens in the form of CoNLL-U dicts.
        """
        self._tokens = []
        self._words = []
        self._dependencies = []
        self._text = None
        self._ents = []
        self._doc = doc

        self._process(sentence)

    def _process(self, sentence):
        st, en = -1, -1
        self.tokens, self.words = [], []
        sentence_meta, tokens = sentence
        for i, entry in enumerate(tokens):
            if CoNLL.ID not in entry:  # manually set a 1-based id for word if not exist
                entry[CoNLL.ID] = str(i + 1)

            new_word = Word(entry)
            self.words.append(new_word)
            idx = int(entry.get(CoNLL.ID))
            if idx <= en:
                self.tokens[-1].words.append(new_word)
            else:
                self.tokens.append(Token(entry, words=[new_word]))
            new_word.parent = self.tokens[-1]

    @property
    def doc(self):
        """ Access the parent doc of this span. """
        return self._doc

    @doc.setter
    def doc(self, value):
        """ Set the parent doc of this span. """
        self._doc = value

    @property
    def text(self):
        """ Access the raw text for this sentence. """
        return self._text

    @text.setter
    def text(self, value):
        """ Set the raw text for this sentence. """
        self._text = value

    @property
    def tokens(self):
        """ Access the list of tokens for this sentence. """
        return self._tokens

    @tokens.setter
    def tokens(self, value):
        """ Set the list of tokens for this sentence. """
        self._tokens = value

    @property
    def words(self):
        """ Access the list of words for this sentence. """
        return self._words

    @words.setter
    def words(self, value):
        """ Set the list of words for this sentence. """
        self._words = value

    def print_tokens(self, file=None):
        """ Print the tokens for this sentence. """
        for tok in self.tokens:
            print(tok.pretty_print(), file=file)

    def tokens_string(self):
        """ Dump the tokens for this sentence into string. """
        toks_string = io.StringIO()
        self.print_tokens(file=toks_string)
        return toks_string.getvalue().strip()

    def print_words(self, file=None):
        """ Print the words for this sentence. """
        for word in self.words:
            print(word.pretty_print(), file=file)

    def words_string(self):
        """ Dump the words for this sentence into string. """
        wrds_string = io.StringIO()
        self.print_words(file=wrds_string)
        return wrds_string.getvalue().strip()

    def to_dict(self):
        """ Dumps the sentence into a list of dictionary for each token in the sentence.
        """
        ret = []
        for token in self.tokens:
            ret += token.to_dict()
        return ret

    def conll(self):
        """Convert doc object into conll string"""

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
