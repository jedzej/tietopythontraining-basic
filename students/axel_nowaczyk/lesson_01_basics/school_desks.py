from functools import reduce


def school_desks():
    a = int(input())
    b = int(input())
    c = int(input())
    sum = reduce((lambda x, y: x + number_of_desks(y)), [0, a, b, c])
    print(int(sum))


def number_of_desks(number_of_students):
    if number_of_students%2 == 0:
        return number_of_students / 2
    else:
        return (number_of_students+1)/2


if __name__ == '__main__':
    school_desks()