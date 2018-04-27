
dictionary = {}
for i in range(int(input('How many lines of text: '))):
    sentence = input('Sentence: ').split()
    for sentence_word in sentence:
        if sentence_word not in dictionary.keys():
            dictionary[sentence_word] = 1
        else:
            dictionary[sentence_word] += 1

dictionary = list(dictionary.items())

for i in range(len(dictionary)):
    dictionary[i] = tuple(reversed(dictionary[i]))

dictionary = sorted(dictionary)

for i in range(len(dictionary)):
    dictionary[i] = list(dictionary[i])
    dictionary[i][0] = -dictionary[i][0]

for i in range(len(dictionary)):
    print(min(dictionary)[1])
    dictionary.remove(min(dictionary))
