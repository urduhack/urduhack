# coding: utf8
"""
Normalization
==============

The normalization of Urdu text is necessary to make it useful for the machine
learning tasks. In the :py:mod:`~urduhack.normalization.normalize` module, the very basic
problems faced when working with Urdu data are handled with ease and
efficiency. All the problems and how :py:mod:`~urduhack.normalization.normalize` module handles
them are listed below.

This modules fixes the problem of correct encodings for the Urdu characters as well as replace Arabic
characters with correct Urdu characters. This module brings all the characters in the specified unicode range
(0600-06FF) for Urdu language.

It also fixes the problem of joining of different Urdu words. By joining we mean that when space between two Urdu words
is removed, they must not make a new word. Their rendering must not change and even after the removal of space
they should look the same.

You can use the library to normalize the Urdu text for correct unicode characters.
By normalization we mean to end the confusion between Urdu and Arabic characters,
to replace two words with one word keeping in mind the context they are used in.
Like the character 'ﺁ' and 'ﺂ' are to be replaced by 'آ'. All this is done using regular expressions.

The normalization of Urdu text is necessary to make it useful for the machine learning tasks.
This module provides the following functionality:

    - Normalizing Single Characters
    - Normalizing Combine Characters
    - Put Spaces Before & After Digits
    - Put Spaces After Urdu Punctuations
    - Put Spaces Before & After English Words
    - Removal of Diacritics from Urdu Text

Normalize Data
---------------

To normalize some text, all you need to do is to import the
function from the module and pass it the text. The :py:func:`~urduhack.normalization.normalize`
function will return a string with normalized characters both
single and combined, proper spaces after digits and punctuations and
diacritics removed.::

    >>> from urduhack import normalize
    >>> text = "اَباُوگل پاکستان ﻤﯿﮟ20سال ﺳﮯ ، وسائل کی کوئی کمی نہیں ﮨﮯ۔"
    >>> normalized_text = normalize(text)

   >>> # The text now contains proper spaces after digits and punctuations,
   >>> # normalized characters and no diacritics!
   >>> normalized_text
   اباوگل پاکستان ﻤﯿﮟ 20 سال ﺳﮯ، وسائل کی کوئی کمی نہیں ﮨﮯ۔

Combine|Join Characters Normalization
--------------------------------------

To normalize combine characters with single character unicode text, use the
:py:func:`~urduhack.normalization.character.normalize_combine_characters`
function in the :py:mod:`~urduhack.normalization.character` module.::

    >>> from urduhack.normalization import normalize_combine_characters

    # In the following string, Alif ('ا') and Hamza ('ٔ ') are separate
    characters
    >>> text = "جرأت"
    >>> normalized_text = normalize_combine_characters(text)

    # Now Alif and Hamza are replaced by a Single Urdu Unicode Character!
    >>> normalized_text
    جرأت

If successful, this function returns a :py:class:`String` object containing
normalized text.

Adding spaces before and after digits (numeric and urdu)
---------------------------------------------------------

To do so you need to import the :py:func:`~urduhack.normalization.digits_space` from
:py:mod:`~urduhack.normalization` and pass it the text. The function will return you
the text after putting spaces at proper places.::

    >>> from urduhack.normalization import digits_space
    >>> text = "20فیصد"
    >>> normalized_text = digits_space(text)
    >>> normalized_text
    20 فیصد

Adding spaces after punctuations
---------------------------------

To do so you need to import the :py:func:`~urduhack.normalization.punctuations_space` from
:py:mod:`~urduhack.normalization` and pass it the text. The function will return you
the text after putting spaces at proper places.::

    >>> from urduhack.normalization import punctuations_space
    >>> text = "ہوتا ہے   ۔  ٹائپ"
    >>> normalized_text = punctuations_space(text)
    >>> normalized_text
    ہوتا ہے۔ ٹائپ

Diacritics Removal
-------------------

The :py:mod:`~urduhack.normalization` module in the UrduHack provides
the functionality to remove Urdu diacritics from text. It is an important
step in pre-processing of the Urdu data.

To remove diacritics from some text, use the :py:func:`~urduhack.normalization.remove_diacritics` function
in the :py:mod:`~urduhack.normalization` module.::

    >>> from urduhack.normalization import remove_diacritics
    >>> text = "شیرِ پنجاب"
    >>> normalized_text = remove_diacritics(text)
    >>> normalized_text
    شیر پنجاب

If successful, this function returns a :py:class:`String` object which
contains the original text minus Urdu diacritics.

Adding space before & after English words
-----------------------------------------

The :py:mod:`~urduhack.normalization` module in the UrduHack provides
the functionality to add spaces before and after English words in the given
Urdu text. It is an important step in normalization of the Urdu data.

To put spaces after English words in Urdu text, use the :py:func:`~urduhack.normalization.english_characters_space`
function in the :py:mod:`~urduhack.normalization` module.::

    >>> from urduhack.normalization import english_characters_space
    >>> text = "خاتون Aliyaنے بچوںUzma and Aliyaکے قتل کا اعترافConfession کیا ہے۔"
    >>> normalized_text = english_characters_space(text)
    >>> normalized_text
    خاتون Aliya نے بچوں Uzma and Aliya کے قتل کا اعتراف Confession کیا ہے۔

If successful, this function returns a :py:class:`String` object which
contains the original text with spaces before & after English words.

"""
from .character import normalize_characters, normalize_combine_characters, punctuations_space, digits_space, \
    remove_diacritics, english_characters_space, normalize

__all__ = ["normalize_characters", "normalize_combine_characters",
           "english_characters_space",
           "punctuations_space", "digits_space", "remove_diacritics",
           "normalize"]
