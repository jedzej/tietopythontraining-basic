number_of_lines = int(input())
loaded_words = dict()
for lines in range(number_of_lines):
    for word in input().split():
        if word in loaded_words:
            loaded_words[word] += 1
        else:
            loaded_words[word] = 1

sorted_list = sorted([(-count, word) for word, count in loaded_words.items()])
for count, word in sorted_list:
    print(word)
