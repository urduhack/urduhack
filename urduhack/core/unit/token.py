# coding: utf8
"""
Token, Word data structures
"""
import json
import unicodedata
from typing import Dict

from urduhack.conll import CoNLL
from urduhack.conll.conllable import Conllable
from urduhack.stop_words import STOP_WORDS

NER = 'ner'
START_CHAR = 'start_char'
END_CHAR = 'end_char'
TYPE = 'span_type'


class Token:
    """ A token class that stores attributes of a token and carries a list of words. A token corresponds to a unit in
     the raw
    text. In some languages such as English, a token has a one-to-one mapping to a word, while in other languages such
     as French,
    a (multi-word) token might be expanded into multiple words that carry syntactic annotations.
    """

    def __init__(self, token_entry: Dict, words=None):
        """ Construct a token given a dictionary format token entry. Optionally link itself to the corresponding words.
        """
        assert token_entry.get(CoNLL.ID) and token_entry.get(CoNLL.TEXT), 'id and text should be included for the token'
        self._id, self._text, self._misc, self._words, self._start_char, self._end_char, self._ner = [None] * 7

        self.id = token_entry.get(CoNLL.ID)
        self.text = token_entry.get(CoNLL.TEXT)
        self.misc = token_entry.get(CoNLL.MISC, None)
        self.ner = token_entry.get(NER, None)
        self.words = words if words is not None else []

        if self.misc is not None:
            self.init_from_misc()

    def init_from_misc(self):
        """ Create attributes by parsing from the `misc` field."""
        for item in self._misc.split('|'):
            key_value = item.split('=', 1)
            if len(key_value) == 1:
                continue  # some key_value can not be splited
            key, value = key_value
            if key in [START_CHAR, END_CHAR]:
                value = int(value)
            # set attribute
            attr = f'_{key}'
            if hasattr(self, attr):
                setattr(self, attr, value)

    @property
    def id(self):
        """ Access the index of this token. """
        return self._id

    @id.setter
    def id(self, value):
        """ Set the token's id value. """
        self._id = value

    @property
    def text(self):
        """ Access the text of this token. Example: 'The' """
        return self._text

    @text.setter
    def text(self, value):
        """ Set the token's text value. Example: 'The' """
        self._text = value

    @property
    def misc(self):
        """ Access the miscellaneousness of this token. """
        return self._misc

    @misc.setter
    def misc(self, value):
        """ Set the token's miscellaneousness value. """
        if self._is_null(value):
            value = None

        self._misc = value
        # self._misc = value if self._is_null(value) == False else None

    @property
    def words(self):
        """ Access the list of syntactic words underlying this token. """
        return self._words

    @words.setter
    def words(self, value):
        """ Set this token's list of underlying syntactic words. """
        self._words = value
        for word in self._words:
            word.parent = self

    @property
    def start_char(self):
        """ Access the start character index for this token in the raw text. """
        return self._start_char

    @property
    def end_char(self):
        """ Access the end character index for this token in the raw text. """
        return self._end_char

    @property
    def ner(self):
        """ Access the NER tag of this token. Example: 'B-ORG'"""
        return self._ner

    @ner.setter
    def ner(self, value):
        """ Set the token's NER tag. Example: 'B-ORG'"""
        if self._is_null(value):
            value = None

        self._ner = value

        # self._ner = value if self._is_null(value) == False else None

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def to_dict(self):
        """ Dumps the token into a list of dictionary for this token with its extended words
        if the token is a multi-word token.
        """
        ret = []
        for word in self.words:
            ret.append(word.to_dict())
        return ret

    def _is_null(self, value):
        return (value is None) or (value == '_')

    @property
    def is_stop(self) -> bool:
        """
        Check the token is stop_word

        Returns:
            bool: Return true|False
        """
        return self.text in STOP_WORDS

    @property
    def is_punct(self) -> bool:
        """
        Check the token is punct

        Returns:
            bool: Return true|False
        """
        for char in self.text:
            if not unicodedata.category(char).startswith('P'):
                return False
        return True


