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
    List of morphological features from the universal features inventory or from a defined language specific extension
``7. HEAD:``
    Head of the current word which is wither the value of ID or zero.
``8. DEPREL:``
    Universal dependencies relation to the HEAD (root if HEAD=0) or a defined language specific subtype of one.
``9. DEPS:``
    Enhanced dependency graph in the form of a list of head-deprel pairs
``10. MISC:``
    Any other annotation apart from the above mentioned fields

"""

from .reader import CoNLL

__all__ = ["CoNLL"]
