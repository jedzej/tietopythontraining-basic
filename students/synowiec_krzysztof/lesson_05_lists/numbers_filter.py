def main():
    strings = [x for x in input().split()]
    unwanted = range(int(input("Provide filter\n")))
    ints = [int(x) for x in strings if int(x) not in unwanted]
    print(ints)


if __name__ == '__main__':
    main()
