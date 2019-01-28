.. py:module:: urduhack.normalization.character
.. py:currentmodule:: urduhack.normalization.character


:py:mod:`urduhack.normalization.character` Module
==================================================

The :py:mod:`~urduhack.normalization.character` module provides the functionality
to replace wrong arabic characters with correct urdu characters.

Examples
--------

Normalizing a piece of text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To normalize some text, all you need to do is to import the
function from the module and pass it the text.

.. code-block:: python

    from urduhack.normalization.character import normalize_characters
    text = "گنہگار مر کر موت"
    normalized_text = normalize_characters(text)

Functions
----------

.. autofunction:: normalize_characters
