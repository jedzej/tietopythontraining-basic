def capitalize(lower_case_word):
    words = lower_case_word.split(' ')
    new_sentence = ''
    for word in words:
        new_sentence += chr(ord(word[0]) - 32) + word[1:] + ' '
    return new_sentence


sentence = input()
print(capitalize(sentence))