class Word(Conllable):
    """ A word class that stores attributes of a word.
    """

    def __init__(self, word_entry: Dict):
        """ Construct a word given a dictionary format word entry.
        """
        assert word_entry.get(CoNLL.ID) and word_entry.get(CoNLL.TEXT), 'id and text should be included for the' \
                                                                        ' word. {}'.format(word_entry)
        self._id, self._text, self._lemma, self._upos, self._xpos, self._feats, self._head, self._deprel, self._deps, \
        self._misc, self._parent = [None] * 11

        self.id = word_entry.get(CoNLL.ID)
        self.text = word_entry.get(CoNLL.TEXT)
        self.lemma = word_entry.get(CoNLL.LEMMA, None)
        self.upos = word_entry.get(CoNLL.UPOS, None)
        self.xpos = word_entry.get(CoNLL.XPOS, None)
        self.feats = word_entry.get(CoNLL.FEATS, None)
        self.head = word_entry.get(CoNLL.HEAD, None)
        self.deprel = word_entry.get(CoNLL.DEPREL, None)
        self.deps = word_entry.get(CoNLL.DEPS, None)
        self.misc = word_entry.get(CoNLL.MISC, None)

        if self.misc is not None:
            self.init_from_misc()

    def init_from_misc(self):
        """ Create attributes by parsing from the `misc` field.
        """
        for item in self._misc.split('|'):
            key_value = item.split('=', 1)
            if len(key_value) == 1:
                continue  # some key_value can not be splited
            key, value = key_value
            # set attribute
            attr = f'_{key}'
            if hasattr(self, attr):
                setattr(self, attr, value)

    @property
    def id(self):
        """ Access the index of this word. """
        return self._id

    @id.setter
    def id(self, value):
        """ Set the word's index value. """
        self._id = value

    @property
    def text(self):
        """ Access the text of this word. Example: 'The'"""
        return self._text

    @text.setter
    def text(self, value):
        """ Set the word's text value. Example: 'The'"""
        self._text = value

    @property
    def lemma(self):
        """ Access the lemma of this word. """
        return self._lemma

    @lemma.setter
    def lemma(self, value):
        """ Set the word's lemma value. """
        if self._is_null(value) or self._text == '_':
            value = None

        self._lemma = value
        # self._lemma = value if self._is_null(value) == False or self._text == '_' else None

    @property
    def upos(self):
        """ Access the universal part-of-speech of this word. Example: 'NOUN'"""
        return self._upos

    @upos.setter
    def upos(self, value):
        """ Set the word's universal part-of-speech value. Example: 'NOUN'"""
        if self._is_null(value):
            value = None

        self._upos = value
        # self._upos = value if self._is_null(value) == False else None

    @property
    def xpos(self):
        """ Access the treebank-specific part-of-speech of this word. Example: 'NNP'"""
        return self._xpos

    @xpos.setter
    def xpos(self, value):
        """ Set the word's treebank-specific part-of-speech value. Example: 'NNP'"""
        if self._is_null(value):
            value = None

        self._xpos = value
        # self._xpos = value if self._is_null(value) == False else None

    @property
    def feats(self):
        """ Access the morphological features of this word. Example: 'Gender=Fem'"""
        return self._feats

    @feats.setter
    def feats(self, value):
        """ Set this word's morphological features. Example: 'Gender=Fem'"""
        if self._is_null(value):
            value = None

        self._feats = value
        # self._feats = value if self._is_null(value) == False else None

    @property
    def head(self):
        """ Access the id of the governer of this word. """
        return self._head

    @head.setter
    def head(self, value):
        """ Set the word's governor id value. """
        if self._is_null(value):
            self._head = None
        else:
            self._head = int(value)
        # self._head = int(value) if self._is_null(value) == False else None

    @property
    def deprel(self):
        """ Access the dependency relation of this word. Example: 'nmod'"""
        return self._deprel

    @deprel.setter
    def deprel(self, value):
        """ Set the word's dependency relation value. Example: 'nmod'"""
        if self._is_null(value):
            value = None

        self._deprel = value
        # self._deprel = value if self._is_null(value) == False else None

    @property
    def deps(self):
        """ Access the dependencies of this word. """
        return self._deps

    @deps.setter
    def deps(self, value):
        """ Set the word's dependencies value. """
        if self._is_null(value):
            value = None

        self._deps = value
        # self._deps = value if self._is_null(value) == False else None

    @property
    def misc(self):
        """ Access the miscellaneousness of this word. """
        return self._misc

    @misc.setter
    def misc(self, value):
        """ Set the word's miscellaneousness value. """
        if self._is_null(value):
            value = None

        self._misc = value
        # self._misc = value if self._is_null(value) == False else None

    @property
    def parent(self):
        """ Access the parent token of this word. In the case of a multi-word token, a token can be the parent of
        multiple words. Note that this should return a reference to the parent token object.
        """
        return self._parent

    @parent.setter
    def parent(self, value):
        """ Set this word's parent token. In the case of a multi-word token, a token can be the parent of
        multiple words. Note that value here should be a reference to the parent token object.
        """
        self._parent = value

    @property
    def pos(self):
        """ Access the universal part-of-speech of this word. Example: 'NOUN'"""
        return self._upos

    @pos.setter
    def pos(self, value):
        """ Set the word's universal part-of-speech value. Example: 'NOUN'"""
        if self._is_null(value):
            value = None

        self._upos = value

        # self._upos = value if self._is_null(value) == False else None

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def to_dict(self):
        """ Dumps the word into a dictionary.
        """
        word_dict = {}
        for field in CoNLL.get_fields():
            if getattr(self, field) is not None:
                word_dict[field] = getattr(self, field)
        return word_dict

    def _is_null(self, value):
        return (value is None) or (value == '_')

    def conll(self) -> str:
        """
        Convert this Word to its CoNLL-U representation.

        A Token's CoNLL-U representation is a line. Note that this method does
        not include a newline at the end.

        Returns:
            str:  A string representing the Word in CoNLL-U format.
        """
        items: list = []
        for field in CoNLL.get_fields():
            value = getattr(self, field)
            if value is None:
                items.append(CoNLL.EMPTY)
            else:
                items.append(str(value))

        return CoNLL.FIELD_DELIMITER.join(items)


