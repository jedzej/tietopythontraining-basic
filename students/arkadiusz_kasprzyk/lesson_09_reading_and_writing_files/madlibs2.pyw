#! python3
"""
madlibs2.pyw - reads in text files and lets the user add their own text
anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

Usage
-----
$ py madlibs2.pyw <file_to_read> <file_to_write>

Examples
--------
$ py madlibs2.pyw sample0.txt sample0-a.txt
$ py madlibs2.pyw sample1.txt sample1-a.txt

Comment
-------
This is better version of madlibs.pyw
unfortunately quite complicated.

It solves the problems not mentioned in the task:

1. templates (or `slots` like 'NOUN' or 'VERB')
   may be followed, preceded and even joined
   by some punctuation mark (dot, comma, hyphen, ...)
   THUS
   we need to have a method for getting __consecutive__ slots
   without using .split() (too many cases to check,
   especially in case of joined words like NOUN-NOUN).

2. additionally slots may overlap, like VERB and ADVERB;
   rules for choosing one of them must be hardcoded.

The first step is to construct a list of slots in the given text,
i.e. all their occurrences with order preserved
and positions in the text remembered.

We must also choose one of the overlapping candidates;
we apply two rules:
1. the first wins,
2. the longer wins (if both begin at the same place in the text).

The second step is getting to __consecutive__ slots,
splitting the text with .partition(),
substituting slots with user input and putting it all together.

The assumption was also NOT to use regular expressions, only string methods.
"""

import sys

template = ['NOUN', 'VERB', 'ADJECTIVE', 'ADVERB']


def findall(str, sub, overlapping=True):
    """
    Returns positions of all occurrences of sub in str
    (optionally non-overlapping).

    str: str
    sub: str
    overlapping: bool
        if True (default) then all accurrences are found,
        if False then only non-overlapping.

    Example
    -------
    findall("abba baba abracadabra","ab")   # [0, 6, 10, 17]
    findall("bababa bababa", "baba")        # [0, 2, 7, 9]
    findall("bababa bababa", "baba", False)        # [0, 7]
    """

    positions = list()

    if overlapping:
        step = 1
    else:
        step = len(sub)

    k = str.find(sub)

    while k >= 0:
        positions.append(k)
        k = str.find(sub, k + step)

    return positions


def occurrences(txt, words):
    """
    Returns all positions of words in txt in the form of
    list of 3-tuples (word, start, end) ordered wrt start and then end.

    txt: str
    words: list of str

    Example
    -------
    occurrences("Ala likes Lola but Lola doesn't like Ala", ['Ala', 'Lola'])
        # [('Ala', 0, 3), ('Lola', 10, 14), ('Lola', 19, 23), ('Ala', 37, 40)]
    occurrences("This is ADVERB and VERB and VERB and ADVERB", \
                                                     ['VERB', 'ADVERB', 'AD'])
        # [('AD',      8, 10),
        #  ('ADVERB',  8, 14),
        #  ('VERB',   10, 14),
        #  ('VERB',   19, 23),
        #  ('VERB',   28, 32),
        #  ('AD',     37, 39),
        #  ('ADVERB', 37, 43),
        #  ('VERB',   39, 43)]
    """

    starts = []
    ends = []
    keys = []

    for key in words:
        starts_key = findall(txt, key)
        ends_key = list(map(lambda k: k + len(key), starts_key))
        keys += [key] * len(starts_key)
        starts += starts_key
        ends += ends_key

    occ = sorted(zip(keys, starts, ends),
                 key=lambda k: (k[1], k[2]))    # (start, end)

    return occ


def remove_overlapping(occ):
    """
    From list created by occurences() removes overlapping entries,
    according to:
    1. the first wins,
    2. the longer wins (if both begin at the same place in the text).

    occ: list created by occurences()

    Example
    -------
    occ = occurrences("This is ADVERB and VERB and VERB and ADVERB", \
                                                     ['VERB', 'ADVERB', 'AD'])
    remove_overlapping(occ)
        # [('ADVERB',  8, 14),
        #  ('VERB',   19, 23),
        #  ('VERB',   28, 32),
        #  ('ADVERB', 37, 43)]
    """
    for k in range(len(occ) - 1):

        # longer wins
        if occ[k][1] == occ[k + 1][1]:      # if have common origin...
            occ.pop(k)                      # ...the first must be shorter
            occ = remove_overlapping(occ)
            break

        # first wins
        # cannot have common origin (it's the case above)
        elif occ[k][2] >= occ[k + 1][1]:    # the first overlaps the second
            occ.pop(k + 1)                  # the second must be removed
            occ = remove_overlapping(occ)
            break

    return occ


def add_article(word):
    if word[0].lower() in ['a', 'e', 'i', 'o']:
        word = "an " + word
    else:
        word = "a " + word
    return word


def main():
    file2read = open(sys.argv[1], 'r')

    file2write = open(sys.argv[2], 'w')

    text = file2read.read()
    print(text)     # It's better to print text before, to know the context

    text_new = ""

    occ = occurrences(text, template)
    occ = remove_overlapping(occ)

    for key, start, end in occ:
        # we need only key

        text_l, key, text = text.partition(key)

        key_new = input("Enter {}: ".format(add_article(key)))

        text_new = text_new + text_l + key_new

    text_new += text

    print("\n" + text_new)

    file2write.write(text_new)

    file2write.close()

    file2read.close()


# %%
if __name__ == "__main__":
    main()
