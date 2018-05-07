# Program display words appearing form the least times to the least
from functions_lesson06 import file_to_list


def list_to_tuples_with_count(word_list):
    words_with_counters = []
    for elem in word_list:
        words_with_counters.append((word_list.count(elem), elem))
        words_with_counters_without_duplication = set(words_with_counters)
    return words_with_counters_without_duplication


def display_sorted_words(words_with_counters):
    words_with_counters = sorted(words_with_counters,
                                 key=lambda x: (-x[0], x[1]))
    print(words_with_counters)
    for elem in words_with_counters:
        print(elem[1])


# display_sorted_words(list_to_tuples_with_count(file_to_list("text.txt")))
display_sorted_words(list_to_tuples_with_count(file_to_list("text2.txt")))
