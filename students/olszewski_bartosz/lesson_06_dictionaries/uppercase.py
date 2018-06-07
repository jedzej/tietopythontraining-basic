a = input()


def capitalize(sentence):
    capitalized_words = []
    for word in sentence.split():
        capitalized_words.append(word.title())
    print(" ".join(capitalized_words))


capitalize(a)
