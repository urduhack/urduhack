# coding: utf8
"""Parser for performing normalization"""

from urduhack.conll import CoNLL
from urduhack.core.unit.document import Document
from urduhack.tokenization import sentence_tokenizer, word_tokenizer
from ..parser import Parser


# class for running the tokenizer
class TokenizeParser(Parser):
    """Test"""

    def _set_up(self, config):
        """pass"""

    def _tokenized_text(self, text):
        """generate dictionary data structure"""

        document = []
        sentences = sentence_tokenizer(text)
        idx = 0

        for sentence in sentences:
            words = word_tokenizer(sentence)
            sent = []
            for token_id, token in enumerate(words):
                sent.append({CoNLL.ID: str(token_id + 1),
                             CoNLL.TEXT: token,
                             CoNLL.MISC: f'start_char={idx}|end_char={idx + len(token)}'})
                idx += len(token) + 1

            document.append(({}, sent))

        return document

    def parse(self, document):
        """pass"""
        conll_data = self._tokenized_text(document)
        return Document(conll_data, document)
