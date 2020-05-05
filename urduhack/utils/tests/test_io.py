# coding: utf8
"""Test IO Module"""
from pathlib import Path

import pytest

from ..io import remove_file, download_from_url, extract_zip, pickle_load, pickle_dump
from ...config import MODELS_URL
WORD_TOKENIZER_WEIGHTS_URL = MODELS_URL["WORD_TOKENIZER_WEIGHTS"]
WORD_TOKENIZER_FILE_NAME = WORD_TOKENIZER_WEIGHTS_URL.split("/")[-1]


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

    with pytest.raises(TypeError, match=r'[E001]'):
        download_from_url(url=123, file_path=1234)

    with pytest.raises(TypeError):
        download_from_url(url=WORD_TOKENIZER_WEIGHTS_URL, file_path=1234)

    temp_model_dir = tmpdir.mkdir("sub")
    model_path = str(temp_model_dir) + "/" + WORD_TOKENIZER_FILE_NAME
    assert isinstance(WORD_TOKENIZER_WEIGHTS_URL, str)
    assert isinstance(model_path, str)
    assert isinstance(WORD_TOKENIZER_FILE_NAME, str)
    download_from_url(WORD_TOKENIZER_WEIGHTS_URL, str(temp_model_dir))
    assert Path(model_path).exists()


def test_extract_zip(tmpdir):
    """Test Case"""

    temp_model_dir = tmpdir.mkdir("sub")
    zipped_file = str(temp_model_dir) + "/" + WORD_TOKENIZER_FILE_NAME

    with pytest.raises(TypeError, match=r'[E001]'):
        extract_zip(zip_file=zipped_file, unzip_dir=1254)

    with pytest.raises(TypeError):
        extract_zip(zip_file=1234, unzip_dir="test_unzip/")

    download_from_url(WORD_TOKENIZER_WEIGHTS_URL, str(temp_model_dir), WORD_TOKENIZER_FILE_NAME)
    unzip_dir = tmpdir.mkdir("unzipped")
    unzip_dir = str(unzip_dir)
    model_path = unzip_dir + "/" + "word_tokenizer.h5"
    vocab_path = unzip_dir + "/" + "vocab.txt"
    extract_zip(zipped_file, unzip_dir)
    assert Path(model_path).exists()
    assert Path(vocab_path).exists()


def test_remove_file(tmpdir):
    """Test Case"""

    with pytest.raises(TypeError, match=r'[E001]'):
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
