#!/usr/bin/env python3

"""
mad_libs.py: a practice project "Mad Libs" from:
https://automatetheboringstuff.com/chapter8/

The program reads in text file(s) and lets the user add their own text anywhere
the word ADJECTIVE, NOUN, ADVERB or VERB appears in the text file.

Usage: ./mad_libs.py <path_1> [<path_2> ... <path_n>]

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import sys
import os


KEYWORDS = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


def read_content(path):
    if os.path.exists(path):
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        file = open(path, 'r')
        content = file.read()
        file.close()
        return content
    else:
        return ''


def substitute_keywords(text):
    words = text.split(' ')
    for idx, word in enumerate(words):
        for keyword in KEYWORDS:
            if keyword in word:
                if keyword[0] == 'A':
                    article = 'an'
                else:
                    article = 'a'
                substitute = input('Enter {} {}: '
                                   .format(article, keyword.lower()))
                words[idx] = words[idx].replace(keyword, substitute, 1)
                break

    return ' '.join(words)


def save_result(in_path, file_content):
    extension_idx = in_path.rfind('.')
    if extension_idx > 0:
        out_path = '{}_MODIFIED{}'.format(in_path[:extension_idx],
                                          in_path[extension_idx:])
    else:
        out_path = '{}_MODIFIED'.format(in_path)

    out_file = open(out_path, 'w')
    out_file.write(file_content)
    out_file.close()


def main():

    args_cnt = len(sys.argv)

    if args_cnt < 2:
        print("Error! At least one correct file path must be given!")

    else:
        for i in range(1, args_cnt):
            in_path = sys.argv[i]

            # read the file content
            content = read_content(in_path)
            if content:

                # create new text by substituting the keywords
                content = substitute_keywords(content)

                # print result and save it in new file
                print(content)
                save_result(in_path, content)

            else:
                print('The path: {} is incorrect!'.format(in_path))


if __name__ == '__main__':
    main()
