"""SentencePiece based word tokenizer module"""

from pathlib import Path
from typing import List

import sentencepiece as spm
from urduhack.stop_words import STOP_WORDS


def _is_token(pieces: list, special_symbol: str = "▁") -> List[str]:
    """
    Check for stopwords and actual words in word pieces

    Args:
         pieces (list): word pieces returned by sentencepiece model
         special_symbol (str): spm prefix special symbol for space
    Returns:
        List of decoded words
    """
    decoded = []
    for piece in pieces:
        if special_symbol not in piece:
            if piece in STOP_WORDS or len(piece) > 3:
                piece = special_symbol + piece
                decoded.append(piece)
            else:
                decoded.append(piece)
        else:
            decoded.append(piece)
    return decoded


def _load_model(model_path: str) -> spm.SentencePieceProcessor:
    """
    Loads pre_trained keras model and vocab file

    Args:
        model_path (str): Path to the spm model file
    Returns:
        spm model class instance
    """
    spm_model = spm.SentencePieceProcessor()
    spm_model.Load(model_file=model_path)
    return spm_model


def _is_model_available(model_path: str) -> None:
    """
    Check if the models file exist.

    Args:
        model_path (str): path to the tokenizer model file
    Raises:
        FileNotFoundError: If model_path does not exist
    Returns: None
    """
    if not Path(model_path).exists():
        _error = "Word tokenizer Model not found!" \
                 "Please run 'urduhack download' in terminal." \
                 "Doc: https://urduhack.readthedocs.io/en/stable/installation.html#downloading-models"
        raise FileNotFoundError(_error)
