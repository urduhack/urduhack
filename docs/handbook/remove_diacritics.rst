Diacritics Removal
-------------------

The :py:mod:`~urduhack.utils.text` module in the UrduHack provides
the functionality to remove Urdu diacritics from text. It is an important
step in pre-processing of the Urdu data.

To remove diacritics from some text, use the :py:func:`~urduhack.utils.text.remove_diacritics` function
in the :py:mod:`~urduhack.utils.text` module.

.. code-block:: python

    from urduhack.utils.text import remove_diacritics
    text = "شیرِ پنجاب"
    processed_text = remove_diacritics(text)

If successful, this function returns a :py:class:`String` object which
contains the original text minus Urdu diacritics.