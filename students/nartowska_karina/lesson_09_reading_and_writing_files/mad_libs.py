def mad_libs():
    dict = {'ADJECTIVE': input('Enter an adjective: '),
            'NOUN': input('Enter a noun: '),
            'ADVERB': input('Enter an adverb: '),
            'VERB': input('Enter a verb: ')}

    file = open('test1.txt')
    content = file.read()
    file.close()

    for i in dict:
        content = content.replace(i, dict[i])
    print(content)

    output_file = open('result', 'w')
    output_file.write(content)
    output_file.close()


def main():
    mad_libs()


if __name__ == "__main__":
    main()
