list_of_words = {}


def frequency_analysis(lines):

    for line in range(lines):
        words = input().split()
        for word in words:
            list_of_words.setdefault(word, 0)
            list_of_words[word] += 1
    for word, value in sorted(list_of_words.items(),
                              key=lambda item: (-item[1], item[0])):
        print(word)


def main():
    user_lines = 0
    try:
        user_lines = int(input('how many lines? '))
    except:
        print('I think its not a number')
    frequency_analysis(user_lines)


if __name__ == '__main__':
    main()
