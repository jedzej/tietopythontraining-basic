countries_with_cities = {}


def add_cities_and_countries(num_of_countries):
    for i in range(num_of_countries):
        list_of_countries = input(
            'Give a country name and cities separate by spaces').split()
        country = list_of_countries[0]
        cities = list_of_countries[1:]
        countries_with_cities.update({c: country for c in cities})


def check_country(city):
    if city in countries_with_cities:
        print(countries_with_cities[city])
    else:
        print('I dont know where is this city')


def main():
    countries_amount = 0
    try:
        countries_amount = int(input('How many countries you wanna add? '))
    except ValueError:
        print('You should enter a number')
        exit()
    add_cities_and_countries(countries_amount)

    num_of_checks = 0
    try:
        num_of_checks = int(input('how many cities you wanna check? '))
    except ValueError:
        print('You should enter a number')
        exit()
    for i in range(num_of_checks):
        if num_of_checks != 0:
            city_check = input()
            check_country(city_check)
        else:
            print('Zero cities to check, bye:)')


if __name__ == '__main__':
    main()
