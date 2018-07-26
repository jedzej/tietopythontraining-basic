'''
Create a Mad Libs program that reads in text files and lets
the user add their own text anywhere the word ADJECTIVE,
NOUN, ADVERB, or VERB appears in the text file.
For example, a text file may look like this:


The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them.


Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
The following text file would then be created:


The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
'''
# ! python3
# mad_libs.py - Create new txt file based on user input and file
#    specified by user in arguments list.
# Usage: py.exe mad_libs.py <text_file_name.txt> - specifies input text file,
#        output file will be created in the same directory with "out" suffix.

import os
import sys


def mad_lib():
    searched_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
    user_interaction = ['Enter an adjective:',
                        'Enter a noun:',
                        'Enter an adverb:',
                        'Enter a verb:']
    if len(sys.argv) == 2:
        if not os.path.exists(sys.argv[1]):
            print("Provided file does not exist. Exit.")
            return
        in_file = open(sys.argv[1])
        lines = in_file.readlines()
        in_file.close()

        out_file = open(sys.argv[1] + 'out', 'w')
        out_file_content = ''
        for line in lines:
            current_index = 0
            find_indexes = [0] * len(searched_words)
            while current_index < len(line):
                for s_word in searched_words:
                    find_indexes[searched_words.index(s_word)] = line.find(
                        s_word, current_index)
                min = len(line)
                searched_index = -1
                for i in range(len(find_indexes)):
                    if find_indexes[i] != -1 and find_indexes[i] < min:
                        min = find_indexes[i]
                        searched_index = i
                if min == len(line):
                    out_file_content += line[current_index:len(line)]
                    current_index = len(line)
                else:
                    new_word = input(user_interaction[searched_index])
                    out_file_content += line[current_index:min]
                    out_file_content += new_word
                    current_index = min + len(searched_words[searched_index])
        out_file.write(out_file_content)
        out_file.close()
        print(out_file_content)


if __name__ == "__main__":
    mad_lib()
