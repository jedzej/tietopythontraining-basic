'''
Statement
Given a string consisting of words separated by spaces.
Determine how many words it has. To solve the problem, use the method count.
'''


def count_words(line):
    return line.count(" ") + 1


if __name__ == "__main__":
    print("Words counter:")
    line_1 = "In the hole in the ground there lived a hobbit"
    line_2 = "One two three four five"
    print(line_1)
    print("There is", count_words(line_1), "words in line above")
    print(line_2)
    print("There is", count_words(line_2), "words in line above")
