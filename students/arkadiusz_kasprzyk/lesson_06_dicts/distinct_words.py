# distinct_words.py

N = int(input("Number of lines: "))
words = set()
for n in range(N):
    line = input("line {}: ".format(n + 1))
    words |= set(line.split())
print(words)
print("{} distinct words in given text.".format(len(words)))
