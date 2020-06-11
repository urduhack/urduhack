# coding: utf8
"""Conll format parser"""

from typing import Dict, Tuple, Any, Optional, List

import regex as re

from urduhack.conll.exception import ParseError

COMMENT_MARKER = '#'
KEY_VALUE_COMMENT_PATTERN = COMMENT_MARKER + r'\s*([^=]+?)\s*=\s*(.+)'
SINGLETON_COMMENT_PATTERN = COMMENT_MARKER + r'\s*(\S.*?)\s*$'
SENTENCE_ID_KEY = 'sent_id'
TEXT_KEY = 'text'
FIELD_DELIMITER = '\t'


def parse_conll_token(line: str) -> dict:
    """
    Parse single conll line

    Args:
        line (str): A single conll-u token line

    Returns:
         A dictionary containing conll-u token attributes

    Raises:
        ParseError: If the number of columns in line are not 10
    """
    if line[-1] == '\n':
        line = line[:-1]

    fields = line.split(FIELD_DELIMITER)
    if len(fields) != 10:
        raise ParseError(f'The number of columns per token line must be 10. Invalid token: {line}')

    token: dict = {
        'ID': fields[0],
        'TEXT': fields[1],
        'LEMMA': fields[2],
        'UPOS': fields[3],
        'XPOS': fields[4],
        'FEATS': fields[5],
        'HEAD': fields[6],
        'DEPREL': fields[7],
        'DEPS': fields[8],
        'MISC': fields[9],
    }

    return token


def parse_conll_sentence(sentence: str) -> Tuple[Dict[Any, Optional[Any]], List[Dict]]:
    """
    Parse single conll sentence

    Args:
        sentence (str):  A complete conllu sentence

    Returns:
        Two dicts containing sentence metadata and token data
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
                    key = kv_match.group(1)
                    val = kv_match.group(2)
                    _meta[key] = val
                elif singleton_match:
                    k = singleton_match.group(1)
                    _meta[k] = None
            else:
                token = parse_conll_token(line)
                _tokens.append(token)
    return _meta, _tokens


def _create_sentence(sent_lines: iter) -> Tuple[Dict[Any, Optional[Any]], List[Dict]]:
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


def _iter_lines(lines: iter) -> iter:
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
