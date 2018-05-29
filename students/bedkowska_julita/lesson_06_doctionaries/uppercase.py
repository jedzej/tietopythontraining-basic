def capitalize(lower_case_word):
    word_as_list = list(lower_case_word)
    word_as_list[0] = chr(ord(word_as_list[0]) - 32)
    lower_case_word = "".join(word_as_list)
    return lower_case_word


given_statement = input("Give the statement: ")
print(' '.join([capitalize(word) for word in given_statement.split()]))
