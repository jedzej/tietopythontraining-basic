"""
The function that takes a string and does the same thing
as the strip() string method.
If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning
and end of the string.
Otherwise, the characters specified in the second argument to the function
will be removed from the string.
"""
import re


# old
def delete_spaces_or_characters(sentence, character=None):
    if character is not None:
        # for remove some strings from sentence
        sentence = re.sub(re.escape(character), '', sentence)
    else:
        string_patern = re.compile(r'^\s+|\s+$')
        sentence = re.sub(string_patern, '', sentence)
    print(sentence)
    return sentence


# new
def delete_spaces_or_characters2(sentence, characters=None):
    if characters is not None:
        # for remove string from beginning and end
        # string_patern = re.compile(character)
        # remove characters from beginning and end, works as strip
        string_patern = (r'^[{0}]*|[{0}]*$'.format(re.escape(characters)))
    else:
        string_patern = re.compile(r'^\s+|\s+$')
    sentence = re.sub(string_patern, '', sentence)
    print(sentence)
    return sentence


sentence1 = "ania ma ko.#!ta 78a"
delete_spaces_or_characters2(sentence1, "a")
sentence1 = 'aoeuaoeuaoeu'
delete_spaces_or_characters2(sentence1, "oau")
