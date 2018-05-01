from operator import itemgetter

number_of_lines = int(input())
words_quantity = dict()
for line in range(number_of_lines):
    entry = input().split(' ')
    for word in entry:
        if word in words_quantity:
            words_quantity[word] = words_quantity[word] + 1
        else:
            words_quantity[word] = 1

list_of_tuples = []
for word in words_quantity:
    list_of_tuples.append((words_quantity[word], word))

list_of_tuples = sorted(list_of_tuples, key=itemgetter(1), reverse=True)
list_of_tuples = sorted(list_of_tuples, key=itemgetter(0), reverse=False)
list_of_tuples.reverse()

for x in range(len(list_of_tuples)):
    print(list_of_tuples[x][1])
