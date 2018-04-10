def comma_code(spam):
    return ' '.join(spam[:-1]) + ' and ' + spam[-1]


def main():
    entry_list = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(entry_list))


if __name__ == "__main__":
    main()

