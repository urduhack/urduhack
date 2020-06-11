"""Test Cases"""

from urduhack.conll.reader import CoNLL


def test_iter_from_string():
    """Test Case"""
    con_reader = CoNLL()
    text = """
    # sent_id = test-s13
    # text = والدین معمولی زخمی ہوئے ہےں۔
    1	والدین	والدین	NOUN	NN	Case=Acc|Gender=Masc|Number=Sing|Person=3	4	nsubj	_	Vib=0|Tam=0|ChunkId=NP|ChunkType=head
    2	معمولی	معمولی	ADJ	JJ	Case=Nom	3	advmod	_	ChunkId=JJP|ChunkType=head
    3	زخمی	زخمی	ADJ	JJ	Case=Nom|Gender=Masc|Number=Sing|Person=3	4	compound	_	Vib=0|Tam=0|ChunkId=JJP2|ChunkType=head
    4	ہوئے	ہو	VERB	VM	Aspect=Perf|Number=Plur|Person=2|Polite=Form|VerbForm=Part|Voice=Act	0	root	_	Vib=یا|Tam=yA|ChunkId=VGF|ChunkType=head|Stype=declarative
    5	ہےں	ہے	AUX	VAUX	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	4	aux	_	SpaceAfter=No|Vib=ہے|Tam=hE|ChunkId=VGF|ChunkType=child
    6	۔	۔	PUNCT	SYM	_	4	punct	_	ChunkId=VGF|ChunkType=child
    """
    data = con_reader.iter_from_string(text=text)
    for line in data:
        sentence = line[0]
        assert sentence['text'] == "والدین معمولی زخمی ہوئے ہےں۔"


def test_load_file(tmpdir):
    """Test Case"""
    text = """
    # sent_id = test-s13
    # text = والدین معمولی زخمی ہوئے ہےں۔
    1	والدین	والدین	NOUN	NN	Case=Acc|Gender=Masc|Number=Sing|Person=3	4	nsubj	_	Vib=0|Tam=0|ChunkId=NP|ChunkType=head
    2	معمولی	معمولی	ADJ	JJ	Case=Nom	3	advmod	_	ChunkId=JJP|ChunkType=head
    3	زخمی	زخمی	ADJ	JJ	Case=Nom|Gender=Masc|Number=Sing|Person=3	4	compound	_	Vib=0|Tam=0|ChunkId=JJP2|ChunkType=head
    4	ہوئے	ہو	VERB	VM	Aspect=Perf|Number=Plur|Person=2|Polite=Form|VerbForm=Part|Voice=Act	0	root	_	Vib=یا|Tam=yA|ChunkId=VGF|ChunkType=head|Stype=declarative
    5	ہےں	ہے	AUX	VAUX	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	4	aux	_	SpaceAfter=No|Vib=ہے|Tam=hE|ChunkId=VGF|ChunkType=child
    6	۔	۔	PUNCT	SYM	_	4	punct	_	ChunkId=VGF|ChunkType=child
    """
    file_name = tmpdir.join("test_conll.txt")
    with open(file_name, "w") as file:
        file.write(text)
    con_reader = CoNLL()
    data = con_reader.load_file(file_name=file_name)
    assert data[0][0]['text'] == "والدین معمولی زخمی ہوئے ہےں۔"


def test_iter_file(tmpdir):
    """Test Case"""
    text = """
    # sent_id = test-s13
    # text = والدین معمولی زخمی ہوئے ہےں۔
    1	والدین	والدین	NOUN	NN	Case=Acc|Gender=Masc|Number=Sing|Person=3	4	nsubj	_	Vib=0|Tam=0|ChunkId=NP|ChunkType=head
    2	معمولی	معمولی	ADJ	JJ	Case=Nom	3	advmod	_	ChunkId=JJP|ChunkType=head
    3	زخمی	زخمی	ADJ	JJ	Case=Nom|Gender=Masc|Number=Sing|Person=3	4	compound	_	Vib=0|Tam=0|ChunkId=JJP2|ChunkType=head
    4	ہوئے	ہو	VERB	VM	Aspect=Perf|Number=Plur|Person=2|Polite=Form|VerbForm=Part|Voice=Act	0	root	_	Vib=یا|Tam=yA|ChunkId=VGF|ChunkType=head|Stype=declarative
    5	ہےں	ہے	AUX	VAUX	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	4	aux	_	SpaceAfter=No|Vib=ہے|Tam=hE|ChunkId=VGF|ChunkType=child
    6	۔	۔	PUNCT	SYM	_	4	punct	_	ChunkId=VGF|ChunkType=child
    """
    file_name = tmpdir.join("test_conll.txt")
    with open(file_name, "w") as file:
        file.write(text)
    con_reader = CoNLL()
    data_iter = con_reader.iter_file(file_name=file_name)
    for data in data_iter:
        sentence = data[0]
        assert sentence['text'] == 'والدین معمولی زخمی ہوئے ہےں۔'
