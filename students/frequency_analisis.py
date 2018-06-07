all_words = {}
words = []

for i in range(int(input())):
    words = input().split()
    for item in words:
        all_words.setdefault(item, 0)
        all_words[item] += 1

all_words_list = [(count, word) for (word, count) in all_words.items()]

new_dict = {}

for pair in all_words.items():
    new_dict.setdefault(pair[1], [])
    new_dict[pair[1]].append(pair[0])

for i in reversed([k for k in new_dict.keys()]):
    for word in sorted(new_dict.get(i)):
        print(word)
        