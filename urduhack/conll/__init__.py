# coding: utf8
"""
CoNLL-U Format
===============
This module reads and parse data in the standard CONLL-U format as provided in universal dependencies.
CONLL-U is a standard format followed to annotate data at sentence level and at word/token level.
Annotations in CONLL-U format fulfil the below points:

    1. Word lines contain the annotations of a word/token in 10 fields are separated by single tab characters
    2. Blank lines mark sentence boundaries
    3. Comment lines start with hash (#)

Each word/token has 10 fields defined in the CONLL-U format. Each field represents different attributes of the token
whose details are given below:

Fields
-------

``1. ID:``
    ID represents the word/token index in the sentence
``2. FORM:``
    Word/token form or punctuation symbol used in the sentence
``3. LEMMA:``
    Root/stem of the word
``4. UPOS:``
    Universal Part-of-Speech tag
``5. XPOS:``
    Language specific part-of-speed tag. underscore if not available
``6. FEATS:``
    Unordered list of morphological features, defined by Universal Dependencies;
    indicates the gender and number of a noun, the tense of a verb, etc.
``7. HEAD:``
    Head of the word, indicates the index of the word to which the current one is related
``8. DEPREL:``
    Universal Dependencies relation; indicates the relation between two words (subject or object of a verb, determiner of a noun, etc.)
``9. DEPS:``
    Language-specific part of speech tags
``10. MISC:``
    Any other annotation apart from the above mentioned fields
    Commentary or other annotation

``UPOS TAGS DETAILS``
    ``ADJ``
    Adjectives are words that typically modify nouns and specify their properties or attributes:
    ``اسمبلی انتخابات کو 'صاف و شفاف' بنانے``
    ``انتخابات مےں 'غیرسماجی' عناصر کی جانب سے بدامنی پھیلائے جانے کا خدشہ ہے``
    ``Examples``
     'واضح' ,'یقینی' ,'ہر'

    ``ADV``
    Adverbs are words that typically modify verbs for such categories as time, place, direction or manner.
    They may also modify adjectives and other adverbs, as in 'very briefly' or 'arguably' wrong.
    ``سوہال نے 24 گیندوں مےں جاریہ سیزن کی 'تیزترین' نصف سنچری بنائی``
    ``Examples``
    'ہرگز' ,'قبل_ازیں' ,'بعد'

    ``INTJ``
    An interjection is a word that is used most often as an exclamation or part of an exclamation.
    It typically expresses an emotional reaction, is not syntactically related to other accompanying expressions,
    and may include a combination of sounds not otherwise found in the language.
    ``چلو اب 'ذرا' دنیا کی سیر کر لیں``
    ``Examples``
    'آہ' ,'ذرا' ,'بس'

    ``NOUN``
    Nouns are a part of speech typically denoting a person, place, thing, animal or idea.
    ``بس اس 'تنہائی' کے 'عالم' مےں اےک 'یاد' 'آواز' بن کر 'سماعت' سے ٹکرائی۔``
    ``Examples``
    'جسٹس' ,'پاکستان' ,'حصہ' ,'خالہ' ,'لوگ'

    ``PROPN``
    A proper noun is a noun (or nominal content word) that is the name (or part of the name) of a specific individual, place, or object.
    ``تاہم 'بھارت' 'کرشنا' کو اپنی منگیتر کے چال و چلن پر شبہ ہوا``
    ``Examples``
    'ڈی' ,'سی' ,'پی' ,'ساؤتھ' ,'احمد' ,'نثار'

    ``VERB``
    A verb is a member of the syntactic class of words that typically signal events and actions, can constitute a minimal predicate in a clause,
    and govern the number and types of other constituents which may occur in the clause. Verbs are often associated with grammatical categories
    like tense, mood, aspect and voice, which can either be expressed inflectionally or using auxilliary verbs or particles.
    ``آزادانہ و منصفانہ انتخابات کو یقینی 'بنایا' جا سکے``
    ``Examples``
    'کہا' ,'رہے'

    ``ADP``
    Adposition is a cover term for prepositions and postpositions. Adpositions belong to a closed set of items that occur before (preposition)
    or after (postposition) a complement composed of a noun phrase, noun, pronoun, or clause that functions as a noun phrase, and that form a
    single structure with the complement to express its grammatical and semantic relation to another unit within a clause.
    ``اےک شخص 'نے' مبینہ طور 'پر' اپنی منگیتر اور اس 'کے' والدین 'پر' چاقو 'سے' حملہ کر کے زخمی کر دیا۔``
    ``Examples``
    'پر' ,'نے' ,'مےں'

    ``AUX``
    An auxiliary is a function word that accompanies the lexical verb of a verb phrase and expresses grammatical distinctions not carried by the lexical verb,
    such as person, number, tense, mood, aspect, voice or evidentiality. It is often a verb (which may have non-auxiliary uses as well) but many languages
    have nonverbal TAME markers and these should also be tagged AUX. The class AUX also include copulas (in the narrow sense of pure linking
    words for nonverbal predication).
    ``انتخابات کو یقینی بنایا 'جا' سکے۔``
    ``Examples``
    'جا' ,'ہے' ,'رہے'

    ``CCONJ``
    A coordinating conjunction is a word that links words or larger constituents without syntactically subordinating one to the other and expresses
    a semantic relationship between them.
    ``انتخابات کی راست نگرانی 'اور' غنڈہ عناصر پر کنٹرول کے لئے سخت_ترین انتظامات کئے جائیں۔``
    ``Examples``
     'لیکن' ,'بدعنوانیوں و بےقاعدگیوں in و'

     ``DET``
     Determiners are words that modify nouns or noun phrases and express the reference of the noun phrase in context. That is, a determiner may indicate
     whether the noun is referring to a definite or indefinite element of a class, to a closer or more distant element, to an element belonging to
     a specified person or thing, to a particular number or quantity, etc
     ``ریاستی حج کمیٹی 'اس' طرح کی کوئی تجویز رکھتی ہے``
     ``Examples``
     'تمام' ,'ہر' ,'جو'

     ``NUM``
     A numeral is a word, functioning most typically as a determiner, adjective or pronoun, that expresses a number and a relation to the number,
     such as quantity, sequence, frequency or fraction.
     ``'اےک' شخص نے مبینہ طور پر اپنی منگیتر اور اس کے والدین پر چاقو سے حملہ کر کے زخمی کر دیا۔``
     ``Examples``
     '۲' ,'۱' ,'۰' ,'چار' ,'اےک'

     ``PART``
     Particles are function words that must be associated with another word or phrase to impart meaning and that do not satisfy definitions
     of other universal parts of speech (e.g. adpositions, coordinating conjunctions, subordinating conjunctions or auxiliary verbs).
     Particles may encode grammatical categories such as negation, mood, tense etc. Particles are normally not inflected, although exceptions may occur.
     ``اس اجلاس مےں اطفال کے حق تعلیم کے قانون کا جائزہ 'بھی' لیا جائے_گا۔``
     ``Examples``
     'ہی' ,'مسٹر' ,'نہیں'

     ``PRON``
     Pronouns are words that substitute for nouns or noun phrases, whose meaning is recoverable from the linguistic or extralinguistic context.
     ``احمد کے بموجب اگر دونوں ہی ٹیمیں 'اپنے' شیڈول مےں معمولی تبدیلی کرتے ہےں``
     ``Examples``
     'اپنی' ,'ازیں' ,'یہاں'

     ``SCONJ``
     A subordinating conjunction is a conjunction that links constructions by making one of them a constituent of the other.
     The subordinating conjunction typically marks the incorporated constituent which has the status of a (subordinate) clause.
     ``وہ ابھی پڑھ ہی رہے تھے 'کہ' بیٹے نے دروازہ کھٹکھٹایا۔``
     ``Examples``
     'اگر' ,'تو'

     ``PUNCT``
     Punctuation marks are non-alphabetical characters and character groups used in many languages to delimit linguistic units in printed text.
     ``ایسے دہشتگردوں کو اسلام سے خارج کر دیا جانا چاہیے'۔'``
     ``Examples``
     '!' ,'.' ,'۔'

     ``SYM``
     A symbol is a word-like entity that differs from ordinary words by form, function, or both.
     ``ایسے'$' دہشتگردوں کو اسلام سے خارج کر دیا جانا چاہیے``
     ``Examples``
     '@', '%'

     ``X``
     The tag X is used for words that for some reason cannot be assigned a real part-of-speech category. It should be used very restrictively.


"""

from .reader import CoNLL

__all__ = ["CoNLL"]
