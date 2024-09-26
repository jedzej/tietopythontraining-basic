'''
Statement
Write a function capitalize(lower_case_word) that takes the lower case
word and returns the word with the first letter capitalized.
Eg., print(capitalize('word')) should print the word Word.
Then, given a line of lowercase ASCII words
(text separated by a single space),
print it with the first letter of each word
capitalized using the your own function capitalize().

In Python there is a function ord(character),
which returns character code in the ASCII chart,
and the function chr(code), which returns the character itself
from the ASCII code. For example, ord('a') == 97, chr(97) == 'a'.
'''


def capitalize(lower_case_word):
    word = list(lower_case_word)
    first_letter = word[0]
    dif = ord('a') - ord('A')
    if ord(first_letter) >= ord('a') and ord(first_letter) <= ord('z'):
        word[0] = chr(ord(first_letter) - dif)
    return ''.join(word)


if __name__ == "__main__":
    for s in input("Enter lowercase words separated by space:").split():
        print(capitalize(s), end=' ')
