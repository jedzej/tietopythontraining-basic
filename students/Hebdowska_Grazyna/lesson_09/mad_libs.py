
key_words = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]
input_file = open("input_file.txt", 'r')
output_file = open("output_file.txt", 'w')

for line in input_file:
    for word in line.split(" "):
        if word in key_words:
            new_word = input("Enter an " + word.lower() + ": ")
            output_file.write(new_word)
        else:
            output_file.write(word)
            output_file.write(" ")

input_file.close()
output_file.close()
