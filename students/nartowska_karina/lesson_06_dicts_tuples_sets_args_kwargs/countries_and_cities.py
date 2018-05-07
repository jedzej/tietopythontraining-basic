def main():
    print("Result:")
    list_of_countries_and_cities = {}
    amount = int(input())
    for i in range(amount):
        country, *cities = input().split()
        for city in cities:
            list_of_countries_and_cities[city] = country
    tests = int(input())
    for i in range(tests):
        city = input()
        print(list_of_countries_and_cities[city])


if __name__ == '__main__':
    main()
