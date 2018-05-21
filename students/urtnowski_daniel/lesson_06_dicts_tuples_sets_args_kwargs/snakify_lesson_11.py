#!/usr/bin/env python3

"""
snakify_lesson_11.py: Solutions for 3 of problems defined in:
Lesson 10. Dictionaries
(https://snakify.org/lessons/dictionaries_dicts/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def access_rights():
    files_cnt = int(input())
    files = {}
    possible_operations = {'R': 'read', 'W': 'write', 'X': 'execute'}

    for i in range(files_cnt):
        line = str(input()).split(' ')
        file = line[0]

        for operation in line[1:]:
            files.setdefault(file, [])
            files[file].append(possible_operations[operation])

    operations_cnt = int(input())

    for i in range(operations_cnt):
        operation, file = str(input()).split(' ')
        if operation in files[file]:
            print('OK')
        else:
            print('Access denied')


def countries_and_cities():

    cities_locations = {}
    countries_num = int(input())

    for i in range(countries_num):
        line = str(input()).split(' ')
        country = line[0]

        for city in line[1:]:
            cities_locations[city] = country

    cities_num = int(input())

    for i in range(cities_num):
        city = str(input())
        print(cities_locations[city])


def compare_words(tuple_1, tuple_2):
    if tuple_1[0] == tuple_2[0]:
        return tuple_1[1] < tuple_2[1]
    else:
        return tuple_1 < tuple_2


def frequency_analysis():
    lines_cnt = int(input())
    words = {}

    for i in range(lines_cnt):
        for word in str(input()).split(' '):
            words.setdefault(word, 0)
            words[word] += 1

    ordered = [(freq, word) for (word, freq) in words.items()]
    ordered.sort(key=lambda tup: (-tup[0], tup[1]))
    [print(word) for (count, word) in ordered]


def main():
    access_rights()
    countries_and_cities()
    frequency_analysis()


if __name__ == '__main__':
    main()
