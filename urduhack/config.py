# coding: utf8
"""This module reasonable for storing all Constant values"""

from pathlib import Path
from typing import Dict

# Directories
USER_HOME_DIR: str = str(Path.home())
URDUHACK_BASE_DIR: str = f"{USER_HOME_DIR}/.urduhack"
URDUHACK_MODElS_DIR: str = f"{URDUHACK_BASE_DIR}/models"
URDUHACK_DATASETS_DIR: str = f"{URDUHACK_BASE_DIR}/datasets"

MODEL_PATH: str = f"{URDUHACK_MODElS_DIR}/tokenizer/word/v1/word_tokenizer.h5"
VOCAB_PATH: str = f"{URDUHACK_MODElS_DIR}/tokenizer/word/v1/vocab.txt"

ROBERTA_PATH: str = f"{URDUHACK_MODElS_DIR}/sentiment/v1/roberta/"
LAYERS_WEIGHTS_PATH: str = f"{URDUHACK_MODElS_DIR}/sentiment/v1/model_layers_weights.pkl"

# Models URLs
MODELS_URL: Dict[str, str] = {
    "WORD_TOKENIZER_WEIGHTS": "https://sgp1.digitaloceanspaces.com/urduhack/models/tokenizer/word/weights_v1.zip",
    "SENTIMENT_V1_WEIGHTS": "https://sgp1.digitaloceanspaces.com/urduhack/models/sentiment/v1/sentiment_v1.zip",
}
