def main():
    letter_to_find = 'f'
    string = input()
    occurrences = string.count(letter_to_find)
    if string.count(letter_to_find) == 1:
        print(string.find(letter_to_find))
    elif occurrences >= 2:
        print(string.find(letter_to_find), string.rfind(letter_to_find))


if __name__ == '__main__':
    main()
