.. py:module:: urduhack.utils.text
.. py:currentmodule:: urduhack.utils.text


:py:mod:`urduhack.utils.text` Module
=====================================

The :py:mod:`~urduhack.utils.text` module provides the functionality
to remove the diacritics from urdu text.

Examples
--------

Removing diacritics from a piece of text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To remove diacritics from some text, all you need to do is to import the
function from the module and pass it the text.

.. code-block:: python

    from urduhack.utils.text import remove_diacritics
    text = "شیرِ پنجاب"
    processed_text = remove_diacritics(text)

Functions
----------

.. autofunction:: remove_diacritics
