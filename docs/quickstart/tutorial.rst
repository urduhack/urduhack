Tutorial
========

CoNLL-U Format
--------------
We aspire to maintain data for all the tasks in CoNNL-U format. CoNLL-U format holds sentence and token level data along with their
attributes. Below we will show how to use urduhack's :py:mod:`~urduhack.CoNLL` module. ::


    >>> from urduhack import CoNLL

To iterate over sentences in CoNLL-U format we will use :py:func:`~urduhack.CoNLL.iter_string` function. ::

    >>> from urduhack.conll.tests.test_parser import CONLL_SENTENCE

It will yield a sentence in proper CoNLL-U format from which we can extract sentence level and token level attributes. ::

    >>> for sentence in CoNLL.iter_string(CONLL_SENTENCE):
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

To load a file in ConLL-U format, we will use :py:func:`urduhack.CoNLL.load_file` function. ::

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

Pipeline Module
---------------
Pipeline is a special module in urduhack. It's importance can be realized by the fact that it performs operation at **Document**,
**Sentence** and **Token** level. We can convert a document to sentence and a sentence into tokens in one go using the pipeline
module. After that we can run models or any other operation at the document, sentence and token levels.
Now we will go into these steps one by on.

Document
^^^^^^^^

We can get the document using pipeline module. ::

    >>> from urduhack import Pipeline
    >>> nlp = Pipeline()
    >>> text = """
    گزشتہ ایک روز کے دوران کورونا کے سبب 118 اموات ہوئیں جس کے بعد اموات کا مجموعہ 3 ہزار 93 ہوگیا ہے۔
    سب سے زیادہ اموات بھی پنجاب میں ہوئی ہیں جہاں ایک ہزار 202 افراد جان کی بازی ہار چکے ہیں۔
    سندھ میں 916، خیبر پختونخوا میں 755، اسلام آباد میں 94، گلگت بلتستان میں 18، بلوچستان میں 93 اور ا?زاد کشمیر میں 15 افراد کورونا وائرس سے جاں بحق ہو چکے ہیں۔
    """
    >>> doc = nlp(text)
    >>> print(doc.text)

Sentence
^^^^^^^^

Now to get the sentences from the Document. ::

    >>> for sentence in doc.sentences:
            print(sentence.text)

Word
^^^^

To get words from sentence. ::

    >>> for word in sentence.words:
            print(word.text)

POS tagger
^^^^^^^^^^

Word class hold Pos tags. ::

    >>> for word in sentence.words:
            print(word.pos)

Lemmatizer
^^^^^^^^^^

Word class hold lemma. ::

    >>> for word in sentence.words:
            print(word.lemma)