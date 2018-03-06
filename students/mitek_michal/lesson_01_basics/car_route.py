import math


def calculate_number_of_days():

    n = int(input("Provide a distance that can move a day "))
    m = int(input("Provide a length in kilometers "))

    print(math.ceil(m/n))


calculate_number_of_days()