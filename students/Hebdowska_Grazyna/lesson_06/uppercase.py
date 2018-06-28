def capitalize(new_word):
    upper_word = new_word[0].upper() + new_word[1:]
    return upper_word


new_words = input(": ")
new_words = new_words.split(' ')
result = ''
for j in new_words:
    result += capitalize(j) + " "

print(result)