class Span:
    """ A span class that stores attributes of a textual span. A span can be typed.
    A range of objects (e.g., entity mentions) can be represented as spans.
    """

    def __init__(self, span_entry=None, tokens=None, span_type=None, doc=None, sent=None):
        """ Construct a span given a span entry or a list of tokens. A valid reference to a doc
        must be provided to construct a span (otherwise the text of the span cannot be initialized).
        """
        assert span_entry is not None or (tokens is not None and span_type is not None), \
            'Either a span_entry or a token list needs to be provided to construct a span.'
        assert doc is not None, 'A parent doc must be provided to construct a span.'
        self._text, self._span_type, self._start_char, self._end_char = [None] * 4
        self._tokens = []
        self._words = []
        self._doc = doc
        self._sent = sent

        if span_entry is not None:
            self.init_from_entry(span_entry)

        if tokens is not None:
            self.init_from_tokens(tokens, span_type)

    def init_from_entry(self, span_entry):
        """ init from entry"""
        self.text = span_entry.get(CoNLL.TEXT, None)
        self.span_type = span_entry.get(TYPE, None)
        self.start_char = span_entry.get(START_CHAR, None)
        self.end_char = span_entry.get(END_CHAR, None)

    def init_from_tokens(self, tokens, span_type):
        """ init from tokens"""
        assert isinstance(tokens, list), 'Tokens must be provided as a list to construct a span.'
        assert len(tokens) > 0, "Tokens of a span cannot be an empty list."
        self.tokens = tokens
        self.span_type = span_type
        # load start and end char offsets from tokens
        self.start_char = self.tokens[0].start_char
        self.end_char = self.tokens[-1].end_char
        # assume doc is already provided and not None
        self.text = self.doc.text[self.start_char:self.end_char]
        # collect the words of the span following tokens
        self.words = [w for t in tokens for w in t.words]

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
        """ Access the text of this span. Example: 'Stanford University'"""
        return self._text

    @text.setter
    def text(self, value):
        """ Set the span's text value. Example: 'Stanford University'"""
        self._text = value

    @property
    def tokens(self):
        """ Access reference to a list of tokens that correspond to this span. """
        return self._tokens

    @tokens.setter
    def tokens(self, value):
        """ Set the span's list of tokens. """
        self._tokens = value

    @property
    def words(self):
        """ Access reference to a list of words that correspond to this span. """
        return self._words

    @words.setter
    def words(self, value):
        """ Set the span's list of words. """
        self._words = value

    @property
    def span_type(self):
        """ Access the type of this span. Example: 'PERSON'"""
        return self._span_type

    @span_type.setter
    def span_type(self, value):
        """ Set the type of this span. """
        self._span_type = value

    @property
    def start_char(self):
        """ Access the start character offset of this span. """
        return self._start_char

    @start_char.setter
    def start_char(self, value):
        """ Set the start character offset of this span. """
        self._start_char = value

    @property
    def end_char(self):
        """ Access the end character offset of this span. """
        return self._end_char

    @end_char.setter
    def end_char(self, value):
        """ Set the end character offset of this span. """
        self._end_char = value

    def to_dict(self):
        """ Dumps the span into a dictionary. """
        attrs = ['text', 'span_type', 'start_char', 'end_char']
        span_dict: dict = {}
        for attr_name in attrs:
            span_dict[attr_name] = getattr(self, attr_name)
        # span_dict = dict([(attr_name, getattr(self, attr_name)) for attr_name in attrs])
        return span_dict

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
