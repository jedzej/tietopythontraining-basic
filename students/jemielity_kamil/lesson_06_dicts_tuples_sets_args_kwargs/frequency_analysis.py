
Dictionary = {}
for i in range(int(input('How many lines of text: '))):
    sentence = input('Sentence: ').split()
    for sentence_word in sentence:
        if sentence_word not in Dictionary.keys():
            Dictionary[sentence_word] = 1
        else:
            Dictionary[sentence_word] += 1

Dictionary = list(Dictionary.items())

for i in range(len(Dictionary)):
    Dictionary[i] = tuple(reversed(Dictionary[i]))

Dictionary = sorted(Dictionary)

for i in range(len(Dictionary)):
    Dictionary[i] = list(Dictionary[i])
    Dictionary[i][0] = -Dictionary[i][0]

for i in range(len(Dictionary)):
    print(min(Dictionary)[1])
    Dictionary.remove(min(Dictionary))
