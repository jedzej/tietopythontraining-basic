# Program return numbers that can are a secret(after receive yes or no answer for lists)
from functions_lesson06 import create_dict_to_n, find_max


def number_check(asked_numbers):
    while True:
        numbers = (input("put numbers with space: "))
        if numbers == "help":
            asked_numbers = {key: val for key, val in asked_numbers.items() if val != 0}
            break
        else:
            numbers = numbers.split(' ')
            numbers = map(int, numbers)
            answer = (input("yes/no: "))
            if answer == "yes":
                for elem in numbers:
                    if asked_numbers[elem] != 0:
                        asked_numbers[elem] += 1
            else:
                for elem in numbers:
                    asked_numbers[elem] = 0
    print("Secret number is on list:")
    find_max(asked_numbers)


n = int((input("range for number:")))
number_check(create_dict_to_n(n))
