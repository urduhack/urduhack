# coding: utf8
"""Conll format parser"""

from typing import Dict, Tuple, Any, Optional, List, Iterator

import regex as re

COMMENT_MARKER = '#'
KEY_VALUE_COMMENT_PATTERN = COMMENT_MARKER + r'\s*([^=]+?)\s*=\s*(.+)'
SINGLETON_COMMENT_PATTERN = COMMENT_MARKER + r'\s*(\S.*?)\s*$'
FIELD_DELIMITER = '\t'


def parse_conll_token(line: str) -> dict:
    """
    Parse single conll line

    Args:
        line (str): A single conll-u token line
    Returns:
         dict: A dictionary containing conll-u token attributes
    Raises:
        ValueError: If the number of columns in line are not 10
    """
    if line[-1] == '\n':
        line = line[:-1]

    fields = line.split(FIELD_DELIMITER)
    if len(fields) != 10:
        raise ValueError(f'The number of columns per token line must be 10. Invalid token: {line}')

    return {
        'id': fields[0],
        'text': fields[1],
        'lemma': fields[2],
        'upos': fields[3],
        'xpos': fields[4],
        'feats': fields[5],
        'head': fields[6],
        'deprel': fields[7],
        'deps': fields[8],
        'misc': fields[9],
    }


def parse_conll_sentence(sentence: str) -> Tuple[Dict[Any, Optional[Any]], List[Dict]]:
    """
    Parse single conll sentence

    Args:
        sentence (str):  A complete conll-u sentence
    Returns:
        tuple: Two dicts containing sentence metadata and token data
    """
    lines = sentence.split('\n')
    sentence_meta = {}
    tokens = []

    for line in lines:
        if line:
            if line[0] == COMMENT_MARKER:
                kv_match = re.match(KEY_VALUE_COMMENT_PATTERN, line)
                singleton_match = re.match(SINGLETON_COMMENT_PATTERN, line)
                if kv_match:
                    key = kv_match.group(1)
                    val = kv_match.group(2)
                    sentence_meta[key] = val
                elif singleton_match:
                    k = singleton_match.group(1)
                    sentence_meta[k] = None
            else:
                token = parse_conll_token(line)
                tokens.append(token)
    return sentence_meta, tokens


def _iter_lines(lines: iter) -> Iterator[Tuple]:
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
            single_conll_sentence = '\n'.join(sent_lines)
            _sentence = parse_conll_sentence(single_conll_sentence)
            sent_lines.clear()
            yield _sentence

    if sent_lines:
        single_conll_sentence = '\n'.join(sent_lines)
        _sentence = parse_conll_sentence(single_conll_sentence)
        yield _sentence


def _load_file(file_name: str) -> List[Tuple]:
    """
    Load a CoNLL-U file given its location.

    Args:
        file_name (str): The location of the file.
    Returns:
        List[Tuple]: A Conll object equivalent to the provided file.
    Raises:
        IOError: If there is an error opening the given filename.
        ParseError: If there is an error parsing the input into a Conll object.
    """
    conll_data = []
    with open(file_name, encoding='utf8') as file:
        for sentence in _iter_lines(file):
            conll_data.append(sentence)

    return conll_data
