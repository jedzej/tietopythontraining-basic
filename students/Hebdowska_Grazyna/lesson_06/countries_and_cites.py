def input_files():
    number_of_countries = int(input('How many countries: '))
    countries = {}
    for i in range(number_of_countries):
        country, *cities = input("Country and cities: ").split(" ")
        countries[country] = cities
    return countries


def input_city():
    number_of_city = int(input('How many cities: '))
    cites = []
    for i in range(number_of_city):
        cites.append(input(str(i + 1) + ": "))
    return cites


def result(cantry, city):
    for i in city:
        for j in cantry.keys():
            if i in cantry[j]:
                print(j)


cantry = input_files()
city = input_city()
result(cantry, city)
