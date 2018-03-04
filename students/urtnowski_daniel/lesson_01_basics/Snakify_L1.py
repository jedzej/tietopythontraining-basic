#!/usr/bin/env python3

"""
Snakify_L1.py: Solutions for 6 problems defined in:
Lesson 1. Input, print and numbers (https://snakify.org/lessons/print_input_numbers)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def sum_of_three_numbers():
    """
    This function reads three numbers and prints their sum
    """
    print("Exercise 1: Sum of three numbers")
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    c = int(input("enter third number: "))

    print("sum: ", (a + b + c))


def area_of_right_angled_triangle():
    """
    This function reads the length of the base and the height of a right-angled triangle and prints the area
    """
    print("Exercise 2: Area of right-angled triangle")
    base = int(input("enter base: "))
    height = int(input("enter height: "))
    print("area: ", ((base * height) / 2))


def hello_harry():
    """
    This function greets the user by printing the word "Hello", a comma, the name of the user and an exclamation
    mark after it.
    """
    print("Exercise 3: Hello Harry!")
    name = input("Enter your name: ")
    print("Hello, " + name + "!")


def apple_sharing():
    """
    The function reads a number of Students and a number of apples and answers how the apples can be distributed
     evenly among the students.
    """
    print("Exercise 4: Apple sharing")
    students_num = int(input("Enter the number of students: "))
    apples_num = int(input("Enter the number of apples: "))
    print("Each single student will get {} apple(s)".format(apples_num // students_num))
    print("In the basket will remain: {} apple(s)".format(apples_num % students_num))


def previous_and_next():
    """
    The function reads an integer number and prints its previous and next numbers.
    """
    entered_number = int(input("Enter a number: "))
    print("The next number for the number " + str(entered_number) + " is " + str(entered_number + 1))
    print("The previous number for the number " + str(entered_number) + " is " + str(entered_number - 1))


def school_desks():
    """
    The function reads a number of students in each of three classes and answers how many desks are needed
     for all the students
    """
    required_desks_num = 0
    for class_name in ("a", "b", "c"):
        students_num = int(input("Enter number of students in class " + class_name + ": "))
        required_desks_num += ((students_num // 2) + (students_num % 2))

    print("Required desks number: ", required_desks_num)


def main():
    sum_of_three_numbers()
    area_of_right_angled_triangle()
    hello_harry()
    apple_sharing()
    previous_and_next()
    school_desks()


if __name__ == '__main__':
    main()
