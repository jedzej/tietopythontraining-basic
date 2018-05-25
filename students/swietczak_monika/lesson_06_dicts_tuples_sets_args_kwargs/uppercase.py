def capitalize(lower_case_word):
    lower_list = list(lower_case_word)
    lower_list[0] = chr(ord(lower_list[0]) - 32)
    lower_case_word = "".join(lower_list)
    return lower_case_word


print(' '.join(
    [capitalize(word) for word in input("Enter some words: ").split()]))
