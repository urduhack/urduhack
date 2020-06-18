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


def test_token_init_from_misc(tmpdir):
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
        for token in sentence.tokens:
            assert token.init_from_misc() is None


def test_token_id(tmpdir):
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
        for token in sentence.tokens:
            assert isinstance(token.id, str)
            token.id = "1"
            assert token.id == "1"


def test_token_text(tmpdir):
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
        for token in sentence.tokens:
            assert isinstance(token.text, str)
            token.text = "کورونا"
            assert token.text == "کورونا"


def test_token_misc(tmpdir):
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
        for token in sentence.tokens:
            assert isinstance(token.misc, str)
            token.misc = "NER"
            assert token.misc == "NER"


def test_token_words(tmpdir):
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
        for token in sentence.tokens:
            assert isinstance(token.words, list)


def test_token_start_char(tmpdir):
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
        for token in sentence.tokens:
            assert token.start_char is None


def test_token_end_char(tmpdir):
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
        for token in sentence.tokens:
            assert token.end_char is None


def test_token_ner(tmpdir):
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
        for token in sentence.tokens:
            assert token.ner is None
            token.ner = "Other"
            assert token.ner == "Other"


def test_token_to_dict(tmpdir):
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
        for token in sentence.tokens:
            assert isinstance(token.to_dict(), list)


def test_word_init_from_misc(tmpdir):
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
        for word in sentence.words:
            assert word.init_from_misc() is None


def test_word_id(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.id, str)
            word.id = "1"
            assert word.id == "1"


def test_word_text(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.text, str)
            word.text = "کورونا"
            assert word.text == "کورونا"


def test_word_lemma(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.lemma, str)
            word.lemma = "_"
            assert word.lemma is None


def test_word_upos(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.upos, str)
            word.upos = "_"
            assert word.upos is None


def test_word_xpos(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.xpos, str)
            word.xpos = "_"
            assert word.xpos is None


def test_word_feats(tmpdir):
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
        for word in sentence.words:
            if word.pos != 'PUNCT':
                assert isinstance(word.feats, str)


def test_word_head(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.head, int)
            word.head = "_"
            assert word.head is None


def test_word_deprel(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.deprel, str)
            word.deprel = "_"
            assert word.deprel is None


def test_word_deps(tmpdir):
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
        for word in sentence.words:
            assert word.deps is None


def test_word_misc(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.misc, str)
            word.misc = "_"
            assert word.misc is None


def test_word_parent(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.parent, Token)
            word.parent = [{"id": "1"}]
            assert word.parent == [{"id": "1"}]


def test_word_pos(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.pos, str)
            word.pos = "_"
            assert word.pos is None


def test_word_to_dict(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.to_dict(), dict)


def test_word_to_conll(tmpdir):
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
        for word in sentence.words:
            assert isinstance(word.conll(), str)