mad_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

in_files = open('input.txt', 'r')
out_files = open('output.txt', 'w')

for line in in_files:
    for word in line.split(" "):
        if word in mad_words:
            print("Enter an" + word)
            new_word = str(input())
            out_files.write(new_word)
        else:
            print(word)
            out_files.write(word)
        out_files.write(" ")
