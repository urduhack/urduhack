# coding: utf8
"""Different file types read/write utils"""

import pickle
from pathlib import Path
from typing import Any, Optional
from zipfile import ZipFile

import requests
import tqdm

from ..errors import Errors


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


def download_from_url(url: str, file_path: str, file_name: Optional[str] = None):
    """
    Download anything from HTTP url

    Args:
        url (str): HTTP url
        file_path (str): location to store file
        file_name (str): Save file as provided file name
    Raises:
        TypeError: If any of the url, file_path and file_name are not str Type.
    """
    if not isinstance(url, str):
        raise TypeError(Errors.E001.format(object_name="url", object_type="str"))
    if not isinstance(file_path, str):
        raise TypeError(Errors.E001.format(object_name="file_path", object_type="str"))

    Path(file_path).mkdir(parents=True, exist_ok=True)

    if file_name is None:
        file_name = url.split('/')[-1]

    file_name = f"{file_path}/{file_name}"
    req = requests.get(url, stream=True)
    file_size = int(req.headers['Content-Length'])
    chunk_size = 1024
    num_bars = int(file_size / chunk_size)

    tqdm_description: str = f"Downloading {file_name.split('/')[-1]}({file_size} bytes)"
    with open(file_name, 'wb') as f_p:
        for chunk in tqdm.tqdm(req.iter_content(chunk_size=chunk_size), total=num_bars, unit='KB',
                               desc=tqdm_description,
                               leave=True):
            f_p.write(chunk)


def extract_zip(zip_file: str, unzip_dir: str):
    """
    Extracts file into the specified directory

    Args:
        zip_file (str): location of the zip file
        unzip_dir (str): Directory into which file will be extracted
    Raises:
        TypeError: If any of zip_file and unzip_dir are not str Type.
    """
    if not isinstance(zip_file, str):
        raise TypeError(Errors.E001.format(object_name="zip_file", object_type="str"))
    if not isinstance(unzip_dir, str):
        raise TypeError(Errors.E001.format(object_name="unzip_dir", object_type="str"))

    with ZipFile(zip_file) as z_file:
        z_file.extractall(unzip_dir)


def remove_file(file_name: str):
    """
    Delete the local file

    Args:
        file_name (str): file to be deleted
    Raises:
        TypeError: if file_name is not str Type.
        FileNotFoundError: If file_name does not exist
    """
    if not isinstance(file_name, str):
        raise TypeError(Errors.E001.format(object_name="file_name", object_type="str"))

    Path(file_name).unlink()
