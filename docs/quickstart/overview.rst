Overview
========

Normalization
-------------

The normalization of Urdu text is necessary to make it useful for the machine
learning tasks. In the :py:mod:`~urduhack.normalization` module, the very basic
problems faced when working with Urdu data are handled with ease and
efficiency. All the problems and how :py:mod:`~urduhack.normalization` module handles
them are listed below.

This modules fixes the problem of correct encodings for the Urdu characters as well as replace Arabic
characters with correct Urdu characters. This module brings all the characters in the specified unicode range
(0600-06FF) for Urdu language.

It also fixes the problem of joining of different Urdu words. By joining we mean that when space between two Urdu words
is removed, they must not make a new word. Their rendering must not change and even after the removal of space
they should look the same.

Tokenization
------------

This module is another crucial part of the Urduhack. This module performs tokenization on sentence. It separates
different sentence from each other and converts each string into a complete **sentence token**. Note here you must not
confuse yourself with the word token. They are two completely different things.

This library provides state of art word tokenizer for Urdu Language. It takes care of the spaces and where to connect
two urdu characters and where not to.

The tokenization of Urdu text is necessary to make it useful for the NLP tasks.
This module provides the following functionality:

    - Sentence Tokenization
    - Word Tokenization

The tokenization of Urdu text is necessary to make it useful for the machine
learning tasks. In the :py:mod:`~urduhack.tokenization` module, we solved the problem related to
sentence and word tokenization.
