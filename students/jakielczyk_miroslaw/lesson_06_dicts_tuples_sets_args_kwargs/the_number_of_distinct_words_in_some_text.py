number_of_lines = int(input())
words_quantity = dict()

for line in range(number_of_lines):
    entry = input().split(' ')
    for word in entry:
        if word not in words_quantity:
            words_quantity[word] = 1
        else:
            words_quantity[word] = words_quantity[word] + 1

print(str(len(words_quantity)))
