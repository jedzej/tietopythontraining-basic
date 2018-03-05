#!/usr/bin/env python3

"""
Snakify_L2.py: Solutions for 9 problems defined in:
Lesson 2.Integer and float numbers (https://snakify.org/lessons/integer_float_numbers)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


from math import fabs
from math import ceil


def last_digit_of_integer():
    """
    This function prints last digit of a given integer number
    """
    print("Exercise 1: Last digit of integer")
    number = int(input("Enter a number: "))

    print("Last digit of the number is: ", (number % 10))


def tens_digit():
    """
    This function prints tens digit of a given integer number
    """
    print("Exercise 2: Tens digit")
    number = int(input("Enter a number: "))

    result = (number // 10) % 10
    print("Tens digit is: ", result)


def sum_of_digits():
    """
    This function prints the sum of digits of a given three-digit number
    """
    print("Exercise 3: Sum of digits")
    number = input("Enter a number: ")

    result = int(number[0]) + int(number[1]) + int(number[2])
    print("The sum of the number digits is: ", result)


def fractional_part():
    """
    This function prints the fractional part of a given real number
    """
    print("Exercise 4: Fractional part")
    number = float(input("Enter a number: "))

    result = number - int(number)
    delta = 0.0000000001
    if fabs(result) < delta:
        result = 0
    else:
        result = round(result, 10)

    print("Fractional part of the number is: ", result)


def first_digit_after_decimal_point():
    """
    This function prints the first digit to the right of the decimal point of a given positive real number
    """
    print("Exercise 5: First digit after decimal point")
    number = float(input("Enter a number: "))

    result = int(number * 10) % 10
    print("The result is: ", result)


def car_route():
    """
    This function prints how many days it will take to cover a route of a given length with given distance
    a car can cover per day.
    """
    print("Exercise 6: Car route")
    efficiency = int(input("Enter a number of kilometers the car can cover per day: "))
    route_len = int(input("Enter a number of kilometers in the route: "))

    result = ceil(route_len / efficiency)
    print("The result is: ", result, " day(s)")


def digital_clock():
    """
    This function reads integer number with minutes passed since midnight and prints how many hours and minutes
    are displayed on the 24h digital clock
    """
    print("Exercise 7: Digital clock")
    number = int(input("Enter a number of minutes passed since midnight: "))

    hours = number // 60
    minutes = number % 60
    print("The actual time is: {}:{}".format(hours, minutes))


def total_cost():
    """
    This function reads a cost of a cupcake in dollars and cents and prints the total cost of given number of cupcakes
    """
    print("Exercise 8: Total cost")
    dollars_per_cupcake = int(input("Enter dollars part of cupcake price: "))
    cents_per_cupcake = int(input("Enter cents part of cupcake price: "))
    number_of_cupcakes = int(input("Enter number of cupcakes: "))

    cupcake_cost_in_cents = (dollars_per_cupcake * 100) + cents_per_cupcake
    total_cost_in_cents = cupcake_cost_in_cents * number_of_cupcakes

    print("The total cost is: {} dollars {} cents".format(total_cost_in_cents // 100, total_cost_in_cents % 100))


def clock_face_1():
    """
    This function reads how many hours, minutes and seconds are passed since the midnight and prints the angle hour
    hand on the clock face right now
    """
    print("Exercise 9: Clock face - 1")
    hours = int(input("Enter the hours number: "))
    minutes = int(input("Enter the minutes number: "))
    seconds = int(input("Enter the seconds number: "))

    time_in_seconds = seconds + ((minutes + (hours * 60)) * 60)
    seconds_per_day = 60 * 60 * 12
    degrees_per_day = 360
    angle = (time_in_seconds / seconds_per_day) * degrees_per_day

    print("The angle is: {} degrees".format(angle))


def main():
    last_digit_of_integer()
    tens_digit()
    sum_of_digits()
    fractional_part()
    first_digit_after_decimal_point()
    car_route()
    digital_clock()
    total_cost()
    clock_face_1()


if __name__ == '__main__':
    main()
