.. py:module:: urduhack.normalization.character
.. py:currentmodule:: urduhack.normalization.character


:py:mod:`urduhack.normalization.character` Module
==================================================

The :py:mod:`~urduhack.normalization.character` module provides the functionality
to replace wrong arabic characters with correct urdu characters and fixed the combine characters issue.

Examples
--------

Normalizing a piece of text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To normalize some text, all you need to do is to import the
function from the module and pass it the text.

.. code-block:: python

    from urduhack.normalization import normalize_characters, normalize_combine_characters
    text = "گنہگار مر کر موت"
    normalized_text = normalize_characters(text)

    text = "آزاد"
    normalized_text = normalize_combine_characters(text)

Functions
----------

.. autofunction:: normalize_characters
.. autofunction:: normalize_combine_characters
