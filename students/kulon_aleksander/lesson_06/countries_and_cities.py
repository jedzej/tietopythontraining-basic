def func():
    countries = {}

    for i in range(int(input())):
        country, *cities = input().split()
        countries[country] = set(cities)

    for i in range(int(input())):
        request = str(input())
        for country, cities in countries.items():
            if request in cities:
                print(country)


def main():
    func()


if __name__ == '__main__':
    main()
