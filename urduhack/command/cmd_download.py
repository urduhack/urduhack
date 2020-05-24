# coding: utf8
"""Download data for online storage"""

import click

from urduhack.utils.resources import download


@click.command()
def cli():
    """
     Download the specific model from s3.
    """
    download()
