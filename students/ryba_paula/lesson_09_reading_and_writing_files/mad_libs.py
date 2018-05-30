def mad_libs():
    source = 'file.txt'
    output = 'result_file.txt'

    words = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']

    with open(output, 'w') as outfile, open(source, 'r') as infile:
        for line in infile:
            for word in line.split(" "):
                if word in words:
                    new_word = str(input("Enter " + str(word) + " - "))
                    outfile.write(new_word)
                else:
                    outfile.write(word)
                outfile.write(" ")


def main():
    mad_libs()


if __name__ == '__main__':
    main()
