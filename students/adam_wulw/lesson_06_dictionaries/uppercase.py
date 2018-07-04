def capitalize(word):
    if word[0] >= 'a' and 'A' < word[0]:
        word = chr(ord(word[0]) - 32) + word[1:]
    return word


low_case_str = input()
low_case_word_list = low_case_str.split(' ')
for word in low_case_word_list:
    print(capitalize(word), end=' ')
