import re

print("Please, type a text to be splitted: ")
text = input()

def splitter(text):
        """Split Russian text by sentences.

        Example:
        >>> splitter("Маша уронила мячик. Мячик уплыл.")
        ['Маша уронила мячик.', 'Мячик уплыл.']
        """
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        return sentences

sentences = splitter(text)

print("Here are the splitted sentences: \n")
for s in sentences:
        print(s)
        print("\n")

"""
Sentences for testing:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true...
Well, with a probability of .9 it isn't.
"""

##Explanation:
##"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"

##(?<!\w\.\w.) Negative Lookbehind - Assert that it is impossible to match the regex below
##\w match any word character [a-zA-Z0-9_]
##\. matches the character . literally
##\w match any word character [a-zA-Z0-9_]
##. matches any character (except newline)

##(?<![A-Z][a-z]\.) Negative Lookbehind - Assert that it is impossible to match the regex below
##[A-Z] match a single character present in the list below
##A-Z a single character in the range between A and Z (case sensitive)
##[a-z] match a single character present in the list below
##a-z a single character in the range between a and z (case sensitive)
##\. matches the character . literally

##(?<=\.|\?) Positive Lookbehind - Assert that the regex below can be matched
##1st Alternative: \.
##\. matches the character . literally
##2nd Alternative: \?
##\? matches the character ? literally
##\s match any white space character [\r\n\t\f ]
