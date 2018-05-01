def main():
    letter_to_find = 'h'
    string = input()
    first, last = string.find(letter_to_find), string.rfind(letter_to_find)
    after_remove = string[:first] + string[last + 1:]
    print(after_remove)


if __name__ == '__main__':
    main()
