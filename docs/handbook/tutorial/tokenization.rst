Tokenization
==============

The tokenization of Urdu text is necessary to make it useful for the machine
learning tasks. In the :py:mod:`~urduhack.tokenization.tokenizer` module, we solved the problem related to
sentence and word tokenization.

Sentence Tokenizer
-----------------------

To covert raw Urdu text into possible sentences, we need to use :py:func:`~urduhack.tokenization.sentence_tokenizer`
function.

To generate sentences from some text.::

   >>> from urduhack.tokenization import sentence_tokenizer
   >>> text = "اَباُوگل پاکستان ﻤﯿﮟ20سال ﺳﮯ ، وسائل کی کوئی کمی نہیں ﮨﮯ۔"
   >>> sentences = sentence_tokenizer(text)

   # list of multiple sentences,
   >>> sentences
   []

If successful, this function returns a :py:class:`List` object containing multiple urdu :py:class:`String`
sentences.