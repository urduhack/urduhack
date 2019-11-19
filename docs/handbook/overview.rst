Overview
========


The **Urduhack Library** adds text processing capabilities to yours Urdu NLP tasks.
It should provide a solid foundation for a general text processing tool.

Let’s take a look at a few possible uses of this library.

Normalization
--------------

You can use the library to normalize the Urdu text for correct unicode characters.
By normalization we mean to end the confusion between Urdu and Arabic characters,
to replace two words with one word keeping in mind the
context they are used in. Like the character 'ﺁ' and 'ﺂ' are to be replaced by 'آ'.
It removes unnecessary spaces and also add
spaces after the punctuation marks. All this is done using regular expressions. 

Tokenization
-------------

This library provides state of art sentence and word tokenizer for Urdu Language. It takes
care of the spaces and where to connect two urdu characters and where not to.