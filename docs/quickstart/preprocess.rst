Text PreProcessing
===================

The pre-processing of Urdu text is necessary to make it useful for the machine
learning tasks. This module assists us in getting rid of unnecessary data. This is more of a
data cleaning module. It cleans our data from various unnecessary elements. It provides following functions:

    - Normalize whitespace
    - Replace urls
    - Replace emails
    - Replace number
    - Replace phone_no
    - Replace currency_symbols

You can look for all the different functions that come with pre-process
module in the reference here :py:mod:`~urduhack.preprocess`.

Example
--------

One of the functionality of pre-processing module is to normalize whitespaces
in the given text.

To normalize whitespaces from some text.::

   >>> from urduhack.preprocess import normalize_whitespace
   >>> text = "عراق اور شام     اعلان کیا ہے دونوں         جلد اپنے     گے؟"
   >>> normalized_text = normalize_whitespace(text)
   >>> normalized_text
   عراق اور شام اعلان کیا ہے دونوں جلد اپنے گے؟

If successful, this function returns a :py:class:`String` object with
whitespaces removed.

Replace Urls
--------------------
While processing any form of text we like to get rid of many unnecessary things, one of those is web urls.
We don't need them as they don't convey any meaningful information. We will use :py:mod:`~urduhack.preprocess.replace_urls`
function from :py:mod:`~urduhack.preprocess.utils` module to replace web urls with a specific text.::

    >>> from urduhack.preprocess import replace_urls
    >>> text = "20 www.gmail.com  فیصد"
    >>> replace_urls(text)
    '20 *URL*  فیصد'
If successful, this function returns a :py:class:`String` object with
urls replaced by "*URL*".

Replace Emails
--------------
In the same way we replace web urls we will replace email addresses as well. We will use
:py:func:`~urduhack.preprocess.replace_emails` function from :py:mod:`~urduhack.preprocess.utils` module to replace emails with a specific text.::

    >>> text = "20 gunner@gmail.com  فیصد"
    >>> from urduhack.preprocess import replace_emails
    >>> replace_emails(text)
    '20 *EMAIL*  فیصد'
If successful, this function returns a :py:class:`String` object with
email address replaced by "*EMAIL*".

Replace Numbers
---------------
In some cases where numbers are also unnecessary in our data. We can get rid of them as well by using
:py:func:`~urduhack.preprocess.replace_numbers` function from :py:mod:`~urduhack.preprocess.utils` module.::

    >>> from urduhack.preprocess import replace_numbers
    >>> text = "20  فیصد"
    >>> replace_numbers(text)
    '*NUMBER*  فیصد'
If successful, this function returns a :py:class:`String` object with
number replaced by "*NUMBER*".

Replace Phone Number
--------------------
To replace a phone number from our text we will utilize :py:func:`~urduhack.preprocess.replace_phone_numbers`
function from :py:mod:`~urduhack.preprocess.utils` module.::

    >>> from urduhack.preprocess import replace_phone_numbers
    >>> text = "یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ 555-123-4567 میں ہوا تھا"
    >>> replace_phone_numbers(text)
    'یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ *PHONE* میں ہوا تھا'
If successful, this function returns a :py:class:`String` object with
number replaced by "*PHONE*".

Replace Currency Symbols
------------------------
To replace a currency symbol, we will utilize :py:func:`~urduhack.preprocess.replace_currency_symbols` function
from :py:mod:`~urduhack.preprocess.utils` module.
A currency symbols will be replaced by its respective representation in characters like $ will be replaced
by USD.::

    >>> from urduhack.preprocess import replace_currency_symbols
    >>> text = "یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ 2003 میں ہوا 33$ تھا۔"
    >>> replace_currency_symbols(text)
    'یعنی لائن آف کنٹرول پر فائربندی کا معاہدہ 2003 میں ہوا 33USD تھا۔'

If successful, this function returns a :py:class:`String` object with
currency symbol replaced by "*USD*".

Remove Punctuation
------------------
To remove punctuations like commas, colons and semicolons etc, we will use :py:func:`~urduhack.preprocess.remove_punctuation`
function from :py:mod:`~urduhack.preprocess.utils` module. It will replace all the punctuations marks by a space::

    >>> from urduhack.preprocess import remove_punctuation
    >>> text = "کر  ؟ سکتی ہے۔ علینا نے"
    >>> remove_punctuation(text)
    'کر    سکتی ہے  علینا نے'

If successful, this function returns a :py:mod:`string` object with punctuation marks replaced by
a space character.

Remove Accents
--------------
To remove urdu we accents, we will use the :py:func:`~urduhack.preprocess.remove_accents` function from
:py:mod:`~urduhack.preprocess.utils` module.::

    >>> from urduhack.preprocess import remove_accents
    >>>text = "دالتِ عظمیٰ درخواست"
    >>> remove_accents(text)
    'دالت عظمی درخواست'

If successful, this function returns a :py:mod:`string` free of "accents".
