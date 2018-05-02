def untypicalJoin(list):
    return ", ".join(list[:-1]) + " and " + list[-1] + "."


def main():
    list = ['apples', 'bananas', 'tofu', 'cats', 'monkeys', 'dogs']
    print(untypicalJoin(list))


if __name__ == '__main__':
    main()
