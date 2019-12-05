Tokenization
==============

The tokenization of Urdu text is necessary to make it useful for the machine
learning tasks. In the :py:mod:`~urduhack.tokenization.tokenizer` module, we solved the problem related to
sentence and word tokenization.

Sentence Tokenizer
-----------------------

To covert raw Urdu text into possible sentences, we need to use :py:func:`~urduhack.tokenization.tokenizer.sentence_tokenizer`
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

Word Tokenizer
-----------------------
To convert the raw Urdu text into tokens, we need to use :py:func:`~urduhack.tokenization.tokenizer.word_tokenizer` function.
Before doing this we need to normalize our sentence as well. For normalizing the urdu sentence use
:py:func:`urduhack.normalization.normalize` function.

To generate tokens from urdu sentence.:
    >>> from urduhack import normalize
    >>> sentence = "عراق اور شام نے اعلان کیا ہے دونوں ممالک جلد اپنے اپنے سفیروں کو واپس بغداد اور دمشق بھیج دیں گے؟"
    >>> sentence = normalize(sentence)
    # normalized sentence
    >>> sentence
    'عراق اور شام نے اعلان کیا ہے دونوں ممالک جلد اپنے اپنے سفیروں کو واپس بغداد اور دمشق بھیج دیں گے؟'
    >>>from urduhack.tokenization import word_tokenizer
    >>>word_tokenizer(sentence)
If the tokenizer runs successfully, this function returns a :py:class:`List` object containing urdu :py:class:`String`
word tokens.
