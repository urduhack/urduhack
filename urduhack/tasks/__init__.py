"""
This module contains different NLP tasks which are listed below.

Sentiment Analysis
------------------

Performs sentiment analysis on urdu text. It analyzes the data using a pre-trained Deep Learning Model.
It takes in a text string to predict whether that particular text is Negative or Positive.
This module has two important functions

    - predict_label
    - predict_id

predict_label returns the predicted label in a string format whereas predict_id
returns the sentiment ids of both Negative and Positive labels.

"""