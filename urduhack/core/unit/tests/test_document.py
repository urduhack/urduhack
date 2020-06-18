
from urduhack import CoNLL
from urduhack.core.unit.document import Document
from urduhack.core.unit.sentence import Sentence
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


def test_sentences(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    assert isinstance(doc.sentences, list)
    doc.sentences = [[{"id": "1", "text": "والدین"}]]
    assert doc.sentences == [[{"id": "1", "text": "والدین"}]]


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
        sentence.text = "والدین زخمی"
        assert sentence.text == "والدین زخمی"


def test_num_tokens(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    assert doc.num_tokens == 6
    doc.num_tokens = 5
    assert doc.num_tokens == 5


def test_num_words(tmpdir):
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = tmpdir.join("test.txt")
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    assert doc.num_words == 6
    doc.num_words = 5
    assert doc.num_words == 5


def test_get():
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = "test.txt"
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    assert isinstance(doc.get(["id"]), list)


def test_set():
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = "test.txt"
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    doc.set(['text'], ["ہے", "ہے", "ہے", "ہے", "ہے", "ہے"])
    for sentence in doc.sentences:
        for token in sentence.words:
            assert token.text == "ہے"


def test_iter_tokens():
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = "test.txt"
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for token in doc.iter_tokens():
        assert isinstance(token, Token)


def test_iter_words():
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = "test.txt"
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    for word in doc.iter_words():
        assert isinstance(word, Word)


def test_to_dict():
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = "test.txt"
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    assert isinstance(doc.to_dict(), list)


def test_conll():
    """Test Case"""
    texts = CONLL_SENTENCE.splitlines()
    file_name = "test.txt"
    with open(file_name, "w") as file:
        for text in texts:
            text = text.strip()
            file.write(text + "\n")
    conll_data = CoNLL.load_file(file_name)
    doc = Document(conll_data)
    assert isinstance(doc.conll(), str)