Normalization
==============

Characters Normalization
-------------------------

The most important module in the UrduHack is the :py:mod:`~urduhack.normalization.character` module,
defined in the module with the same name. You can use this module separately to normalize
a piece of text to a proper specified Urdu range (0600-06FF).

To normalize some text, use the :py:func:`~urduhack.normalization.character.normalize_characters` function
in the :py:mod:`~urduhack.normalization.character` module::

    >>> from urduhack.normalization import normalize_characters
    >>> normalized_text = normalize_characters(un_normalized_text)

If successful, this function returns a :py:class:`String` object containing
normalized text.

Combine|Join Characters Normalization
--------------------------------------

To normalize combine characters with single character unicode text, use the :py:func:`~urduhack.normalization.character.normalize_combine_characters`
function in the :py:mod:`~urduhack.normalization.character` module::

    >>> from urduhack.normalization import normalize_combine_characters
    >>> normalized_text = normalize_combine_characters(un_normalized_text)

If successful, this function returns a :py:class:`String` object containing
normalized text.

Pre-processing for Tokenization
--------------------------------

Tokenization is a core process of Natural Language Processing. It is needed
in order to process data of any language. To make the tokenization of urdu text
easy and efficient, it is necessary to add spaces before and after urdu/numeric
digits and spaces after punctuations.

Adding spaces before and after digits (numeric and urdu)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To do so you need to import the :py:func:`~urduhack.normalization.util.digits_space` from
:py:mod:`~urduhack.normalization` and pass it the text. The function will return you
the text after putting spaces at proper places.

.. code-block:: python

    from urduhack.normalization import digits_space
    text = "گنہگار4مر کر موت2"
    normalized_text = digits_space(text)


Adding spaces after punctuations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To do so you need to import the :py:func:`~urduhack.normalization.util.punctuations_space` from
:py:mod:`~urduhack.normalization` and pass it the text. The function will return you
the text after putting spaces at proper places.

.. code-block:: python

    from urduhack.normalization import punctuations_space
    text = "گنہگمر کر موت-گنہگمر-گرموت-"
    normalized_text = punctuations_space(text)

Adding spaces between joined words
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :py:mod:`~urduhack.normalization.util` module provides functionality
to put proper spaces after the urdu words which are distinct but written together.
For example, 'کےبعد' are two different words but written together. The
:py:func:`~urduhack.normalization.util.fix_join_words` function will put
a space between these two words and return a string like this 'کے بعد'.

.. code-block:: python

    from urduhack.normalization.util import fix_join_words
    text = "کےبعد"
    normalized_text = fix_join_words(text)

Diacritics Removal
^^^^^^^^^^^^^^^^^^^

The :py:mod:`~urduhack.normalization.util` module in the UrduHack provides
the functionality to remove Urdu diacritics from text. It is an important
step in pre-processing of the Urdu data.

To remove diacritics from some text, use the :py:func:`~urduhack.normalization.util.remove_diacritics` function
in the :py:mod:`~urduhack.normalization` module.

.. code-block:: python

    from urduhack.normalization import remove_diacritics
    text = "شیرِ پنجاب"
    processed_text = remove_diacritics(text)

If successful, this function returns a :py:class:`String` object which
contains the original text minus Urdu diacritics.