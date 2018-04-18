string = input('String: ')
first_word = string[:string.find(' ')]
second_word = string[string.find(' ')+1:]
print(second_word + " " + first_word)
