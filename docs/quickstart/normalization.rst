Normalization
==============

The normalization of Urdu text is necessary to make it useful for the machine
learning tasks. In the :py:mod:`~urduhack.normalization.normalize` module, the very basic
problems faced when working with Urdu data are handled with ease and
efficiency. All the problems and how :py:mod:`~urduhack.normalization.normalize` module handles
them are listed below.

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

   # The text now contains proper spaces after digits and punctuations,
   # normalized characters and no diacritics!
   >>> normalized_text
   اباوگل پاکستان ﻤﯿﮟ 20 سال ﺳﮯ، وسائل کی کوئی کمی نہیں ﮨﮯ۔


Characters Normalization
-------------------------

The most important module in the UrduHack is the :py:mod:`~urduhack.normalization.character` module,
defined in the module with the same name. You can use this module separately to normalize
a piece of text to a proper specified Urdu range (0600-06FF). To get an understanding of how this module works, one
needs to understand unicode. Every character has a unicode. You can search for any character unicode from any language
you will find it. No two characters can have the same unicode. This module works with reference to the unicodes. Now as
urdu language has its roots in Arabic, Parsian and Turkish. So we have to deal with all those characters and convert them
to a normal urdu character. To get a bit more of what the above explanation means is.::

     >>> all_fes = ['ﻑ', 'ﻒ', 'ﻓ', 'ﻔ', ]
        >>> urdu_fe = 'ف'

All the characters in all_fes are same but they come from different languages and they all have different unicodes. Now as
computers deal with numbers, same character appearing in more than one place in a different language will have a different
unicode and that will create confusion which will be create problems in understanding the context of the data.
:py:mod:`~character` module will eliminate this problem by replacing all the characters in all_fes by urdu_fe.

To normalize some text, use the :py:func:`~urduhack.normalization.character.normalize_characters` function
in the :py:mod:`~urduhack.normalization.character` module::

    >>> from urduhack.normalization import normalize_characters

    # Text containing characters from Arabic Unicode block
    >>> text = "مجھ کو جو توڑا ﮔیا تھا"
    >>> normalized_text = normalize_characters(text)

    # Normalized text - Arabic characters are now replaced with Urdu characters
    >>> normalized_text
    مجھ کو جو توڑا گیا تھا

If successful, this function returns a :py:class:`String` object containing
normalized text.

Combine|Join Characters Normalization
--------------------------------------

To normalize combine characters with single character unicode text, use the :py:func:`~urduhack.normalization.character.normalize_combine_characters`
function in the :py:mod:`~urduhack.normalization.character` module::

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

To put spaces after English words in Urdu text, use the :py:func:`~urduhack.normalization.english_characters_space` function
in the :py:mod:`~urduhack.normalization` module.::

    >>> from urduhack.normalization import english_characters_space
    >>> text = "خاتون Aliyaنے بچوںUzma and Aliyaکے قتل کا اعترافConfession کیا ہے۔"
    >>> normalized_text = english_characters_space(text)
    >>> normalized_text
    خاتون Aliya نے بچوں Uzma and Aliya کے قتل کا اعتراف Confession کیا ہے۔

If successful, this function returns a :py:class:`String` object which
contains the original text with spaces before & after English words.