# coding: utf8
"""Test IO Module"""
from pathlib import Path

import pytest

from urduhack.utils.io import remove_file, download_from_url, pickle_load, pickle_dump
from urduhack.config import MODELS_URL
SENTIMENT_WEIGHTS_URL = MODELS_URL["SENTIMENT_V1_WEIGHTS"]
SENTIMENT_FILE_NAME = SENTIMENT_WEIGHTS_URL.split("/")[-1]


def test_pickle_dump(tmpdir):
    """Test Case"""
    text = "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    data = text.split()
    tmp_dir = tmpdir.mkdir("sub_dir")
    tmp_file = tmp_dir.join("hello.pkl")
    pickle_dump(tmp_file, data)
    loaded = pickle_load(tmp_file)
    assert loaded == data


def test_download_from_url(tmpdir):
    """Test Case"""

    with pytest.raises(TypeError, match=r'str'):
        download_from_url(file_name='test_abc', url=123, download_dir=1234, cache_dir='cache_test')

    with pytest.raises(TypeError):
        download_from_url(file_name='test_abc', url=SENTIMENT_WEIGHTS_URL, download_dir=1234, cache_dir=543)

    temp_model_dir = tmpdir.mkdir("sub")
    model_path = str(temp_model_dir) + "/test_sentiment/" + SENTIMENT_FILE_NAME
    assert isinstance(SENTIMENT_WEIGHTS_URL, str)
    assert isinstance(model_path, str)
    assert isinstance(SENTIMENT_FILE_NAME, str)
    download_from_url(file_name=SENTIMENT_FILE_NAME, url=SENTIMENT_WEIGHTS_URL,
                      download_dir="test_sentiment", cache_dir=str(temp_model_dir))
    assert Path(model_path).exists()


def test_remove_file(tmpdir):
    """Test Case"""

    with pytest.raises(TypeError, match=r'[str]'):
        remove_file(file_name=123456)

    with pytest.raises(FileNotFoundError):
        remove_file(file_name="no_file")

    tmp_dir = tmpdir.mkdir("sub_dir")
    tmp_file = tmp_dir.join("hello.txt")
    with open(tmp_file, "w", encoding="utf-8") as temp_file:
        temp_file.write("ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی")
    file_name = str(tmp_file)
    assert Path(tmp_dir).exists()
    assert Path(tmp_file).exists()
    with open(tmp_file, "r", encoding="utf-8") as read_file:
        line = read_file.read()
        assert line == "ترقی رکنے سے آہستہ آہستہ پاکستان نیچے چلاگی"
    remove_file(file_name)
    assert Path(tmp_file).exists() is False
