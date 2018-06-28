"""
Create a Mad Libs program that reads in text files
and lets the user add their own text anywhere the word
ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
"""

import re

REPLACE_WORDS = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]


def main():
    input_file = open("text_file_input.txt")
    output_file = open("text_file_output.txt", 'w')
    text = input_file.read()
    input_file.close()

    text = re.sub('[,.]', '', text)
    text = text.split(" ")

    for word in text:
        if word in REPLACE_WORDS:
            print("Please write a word to replace \"" + word + "\":")
            word = str(input())
        output_file.write(word + " ")

    output_file.close()


if __name__ == '__main__':
    main()
