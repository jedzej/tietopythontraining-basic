KEY_WORDS = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
NO_PATTERN = "No pattern"
OUTPUT_FILE = 'output.txt'
INPUT_FILE = 'input.txt'


def main():
    writer = open(OUTPUT_FILE, 'w')
    reader = open(INPUT_FILE)
    for line in reader:
        words = line.split()
        mad_words = []
        for w in words:
            p = look_for_pattern(w)
            if p != NO_PATTERN:
                w = w.replace(p, input("Enter a {}: ".format(p.lower())))
            mad_words.append(w)
        writer.write(" ".join(mad_words) + "\n")
    writer.close()
    reader.close()

    with open(OUTPUT_FILE, 'r') as output_reader:
        for line in output_reader:
            print(line)


def look_for_pattern(word):
    for pattern in KEY_WORDS:
        if pattern in word:
            return pattern
    return NO_PATTERN


if __name__ == '__main__':
    main()
