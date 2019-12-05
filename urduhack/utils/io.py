# coding: utf8
"""Different file types read/write utils"""

import os
import pickle
from pathlib import Path
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


def download_from_url(url: str, file_path: str, ) -> None:
    """
    Download anything from HTTP url

    Args:
        url (str): HTTP url
        file_path (str): location to store file

    Returns:
        None
    """
    if not isinstance(url, str):
        raise TypeError(Errors.E001.format(object_name="url", object_type="str"))
    if not isinstance(file_path, str):
        raise TypeError(Errors.E001.format(object_name="file_path", object_type="str"))

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_name = f"{file_path}/{url.split('/')[-1]}"
    with smart_open.open(url, "rb") as in_file:
        with open(file_name, "wb") as out_file:
            for line in in_file:
                out_file.write(line)


def extract_zip(zip_file: str, unzip_dir: str) -> None:
    """
    Extracts file into the specified directory

    Args:
        zip_file (str): location of the zip file
        unzip_dir (str): Directory into which file will be extracted
    Returns:
        None
    """
    if not isinstance(zip_file, str):
        raise ValueError(Errors.E001.format(object_name="zip_file", object_type="str"))
    if not isinstance(unzip_dir, str):
        raise ValueError(Errors.E001.format(object_name="unzip_dir", object_type="str"))

    with ZipFile(zip_file) as z_file:
        z_file.extractall(unzip_dir)


def remove_file(file_name: str) -> None:
    """Deletes the file

    Args:
        file_name (str): file to be deleted

    Returns:
        None
    """
    if Path(file_name).exists():
        os.remove(file_name)
