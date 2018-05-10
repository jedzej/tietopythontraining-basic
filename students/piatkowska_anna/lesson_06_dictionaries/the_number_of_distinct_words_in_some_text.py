'''
Statement
Given a number n, followed by n lines of text,
print the number of distinct words that appear in the text.
For this, we define a word to be a sequence of non-whitespace characters,
seperated by one or more whitespace or newline characters.
Punctuation marks are part of a word, in this definition.

'''


a = int(input())
words = set()
for i in range(a):
    line = input().split()
    for word in line:
        words.add(word)
print(len(words))
