#!/usr/bin/env python3
"""Madlibs exercise"""


def read_file(file_path):
    """Helper function that opens and reads file content"""
    try:
        in_file = open(file_path, 'r')
    except FileNotFoundError as err:
        print('Error: {0}'.format(err))
        return ''
    text = in_file.read()
    in_file.close()
    return text


def replace(text):
    """Replace keywords with user input"""
    keys = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
    words = text.split(' ')
    for idx, word in enumerate(words):
        for key in keys:
            if key in word:
                if key == 'ADJECTIVE':
                    print('Enter an', end=' ')
                else:
                    print('Enter a', end=' ')
                print(key.lower())
                words[idx] = words[idx].replace(key, input(), 1)
                break
    return ' '.join(words)


def main():
    """Main Function"""

    text = read_file('in.txt')
    if text:
        new_text = replace(text)
        print(new_text)
        out_file = open('out.txt', 'w')
        out_file.write(new_text)
        out_file.close()


if __name__ == '__main__':
    main()
