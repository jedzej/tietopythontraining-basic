def main():
    cc_pairs = dict()
    results = dict()
    country_number = int(input())

    for i in range(country_number):

        country_name, cities = input().split(' ', 1)
        for city in cities.split():
            cc_pairs[city] = country_name

    city_number = int(input())

    for i in range(city_number):
        city_to_check = input()
        results[i] = cc_pairs[city_to_check]

    for v in results.values():
        print(v)


if __name__ == '__main__':
    main()
