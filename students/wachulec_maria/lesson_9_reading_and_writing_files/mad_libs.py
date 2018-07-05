def get_word_list_from_file(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text.split()


def check_punctuation(words, index):
    if not words[index].isalnum():
        dot = words[index][-1]
        words[index] = words[index][:-1]
        return words, dot
    return words, ''


def change_word(words, index):
    if words[index].lower()[0] in VOWEL:
        words[index] = input("Enter an " + words[index].lower() + ': ')
    else:
        words[index] = input("Enter a " + words[index].lower() + ': ')
    return words


def mad_libs(file_path):
    list_of_words = get_word_list_from_file(file_path)
    for id_word in range(len(list_of_words)):
        list_of_words, dot = check_punctuation(list_of_words, id_word)
        if list_of_words[id_word].upper() in SUBSTITUTION:
            list_of_words = change_word(list_of_words, id_word)
        if dot:
            list_of_words[id_word] = list_of_words[id_word] + dot
    return ' '.join(list_of_words)


VOWEL = 'aeyio'
SUBSTITUTION = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
print(mad_libs('text_file.txt'))
