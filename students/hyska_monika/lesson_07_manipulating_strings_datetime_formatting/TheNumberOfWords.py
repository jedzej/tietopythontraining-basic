# Count words
from functions_lesson07 import file_to_list


# function check number of words in file (for list)
def count_words(word_list):
    print(len(word_list))
    return len(word_list)


# function check number of words in string
def count_words_str(text):
    print(len(text.split()))
    return len(text.split())


a = "sss aa es"
print('Number of word for text: ')
count_words_str(a)

print('\nNumber of word for text in file: ')
count_words(file_to_list("text3.txt"))
