# coding: utf8
"""Conll format parser"""

from typing import Dict

import regex as re

from .exception import ParseError
from .reader import CoNLL

COMMENT_MARKER = '#'
KEY_VALUE_COMMENT_PATTERN = COMMENT_MARKER + r'\s*([^=]+?)\s*=\s*(.+)'
SINGLETON_COMMENT_PATTERN = COMMENT_MARKER + r'\s*(\S.*?)\s*$'
SENTENCE_ID_KEY = 'sent_id'
TEXT_KEY = 'text'
FIELD_DELIMITER = '\t'


def parse_conll_token(line: str) -> Dict:
    """Parse single conll line"""
    if line[-1] == '\n':
        line = line[:-1]

    fields = line.split(FIELD_DELIMITER)
    if len(fields) != 10:
        raise ParseError(f'The number of columns per token line must be 10. Invalid token: {line}')

    token: dict = {
        CoNLL.ID: fields[0],
        CoNLL.TEXT: fields[1],
        CoNLL.LEMMA: fields[2],
        CoNLL.UPOS: fields[3],
        CoNLL.XPOS: fields[4],
        CoNLL.FEATS: fields[5],
        CoNLL.HEAD: fields[6],
        CoNLL.DEPREL: fields[7],
        CoNLL.DEPS: fields[8],
        CoNLL.MISC: fields[9],
    }

    return token


def parse_conll_sentence(sentence):
    """
    Parse single conll sentence
    """
    lines = sentence.split('\n')
    _meta = {}
    _tokens = []

    for line in lines:
        if line:
            if line[0] == COMMENT_MARKER:
                kv_match = re.match(KEY_VALUE_COMMENT_PATTERN, line)
                singleton_match = re.match(SINGLETON_COMMENT_PATTERN, line)
                if kv_match:
                    k = kv_match.group(1)
                    v = kv_match.group(2)
                    _meta[k] = v
                elif singleton_match:
                    k = singleton_match.group(1)
                    _meta[k] = None
            else:
                token = parse_conll_token(line)
                _tokens.append(token)
    return _meta, _tokens


def _create_sentence(sent_lines):
    """
    Creates a Sentence object given the current state of the source iteration.

    Args:
        sent_lines: An iterable of the lines that make up the source.

    Returns:
        The created Sentence.

    Raises:
        ParseError: If the sentence source is not valid.
    """
    return parse_conll_sentence('\n'.join(sent_lines))


def _iter_lines(lines):
    """
    Iterate over the constructed sentences in the given lines.

    This method correctly takes into account newpar and newdoc comments as well.

    Args:
        lines: An iterator over the lines to parse.

    Yields:
        An iterator over the constructed Sentence objects found in the source.

    Raises:
        ValueError: If there is an error constructing the Sentence.
    """
    sent_lines = []
    for line in lines:
        line = line.strip()
        # Collect all lines until there is a blank line. Then all the
        # collected lines were between blank lines and are a sentence.
        if line:
            sent_lines.append(line)
        elif sent_lines:
            conll_sentence = _create_sentence(sent_lines)
            sent_lines.clear()
            yield conll_sentence

    if sent_lines:
        conll_sentence = _create_sentence(sent_lines)
        yield conll_sentence
