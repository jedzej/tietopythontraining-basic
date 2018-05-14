"""
Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or
VERB appears in the text file
The program would find these occurrences and prompt the user to replace them.
The results should be printed to the screen and saved to a new text file.
"""
import os
from datetime import date
import random


def set_words_on_file(file_name, word_to_replace):
    file_text = open(file_name).read()
    print("My file:\n" + file_text)
    my_file_without_dots = file_text.replace(".", "")
    all_words = my_file_without_dots.split(" ")
    new_file_name = str(os.path.splitext(file_name)[0]) + \
        "_" + str(date.today()) + "_" + str(random.randrange(999)) + ".txt"
    with open(new_file_name, "w+") as changed_file:
        for elem in all_words:
            if elem in word_to_replace:
                print("Enter " + elem + ": ")
                new_word = input(str())
                file_text = file_text.replace(elem, new_word)
        changed_file.write(file_text)
        print("Changed file:\n" + file_text)
        changed_file.close()


my_file_name = "./txt_files/text1.txt"
base_words = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]
set_words_on_file(my_file_name, base_words)
