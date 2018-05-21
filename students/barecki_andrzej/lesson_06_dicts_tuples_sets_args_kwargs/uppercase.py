import os


def capitalize(lower_case_word):
    word = []
    for character in lower_case_word:
        word.append(character)
    if (int(ord(word[0])) >= 97) and (int(ord(word[0])) <= 122):
        word[0] = chr(int(ord(word[0])) - 32)
    return ''.join(word)


while True:
    in_string = input().split()
    for elem in in_string:
        print(capitalize(elem) + " ", end='')
    print(os.linesep)
