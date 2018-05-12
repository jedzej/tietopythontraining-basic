def the_number_of_distinct_words(text):
    words = {}
    for i in range(len(text)):
        new_text = text[i].split()
        for j in new_text:
            if j not in words.keys():
                words[j] = 1
    words_amount = len(words)
    return words_amount


def main():
    print("Enter amount of lines and text:")
    lines_of_text = int(input())
    data = []
    for i in range(lines_of_text):
        data.append(input())
    print("Result:")
    print(the_number_of_distinct_words(data))


if __name__ == '__main__':
    main()
