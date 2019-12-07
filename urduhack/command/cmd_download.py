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
    extract_file = f"{URDUHACK_MODElS_DIR}/{_url.split('/')[-1]}"
    download_from_url(url=_url, file_path=URDUHACK_MODElS_DIR)
    extract_zip(zip_file=extract_file, unzip_dir=URDUHACK_MODElS_DIR)
