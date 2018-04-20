def capitalize(lowercase_word):
    return word[0].upper() + lowercase_word[1:]


words = input('Enter word or sentence: ').split()

for word in words:
    print(capitalize(word), end=' ')
