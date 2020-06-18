from urduhack import CoNLL
from urduhack.core.unit.document import Document
from urduhack.core.unit.sentence import Sentence
from urduhack.core.unit.token import Token

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


def test_meta_present(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        assert isinstance(sentence, Sentence)
        assert sentence.meta_present(key="text") is True


def test_meta_value(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        assert isinstance(sentence, Sentence)
        assert sentence.meta_value(key="text") == "والدین معمولی زخمی ہوئے ہےں۔"


def test_set_meta(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        sentence.set_meta('test_id', 100)
        assert sentence.meta_value(key="test_id") == 100


def test_doc(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        isinstance(sentence.doc, Document)
        sentence.doc = [[{'id': '1', 'text': 'زخمی'}]]
        assert sentence.doc == [[{'id': '1', 'text': 'زخمی'}]]


def test_text(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        assert sentence.text is None
        sentence.text = "کورونا وائرس کے وار جاری"
        assert sentence.text == "کورونا وائرس کے وار جاری"


def test_tokens(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        assert isinstance(sentence.tokens, list)
        sentence.tokens = [{'id': "1", "text": "کورونا"}, {"id": "2", "text": "وائرس"}]
        assert sentence.tokens == [{'id': "1", "text": "کورونا"}, {"id": "2", "text": "وائرس"}]


def test_words(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        assert isinstance(sentence.words, list)
        sentence.words = [{'id': "1", "text": "کورونا"}, {"id": "2", "text": "وائرس"}]
        assert sentence.words == [{'id': "1", "text": "کورونا"}, {"id": "2", "text": "وائرس"}]


def test_to_dict(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        assert isinstance(sentence.to_dict(), list)


def test_conll(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for sentence in doc.sentences:
        assert isinstance(sentence.conll(), str)