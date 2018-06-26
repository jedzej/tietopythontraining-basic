secret_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

input_file_name = input('Enter file name to open: ')

input_file = open(input_file_name, 'r')
contents = input_file.read()
input_file.close()

for word in secret_words:
    while word in contents:
        contents = contents.replace(word,
                                    input("Enter an " +
                                          word.lower() + ': '), 1)

output_file_name = input('Enter file name to save content to: ')
output_file = open(output_file_name, 'w')
output_file.write(contents)
output_file.close()

print(contents)
