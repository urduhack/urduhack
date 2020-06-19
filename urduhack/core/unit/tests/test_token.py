# coding: utf8
"""
Test cases for Tokens
"""
from urduhack import CoNLL
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


def test_token():
    """test cases"""
    for sentence in CoNLL.iter_string(CONLL_SENTENCE):
        _, tokens = sentence
        for token in tokens:
            token = Token(token)
            assert isinstance(token, Token)
            assert isinstance(token.id, str)
            assert isinstance(token.text, str)
            assert isinstance(token.misc, str)
            assert isinstance(token.words, list)
            assert isinstance(token.to_dict(), list)
            assert token.start_char is None
            assert token.end_char is None
            assert token.ner is None


def test_word():
    """test cases"""
    for sentence in CoNLL.iter_string(CONLL_SENTENCE):
        _, words = sentence
        for word in words:
            word = Word(word)
            assert isinstance(word, Word)
            assert isinstance(word.id, str)
            assert isinstance(word.lemma, str)
            assert isinstance(word.upos, str)
            assert isinstance(word.xpos, str)
            assert word.deps is None
            assert isinstance(word.deprel, str)
            assert isinstance(word.pos, str)
            if word.upos != "PUNCT":
                assert isinstance(word.feats, str)
            assert isinstance(word.head, int)
            assert word.parent is None
            assert isinstance(word.to_dict(), dict)
            assert isinstance(word.conll(), str)
