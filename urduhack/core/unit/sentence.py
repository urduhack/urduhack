# coding: utf8
"""
Sentence data structures
"""
import json
import operator
from typing import Tuple

from urduhack.conll import CoNLL
from urduhack.conll.conllable import Conllable
from .token import Token, Word


class Sentence(Conllable):
    """ A sentence class that stores attributes of a sentence and carries a list of tokens.
    """

    def __init__(self, sentence: Tuple[dict, list], doc=None):
        """ Construct a sentence given a dict object which contain sentence meta and
        tokens in the form of CoNLL-U dicts.
        """
        self._meta = {}
        self._tokens = []
        self._words = []
        self._dependencies = []
        self._text = None
        self._ents = []
        self._doc = doc

        self._process(sentence)

    def meta_value(self, key: str) -> str:
        """
        Returns the value associated with the key in the metadata (comments).

        Args:
            key (str): The key whose value to look up.
        Returns:
            str: The value associated with the key as a string. If the key is a singleton then None is returned.
        Raises:
            KeyError: If the key is not present in the comments.
        """
        return self._meta[key]

    def meta_present(self, key: str) -> bool:
        """
        Check if the key is present as a singleton or as a pair.

        Args:
            key (str): The value to check for in the comments.
        Returns:
            bool: True if the key was provided as a singleton or as a key value pair. False otherwise.
        """
        return key in self._meta

    def set_meta(self, key: str, value: str = None):
        """
        Set the metadata or comments associated with this Sentence.

        Args:
            key (str): The key for the comment.
            value (str): The value to associate with the key. If the comment is a
                singleton, this field can be ignored or set to None.
        """
        self._meta[key] = value

    def _process(self, sentence):
        e_n = -1
        self.tokens, self.words = [], []
        sentence_meta, tokens = sentence

        for key, value in sentence_meta.items():
            self.set_meta(key, value)

        for i, entry in enumerate(tokens):
            if CoNLL.ID not in entry:  # manually set a 1-based id for word if not exist
                entry[CoNLL.ID] = str(i + 1)

            new_word = Word(entry)
            self.words.append(new_word)
            idx = int(entry.get(CoNLL.ID))
            if idx <= e_n:
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
    def text(self) -> str:
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

    def to_dict(self):
        """ Dumps the sentence into a list of dictionary for each token in the sentence.
        """
        ret = []
        for token in self.tokens:
            ret += token.to_dict()
        return ret

    def conll(self) -> str:
        """
        Convert the sentence to a CoNLL-U representation.

        Returns:
            str: A string representing the Sentence in CoNLL-U format.
        """
        if not self.meta_present("text") and self.text is not None:
            self.set_meta("text", self.text)

        lines = []
        sorted_meta = sorted(self._meta.items(), key=operator.itemgetter(0))
        for meta in sorted_meta:
            if meta[1] is not None:
                line = f'{CoNLL.COMMENT_MARKER} {meta[0]} = {meta[1]}'
            else:
                line = f'{CoNLL.COMMENT_MARKER} {meta[0]}'

            lines.append(line)

        for word in self.words:
            lines.append(word.conll())

        return '\n'.join(lines)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
