def capitalize(lower_case_word):
    return lower_case_word.title()


if __name__ == '__main__':
    sentence = input('Please enter a sentence: ')

    # Sentence at once
    print(capitalize(sentence))

    # Each word separately
    words = sentence.split()
    for word in words:
        print(capitalize(word), end=' ')
