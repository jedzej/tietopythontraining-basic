import operator

n = int(input())
words_dict = {}
for i in range(n):
    words = input().split()
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
words_tuples = []
for elem in words_dict:
    words_tuples.append((words_dict[elem], elem))

for elem in sorted(sorted(words_tuples, key=operator.itemgetter(1)),
                   key=operator.itemgetter(0), reverse=True):
    print(elem[1])
