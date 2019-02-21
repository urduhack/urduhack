Pre-Process
===========

The pre-processing of Urdu text is necessary to make it useful for the machine
learning tasks. This module provides the following functionalities:

    - Normalize whitespace
    - Replace urls
    - Replace emails
    - Replace number
    - Replace phone_no
    - Replace currency_symbols

You can look for all the different functions that come with pre-process
module in the reference here :py:mod:`~urduhack.preprocess`.

Example
--------

One of the functionalities of pre-processing module is to normalize whitespaces
in the given text.

To normalize whitespaces from some text.::

   >>> from urduhack.preprocess import normalize_whitespace
   >>> text = "عراق اور شام     اعلان کیا ہے دونوں         جلد اپنے     گے؟"
   >>> normalized_text = normalize_whitespace(text)
   >>> normalized_text
   عراق اور شام اعلان کیا ہے دونوں جلد اپنے گے؟

If successful, this function returns a :py:class:`String` object with
whitespaces removed.