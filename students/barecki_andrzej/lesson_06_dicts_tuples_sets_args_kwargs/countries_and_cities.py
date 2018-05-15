def main():
    """"Create empty dictionary of files"""
    country_dict = dict()

    """"set number of countries in dictionary"""
    number_of_countries_in_dict = int(input())

    """"Add country to dictionary"""
    for _ in range(number_of_countries_in_dict):
        single_country = [x for x in input().split(' ')]
        country_dict[single_country[0]] = set(single_country[1:])

    """"set number of cities that will be checked"""
    number_of_cities_to_check = int(input())

    """"check city and realated country based on country_dict"""
    for _ in range(number_of_cities_to_check):
        city = input()
        for key, val in country_dict.items():
            if city in val:
                print(key)


if __name__ == '__main__':
    main()
