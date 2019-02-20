Release Notes
==============

.. note:: Contributors please include release notes as needed or appropriate with your bug fixes, feature additions and tests.

0.1.0
-----

Changes:

- **Normalize function**
    Single function added to do all normalize stuff. To normalize some text,
    all you need to do is to import this function ``urduhack.normalize`` and it will return a string
    with normalized characters both single and combined, proper spaces after digits and punctuations,
    also remove the diacritics.

- **Sentence Tokenizer**
    Urdu sentence tokenization functionality added. To covert raw Urdu text into possible sentences,
    we need to use ``urduhack.tokenization.sentence_tokenizer`` function.

Bug fixes:

- Fixed bugs in ``remove_diacritics()``

0.0.2
-----

Changes:

- **Character Level Normalization**
    The ``urduhack.normalization.character`` module provides the functionality
    to replace wrong arabic characters with correct urdu characters.

- **Space Normalization**
    The ``urduhack.normalization.space.util`` module provides functionality to
    put proper spaces before and after numeric digits, urdu digits and punctuations (urdu text).

- **Diacritics Removal**
    The ``urduhack.utils.text.remove_diacritics`` module in the UrduHack provides
    the functionality to remove Urdu diacritics from text. It is an important
    step in pre-processing of the Urdu data.

0.0.1
-----

Changes:

- Urdu character normalization api added.
- Urdu space normalization utilities functionality added.
- urdu characters correct unicode ranges added.
