# coding: utf8
"""
CoNLL-U Format
===============
This module reads and parse data in the standard CONLL-U format as provided in universal dependencies.
CONLL-U is a standard format followed to annotate data at sentence level and at word/token level.
Annotations in CONLL-U format fulfil the below points:

    1. Word lines contain the annotations of a word/token in 10 fields are separated by single tab characters
    2. Blank lines mark sentence boundaries
    3. Comment lines start with hash (#)

Each word/token has 10 fields defined in the CONLL-U format. Each field represents different attributes of the token
whose details are given below:

Fields
-------

``1. ID:``
    ID represents the word/token index in the sentence
``2. FORM:``
    Word/token form or punctuation symbol used in the sentence
``3. LEMMA:``
    Root/stem of the word
``4. UPOS:``
    Universal Part-of-Speech tag
``5. XPOS:``
    Language specific part-of-speed tag. underscore if not available
``6. FEATS:``
    Unordered list of morphological features, defined by Universal Dependencies;
    indicates the gender and number of a noun, the tense of a verb, etc.
``7. HEAD:``
    Head of the word, indicates the index of the word to which the current one is related
``8. DEPREL:``
    Universal Dependencies relation; indicates the relation between two words (subject or object of a verb, determiner of a noun, etc.)
``9. DEPS:``
    Language-specific part of speech tags
``10. MISC:``
    Any other annotation apart from the above mentioned fields
    Commentary or other annotation

"""

from .reader import CoNLL

__all__ = ["CoNLL"]
