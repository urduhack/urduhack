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