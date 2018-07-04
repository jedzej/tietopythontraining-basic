from operator import itemgetter

n = int(input())
dictionary = {}

for _ in range(n):
    for word in input().split():
        dictionary[word] = dictionary.get(word, 0) + 1

words_in_order = [(nr, key) for key, nr in dictionary.items()]
words_in_order = sorted(words_in_order, key=itemgetter(1))
words_in_order = sorted(words_in_order, key=itemgetter(0), reverse=True)

for _, word in words_in_order:
    print(word)
