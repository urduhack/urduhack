# coding: utf8
"""Download data for online storage"""

import click

from urduhack.config import MODELS_URL
from urduhack.utils.io import download_from_url


@click.command()
def cli():
    """
     Download the specific model from s3.
    """
    _url = MODELS_URL['WORD_TOKENIZER_WEIGHTS']
    file_name = _url.split("/")[-1]
    download_from_url(file_name=file_name, url=_url, download_dir='models/tokenizer/word/v1')

    # Sentiment model
    _url = MODELS_URL['SENTIMENT_V1_WEIGHTS']
    file_name = _url.split("/")[-1]
    download_from_url(file_name=file_name, url=_url, download_dir='models/sentiment/v1')
