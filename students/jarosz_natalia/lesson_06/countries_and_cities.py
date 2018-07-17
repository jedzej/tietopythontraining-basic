def countries():
    motherland = {}

    for i in range(int(input())):
        country, *cities = input().split()
        for city in cities:
            motherland[city] = country

    for i in range(int(input())):
        print(motherland[input()])


def main():
    countries()


if __name__ == '__main__':
    main()
