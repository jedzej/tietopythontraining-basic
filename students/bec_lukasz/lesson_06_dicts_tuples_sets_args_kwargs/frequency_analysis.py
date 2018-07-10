words = []
words_dict = {}
for i in range(int(input())):
    words.append(input().split())

for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j] in words_dict:
            words_dict[words[i][j]] += 1
        else:
            words_dict[words[i][j]] = 1

tuples = [(-j, i) for i, j in words_dict.items()]
for count, word in sorted(tuples):
    print(word)
