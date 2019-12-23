"""
Sentiment Analysis Module
--------------------------

Performs sentiment analysis on urdu textual data. It analyzes the data using a pre-trained Deep Learning Model. It takes in a text
string to predict whether that particular text(sentiment) is Negative, Neutral or Positive. This module has two important functions

    - get_sentiment_label
    - get_sentiment_probability

get_sentiment_label returns the predicted label in a string format whereas get_sentiment_probability
returns the probabilities of all the three sentiments which are 'Negative', 'Neutral' and 'Positive'.

Remember columns of get_sentiment_probability follow the following order.
    - 1st Column: 'Negative'
    - 2nd Column: 'Neutral'
    - 3rd Column: 'Positive'
"""

from .sentiment_analysis import get_sentiment_label, get_sentiment_probability

__all__ = ["get_sentiment_label", "get_sentiment_probability"]