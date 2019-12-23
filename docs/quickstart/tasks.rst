Tasks
=====

Contains different Natural Language Processing tasks some of which are listed below:

    - Sentiment Analysis

Sentiment Analysis
------------------

To perform sentiment analysis all you have to do is import the package you want to use and give in your data.
For this purpose, tasks module offers two functions. One is :py:func:`~get_sentiment_label` and
the other is :py:func:`~get_sentiment_probability`. So let's use them.::

    >>> from urduhack.tasks import get_sentiment_label
    >>> text = " 13 سال بعد ہوم سیریز جیتنے کا اعزاز حاصل کر لیا ہے"
    >>> get_sentiment_label(text)
    array(['Positive'], dtype='<U8')

Similarly to get the probabilities of all sentiments::

    >>> from urduhack.tasks import get_sentiment_probability
    >>> text = " 13 سال بعد ہوم سیریز جیتنے کا اعزاز حاصل کر لیا ہے"
    >>> get_sentiment_probability(text)
    array([[0.0110281 , 0.04892549, 0.9400465 ]], dtype=float32)

Remember the first column is for "Negative", second for "Neutral" and third for "Positive".
