from operator import itemgetter

n = int(input())
words_freq = {}
for _ in range(n):
    for word in input().split():
        words_freq[word] = words_freq.get(word, 0) + 1

words_list = [(val, key) for key, val in words_freq.items()]
words_list = sorted(sorted(words_list, key=itemgetter(1)), key=itemgetter(0),
                    reverse=True)
for _, word in words_list:
    print(word)
