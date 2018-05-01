"""
Given a number n, followed by n lines of text,
print the number of distinct words that appear in the text.
For this, we define a word to be a sequence of
non-whitespace characters, seperated by one or more
whitespace or newline characters. Punctuation marks
are part of a word, in this definition.
"""


def main():
    word_set = set()
    rows = int(input())
    for i in range(rows):
        line = input().split()
        for word in line:
            word_set.add(word)
    print(len(word_set))


if __name__ == '__main__':
    main()
