'''
Statement
Given a string. Replace in this string all the numbers 1 by the word one.
'''


def replace_1_with_one(input_string):
    return input_string.replace("1", "one")


if __name__ == "__main__":
    word = "1 + 1 = 2"
    word_two = "1231213"
    print(replace_1_with_one(word))
    print(replace_1_with_one(word_two))
