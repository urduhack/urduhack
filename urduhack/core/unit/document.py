# coding: utf8
"""
Document data structure
"""

import json
from typing import List, Tuple

from urduhack.conll.conllable import Conllable
from .sentence import Sentence


class Document(Conllable):
    """ A document class that stores attributes of a document and carries a list of sentences."""

    def __init__(self, sentences: List[Tuple[dict, list]], text: str = None):
        """ Construct a document given a list of sentences in the form of lists of CoNLL-U dicts.

        Args:
            sentences (list): List of sentences, which being a tuple of dict, list of token entry (CoNLL-U dict).
            text (str): Urdu text of the document.
        """
        self._sentences: list = []
        self._text: str = text
        self._num_tokens: int = 0
        self._num_words: int = 0
        self._process(sentences)

    @property
    def text(self) -> str:
        """
        Access the Urdu text for this document.

        Returns:
            str: Document text
        """
        return self._text

    @property
    def sentences(self) -> list:
        """ Access the list of sentences for this document. """
        return self._sentences

    @property
    def num_tokens(self) -> int:
        """ Access the number of tokens for this document. """
        return self._num_tokens

    @num_tokens.setter
    def num_tokens(self, value):
        """ Set the number of tokens for this document. """
        self._num_tokens = value

    @property
    def num_words(self) -> int:
        """ Access the number of words for this document. """
        return self._num_words

    @num_words.setter
    def num_words(self, value):
        """ Set the number of words for this document. """
        self._num_words = value

    def _process(self, sentences):
        """process sentences in to words and tokens"""
        for sentence in sentences:
            self.sentences.append(Sentence(sentence, doc=self))
            begin_idx, end_idx = self.sentences[-1].tokens[0].start_char, self.sentences[-1].tokens[-1].end_char
            if all([self.text is not None, begin_idx is not None, end_idx is not None]):
                self.sentences[-1].text = self.text[begin_idx: end_idx]

        self.num_tokens = sum([len(sentence.tokens) for sentence in self.sentences])
        self.num_words = sum([len(sentence.words) for sentence in self.sentences])

    def get(self, fields, as_sentences=False, from_token=False):
        """ Get fields from a list of field names. If only one field name is provided, return a list
        of that field; if more than one, return a list of list. Note that all returned fields are after
        multi-word expansion.

        Args:
            fields (list): name of the fields as a list
            as_sentences (bool): if True, return the fields as a list of sentences; otherwise as a whole list
            from_token (bool): if True, get the fields from Token; otherwise from Word

        Returns:
            list: All requested fields.
        """
        assert isinstance(fields, list), "Must provide field names as a list."
        assert len(fields) >= 1, "Must have at least one field."

        results = []
        for sentence in self.sentences:
            cursent = []
            # decide word or token
            if from_token:
                units = sentence.tokens
            else:
                units = sentence.words
            for unit in units:
                if len(fields) == 1:
                    cursent += [getattr(unit, fields[0])]
                else:
                    cursent += [[getattr(unit, field) for field in fields]]

            # decide whether append the results as a sentence or a whole list
            if as_sentences:
                results.append(cursent)
            else:
                results += cursent
        return results

    def set(self, fields, contents, to_token=False):
        """ Set fields based on contents. If only one field (singleton list) is provided, then a list
        of content will be expected; otherwise a list of list of contents will be expected.

        Args:
            fields (list): name of the fields as a list
            contents (list): field values to set; total length should be equal to number of words/tokens
            to_token (bool): if True, set field values to tokens; otherwise to words
        """
        assert isinstance(fields, list), "Must provide field names as a list."
        assert isinstance(contents, list), "Must provide contents as a list (one item per line)."
        assert len(fields) >= 1, "Must have at least one field."

        assert (to_token and self.num_tokens == len(contents)) or self.num_words == len(contents), \
            "Contents must have the same number as the original file."

        cidx = 0
        for sentence in self.sentences:
            # decide word or token
            if to_token:
                units = sentence.tokens
            else:
                units = sentence.words
            for unit in units:
                if len(fields) == 1:
                    setattr(unit, fields[0], contents[cidx])
                else:
                    for field, content in zip(fields, contents[cidx]):
                        setattr(unit, field, content)
                cidx += 1

    def iter_words(self):
        """ An iterator that returns all of the words in this Document. """
        for sentence in self.sentences:
            yield from sentence.words

    def iter_tokens(self):
        """ An iterator that returns all of the tokens in this Document. """
        for sentence in self.sentences:
            yield from sentence.tokens

    def to_dict(self) -> list:
        """ Dumps the whole document into a list of list of dictionary for each token in each sentence in the doc.
        """
        return [sentence.to_dict() for sentence in self.sentences]

    def conll(self) -> str:
        """
        Output the Conll object to a CoNLL-U formatted string.

        Returns:
            str: The CoNLL-U object as a string. This string will end in a newline.
        """
        # Add newlines along with sentence strings so that there is no need to
        # slice potentially long lists or modify strings.
        components = list(map(lambda sent: sent.conll(), self.sentences))
        components.append('')

        return '\n\n'.join(components)

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
