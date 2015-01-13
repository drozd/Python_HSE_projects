import re

def get_words(text):
#    return list(extract_words(text))
    r = re.compile('[\W+-]',re.U)
    return [word for word in r.split(text) if word]

GROUPING_SPACE_REGEX = re.compile('([^\w_-]|[+])', re.U)

def simple_word_tokenize(text):
    """
    Split text into tokens. Don't split by hyphen.
    """
    return [t for t in GROUPING_SPACE_REGEX.split(text)
            if t and not t.isspace()]

text = """
Sentences for testing:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true...
Well, with a probability of .9 it isn't.
"""

for w in get_words(text):
    print(w)

##for w in simple_word_tokenize(text):
##    print(w)
