#! python3
"""
madlibs.pyw - reads in text files and lets the user add their own text
anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

These words may be followed (or preceded) by punctuation marks which then
must be followed (or preceded) by whitespace.
Cases like NOUN-NOUN will not be recognised (see the second Example).

Usage
-----
$ py madlibs.pyw <file_to_read> <file_to_write>

Examples
--------
$ py madlibs.pyw sample0.txt sample0-a.txt
$ py madlibs.pyw sample1.txt sample1-a.txt
"""

import sys


def substitute(word):

    word_stripped = word.strip(".,;:-_?!")

    if word_stripped in ['NOUN', 'VERB', 'ADJECTIVE', 'ADVERB']:

        if word_stripped[0] == 'A':
            word_article = "an " + word_stripped
        else:
            word_article = "a " + word_stripped

        word_new = input("Enter {}: ".format(word_article))

        result = word.replace(word_stripped, word_new)

    else:

        result = word

    return result


file2read = open(sys.argv[1], 'r')

file2write = open(sys.argv[2], 'w')

newlines = []

for line in file2read:
    print("\n" + line.strip("\n"))
    words = line.split()
    for w in range(len(words)):
        words[w] = substitute(words[w])
    newlines.append(" ".join(words))

newtxt = "\n".join(newlines)

print("\n" + newtxt)

file2write.write(newtxt)

file2write.close()

file2read.close()
