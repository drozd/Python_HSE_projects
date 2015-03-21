import re

print("Please, type a text to be tokenized: ")
text = input()

punct = ['.', '!', '?',',', ':', ';', '"', '»', '”', '«', '“', '„',
         ')', '(', ']', '[', '>', '<', '$', '%', '№', '#']
hyphens = ['—','-']

def check_am_pm(token, tokens):
    if re.match('am|pm|a\.m|p\.m', token):
            index = tokens.index(token)
            new_token = tokens[index-1]+" "+token
            tokens[index-1] = new_token
            tokens.pop(index)

def check_extra_space(token, tokens):
    # to avoid misspelling
    if re.match('(.*\-$)', token):
            index = tokens.index(token)
            new_token = token+tokens[index+1]
            tokens[index] = new_token
            tokens.pop(index+1)

def get_tokens(text):
    """
    Tokenize words.
    We decided to leave punctuation.
    """
    tokens = text.split()
    for token in tokens:
        check_am_pm(token, tokens)
        check_extra_space(token, tokens)
        
    return tokens

print("Here are the tokens: \n")
for w in get_tokens(text):
    print(w)
print("Number of tokens: ", + len(get_tokens(text)))


"""
Sentence for testing:
At 21.30 p.m. Mr. Smith bought cheapsite.com for 1.5 million dollars in New- York, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.
"""
