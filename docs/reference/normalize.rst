.. py:module:: urduhack.normalize
.. py:currentmodule:: urduhack.normalize


:py:mod:`urduhack.normalize` Module
====================================

The :py:mod:`~urduhack.normalize` module provides the following
functionalities:

    - Normalizing Single Characters
    - Normalizing Combine Characters
    - Put Spaces Before & After Digits
    - Put Spaces After Urdu Punctuations
    - Removal of Diacritics from Urdu Text

Examples
--------

Normalizing a piece of text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To normalize some text, all you need to do is to import the
function from the module and pass it the text.::


   >>> from urduhack import normalize
   >>> text = "اَباُوگل پاکستان ﻤﯿﮟ20سال ﺳﮯ ، وسائل کی کوئی کمی نہیں ﮨﮯ۔"
   >>> normalized_text = normalize_characters(text)

   # The text now contains proper spaces after digits and punctuations,
   # normalized characters and no diacritics!
   >>> normalized_text
   اباوگل پاکستان ﻤﯿﮟ 20 سال ﺳﮯ، وسائل کی کوئی کمی نہیں ﮨﮯ۔

Functions
----------

.. autofunction:: urduhack.normalize
   :noindex:
