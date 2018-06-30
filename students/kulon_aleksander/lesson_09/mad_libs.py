import argparse

mad_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


def find_mad_word(word):
    for w in mad_words:
        if w in word:
            return w
    return None


def main():
    parser = argparse.ArgumentParser(description='Mad Libs program')
    parser.add_argument('-i', metavar='in-file',
                        type=argparse.FileType('r'),
                        default='input_file.txt')
    parser.add_argument('-o', metavar='out-file',
                        type=argparse.FileType('w'),
                        default='output_file.txt')

    args = parser.parse_args()

    modified_text = ""
    for line in args.i.readlines():
        words = []
        for word in line.split():
            mad_word = find_mad_word(word)
            if mad_word:
                word = word.replace(mad_word, input("Enter {}:\n".format(
                    mad_word.lower())))
            words.append(word)
        modified_text += ' '.join(words) + '\n'

    print(modified_text)

    args.o.write(modified_text)
    args.o.close()


if __name__ == "__main__":
    main()
