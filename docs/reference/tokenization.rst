.. py:module:: urduhack.tokenization
.. py:currentmodule:: urduhack.tokenization


:py:mod:`urduhack.tokenization` Module
==================================================

The :py:mod:`~urduhack.tokenization` module provides the functionality
to generate tokens (both sentence and word wise) from some Urdu text.

Examples
--------

Generating tokens
^^^^^^^^^^^^^^^^^^
To generate tokens from raw Urdu text you need to use
:py:func:`~urduhack.tokenization.sentence_tokenizer`
function.

To generate sentences from some text.::

   >>> from urduhack.tokenization import sentence_tokenizer
   >>> text = "عراق اور شام نے اعلان کیا ہے دونوں ممالک جلد اپنے اپنے سفیروں کو واپس بغداد اور دمشق بھیج دیں گے؟"
   >>> sentences = sentence_tokenizer(text)

   # list of multiple sentences,
   >>> sentences
   ["دونوں ممالک جلد اپنے اپنے سفیروں کو واپس بغداد اور دمشق بھیج دیں گے؟" ,"عراق اور شام نے اعلان کیا ہے۔"]

If successful, this function returns a :py:class:`List` object containing multiple urdu :py:class:`String`
sentences.

Functions
----------

.. autofunction:: sentence_tokenizer
