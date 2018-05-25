'''
Statement
Given a string consisting of exactly two words separated by a space.
Print a new string with the first and second word positions swapped
(the second word is printed first).
This task should not use loops and if.
'''


def swap_two_words(words):
    space_index = words.find(" ")
    return " ".join([words[space_index + 1:], words[:space_index]])


if __name__ == "__main__":
    print("Two words swap")
    words_1 = "Hello, world!"
    words_2 = "Bob budowniczy"
    print(words_1)
    print(swap_two_words(words_1))
    print(words_2)
    print(swap_two_words(words_2))
