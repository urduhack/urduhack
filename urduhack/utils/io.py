# coding: utf8
"""Different file types read/write utils"""

import pickle
from pathlib import Path
from typing import Any, Optional

import tensorflow as tf

from ..config import URDUHACK_BASE_DIR


def pickle_dump(file_name: str, data: Any):
    """
    Save the python object in pickle format

    Args:
        file_name (str): file name
        data (Any): Any data type
    """
    with open(file_name, 'wb') as file:
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)


def pickle_load(file_name: str) -> Any:
    """
    Load the pickle file

    Args:
        file_name (str):  file name
    Returns:
        Any: python object type
    """
    with open(file_name, 'rb') as file:
        return pickle.load(file)


def download_from_url(file_name: str, url: str, download_dir: str, cache_dir: Optional[str] = None):
    """
    Download anything from HTTP url

    Args:
        file_name (str): Save file as provided file name
        url (str): HTTP url
        download_dir (str): location to store file
        cache_dir (str): Main download dir
    Raises:
        TypeError: If any of the url, file_path and file_name are not str Type.
    """
    if not isinstance(url, str):
        raise TypeError(f"{url} must be str type.")
    if not isinstance(file_name, str):
        raise TypeError(f"{file_name} must be str type.")
    if not isinstance(download_dir, str):
        raise TypeError(f"{download_dir} must be str type.")

    if cache_dir is None:
        cache_dir = URDUHACK_BASE_DIR

    Path(cache_dir).mkdir(parents=True, exist_ok=True)
    tf.keras.utils.get_file(fname=file_name, origin=url, cache_subdir=download_dir, cache_dir=cache_dir, extract=True)


def remove_file(file_name: str):
    """
    Delete the local file

    Args:
        file_name (str): File to be deleted
    Raises:
        TypeError: If file_name is not str Type.
        FileNotFoundError: If file_name does not exist
    """
    if not isinstance(file_name, str):
        raise TypeError(f"{file_name} must be str type.")

    Path(file_name).unlink()
