Tasks
=====

Contains different Natural Language Processing tasks which are listed below:

    - Sentiment Analysis

Sentiment Analysis
------------------
Let's perform sentiment analysis using state of the art language models. We have used a Multiligual pretrained
XLM-Roberta model to generate contextual word embeddings. These word embeddings were then fed into a Convolution Neural
Network. After complete training, the network weights were saved and are being used in prediction. For more details on
XLM-Roberta read the official XLM-Roberta `Paper <https://arxiv.org/pdf/1911.02116.pdf>`_. This model is trained using Urdu
version of imdb dataset from kaggle.
Now to perform sentiment analysis we need to import the sentiment package from the tasks module. To get the sentiment
we will use the :py:func:`~urduhack.tasks.sentiment.predict_label` function.::


    >>> from urduhack.tasks import sentiment
    >>> text = "تفصیلات کے مطابق مشیر خزانہ حفیظ شیخ کی زیر صدارت اقتصادی رابطہ کمیٹی کا اجلاس ہوا"
    >>> sentiment.predict_label(text)
    'Positive'

Similarly to get the id of the sentiment use the function :py:func:`~urduhack.tasks.sentiment.predict_id` function.::

    >>> from urduhack.tasks import sentiment
    >>> text = "تفصیلات کے مطابق مشیر خزانہ حفیظ شیخ کی زیر صدارت اقتصادی رابطہ کمیٹی کا اجلاس ہوا"
    >>>  sentiment.predict_id(text)
    1

Remember the id 0 is for "Negative" and 1 for "Positive".
