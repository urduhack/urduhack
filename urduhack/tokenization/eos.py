# coding: utf8
"""Sentence tokenization module"""
from regex import sub
from ..errors import Errors

# Global Variables
URDU_CONJUNCTIONS = ['جنہیں', 'جس', 'جن', 'جو', 'اور', 'اگر', 'اگرچہ', 'لیکن', 'مگر', 'پر', 'یا', 'تاہم', 'کہ', 'کر','تو', 'گے', 'گی', 'وہاں' ]
URDU_NEWLINE_WORDS = ['کیجیے','کیجئے', 'گئیں', 'تھیں', 'ہوں', 'خریدا', 'گے', 'ہونگے', 'گا', 'چاہیے', 'ہوئیں', 'گی',
                      'تھا', 'تھی', 'تھے', 'ہیں', 'ہے',
                      ]


def _split_and_keep(_str, separator):
    """Replace end of sentence with separator"""
    if not _str:
        return []
    max_p = chr(ord(max(_str)) + 1)
    return _str.replace(separator, separator + max_p).split(max_p)


def _generate_sentences(text: str):
    """Generate a list of urdu sentences from a given string.
    This function automatically fixes multiple whitespaces
    or new lines so you just need to pass the data and
    get sentences in return.
    Args:
        text (str): base str
    Returns:
        list
    Raises:
        TypeError: If text is not a str Type
    """

    if not isinstance(text, str):
        raise TypeError(Errors.E001.format(object_name=text, object_type=str))

    all_sentences = []
    sentences = _split_and_keep(text, '۔')
    sen_counter = 0
    for sentence in sentences:
        if sentence and (len(sentence.split()) >= 2):
            if '؟' in sentence:
                q_sentences = _split_and_keep(sentence, '؟')
                for _sen in q_sentences:
                    _sen = sub(r"\n", " ", _sen)
                    _sen = sub(' +', ' ', _sen)
                    # Removing trailing spaces and splitting
                    _sen = _sen.split()
                    new_sent = ""
                    for index, word in enumerate(_sen):
                        if word in URDU_NEWLINE_WORDS and index + 1 < len(
                                _sen) and _sen[index + 1] not in URDU_CONJUNCTIONS:
                            new_sent += " " + word + "۔"
                        else:
                            new_sent += " " + word

                    for sen in _split_and_keep(new_sent, '۔'):
                        if sen and len(sen.split()) >= 2:
                            all_sentences.append(sen.strip())

            else:
                sentence = sub(r"\n", " ", sentence)
                sentence = sub(' +', ' ', sentence)
                # Removing trailing spaces and splitting
                sentence = sentence.split()
                new_sent = ""

                for index, word in enumerate(sentence):
                    if word in URDU_NEWLINE_WORDS and index + 1 < len(
                            sentence) and \
                            sentence[index + 1] not in URDU_CONJUNCTIONS:

                        new_sent += " " + word + "۔"
                    else:
                        new_sent += " " + word
                for sen in _split_and_keep(new_sent, '۔'):
                    if sen and len(sen.split()) >= 2:
                        all_sentences.append(sen.strip())
        sen_counter += 1
    return all_sentences
