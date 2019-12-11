Quickstart
==========

Every python package needs an import statement so let's do that first.::

    >>>import urduhack


Basic Introduction
------------------
NLP library for different Urdu language tasks. **urduhack** has different modules all of which serve a specific purpose. You can load any of them
and check out their results by giving in your inputs. urduhack has got some magic functions that can make your life easier. You just need to access a
particular module and get amazing results by giving in your data.
Normalization, Tokenization and Preprocess are the main modules of Urduhack.

Working with Urdu Text
---------------------
Working with urduhack is very easy and straightforward. You import the package
you want to utilize and feed in the data. Let's say we have an urdu text corpus. For Deep Learning
work we need to clean our data and make it ready for training the model. So we'll learn step by step how that
cleaning process go.
To Normalize the urdu text we will use.::

    >>>from urduhack import normalize
    >>>text = " اس رقم سے پاکستان کو اپنے مالیاتی معاملات بہتر بنانے اور بجٹ خسارے سے نمٹنے میں مدد ملے ﮕی"
    >>>normalized_text = normalize(text)
    >>>print(normalized)
    ' اس رقم سے پاکستان کو اپنے مالیاتی معاملات بہتر بنانے اور بجٹ خسارے سے نمٹنے میں مدد ملے گی'

Similarly to make separate sentence tokens we will use the :py:func:`~sentence_tokenizer` function from
:py:mod:`~urduhack.tokenization.tokenizer` module.::

    >>> from urduhack.tokenization import sentence_tokenizer
    >>>text = " آئی ایم ایف کی اصلاحات پر عملدرآمد کے بعد کیاگیاہے۔ اس رقم سے پاکستان کو اپنے مالیاتی معاملات بہتر بنانے اور بجٹ خسارے سے نمٹنے میں مدد ملے گی۔"
    >>>sentence_tokens = sentence_tokenizer(text)
    >>>print(sentence_tokens)
    ['آئی ایم ایف کی اصلاحات پر عملدرآمد کے بعد کیاگیاہے۔', 'اس رقم سے پاکستان کو اپنے مالیاتی معاملات بہتر بنانے اور بجٹ خسارے سے نمٹنے میں مدد ملے گی۔']

In the very same way, the one very important and the most crucial functionality that urduhack posses is to make word tokens.
A broader and clear explanation of this function will be given later in the documents. That function is
:py:func:`~urduhack.tokenization.word_tokenizer` from :py:mod:`~urduhack.tokenization.tokenizer` module.
Let's see the magic of :py:func:`~urduhack.tokenization.word_tokenizer`.::

    >>> from urduhack.tokenization import word_tokenizer
    >>>text = "اس رقم سے پاکستان کو اپنے مالیاتی معاملات بہتر بنانے اور بجٹ خسارے سے نمٹنے میں مدد ملے گی"
    >>>word_tokens = word_tokenizer(text)
    >>>print(word_tokens)
     ['اس', 'رقم', 'سے', 'پاکستان', 'کو', 'اپنے', 'مالیاتی', 'معاملات', 'بہتر', 'بنانے', 'اور', 'بجٹ', 'خسارے', 'سے', 'نمٹنے', 'میں', 'مدد', 'ملے', 'گی']

.. toctree::
   :maxdepth: 2

   command
   normalization
   preprocess
   tokenization