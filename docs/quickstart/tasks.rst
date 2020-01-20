Tasks
=====

Contains different Natural Language Processing tasks some of which are listed below:

    - Sentiment Analysis

Sentiment Analysis
------------------
Let's perform sentiment analysis using state of the art language models. We have used a Multiligual pretrained
roberta model to generate contextual word embeddings. These word embeddings were then fed into a Convolution Neural
Network. After complete training, the network weights were saved and are being used in prediction. For more details on
Roberta read the official Roberta `Paper <https://arxiv.org/abs/1907.11692>`_.
Now to perform sentiment analysis all you have to do is import the package you want to use and give in your data.
For this purpose, tasks module offers two functions. One is :py:func:`~predict_sentiment_label` and
the other is :py:func:`~predict_sentiment_id`. So let's use them.::

    >>> from urduhack.tasks import predict_sentiment_label
    >>> text = "تفصیلات کے مطابق مشیر خزانہ حفیظ شیخ کی زیر صدارت اقتصادی رابطہ کمیٹی کا اجلاس ہوا"
    >>> predict_sentiment_label(text)
    'Positive'

Similarly to get the probabilities of all sentiments::

    >>> from urduhack.tasks import predict_sentiment_id
    >>> text = "تفصیلات کے مطابق مشیر خزانہ حفیظ شیخ کی زیر صدارت اقتصادی رابطہ کمیٹی کا اجلاس ہوا"
    >>>  predict_sentiment_id(text)
    1

Remember the id 0 is for "Negative", 1 for "Positive" and 2 for "Neutral".
