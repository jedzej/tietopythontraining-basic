def capitalize(letter):
    letter = (chr(ord(letter)-32))
    return letter


list_words = [str(i) for i in input().split()]

for i in range(len(list_words)):
    list_words[i] = capitalize(list_words[i][0]) + list_words[i][1:]

print(' '.join(list_words))
