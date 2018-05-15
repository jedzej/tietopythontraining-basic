def capitalize(lower_case_word):
    return chr(ord(lower_case_word[0]) - 0x20) + lower_case_word[1:]


words = input().split()
cap_words = []
for word in words:
    cap_words.append(capitalize(word))
print(' '.join(cap_words))
