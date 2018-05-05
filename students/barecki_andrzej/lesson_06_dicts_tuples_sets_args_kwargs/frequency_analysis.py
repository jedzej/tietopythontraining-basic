def main():
    """"Create empty dictionary of files"""
    text_dict = dict()

    """"set number of lines in text"""
    number_of_lines_in_text = int(input())

    """"Add words to dictionary"""
    for _ in range(number_of_lines_in_text):
        single_line = [x for x in input().split(' ')]
        for word in single_line:
            if word in text_dict:
                text_dict[word] += 1
            else:
                text_dict[word] = 1

    """"Create sorted list of tuples contained freq number and given word"""
    sort_list = sorted([(-value, key) for key, value in text_dict.items()])

    """"Print result"""
    for elem in sort_list:
        print(elem[1])


if __name__ == '__main__':
    main()
