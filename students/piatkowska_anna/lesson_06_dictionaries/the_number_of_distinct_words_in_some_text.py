'''
Statement
Given a number n, followed by n lines of text,
print the number of distinct words that appear in the text.
For this, we define a word to be a sequence of non-whitespace characters,
seperated by one or more whitespace or newline characters.
Punctuation marks are part of a word, in this definition.

'''


def dist_word():
    a = int(input("Enter number of lines: "))
    words = set()
    for i in range(a):
        line = input("Enter words: ").split()
        for word in line:
            words.add(word)
    print("Number of words in entered lines:")
    print(len(words))


if __name__ == "__main__":
    dist_word()
