#!/usr/bin/env python3

lines = int(input())

words_freq = dict()

for i in range(lines):
    new_words = input().split()
    for word in new_words:
        words_freq.setdefault(word, 0)
        words_freq[word] += 1

sorted_alpha = [(word, words_freq[word]) for word in sorted(words_freq)]

sorted = sorted(sorted_alpha, key=lambda word: word[1], reverse=True)

for word, freq in sorted:
    print(word)
