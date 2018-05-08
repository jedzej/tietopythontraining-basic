"""
The function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the string.
Otherwise, the characters specified in the second argument to the function
will be removed from the string.
"""
import re


def delete_spaces_or_characters(sentence, character = None):
    if character is not None:
        sentence = re.sub(re.escape(character), '', sentence)
    else:
        string_patern = re.compile(r'^\s+|\s+$')
        sentence = re.sub(string_patern, '', sentence)
    print(sentence)
    return sentence


sentence1 = "    ania ma ko.#!ta 78     "
delete_spaces_or_characters(sentence1)
delete_spaces_or_characters(sentence1, ".#!")
delete_spaces_or_characters(sentence1, "a")

