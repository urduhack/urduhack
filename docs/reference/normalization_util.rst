.. py:module:: urduhack.normalization.util
.. py:currentmodule:: urduhack.normalization.util


:py:mod:`urduhack.normalization.util` Module
==================================================

The :py:mod:`~urduhack.normalization.util` module provides functionality
to put proper spaces before and after numeric digits, urdu digits and punctuations (urdu text).

Examples
---------

Adding spaces before and after digits (numeric and urdu)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To do so you need to import the function from module and pass it the text.
The function will return you the text after putting spaces at proper places.

.. code-block:: python

    from urduhack.normalization import digits_space
    text = "گنہگار4مر کر موت2"
    normalized_text = digits_space(text)


Functions
----------

.. autofunction:: digits_space
.. autofunction:: punctuations_space

