def main():
    """"set number of lines of text"""
    lines_number = int(input())

    word_dictionary = set()
    for _ in range(lines_number):

        """"Record single line"""
        single_line = input().split(' ')

        """"Update word dictionary"""
        for elem in single_line:
            word_dictionary.add(elem)

    """"Print total number of words in dictionary"""
    print(len(word_dictionary))


if __name__ == '__main__':
    main()
