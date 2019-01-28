.. py:module:: urduhack.normalization.space.words
.. py:currentmodule:: urduhack.normalization.space.words

:py:mod:`urduhack.normalization.space.words` Module
====================================================

The :py:mod:`~urduhack.normalization.space.words` module provides functionality
to put proper spaces after the urdu words which are distinct but written together.

Examples
--------

Fixing joined words
^^^^^^^^^^^^^^^^^^^^

To do so you need to import the function from module and pass it the text.
The function will return you the text after putting spaces at proper places.

.. code-block:: python

    from urduhack.normalization.space.words import fix_join_words
    text = "مرکر"
    normalized_text = fix_join_words(text)


Functions
----------

.. autofunction:: fix_join_words
