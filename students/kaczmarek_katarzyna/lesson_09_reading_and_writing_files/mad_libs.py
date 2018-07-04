mad_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


def find_mad_word(word):
    for w in mad_words:
        if w in word:
            return w
    return None


def main():
    with open('input_file.txt', 'r') as input_file:
        modified_text = ""
        for line in input_file.readlines():
            words = []
            for word in line.split():
                mad_word = find_mad_word(word)
                if mad_word:
                    word = word.replace(mad_word, input("Enter {}:\n".format(
                        mad_word.lower())))
                words.append(word)
            modified_text += ' '.join(words) + '\n'

    print(modified_text)

    with open('output_file.txt', 'w') as output_file:
        output_file.write(modified_text)


if __name__ == "__main__":
    main()
