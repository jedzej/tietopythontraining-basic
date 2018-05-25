def capitalize(lower_case_word):
    title = lower_case_word[0].upper() + lower_case_word[1:]
    return title


print(' '.join(
    [capitalize(word) for word in input("Enter some words: ").split()]))
