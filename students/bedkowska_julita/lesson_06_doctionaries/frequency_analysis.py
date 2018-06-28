num_of_lines = int(input('Give the number of lines: '))
print('Give ' + str(num_of_lines) + ' lines of words: ')
words_frequency = dict()
for _ in range(num_of_lines):
    words = input().split()
    for word in words:
        words_frequency[word] = words_frequency.get(word, 0) + 1

print('Sorted list of words:')
words_tuples = [(-count, word) for (word, count) in words_frequency.items()]
for c, word in sorted(words_tuples):
    print(word)
