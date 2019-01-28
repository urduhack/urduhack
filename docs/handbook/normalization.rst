Normalization
==============

Using the Normalization Module
-------------------------------

The most important module in the UrduHack is the :py:mod:`~urduhack.normalization` module,
defined in the module with the same name. You can use this module separately to normalize
a piece of text to a proper specified Urdu range (0600-06FF).

To normalize some text, use the :py:func:`normalize_function()` function
in the :py:mod:`~urduhack.normalization` module::

    >>> from urduhack.normalization.character import normalize_function
    >>> normalized_text = normalize_function(un_normalized_text)

If successful, this function returns a :py:class:`String` object containing
normalized text.
