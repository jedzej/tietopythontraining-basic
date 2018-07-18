words_to_find = ['ADJECTIVE', 'NOUN', 'VERB', 'NOUN2']

filename = input("Enter a filename: ")
text_file = open(filename, "r")
content = text_file.read()
text_file.close()

for word in words_to_find:
    content = content.replace(word, input("Enter an " + word.lower() + ': '),
                              1)

write_filename = input("Enter a filename for writing the data: ")
write_filename = open(write_filename, 'w')
write_filename.write(content)
write_filename.close()

print(content)
