"""Test Cases for sentiment module"""

from urduhack.utils import pickle_load
from ...config import SENTIMENT_VOCAB_PATH, MAX_SEQUENCE_LENGTH
from ..sentiment_analysis import convert_word_to_index, pad_sequences


def test_convert_word_to_index():
    """Test Case"""
    word_tokens = [['او', 'آئی', 'سی', 'کے', 'پلیٹ', 'فارم', 'سے', 'بھی', 'بھارت', 'پر', 'بے', 'پناہ', 'تنقید', 'ہو', 'رہی', 'ہے']]
    word_index = pickle_load(SENTIMENT_VOCAB_PATH)
    sequences = convert_word_to_index(word_tokens, word_index)
    for token in sequences:
        for element in token:
            assert isinstance(element, int)


def test_pad_sequences():
    """Test Case"""
    sequences = [[1, 2, 3, 4, 5, 6, 6], [77, 34, 12, 32, 76]]
    padded = pad_sequences(sequences)
    assert padded.shape[1] == MAX_SEQUENCE_LENGTH
