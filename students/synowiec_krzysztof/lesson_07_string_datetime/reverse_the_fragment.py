def main():
    letter_to_find = 'h'
    s = input()
    first, last = s.find(letter_to_find), s.rfind(letter_to_find)
    after_reverse = s[:first + 1] + s[first + 1:last][::-1] + s[last:]
    print(after_reverse)


if __name__ == '__main__':
    main()
