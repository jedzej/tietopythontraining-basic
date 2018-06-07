# https://snakify.org/lessons/sets/problems/number_of_words/
# Number of words
# piotrsta


if __name__ == "__main__":
    lines = int(input('How many lines of text? : '))
    words = set()

    for line in range(lines):
        words.update(input().split())
    print(str(len(words)) + ' different words appeared.')

# TO DO
# Input Validation
