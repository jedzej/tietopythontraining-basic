# The number of distinct words in some text. Program display words appearing form the least times to the least
from functions_lesson06 import file_to_list


def count_words(word_list):
    words_without_duplication = set(word_list)
    print(sorted(words_without_duplication))
    print("Nuber of words - not repeated: ", len(words_without_duplication))
    return len(words_without_duplication)


count_words(file_to_list("text.txt"))
count_words(file_to_list("text2.txt"))
count_words(file_to_list("text3.txt"))
