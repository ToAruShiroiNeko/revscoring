import sys

from .space_delimited import SpaceDelimited

try:
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("italian")
except ValueError:
    raise ImportError("Could not load stemmer for {0}. ".format(__name__))

try:
    from nltk.corpus import stopwords as nltk_stopwords
    stopwords = set(nltk_stopwords.words('italian'))
except LookupError:
    raise ImportError("Could not load stopwords for {0}. ".format(__name__) +
                      "You may need to install the nltk 'stopwords' " +
                      "corpora.  See http://www.nltk.org/data.html")

try:
    import enchant
    dictionary = enchant.Dict("it")
except enchant.errors.DictNotFoundError:
    raise ImportError("No enchant-compatible dictionary found for 'it'.  " +
                      "Consider installing 'myspell-it'.")

badwords = [
    r"anale",
    r"ano",
    r"bastard[io]",
    r"buttana",
    r"cac(a|are|ata)",
    r"cacc(a|he|ol[ae])",
    r"caga(re|t[aeo])?",
    r"cavolat[ae]",
    r"cazz(at[ae]|[io]|on[ei])?",
    r"cesso",
    r"ciccione",
    r"ciuccia",
    r"coglion[ei]",
    r"cojone",
    r"cretin[io]",
    r"culo",
    r"deficent[ei]",
    r"fancazzista",
    r"fanculo",
    r"fi[cg](a|he|o)",
    r"fott(e|iti|uto)",
    r"fregna",
    r"froci(o|one)?",
    r"gnocca",
    r"idiota",
    r"incul(are|ato|o)",
    r"kazzo",
    r"maiala",
    r"merd(a|accia|e|os[oa])?",
    r"mignotta",
    r"min(ch|k)ia",
    r"pen[ei]",
    r"pip+[iae]",
    r"pirla",
    r"piscio",
    r"pisell(ino|o|one)",
    r"pompin[io]",
    r"porc[ao]",
    r"porno",
    r"pupu",
    r"putta(n[ea]|nella|niere)?",
    r"puzza(no|te|va)?", "puzz(i|olente|one)",
    r"ricchione",
    r"sb[ou]rr[ao]",
    r"scem[aio]",
    r"schifo(s[ao])?",
    r"scopa(re|t[aeo]|va)",
    r"scor+egg(ia|e)",
    r"seghe",
    r"sfigat[io]",
    r"siffredi",
    r"skifo",
    r"sperma",
    r"stocazzo",
    r"stronza(t[ae])?",
    r"stronz[io]",
    r"stupido",
    r"suca",  r"succhia",
    r"suka",
    r"tette",
    r"troi[ae]",
    r"trombare",
    r"vaf+anculo",
    r"znccn[kl]",
    r"zoccola"
]

informals = [
    "(ah)+a?",
    "amo",
    "avete",
    "banana",
    "bla",
    "brutt[io]",
    "cavolo",
    "chiamo",
    "ciao+",
    "cmq",
    "consigliamo",
    "corsivo",
    "dovete",
    "fermatevi",
    "frega",
    "grassetto",
    "(ha)+",
    "inserisci",
    "intestazione",
    "leggete",
    "lol",
    "mamma",
    "nascondi",
    "perche",
    "potete",
    "raga",
    "sapete",
    "scrivete",
    "scusate",
    "siete",
    "sto",
    "tua",
    "volete"
]


sys.modules[__name__] = SpaceDelimited(
    __name__,
    doc="""
italian
=======

revision
--------
.. autoattribute:: revision.words
.. autoattribute:: revision.content_words
.. autoattribute:: revision.badwords
.. autoattribute:: revision.misspellings
.. autoattribute:: revision.informals
.. autoattribute:: revision.infonoise

parent_revision
---------------
.. autoattribute:: parent_revision.words
.. autoattribute:: parent_revision.content_words
.. autoattribute:: parent_revision.badwords
.. autoattribute:: parent_revision.misspellings
.. autoattribute:: parent_revision.informals
.. autoattribute:: parent_revision.infonoise

diff
----
.. autoattribute:: diff.words_added
.. autoattribute:: diff.words_removed
.. autoattribute:: diff.badwords_added
.. autoattribute:: diff.badwords_removed
.. autoattribute:: diff.misspellings_added
.. autoattribute:: diff.misspellings_removed
.. autoattribute:: diff.informals_added
.. autoattribute:: diff.informals_removed
    """,
    badwords=badwords,
    dictionary=dictionary,
    informals=informals,
    stemmer=stemmer,
    stopwords=stopwords
)
