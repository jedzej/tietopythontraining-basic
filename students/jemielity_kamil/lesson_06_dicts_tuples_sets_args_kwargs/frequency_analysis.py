
dictionary = {}
for i in range(int(input('How many lines of text: '))):
    sentence = input('Sentence: ').split()
    for sentence_word in sentence:
        if sentence_word not in dictionary.keys():
            dictionary[sentence_word] = 1
        else:
            dictionary[sentence_word] += 1

new_list = list(dictionary.items())

for i in range(len(dictionary)):
    new_list[i] = tuple(reversed(new_list[i]))

dictionary = sorted(dictionary)

for i in range(len(new_list)):
    new_list[i] = list(new_list[i])
    new_list[i][0] = -new_list[i][0]

for i in range(len(new_list)):
    print(min(new_list)[1])
    new_list.remove(min(new_list))
