# coding: utf8
"""Different file types read/write utils"""

import os
import pickle
from typing import Any
import smart_open
from zipfile import ZipFile


def pickle_dump(file_name: str, data) -> None:
    """
    Save the python object in pickle format

    Args:
        file_name (str): file name
        data: Any data type

    Returns:
        None
    """
    with open(file_name, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


def pickle_load(file_name: str) -> Any:
    """

    Args:
        file_name (str):  file name

    Returns:
        Any: python object type
    """
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def download_weights(url: str, file_name: str, path: str):
    """
    Args:
        url (str): url
        file_name (str): file name
        path (str): path to the model

    Returns:
        Any: python object type
    """
    with smart_open.open(url, "rb") as in_file:
        with open(file_name, "wb") as out_file:
            for line in in_file:
                out_file.write(line)

    if not os.path.exists(path):
        os.makedirs(path)
    with ZipFile(file_name) as z_file:
        z_file.extractall(path)
    os.remove(file_name)