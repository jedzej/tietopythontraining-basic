"""
Write a function capitalize(lower_case_word) that takes
the lower case word and returns the word with the first
letter capitalized. Eg., print(capitalize('word'))
should print the word Word.

Then, given a line of lowercase ASCII words (text separated
by a single space), print it with the first letter of each
word capitalized using the your own function capitalize().

In Python there is a function ord(character), which
returns character code in the ASCII chart, and the function
 chr(code), which returns the character itself from the
 ASCII code. For example, ord('a') == 97, chr(97) == 'a'.
"""


def capitalize(lower_case_word):
    line = lower_case_word[0].upper()
    line += lower_case_word[1:]
    return line


def main():
    sentence = input().split()
    for word in sentence:
        print(capitalize(word), end=' ')


if __name__ == '__main__':
    main()
