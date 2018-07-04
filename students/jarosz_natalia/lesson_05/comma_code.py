def comma_code(arg):
    result = " "
    for i in range(len(arg) - 1):
        result += arg[i] + ", "
    result += "and " + arg[-1]
    return result


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))


if __name__ == "__main__":
    main()
