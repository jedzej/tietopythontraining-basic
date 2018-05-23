line_nr = int(input())
city_country = {}
words_set = {}

for i in range(line_nr):
    line_str = input()
    line_list = line_str.split(' ')

    for word in line_list:
        words_set.setdefault(word, 0)
        words_set[word] = words_set[word] - 1

tup_list = []
for k, v in words_set.items():
    tup = (v, k)
    tup_list.append(tup)

tup_list.sort()
for word in tup_list:
    print(word[1])
