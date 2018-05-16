def replace_the_substring():
    text = str(input())
    ones = [pos for pos, char in enumerate(text) if char == '1']
    print(text.replace('1', 'one', len(ones)))


def main():
    replace_the_substring()


if __name__ == '__main__':
    main()
