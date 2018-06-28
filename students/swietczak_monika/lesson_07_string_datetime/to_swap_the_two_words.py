words = input("Enter two words with space between them: ")
space_index = words.find(" ")
first_word = words[0:space_index]
second_word = words[space_index + 1:]
print(second_word, first_word)
