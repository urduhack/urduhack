# coding: utf8
"""Different file types read/write utils"""

import os
import pickle
from typing import Any
from zipfile import ZipFile

import smart_open

from ..errors import Errors


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


def download_from_url(url: str, file_path: str, file_name: str) -> None:
    """
    Download anything from HTTP url

    Args:
        url (str): HTTP url
        file_path (str): location to store file
        file_name (str): name of the file

    Returns:
        None
    """
    if not isinstance(url, str):
        raise TypeError(Errors.E001.format(object_name="url", object_type="str"))
    if not isinstance(file_path, str):
        raise TypeError(Errors.E001.format(object_name="file_path", object_type="str"))
    if not isinstance(file_name, str):
        raise TypeError(Errors.E001.format(object_name="file_name", object_type="str"))

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    with smart_open.open(url, "rb") as in_file:
        with open(file_name, "wb") as out_file:
            for line in in_file:
                out_file.write(line)


def extract_weights(file_path: str, model_dir: str, file_dir: str) -> None:
    """
    Extracts file into the specified directory

    Args:
        file_path (str): location of the zip file
        model_dir (str): Directory into which file will be extracted
        file_dir (str): directory containing downloaded file

    Returns:
        None
    """
    if not isinstance(file_path, str):
        raise ValueError(Errors.E001.format(object_name="file_path", object_type="str"))
    if not isinstance(file_path, str):
        raise ValueError(Errors.E001.format(object_name="model_dir", object_type="str"))
    if not isinstance((file_dir, str)):
        raise ValueError(Errors.E001.format(object_name="file_dir", object_type="str"))

    with ZipFile(file_path) as z_file:
        z_file.extractall(model_dir)
        os.remove(file_path)
        os.rmdir(file_dir)
