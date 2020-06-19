# coding: utf8
"""
Test cases for document
"""
from urduhack import CoNLL
from urduhack.core.unit.document import Document
from urduhack.core.unit.token import Token, Word

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


def test_document(tmpdir):
    """
    test cases
    """
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w", encoding="utf8") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")

    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)

    assert isinstance(doc.sentences, list)
    assert doc.num_tokens == 6
    assert doc.num_words == 6

    for token in doc.iter_tokens():
        assert isinstance(token, Token)

    for word in doc.iter_words():
        assert isinstance(word, Word)

    assert isinstance(doc.to_dict(), list)

    assert isinstance(doc.conll(), str)

    words_to_check = []
    match_word = "والدین"
    for sentence in doc.sentences:
        for word in sentence.words:
            words_to_check.append(word.text)

    assert match_word in words_to_check
