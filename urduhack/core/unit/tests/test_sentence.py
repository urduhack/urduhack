# coding: utf8
"""
Test cases for sentence
"""
from urduhack import CoNLL
from urduhack.core.unit.sentence import Sentence
from urduhack.core.unit.token import Word, Token

CONLL_SENTENCE = """
# sent_id = test-s13
# text = والدین معمولی زخمی ہوئے ہےں۔
1	والدین	والدین	NOUN	NN	Case=Acc|Gender=Masc|Number=Sing|Person=3	4	nsubj	_	Vib=0|Tam=0|ChunkId=NP|ChunkType=head
2	معمولی	معمولی	ADJ	JJ	Case=Nom	3	advmod	_	ChunkId=JJP|ChunkType=head
3	زخمی	زخمی	ADJ	JJ	Case=Nom|Gender=Masc|Number=Sing|Person=3	4	compound	_	Vib=0|Tam=0|ChunkId=JJP2|ChunkType=head
4	ہوئے	ہو	VERB	VM	Aspect=Perf|Number=Plur|Person=2|Polite=Form|VerbForm=Part|Voice=Act	0	root	_	Vib=یا|Tam=yA|ChunkId=VGF|ChunkType=head|Stype=declarative
5	ہےں	ہے	AUX	VAUX	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	4	aux	_	SpaceAfter=No|Vib=ہے|Tam=hE|ChunkId=VGF|ChunkType=child
6	۔	۔	PUNCT	SYM	_	4	punct	_	ChunkId=VGF|ChunkType=child
"""


def test_sentence():
    """Test case"""
    _sentence = None
    for sentence in CoNLL.iter_string(CONLL_SENTENCE):
        _sentence = sentence

    sentence_obj = Sentence(_sentence)

    assert sentence_obj.meta_present("text") is True
    assert sentence_obj.meta_value("text") == "والدین معمولی زخمی ہوئے ہےں۔"

    sentence_obj.set_meta('number_check', "100")
    assert sentence_obj.meta_value("number_check") == "100"

    for word in sentence_obj.words:
        assert isinstance(word, Word)
    for token in sentence_obj.tokens:
        assert isinstance(token, Token)

    assert isinstance(sentence_obj.to_dict(), list)
    assert isinstance(sentence_obj.conll(), str)
