def main():
    letter_to_find = 'f'
    string = input()
    occurrences = string.count(letter_to_find)
    if occurrences >= 2:
        first_index = string.find(letter_to_find)
        print(string.find(letter_to_find, first_index + 1))
    elif occurrences == 1:
        print(-1)
    else:
        print(-2)


if __name__ == '__main__':
    main()
