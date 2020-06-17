Tutorial
========

How to explore CoNLL-U Format
-----------------------------
We aspire to maintain data for all the tasks in CoNNL-U format. CoNLL-U format holds sentence and token level data along with their
attributes. Below we will show how to use urduhack's :py:mod:`~urduhack.CoNLL` module.::


    >>> from urduhack import CoNLL

To iterate over sentences in CoNLL-U format we will use :py:func:`~urduhack.CoNLL.iter_string` function.::

    >>> from urduhack.conll.tests.test_parser import CONLL_SENTENCE
    >>> text_iterator = CoNLL.iter_string(CONLL_SENTENCE)

It will yield a sentence in proper CoNLL-U format from which we can extract sentence level and token level attributes.::

    >>> for sentence in text_iterator:
            sent_meta, tokens = sentence
            print(f"Sentence ID: {sent_meta['sent_id']}")
            print(f"Sentence Text: {sent_meta['text']}")
            for token in tokens:
            print(token)
    Sentence ID: test-s13
    Sentence Text: والدین معمولی زخمی ہوئے ہےں۔
    {'id': '1', 'text': 'والدین', 'lemma': 'والدین', 'upos': 'NOUN', 'xpos': 'NN', 'feats': 'Case=Acc|Gender=Masc|Number=Sing|Person=3', 'head': '4', 'deprel': 'nsubj', 'deps': '_', 'misc': 'Vib=0|Tam=0|ChunkId=NP|ChunkType=head'}
    {'id': '2', 'text': 'معمولی', 'lemma': 'معمولی', 'upos': 'ADJ', 'xpos': 'JJ', 'feats': 'Case=Nom', 'head': '3', 'deprel': 'advmod', 'deps': '_', 'misc': 'ChunkId=JJP|ChunkType=head'}
    {'id': '3', 'text': 'زخمی', 'lemma': 'زخمی', 'upos': 'ADJ', 'xpos': 'JJ', 'feats': 'Case=Nom|Gender=Masc|Number=Sing|Person=3', 'head': '4', 'deprel': 'compound', 'deps': '_', 'misc': 'Vib=0|Tam=0|ChunkId=JJP2|ChunkType=head'}
    {'id': '4', 'text': 'ہوئے', 'lemma': 'ہو', 'upos': 'VERB', 'xpos': 'VM', 'feats': 'Aspect=Perf|Number=Plur|Person=2|Polite=Form|VerbForm=Part|Voice=Act', 'head': '0', 'deprel': 'root', 'deps': '_', 'misc': 'Vib=یا|Tam=yA|ChunkId=VGF|ChunkType=head|Stype=declarative'}
    {'id': '5', 'text': 'ہےں', 'lemma': 'ہے', 'upos': 'AUX', 'xpos': 'VAUX', 'feats': 'Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'head': '4', 'deprel': 'aux', 'deps': '_', 'misc': 'SpaceAfter=No|Vib=ہے|Tam=hE|ChunkId=VGF|ChunkType=child'}
    {'id': '6', 'text': '۔', 'lemma': '۔', 'upos': 'PUNCT', 'xpos': 'SYM', 'feats': '_', 'head': '4', 'deprel': 'punct', 'deps': '_', 'misc': 'ChunkId=VGF|ChunkType=child'}

To load a file in ConLL-U format, we will use :py:func:`urduhack.CoNLL.load_file` function.::

    >>> sentences = ConLL.load_file("urdu_text.conll")
    >>> for sentence in sentences:
                sent_meta, tokens = sentence
                print(f"Sentence ID: {sent_meta['sent_id']}")
                print(f"Sentence Text: {sent_meta['text']}")
                for token in tokens:
                    print(token)
    Sentence ID: test-s13
    Sentence Text: والدین معمولی زخمی ہوئے ہےں۔
    {'id': '1', 'text': 'والدین', 'lemma': 'والدین', 'upos': 'NOUN', 'xpos': 'NN', 'feats': 'Case=Acc|Gender=Masc|Number=Sing|Person=3', 'head': '4', 'deprel': 'nsubj', 'deps': '_', 'misc': 'Vib=0|Tam=0|ChunkId=NP|ChunkType=head'}
    {'id': '2', 'text': 'معمولی', 'lemma': 'معمولی', 'upos': 'ADJ', 'xpos': 'JJ', 'feats': 'Case=Nom', 'head': '3', 'deprel': 'advmod', 'deps': '_', 'misc': 'ChunkId=JJP|ChunkType=head'}
    {'id': '3', 'text': 'زخمی', 'lemma': 'زخمی', 'upos': 'ADJ', 'xpos': 'JJ', 'feats': 'Case=Nom|Gender=Masc|Number=Sing|Person=3', 'head': '4', 'deprel': 'compound', 'deps': '_', 'misc': 'Vib=0|Tam=0|ChunkId=JJP2|ChunkType=head'}
    {'id': '4', 'text': 'ہوئے', 'lemma': 'ہو', 'upos': 'VERB', 'xpos': 'VM', 'feats': 'Aspect=Perf|Number=Plur|Person=2|Polite=Form|VerbForm=Part|Voice=Act', 'head': '0', 'deprel': 'root', 'deps': '_', 'misc': 'Vib=یا|Tam=yA|ChunkId=VGF|ChunkType=head|Stype=declarative'}
    {'id': '5', 'text': 'ہےں', 'lemma': 'ہے', 'upos': 'AUX', 'xpos': 'VAUX', 'feats': 'Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin', 'head': '4', 'deprel': 'aux', 'deps': '_', 'misc': 'SpaceAfter=No|Vib=ہے|Tam=hE|ChunkId=VGF|ChunkType=child'}
    {'id': '6', 'text': '۔', 'lemma': '۔', 'upos': 'PUNCT', 'xpos': 'SYM', 'feats': '_', 'head': '4', 'deprel': 'punct', 'deps': '_', 'misc': 'ChunkId=VGF|ChunkType=child'}
