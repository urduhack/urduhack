# coding: utf8
"""Download data for online storage"""

import click

from urduhack.config import MODELS_URL, URDUHACK_MODElS_DIR
from urduhack.utils.io import download_from_url, extract_zip


@click.command()
def cli() -> None:
    """
     Download the specific model from s3.

    Args:

    Returns:
        None

    """
    _url = MODELS_URL['WORD_TOKENIZER_WEIGHTS']
    model_file_name = _url.split("/")[-1]
    model_file_path = f"{URDUHACK_MODElS_DIR}/{model_file_name}"
    version = model_file_name[8:10]
    unzip_dir = f"{URDUHACK_MODElS_DIR}/tokenizer/word/{version}"
    download_from_url(url=_url, file_path=URDUHACK_MODElS_DIR)
    extract_zip(zip_file=model_file_path, unzip_dir=unzip_dir)
