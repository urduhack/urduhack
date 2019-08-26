import numpy as np
import tensorflow as tf

class UrduWordTokenizer:
    """
    An UrduWordTokenizer object is a self contained tokenizer capable
    of tokenizing words in an urdu sentence as well as fixing errors in
    urdu sentences.

    """
    def __init__(self, vocab_file='vocab.txt', model_file='word_tokenizer.h5'):
        """
        Creates a UrduWordTokenizer object based on the files specified
        
        Args:
            vocab_file (str): Path to the vocabulary file of the tokenizer, contains all characters model can identify
            model_file (str): Path to HDF5 file used to load tokenizer model
        """
        self._load_vocab(vocab_file)
        self._tokenizer = tf.keras.models.load_model(model_file)
        self._max_length = 256
        self._min_length = 10
        self._threshold = 0.5

    def _load_vocab(self, file: str):
        """
        Used privately by UrduWordTokenizer object to intialize dictionaries mapping characters to embedding ids and vice versa.
        
        Args:
            file (str): Path to the vocabulary file of the tokenizer, contains all characters model can identify
        """
        vocab_file = open(file)
        vocab = vocab_file.readline()
        vocab = list('_' + vocab)
        vocab.remove('\n')
        self._char2idx = {char: idx for idx, char in enumerate(vocab)}
        self._idx2char = {idx: char for idx, char in enumerate(vocab)}
  
    def _preprocess_sentences(self, sentences: list) -> np.array:
        """
        Used privately by UrduWordTokenizer object to remove whitespaces from sentences received, map their characters to 
        embedding ids and pad them to equal lengths.
        
        Args:
            sentences (list): List of sentences to preprocess
        
        Returns:
            np.array: Preprocessed setences returned in the form of a 3-dimensional array
        """
        input_chars = np.chararray((len(sentences),self._max_length),unicode=True)
        input_ = np.zeros((len(sentences),self._max_length),dtype=int)
        for i,sentence in enumerate(sentences):
            ls = np.array(list(sentence))
            spaces = (ls==' ')
            chars = ls[~spaces]
            if (len(chars)>self._max_length):
                continue
            input_chars[i,:len(chars)] = chars
        for key,value in self._char2idx.items():
            input_[input_chars == key] = value
        return input_

    def _retrieve_sentence(self, x: np.array, y: np.array) -> str:
        """
        Used privately by UrduWordTokenizer object to convert preprocessed array and predicted spaces to readable sentence.
        
        Args:
            x (np.array): Array representing characters in sentence
            y (np.array): Array representing predicted spaces in sentence
        
        Returns:
            str: Predicted sentence
        """
        mask = (x != 0)
        letters = x[mask]
        spaces = y[mask]
        final = ''
        for letter in range(letters.shape[0]):
            idx = letters[letter]
            if(idx!=0):
                final += self._idx2char[idx]
            if spaces[letter] >= self._threshold:
                final += ' '
        return final
  
    def _retrieve_words(self, x: np.array, y: np.array) -> list:
        """
        Used privately by UrduWordTokenizer object to convert preprocessed array and predicted spaces to list of words.
        
        Args:
            x (np.array): Array representing characters in sentence
            y (np.array): Array representing predicted spaces in sentence
        
        Returns:
            list: Tokenized words
        """
        sentence = self._retrieve_sentence(x,y)
        tokens = sentence.split(' ')
        return tokens
  
    def tokenize_words(self, sentence: str) -> list:
        """
        Tokenizes words of sentence received
        word: str
        Args:word: str
            sentence (str): Urdu sentence to be tokenizedword: str
        
        Returns:
            list: Tokenized words
        """
        model_input = self._preprocess_sentences([sentence])
        prediction = self._tokenizer.predict(model_input)
        return self._retrieve_words(np.squeeze(model_input),np.squeeze(prediction))
  
    def fix_sentence(self, sentence: str) -> str:
        """
        Fixes errors in spaces within sentence
        
        Args:
            sentence (str): Urdu sentenced to be fixed
        
        Returns:
            str: Fixed urdu sentence with correctly occuring spaces
        """
        model_input = self._preprocess_sentences([sentence])
        prediction = self._tokenizer.predict(model_input)
        return self._retrieve_sentence(np.squeeze(model_input),np.squeeze(prediction))
