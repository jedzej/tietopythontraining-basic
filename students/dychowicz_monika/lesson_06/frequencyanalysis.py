def measure_frequency():
    line_number = int(input("Enter number of lines: "))
    words = {}
    for i in range(line_number):
        line = input("Enter line of words separated by space: ").split()
        for word in line:
            words.setdefault(word, 0)
            words[word] += 1
    words_list = []
    for k, v in words.items():
        words_list.append(tuple([v, k]))
    words_list.sort(key=lambda val: val[1], reverse=False)
    words_list.sort(key=lambda val: val[0], reverse=True)
    print("List of words in order of occurrences: ")
    for i in words_list:
        print(i[1])


if __name__ == "__main__":
    measure_frequency()