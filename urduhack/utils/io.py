# coding: utf8
"""Different file types read/write utils"""

import pickle
from typing import Any


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
