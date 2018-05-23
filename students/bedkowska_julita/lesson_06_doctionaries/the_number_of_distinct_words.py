lines = int(input('Give the number of lines: '))
words_set = set()
print('Give the text: ')
for i in range(lines):
    words = input().split()
    for word in words:
        words_set.add(word)

print('Number of distinct wors: ' + str(len(words_set)))
