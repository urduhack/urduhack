"""
Sentiment Analysis Module
--------------------------

Performs sentiment analysis on urdu textual data. It analyzes the data using a pre-trained Deep Learning Model.
It takes in a text string to predict whether that particular text(sentiment) is Negative, Positive or Neutral.
This module has two important functions

    - predict_sentiment_label
    - predict_sentiment_id

predict_sentiment_label returns the predicted label in a string format whereas predict_sentiment_id
returns the sentiment ids of all the three sentiment labels which are 'Negative', 'Positive' and 'Neutral'.

"""
from .sentiment_analysis import predict_sentiment_id, predict_sentiment_label

__all__ = ['predict_sentiment_label', 'predict_sentiment_id']