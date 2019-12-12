# coding: utf8
"""Test cases for text.py file"""
from pathlib import Path

import pytest

from ..io import remove_file, download_from_url, extract_zip
from ...config import MODELS_URL
WORD_TOKENIZER_WEIGHTS_URL = MODELS_URL["WORD_TOKENIZER_WEIGHTS"]
WORD_TOKENIZER_FILE_NAME = WORD_TOKENIZER_WEIGHTS_URL.split("/")[-1]


def test_download_from_url(tmpdir):
    """Test Case"""

    with pytest.raises(TypeError, match=r'[E001]'):
        download_from_url(url=123, file_path=1234, file_name=12)

    temp_model_dir = tmpdir.mkdir("sub")
    model_path = str(temp_model_dir) + "/" + WORD_TOKENIZER_FILE_NAME
    assert isinstance(WORD_TOKENIZER_WEIGHTS_URL, str) is True
    assert isinstance(model_path, str) is True
    assert isinstance(WORD_TOKENIZER_FILE_NAME, str) is True
    download_from_url(WORD_TOKENIZER_WEIGHTS_URL, str(temp_model_dir), WORD_TOKENIZER_FILE_NAME)
    assert Path(model_path).exists() is True


def test_extract_zip(tmpdir):
    """Test Case"""

    with pytest.raises(TypeError, match=r'[E001]'):
        extract_zip(zip_file=123, unzip_dir=1254)

    temp_model_dir = tmpdir.mkdir("sub")
    zipped_file = str(temp_model_dir) + "/" + WORD_TOKENIZER_FILE_NAME
    download_from_url(WORD_TOKENIZER_WEIGHTS_URL, str(temp_model_dir), WORD_TOKENIZER_FILE_NAME)
    unzip_dir = tmpdir.mkdir("unzipped")
    unzip_dir = str(unzip_dir)
    model_path = unzip_dir + "/" + "word_tokenizer.h5"
    vocab_path = unzip_dir + "/" + "vocab.txt"
    extract_zip(zipped_file, unzip_dir)
    assert Path(model_path).exists() is True
    assert Path(vocab_path).exists() is True


def test_remove_file(tmpdir):
    """Test Case"""

    with pytest.raises(TypeError, match=r'[E001]'):
        remove_file(file_name=123456)

    with pytest.raises(FileNotFoundError):
        remove_file(file_name="no_file")

    tmp_dir = tmpdir.mkdir("sub_dir")
    tmp_file = tmp_dir.join("hello.txt")
    tmp_file.write("This is a test Text")
    file_name = str(tmp_file)
    assert Path(tmp_dir).exists() is True
    assert Path(tmp_file).exists() is True
    assert tmp_file.read() == "This is a test Text"
    remove_file(file_name)
    assert Path(tmp_file).exists() is False
