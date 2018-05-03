import os


def capitalize(lower_case_word):
    internal_list = []
    for character in lower_case_word:
        internal_list.append(character)
    if (int(ord(internal_list[0])) >= 97) and (int(ord(internal_list[0])) <= 122):
        internal_list[0] = chr(int(ord(internal_list[0])) - 32)
    return ''.join(internal_list)


while True:
    in_string = input().split()
    for elem in in_string:
        print(capitalize(elem) + " ", end='')
    print(os.linesep)
