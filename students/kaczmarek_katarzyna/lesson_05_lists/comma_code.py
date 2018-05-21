def stringify(items):
    if len(items) > 0:
        return ", ".join(str(item) for item in items[:-1]) + \
               " and " + str(items[-1])
    else:
        print("No items")


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    various = ['StrValue1', 'StrValue2', 100, 23.8, True, None]
    print(stringify(spam))
    print(stringify(various))


if __name__ == '__main__':
    main()
