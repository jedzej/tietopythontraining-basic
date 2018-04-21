n = int(input())
dictionary = {}

for _ in range(n):
    for word in input().split():
        dictionary[word] = dictionary.get(word, 0) + 1

words_in_order = [(nr, key) for key, nr in dictionary.items()]

print(len(words_in_order))
