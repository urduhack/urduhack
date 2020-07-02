# coding: utf8
"""This module reasonable for storing all Constant values"""

from pathlib import Path
from typing import Dict

# Directories
USER_HOME_DIR: str = str(Path.home())
URDUHACK_BASE_DIR: str = f"{USER_HOME_DIR}/.urduhack"
URDUHACK_MODElS_DIR: str = f"{URDUHACK_BASE_DIR}/models"
URDUHACK_DATASETS_DIR: str = f"{URDUHACK_BASE_DIR}/datasets"

WORD_TOKENIZER_MODEL_PATH: str = f"{URDUHACK_MODElS_DIR}/tokenizer/word/word_tokenizer.h5"
WORD_TOKENIZER_VOCAB_PATH: str = f"{URDUHACK_MODElS_DIR}/tokenizer/word/vocab.txt"

POS_TAGGER_WEIGHTS_PATH: str = f"{URDUHACK_MODElS_DIR}/tagger/pos/tf_pos_weights.h5"
POS_WORD2IDX_PATH: str = f"{URDUHACK_MODElS_DIR}/tagger/pos/word2idx.json"
POS_TAG2IDX_PATH: str = f"{URDUHACK_MODElS_DIR}/tagger/pos/tag2idx.json"

NER_WEIGHTS_PATH: str = f"{URDUHACK_MODElS_DIR}/ner/tf_ner_weights.h5"
NER_WORD2IDX_PATH: str = f"{URDUHACK_MODElS_DIR}/ner/word2idx.json"
NER_TAG2IDX_PATH: str = f"{URDUHACK_MODElS_DIR}/ner/tag2idx.json"

# Models URLs
MODELS_URL: Dict[str, str] = {
    "WORD_TOKENIZER_WEIGHTS": "https://github.com/urduhack/resources/releases/download/"
                              "word_tokenizer/word_tokenizer.zip",
    "SENTIMENT_V1_WEIGHTS": "https://sgp1.digitaloceanspaces.com/urduhack/models/sentiment/v1/sentiment_v1.zip",
    "POS_TAGGER_WEIGHTS": "https://github.com/urduhack/resources/releases/download/pos_tagger/pos_tagger.zip",
    "NER_WEIGHTS": "https://github.com/urduhack/resources/releases/download/ner/ner.zip"
}
