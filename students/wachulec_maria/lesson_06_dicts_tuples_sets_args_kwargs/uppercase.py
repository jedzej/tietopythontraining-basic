def capitalize(word):
    between_large_small_distance = 32
    word = chr(ord(word[0]) - between_large_small_distance) + word[1:]
    return word


def uppercase(sentence_in_list):
    for i in range(len(sentence_in_list)):
        sentence_in_list[i] = capitalize(sentence_in_list[i])
    sentence = ' '.join([str(elem) for elem in sentence_in_list])
    return sentence


text = input().split()
uppercase_text = uppercase(text)
print(uppercase_text)
