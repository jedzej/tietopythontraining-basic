def main():
    letter = 'h'
    string = input()
    first, last = string.find(letter), string.rfind(letter)
    start_string = string[:first + 1]
    end_string = string[last:]
    replaced_string = string[first + 1: last].replace('h', 'H')
    string = start_string + replaced_string + end_string
    print(string)


if __name__ == '__main__':
    main()
