# coding: utf8
"""Test Cases"""

from urduhack.conll.parser import parse_conll_sentence, parse_conll_token, _iter_lines

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


def test_parse_conll_sentence(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w", encoding="utf8") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    with open(file_name, "r", encoding="utf8") as file:
        sentence = file.read()
        s_meta, token_ = parse_conll_sentence(sentence)
        print(token_)
    assert isinstance(s_meta, dict)
    assert isinstance(token_, list)
    assert s_meta['text'] == 'والدین معمولی زخمی ہوئے ہےں۔'


def test_parse_conll_token():
    """Test Case"""
    text = """
    1	والدین	والدین	NOUN	NN	Case=Acc|Gender=Masc|Number=Sing|Person=3	4	nsubj	_	Vib=0|Tam=0|ChunkId=NP|ChunkType=head,
    """
    parsed_token = parse_conll_token(text)
    assert isinstance(parsed_token, dict)
    assert parsed_token['text'] == 'والدین'
    assert parsed_token['lemma'] == 'والدین'


def test_iter_lines(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w", encoding="utf8") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    with open(file_name, "r", encoding="utf8") as file:
        lines = file.readlines()
        lines = _iter_lines(lines)
        for line in lines:
            sentence = line[0]
            assert isinstance(sentence, dict)
            assert sentence['text'] == 'والدین معمولی زخمی ہوئے ہےں۔'
