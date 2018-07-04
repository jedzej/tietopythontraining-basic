line_nr = int(input())
word_set = set()

for i in range(line_nr):
    word_list = input().split()
    for word in word_list:
        word_set.add(word)
print(len(word_set))
