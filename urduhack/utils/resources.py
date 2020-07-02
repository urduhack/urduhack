# coding: utf8
"""resources module is responsible for download all type of data"""
from ..config import MODELS_URL
from ..utils.io import download_from_url


def download():
    """
     Download the specific model from s3.
    """
    _url = MODELS_URL['WORD_TOKENIZER_WEIGHTS']
    file_name = _url.split("/")[-1]
    download_from_url(file_name=file_name, url=_url, download_dir='models/tokenizer/word/')

    _url = MODELS_URL["POS_TAGGER_WEIGHTS"]
    file_name = _url.split("/")[-1]
    download_from_url(file_name=file_name, url=_url, download_dir='models/tagger/pos/')

    _url = MODELS_URL["NER_WEIGHTS"]
    file_name = _url.split("/")[-1]
    download_from_url(file_name=file_name, url=_url, download_dir='models/ner/')

    # Sentiment model
    # _url = MODELS_URL['SENTIMENT_V1_WEIGHTS']
    # file_name = _url.split("/")[-1]
    # download_from_url(file_name=file_name, url=_url, download_dir='models/sentiment/v1')
